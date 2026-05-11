from __future__ import annotations

from contextlib import asynccontextmanager
from typing import Any, AsyncIterator

import httpx

from osdu_python_client.auth import TokenProvider, provider_for
from osdu_python_client.config import OsduConfig
from osdu_python_client.hooks import async_partition_hook
from osdu_python_client.services.facade import ServiceFacade
from osdu_python_client.services.registry import (
    SERVICE_BY_ATTR,
    ServiceSpec,
    load_authenticated_client,
)
from osdu_python_client.transport import AsyncRetryTransport


class AsyncOsduClient:
    def __init__(
        self,
        config: OsduConfig | None = None,
        token_provider: TokenProvider | None = None,
    ) -> None:
        self._services: dict[str, ServiceFacade] = {}
        self._httpx_clients: dict[str, httpx.AsyncClient] = {}
        self.config = config or OsduConfig()
        self._provider = token_provider or provider_for(self.config)
        self._transport = AsyncRetryTransport(
            self._provider,
            max_attempts=self.config.retry_attempts,
            base_delay=self.config.retry_base_delay,
        )

    def _build_service(self, spec: ServiceSpec) -> ServiceFacade:
        auth_cls = load_authenticated_client(spec)
        base_url = self.config.url_for(spec.attr)
        timeout = httpx.Timeout(self.config.timeout_seconds)
        httpx_client = httpx.AsyncClient(
            base_url=base_url,
            transport=self._transport,
            timeout=timeout,
            verify=self.config.verify_ssl,
            event_hooks={
                "request": [async_partition_hook(self.config.data_partition_id)]
            },
        )
        self._httpx_clients[spec.attr] = httpx_client
        auth_client = auth_cls(base_url=base_url, token="")
        auth_client.set_async_httpx_client(httpx_client)
        return ServiceFacade(
            spec.module, auth_client, self.config.data_partition_id, is_async=True
        )

    def __getattr__(self, name: str) -> Any:
        if name.startswith("_"):
            raise AttributeError(name)
        spec = SERVICE_BY_ATTR.get(name)
        if spec is None:
            raise AttributeError(
                f"{type(self).__name__!r} has no attribute {name!r}"
            )
        services = self.__dict__.get("_services")
        if services is None:
            raise AttributeError(name)
        cached = services.get(name)
        if cached is not None:
            return cached
        facade = self._build_service(spec)
        services[name] = facade
        return facade

    def __dir__(self) -> list[str]:
        return sorted({*super().__dir__(), *SERVICE_BY_ATTR})

    @asynccontextmanager
    async def with_headers(
        self, *, service: str | None = None, **headers: str
    ) -> AsyncIterator["AsyncOsduClient"]:
        if service is not None:
            getattr(self, service)
            targets = [self._httpx_clients[service]]
        else:
            targets = list(self._httpx_clients.values())

        saved = [(c, dict(c.headers)) for c in targets]
        for c in targets:
            c.headers.update(headers)
        try:
            yield self
        finally:
            for c, prev in saved:
                c.headers.clear()
                c.headers.update(prev)

    async def aclose(self) -> None:
        for c in self._httpx_clients.values():
            await c.aclose()
        self._httpx_clients.clear()
        self._services.clear()
        await self._transport.aclose()

    async def __aenter__(self) -> "AsyncOsduClient":
        return self

    async def __aexit__(self, *args: Any) -> None:
        await self.aclose()
