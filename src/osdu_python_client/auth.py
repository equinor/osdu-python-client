from __future__ import annotations

import pathlib
import threading
from typing import Any, Protocol, runtime_checkable

from osdu_python_client.config import OsduConfig
from osdu_python_client.errors import OsduAuthError, OsduConfigError


@runtime_checkable
class TokenProvider(Protocol):
    def get_token(self, force_refresh: bool = False) -> str: ...


def _load_cache(path: pathlib.Path) -> Any:
    from msal import SerializableTokenCache

    cache = SerializableTokenCache()
    if path.exists():
        cache.deserialize(path.read_text(encoding="utf-8"))
    return cache


def _save_cache(cache: Any, path: pathlib.Path) -> None:
    if cache.has_state_changed:
        path.write_text(cache.serialize(), encoding="utf-8")


class _MsalProviderBase:
    def __init__(self, config: OsduConfig) -> None:
        self._config = config
        self._lock = threading.Lock()
        self._cache_path = pathlib.Path(config.msal_cache_path)
        self._cache = _load_cache(self._cache_path)
        self._app = self._build_app()

    def _build_app(self) -> Any:  # pragma: no cover - subclasses override
        raise NotImplementedError

    def _persist(self) -> None:
        _save_cache(self._cache, self._cache_path)

    def _try_silent(self, force_refresh: bool) -> dict[str, Any] | None:
        accounts = self._app.get_accounts()
        if not accounts:
            return None
        return self._app.acquire_token_silent(
            scopes=self._config.scopes_list,
            account=accounts[0],
            force_refresh=force_refresh,
        )

    def _extract_token(self, result: dict[str, Any] | None) -> str:
        token = result.get("access_token") if isinstance(result, dict) else None
        if not token:
            raise OsduAuthError(f"Authentication failed: {result}")
        return token


class MsalInteractiveProvider(_MsalProviderBase):
    def _build_app(self) -> Any:
        from msal import PublicClientApplication

        return PublicClientApplication(
            client_id=self._config.client_id,
            authority=self._config.authority,
            token_cache=self._cache,
        )

    def get_token(self, force_refresh: bool = False) -> str:
        with self._lock:
            result = self._try_silent(force_refresh=force_refresh)
            if not result or "access_token" not in result:
                result = self._app.acquire_token_interactive(
                    scopes=self._config.scopes_list
                )
            self._persist()
            return self._extract_token(result)


class MsalDeviceFlowProvider(_MsalProviderBase):
    def __init__(
        self,
        config: OsduConfig,
        prompt_callback: Any | None = None,
    ) -> None:
        super().__init__(config)
        self._prompt_callback = prompt_callback or (lambda flow: print(flow["message"]))

    def _build_app(self) -> Any:
        from msal import PublicClientApplication

        return PublicClientApplication(
            client_id=self._config.client_id,
            authority=self._config.authority,
            token_cache=self._cache,
        )

    def get_token(self, force_refresh: bool = False) -> str:
        with self._lock:
            result = self._try_silent(force_refresh=force_refresh)
            if not result or "access_token" not in result:
                flow = self._app.initiate_device_flow(scopes=self._config.scopes_list)
                if "user_code" not in flow:
                    raise OsduAuthError(f"Device flow init failed: {flow}")
                self._prompt_callback(flow)
                result = self._app.acquire_token_by_device_flow(flow)
            self._persist()
            return self._extract_token(result)


class ClientCredentialsProvider(_MsalProviderBase):
    def __init__(self, config: OsduConfig) -> None:
        if not config.client_secret:
            raise OsduConfigError(
                "client_secret is required for client_credentials auth_mode"
            )
        super().__init__(config)

    def _build_app(self) -> Any:
        from msal import ConfidentialClientApplication

        return ConfidentialClientApplication(
            client_id=self._config.client_id,
            authority=self._config.authority,
            client_credential=self._config.client_secret,
            token_cache=self._cache,
        )

    def get_token(self, force_refresh: bool = False) -> str:
        with self._lock:
            result: dict[str, Any] | None = None
            if not force_refresh:
                result = self._app.acquire_token_silent(
                    scopes=self._config.scopes_list, account=None
                )
            if not result or "access_token" not in result:
                result = self._app.acquire_token_for_client(
                    scopes=self._config.scopes_list
                )
            self._persist()
            return self._extract_token(result)


def provider_for(config: OsduConfig) -> TokenProvider:
    match config.auth_mode:
        case "interactive":
            return MsalInteractiveProvider(config)
        case "device_flow":
            return MsalDeviceFlowProvider(config)
        case "client_credentials":
            return ClientCredentialsProvider(config)
