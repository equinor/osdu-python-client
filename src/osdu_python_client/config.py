from typing import Literal

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

AuthMode = Literal["interactive", "device_flow", "client_credentials"]


class OsduConfig(BaseSettings):
    server: str

    crs_catalog_endpoint: str = Field("/api/crs/catalog/v2")
    crs_converter_endpoint: str = Field("/api/crs/converter/v2")
    dataset_endpoint: str = Field("/api/dataset/v1")
    entitlements_endpoint: str = Field("/api/entitlements/v2")
    file_endpoint: str = Field("/api/file/v2")
    indexer_endpoint: str = Field("/api/indexer/v2")
    legal_endpoint: str = Field("/api/legal/v1")
    notification_endpoint: str = Field("/api/notification/v1")
    partition_endpoint: str = Field("/api/partition/v1")
    policy_endpoint: str = Field("/api/policy/v1")
    register_endpoint: str = Field("/api/register/v1")
    schema_endpoint: str = Field("/api/schema-service/v1")
    search_endpoint: str = Field("/api/search/v2")
    storage_endpoint: str = Field("/api/storage/v2")
    unit_endpoint: str = Field("/api/unit/v3")
    wellbore_ddms_endpoint: str = Field("/api/os-wellbore-ddms")
    workflow_endpoint: str = Field("/api/workflow/v1")

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

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    def url(self, endpoint: str) -> str:
        return f"{self.server.rstrip('/')}{endpoint}"

    @property
    def crs_catalog_url(self) -> str:
        return self.url(self.crs_catalog_endpoint)

    @property
    def crs_converter_url(self) -> str:
        return self.url(self.crs_converter_endpoint)

    @property
    def dataset_url(self) -> str:
        return self.url(self.dataset_endpoint)

    @property
    def entitlements_url(self) -> str:
        return self.url(self.entitlements_endpoint)

    @property
    def file_url(self) -> str:
        return self.url(self.file_endpoint)

    @property
    def indexer_url(self) -> str:
        return self.url(self.indexer_endpoint)

    @property
    def legal_url(self) -> str:
        return self.url(self.legal_endpoint)

    @property
    def notification_url(self) -> str:
        return self.url(self.notification_endpoint)

    @property
    def partition_url(self) -> str:
        return self.url(self.partition_endpoint)

    @property
    def policy_url(self) -> str:
        return self.url(self.policy_endpoint)

    @property
    def register_url(self) -> str:
        return self.url(self.register_endpoint)

    @property
    def schema_url(self) -> str:
        return self.url(self.schema_endpoint)

    @property
    def search_url(self) -> str:
        return self.url(self.search_endpoint)

    @property
    def storage_url(self) -> str:
        return self.url(self.storage_endpoint)

    @property
    def unit_url(self) -> str:
        return self.url(self.unit_endpoint)

    @property
    def wellbore_ddms_url(self) -> str:
        return self.url(self.wellbore_ddms_endpoint)

    @property
    def workflow_url(self) -> str:
        return self.url(self.workflow_endpoint)

    @property
    def scopes_list(self) -> list[str]:
        return self.scopes.split()
