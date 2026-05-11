from __future__ import annotations

import importlib
import inspect
import pkgutil
from types import ModuleType
from typing import Any

from osdu_python_client.errors import OsduError


_ERROR_BODY_MAX = 1024


def _unwrap(response: Any) -> Any:
    status = response.status_code
    code = status.value if hasattr(status, "value") else int(status)
    if 200 <= code < 300:
        return response.parsed
    detail: Any = response.parsed
    if detail is None:
        content = getattr(response, "content", None)
        if content:
            text = (
                content.decode("utf-8", errors="replace")
                if isinstance(content, bytes)
                else str(content)
            )
            detail = (
                text
                if len(text) <= _ERROR_BODY_MAX
                else f"{text[:_ERROR_BODY_MAX]}... [truncated]"
            )
    raise OsduError(f"Request failed: status={code} detail={detail!r}")


class Endpoint:
    """Callable proxy over a generated endpoint module.

    Default ``__call__`` invokes ``sync_detailed`` (or ``asyncio_detailed`` for
    async facades), auto-binds ``client=`` and ``data_partition_id=``, and
    returns the parsed body on 2xx or raises ``OsduError``.

    ``.detailed(...)`` returns the full ``Response`` envelope for callers who
    need status code / headers / raw parsed error model.
    """

    __slots__ = (
        "_mod",
        "_client",
        "_partition",
        "_is_async",
        "_sync_detailed",
        "_async_detailed",
        "_accepts_partition",
    )

    def __init__(
        self,
        op_module: ModuleType,
        client: Any,
        partition: str,
        *,
        is_async: bool,
    ) -> None:
        self._mod = op_module
        self._client = client
        self._partition = partition
        self._is_async = is_async
        self._sync_detailed = getattr(op_module, "sync_detailed", None)
        self._async_detailed = getattr(op_module, "asyncio_detailed", None)
        primary = self._async_detailed if is_async else self._sync_detailed
        if primary is None:
            raise AttributeError(
                f"{op_module.__name__} is missing "
                f"{'asyncio_detailed' if is_async else 'sync_detailed'}"
            )
        self._accepts_partition = (
            "data_partition_id" in inspect.signature(primary).parameters
        )

    def _bind(self, kw: dict[str, Any]) -> dict[str, Any]:
        kw["client"] = self._client
        if self._accepts_partition and "data_partition_id" not in kw:
            kw["data_partition_id"] = self._partition
        return kw

    def __call__(self, *args: Any, **kw: Any) -> Any:
        if self._is_async:
            return self._async_call(*args, **kw)
        return _unwrap(self._sync_detailed(*args, **self._bind(kw)))

    def detailed(self, *args: Any, **kw: Any) -> Any:
        if self._is_async:
            return self._async_detailed(*args, **self._bind(kw))
        return self._sync_detailed(*args, **self._bind(kw))

    async def _async_call(self, *args: Any, **kw: Any) -> Any:
        return _unwrap(await self._async_detailed(*args, **self._bind(kw)))


class ServiceFacade:
    """Dynamic facade over a generated service package.

    Resolves attribute access against the service's ``api`` subpackages and
    returns an :class:`Endpoint` proxy. Unknown attribute names fall through
    to the wrapped :class:`AuthenticatedClient`, so escape hatches like
    ``get_httpx_client()`` keep working.
    """

    def __init__(
        self,
        service_module: str,
        client: Any,
        partition: str,
        *,
        is_async: bool,
    ) -> None:
        self._service_module = service_module
        self._client = client
        self._partition = partition
        self._is_async = is_async
        self._endpoints: dict[str, Endpoint] = {}
        self._op_index: dict[str, str] | None = None

    @property
    def raw(self) -> Any:
        return self._client

    def _build_index(self) -> dict[str, str]:
        index: dict[str, str] = {}
        api_pkg = importlib.import_module(f"{self._service_module}.api")
        for _, group_name, is_pkg in pkgutil.iter_modules(api_pkg.__path__):
            if not is_pkg or group_name.startswith("_"):
                continue
            group_pkg = importlib.import_module(f"{api_pkg.__name__}.{group_name}")
            for _, op_name, op_is_pkg in pkgutil.iter_modules(group_pkg.__path__):
                if op_is_pkg or op_name.startswith("_"):
                    continue
                if op_name in index:
                    raise RuntimeError(
                        f"Duplicate operation '{op_name}' in {self._service_module}: "
                        f"{index[op_name]} vs {group_pkg.__name__}.{op_name}"
                    )
                index[op_name] = f"{group_pkg.__name__}.{op_name}"
        return index

    def __getattr__(self, name: str) -> Any:
        if name.startswith("_"):
            raise AttributeError(name)
        endpoints = self.__dict__.get("_endpoints")
        if endpoints is None:
            raise AttributeError(name)
        cached = endpoints.get(name)
        if cached is not None:
            return cached
        if self._op_index is None:
            self._op_index = self._build_index()
        mod_path = self._op_index.get(name)
        if mod_path is None:
            return getattr(self._client, name)
        op_mod = importlib.import_module(mod_path)
        ep = Endpoint(op_mod, self._client, self._partition, is_async=self._is_async)
        endpoints[name] = ep
        return ep

    def __dir__(self) -> list[str]:
        if self._op_index is None:
            try:
                self._op_index = self._build_index()
            except Exception:
                self._op_index = {}
        return sorted({*super().__dir__(), *self._op_index, *dir(self._client)})
