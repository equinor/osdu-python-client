from __future__ import annotations

from contextlib import contextmanager
from typing import TYPE_CHECKING, Any, Iterator

if TYPE_CHECKING:
    from osdu_python_client.services.search import SearchService

import httpx

from osdu_python_client.auth import TokenProvider, provider_for
from osdu_python_client.config import OsduConfig
from osdu_python_client.hooks import partition_hook
from osdu_python_client.services.registry import (
    SERVICE_BY_ATTR,
    ServiceSpec,
    import_target,
    load_authenticated_client,
)
from osdu_python_client.transport import RetryTransport


class OsduClient:
    if TYPE_CHECKING:
        # Type hints for IDE / static-analysis support. Runtime resolution is
        # registry-driven via ``__getattr__``; see ``SERVICE_REGISTRY``.
        search: "SearchService"
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
        # Set the service cache first so __getattr__ never sees a missing slot
        # while the rest of __init__ is still running.
        self._services: dict[str, Any] = {}
        self._httpx_clients: dict[str, httpx.Client] = {}
        self.config = config or OsduConfig()
        self._provider = token_provider or provider_for(self.config)
        self._transport = RetryTransport(
            self._provider,
            max_attempts=self.config.retry_attempts,
            base_delay=self.config.retry_base_delay,
        )

    def _build(self, name: str, base_url: str, auth_cls: type) -> Any:
        timeout = httpx.Timeout(self.config.timeout_seconds)
        httpx_client = httpx.Client(
            base_url=base_url,
            transport=self._transport,
            timeout=timeout,
            verify=self.config.verify_ssl,
            event_hooks={"request": [partition_hook(self.config.data_partition_id)]},
        )
        self._httpx_clients[name] = httpx_client
        client = auth_cls(base_url=base_url, token="")
        client.set_httpx_client(httpx_client)
        return client

    def _build_service(self, spec: ServiceSpec) -> Any:
        auth_cls = load_authenticated_client(spec)
        base_url = getattr(self.config, spec.config_url_attr)
        client = self._build(spec.attr, base_url, auth_cls)
        if spec.sync_wrapper:
            wrapper_cls = import_target(spec.sync_wrapper)
            client = wrapper_cls(client, self.config.data_partition_id)
        return client

    def __getattr__(self, name: str) -> Any:
        # __getattr__ runs only when normal lookup fails, so this never shadows
        # real instance attributes (config, _services, …) set in __init__.
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

    @contextmanager
    def with_headers(
        self, *, service: str | None = None, **headers: str
    ) -> Iterator["OsduClient"]:
        """Temporarily set extra headers on one or all built service clients.

        Useful for per-service overrides (e.g. ``frame-of-reference`` on CRS calls).
        """
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

    def close(self) -> None:
        for c in self._httpx_clients.values():
            c.close()
        self._httpx_clients.clear()
        self._services.clear()
        self._transport.close()

    def __enter__(self) -> "OsduClient":
        return self

    def __exit__(self, *args: Any) -> None:
        self.close()
