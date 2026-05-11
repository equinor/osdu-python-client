import logging
from typing import Literal

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

from osdu_python_client.services.registry import SERVICE_BY_ATTR

AuthMode = Literal["interactive", "device_flow", "client_credentials"]

# MSAL adds these automatically and rejects them in caller-supplied scope
# lists. Filter them so configs copied from other tools (e.g. osdu-cli) just
# work.
_MSAL_RESERVED_SCOPES: frozenset[str] = frozenset(
    {"openid", "profile", "offline_access"}
)

log = logging.getLogger(__name__)


class OsduConfig(BaseSettings):
    server: str

    data_partition_id: str
    authority: str
    scopes: str
    client_id: str

    auth_mode: AuthMode = "interactive"
    client_secret: str | None = None
    msal_cache_path: str = ".msal_token_cache.bin"

    timeout_seconds: float = 30.0
    retry_attempts: int = 3
    retry_base_delay: float = 0.5

    verify_ssl: bool = True

    endpoint_overrides: dict[str, str] = Field(default_factory=dict)

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    def endpoint_for(self, service: str) -> str:
        override = self.endpoint_overrides.get(service)
        if override is not None:
            return override
        spec = SERVICE_BY_ATTR.get(service)
        if spec is None:
            raise KeyError(f"Unknown service {service!r}")
        return spec.endpoint

    def url_for(self, service: str) -> str:
        return f"{self.server.rstrip('/')}{self.endpoint_for(service)}"

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
