"""Azure / Entra ID token providers backed by MSAL."""

from __future__ import annotations

import logging
import pathlib
import threading
from typing import TYPE_CHECKING, Any, Literal

from pydantic_settings import BaseSettings, SettingsConfigDict

from osdu_python_client.auth._base import (
    TokenProvider,
    register_provider,
)
from osdu_python_client.errors import OsduAuthError, OsduConfigError

if TYPE_CHECKING:
    from osdu_python_client.config import OsduConfig

log = logging.getLogger(__name__)

AzureAuthMode = Literal["interactive", "device_flow", "client_credentials"]

# MSAL adds these implicitly and rejects them in caller-supplied scope lists.
_MSAL_RESERVED_SCOPES: frozenset[str] = frozenset(
    {"openid", "profile", "offline_access"}
)


class AzureMsalConfig(BaseSettings):
    """Azure-specific auth settings, loaded from the same ``.env`` as OsduConfig.

    The env var names (``AUTHORITY``, ``SCOPES``, ``CLIENT_ID``, ``CLIENT_SECRET``,
    ``AUTH_MODE``, ``MSAL_CACHE_PATH``) are unchanged from the pre-split layout.
    """

    authority: str
    scopes: str
    client_id: str
    client_secret: str | None = None
    auth_mode: AzureAuthMode = "interactive"
    msal_cache_path: str = ".msal_token_cache.bin"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    @property
    def scopes_list(self) -> list[str]:
        raw = self.scopes.split()
        filtered = [s for s in raw if s.lower() not in _MSAL_RESERVED_SCOPES]
        dropped = [s for s in raw if s.lower() in _MSAL_RESERVED_SCOPES]
        if dropped:
            log.debug(
                "ignoring MSAL-reserved scopes from config: %s (MSAL adds these itself)",
                dropped,
            )
        return filtered


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
    def __init__(self, config: AzureMsalConfig) -> None:
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
            if result and "access_token" in result:
                log.debug("token acquired silently (force_refresh=%s)", force_refresh)
            else:
                log.info("interactive auth flow required")
                result = self._app.acquire_token_interactive(
                    scopes=self._config.scopes_list
                )
                log.debug("token acquired via interactive flow")
            self._persist()
            return self._extract_token(result)


class MsalDeviceFlowProvider(_MsalProviderBase):
    def __init__(
        self,
        config: AzureMsalConfig,
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
            if result and "access_token" in result:
                log.debug("token acquired silently (force_refresh=%s)", force_refresh)
            else:
                flow = self._app.initiate_device_flow(scopes=self._config.scopes_list)
                if "user_code" not in flow:
                    raise OsduAuthError(f"Device flow init failed: {flow}")
                log.info("device flow initiated — awaiting user code entry")
                self._prompt_callback(flow)
                result = self._app.acquire_token_by_device_flow(flow)
                log.debug("token acquired via device flow")
            self._persist()
            return self._extract_token(result)


class ClientCredentialsProvider(_MsalProviderBase):
    def __init__(self, config: AzureMsalConfig) -> None:
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
            if result and "access_token" in result:
                log.debug("client_credentials token acquired silently")
            else:
                log.debug("client_credentials acquiring new token (force_refresh=%s)", force_refresh)
                result = self._app.acquire_token_for_client(
                    scopes=self._config.scopes_list
                )
            self._persist()
            return self._extract_token(result)


def _factory(_config: "OsduConfig") -> TokenProvider:
    azure_config = AzureMsalConfig()
    match azure_config.auth_mode:
        case "interactive":
            return MsalInteractiveProvider(azure_config)
        case "device_flow":
            return MsalDeviceFlowProvider(azure_config)
        case "client_credentials":
            return ClientCredentialsProvider(azure_config)


register_provider("azure_msal", _factory)
