from __future__ import annotations

from contextlib import asynccontextmanager
from typing import TYPE_CHECKING, Any, AsyncIterator

if TYPE_CHECKING:
    from osdu_python_client.services.search import AsyncSearchService

import httpx

from osdu_python_client.auth import TokenProvider, provider_for
from osdu_python_client.config import OsduConfig
from osdu_python_client.hooks import async_partition_hook
from osdu_python_client.services.registry import (
    SERVICE_BY_ATTR,
    ServiceSpec,
    import_target,
    load_authenticated_client,
)
from osdu_python_client.transport import AsyncRetryTransport


class AsyncOsduClient:
    if TYPE_CHECKING:
        # Type hints for IDE / static-analysis support. Runtime resolution is
        # registry-driven via ``__getattr__``; see ``SERVICE_REGISTRY``.
        search: "AsyncSearchService"
        storage: Any
        schema: Any
        entitlements: Any
        legal: Any
        file: Any
        dataset: Any
        indexer: Any
        notification: Any
        partition: Any
        policy: Any
        register: Any
        unit: Any
        crs_catalog: Any
        crs_conversion: Any
        wellbore_ddms: Any
        workflow: Any

    def __init__(
        self,
        config: OsduConfig | None = None,
        token_provider: TokenProvider | None = None,
    ) -> None:
        self._services: dict[str, Any] = {}
        self._httpx_clients: dict[str, httpx.AsyncClient] = {}
        self.config = config or OsduConfig()
        self._provider = token_provider or provider_for(self.config)
        self._transport = AsyncRetryTransport(
            self._provider,
            max_attempts=self.config.retry_attempts,
            base_delay=self.config.retry_base_delay,
        )

    def _build(self, name: str, base_url: str, auth_cls: type) -> Any:
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
        self._httpx_clients[name] = httpx_client
        client = auth_cls(base_url=base_url, token="")
        client.set_async_httpx_client(httpx_client)
        return client

    def _build_service(self, spec: ServiceSpec) -> Any:
        auth_cls = load_authenticated_client(spec)
        base_url = getattr(self.config, spec.config_url_attr)
        client = self._build(spec.attr, base_url, auth_cls)
        if spec.async_wrapper:
            wrapper_cls = import_target(spec.async_wrapper)
            client = wrapper_cls(client, self.config.data_partition_id)
        return client

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
        client = self._build_service(spec)
        services[name] = client
        return client

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
