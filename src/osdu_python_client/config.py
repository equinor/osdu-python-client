from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

from osdu_python_client.services.registry import SERVICE_BY_ATTR


class OsduConfig(BaseSettings):
    """CSP-agnostic OSDU client configuration.

    Auth is delegated to a pluggable provider (see ``osdu_python_client.auth``).
    Each registered provider reads its own settings — e.g. ``AzureMsalConfig``
    handles MSAL env vars for ``auth_provider='azure_msal'``.
    """

    server: str
    data_partition_id: str

    auth_provider: str = "azure_msal"

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
