"""Application configuration"""

import pytest
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class CoreConfig(BaseSettings):
    """Application configuration based on .env file or environment variables.
    ref: https://docs.pydantic.dev/latest/concepts/pydantic_settings/
    """

    server: str

    crs_catalog_endpoint: str = Field("/api/crs/catalog/v2")
    crs_converter_endpoint: str = Field("/api/crs/converter/v2")
    entitlements_endpoint: str = Field("/api/entitlements/v2")
    file_endpoint: str = Field("/api/file/v2")
    legal_endpoint: str = Field("/api/legal/v1")
    schema_endpoint: str = Field("/api/schema/v1/")
    search_endpoint: str = Field("/api/search/v2")
    storage_endpoint: str = Field("/api/storage/v2")
    unit_endpoint: str = Field("/api/unit/v3")
    workflow_endpoint: str = Field("/api/workflow/v1")

    data_partition_id: str
    authority: str
    scopes: str
    client_id: str

    @property
    def crs_catalog_url(self):
        return f"{self.server}{self.crs_catalog_endpoint}"

    @property
    def crs_converter_url(self):
        return f"{self.server}{self.crs_converter_endpoint}"

    @property
    def entitlements_url(self):
        return f"{self.server}{self.entitlements_endpoint}"

    @property
    def file_url(self):
        return f"{self.server}{self.file_endpoint}"

    @property
    def legal_url(self):
        return f"{self.server}{self.legal_endpoint}"

    @property
    def schema_url(self):
        return f"{self.server}{self.schema_endpoint}"

    @property
    def search_url(self):
        return f"{self.server}{self.search_endpoint}"

    @property
    def storage_url(self):
        return f"{self.server}{self.storage_endpoint}"

    @property
    def unit_url(self):
        return f"{self.server}{self.unit_endpoint}"

    @property
    def workflow_url(self):
        return f"{self.server}{self.workflow_endpoint}"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )

@pytest.fixture(scope="session")
def config() -> CoreConfig:
    """
    Session-scoped config loaded from `.env` or environment variables via Pydantic Settings.
    """
    return CoreConfig()
