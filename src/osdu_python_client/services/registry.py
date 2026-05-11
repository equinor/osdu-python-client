from __future__ import annotations

import importlib
from dataclasses import dataclass


@dataclass(frozen=True)
class ServiceSpec:
    """Declares how a generated package is exposed on the facade.

    - ``attr``: property name on ``OsduClient`` / ``AsyncOsduClient`` and the
      key used in ``OsduConfig.endpoint_overrides``.
    - ``module``: generated package path; ``<module>.client.AuthenticatedClient``
      is imported lazily.
    - ``endpoint``: default base path appended to ``OsduConfig.server`` to form
      the service URL. Overridable via ``endpoint_overrides``.
    """

    attr: str
    module: str
    endpoint: str


SERVICE_REGISTRY: tuple[ServiceSpec, ...] = (
    ServiceSpec("search", "osdu_python_client.generated.search", "/api/search/v2"),
    ServiceSpec("storage", "osdu_python_client.generated.storage", "/api/storage/v2"),
    ServiceSpec("schema", "osdu_python_client.generated.schema", "/api/schema-service/v1"),
    ServiceSpec("entitlements", "osdu_python_client.generated.entitlements", "/api/entitlements/v2"),
    ServiceSpec("legal", "osdu_python_client.generated.legal", "/api/legal/v1"),
    ServiceSpec("file", "osdu_python_client.generated.file", "/api/file/v2"),
    ServiceSpec("dataset", "osdu_python_client.generated.dataset", "/api/dataset/v1"),
    ServiceSpec("indexer", "osdu_python_client.generated.indexer", "/api/indexer/v2"),
    ServiceSpec("notification", "osdu_python_client.generated.notification", "/api/notification/v1"),
    ServiceSpec("partition", "osdu_python_client.generated.partition", "/api/partition/v1"),
    ServiceSpec("policy", "osdu_python_client.generated.policy", "/api/policy/v1"),
    ServiceSpec("register", "osdu_python_client.generated.register", "/api/register/v1"),
    ServiceSpec("unit", "osdu_python_client.generated.unit", "/api/unit/v3"),
    ServiceSpec("crs_catalog", "osdu_python_client.generated.crs_catalog", "/api/crs/catalog/v2"),
    ServiceSpec("crs_conversion", "osdu_python_client.generated.crs_conversion", "/api/crs/converter/v2"),
    ServiceSpec("wellbore_ddms", "osdu_python_client.generated.wellbore_ddms", "/api/os-wellbore-ddms"),
    ServiceSpec("workflow", "osdu_python_client.generated.ingestion_workflow_service", "/api/workflow/v1"),
)

SERVICE_BY_ATTR: dict[str, ServiceSpec] = {s.attr: s for s in SERVICE_REGISTRY}


def load_authenticated_client(spec: ServiceSpec) -> type:
    module = importlib.import_module(f"{spec.module}.client")
    return module.AuthenticatedClient
