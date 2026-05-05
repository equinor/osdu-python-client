from __future__ import annotations

import importlib
from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class ServiceSpec:
    """Single source of truth wiring a facade attribute to a generated client.

    - ``attr``: property name exposed on ``OsduClient`` / ``AsyncOsduClient``
      (e.g. ``"search"``, ``"workflow"``).
    - ``module``: the generated package path, e.g. ``"osdu_python_client.generated.search"``.
      ``<module>.client.AuthenticatedClient`` is imported on first access.
    - ``config_url_attr``: attribute on ``OsduConfig`` returning the base URL,
      e.g. ``"search_url"``.
    - ``sync_wrapper`` / ``async_wrapper``: optional ``"pkg.module:ClassName"``
      targets for ergonomic wrappers around the raw ``AuthenticatedClient``.
      The wrapper is invoked as ``Wrapper(generated_client, data_partition_id)``.
    """

    attr: str
    module: str
    config_url_attr: str
    sync_wrapper: str | None = None
    async_wrapper: str | None = None


SERVICE_REGISTRY: tuple[ServiceSpec, ...] = (
    ServiceSpec(
        "search",
        "osdu_python_client.generated.search",
        "search_url",
        sync_wrapper="osdu_python_client.services.search:SearchService",
        async_wrapper="osdu_python_client.services.search:AsyncSearchService",
    ),
    ServiceSpec("storage", "osdu_python_client.generated.storage", "storage_url"),
    ServiceSpec("schema", "osdu_python_client.generated.schema", "schema_url"),
    ServiceSpec("entitlements", "osdu_python_client.generated.entitlements", "entitlements_url"),
    ServiceSpec("legal", "osdu_python_client.generated.legal", "legal_url"),
    ServiceSpec("file", "osdu_python_client.generated.file", "file_url"),
    ServiceSpec("dataset", "osdu_python_client.generated.dataset", "dataset_url"),
    ServiceSpec("indexer", "osdu_python_client.generated.indexer", "indexer_url"),
    ServiceSpec("notification", "osdu_python_client.generated.notification", "notification_url"),
    ServiceSpec("partition", "osdu_python_client.generated.partition", "partition_url"),
    ServiceSpec("policy", "osdu_python_client.generated.policy", "policy_url"),
    ServiceSpec("register", "osdu_python_client.generated.register", "register_url"),
    ServiceSpec("unit", "osdu_python_client.generated.unit", "unit_url"),
    ServiceSpec("crs_catalog", "osdu_python_client.generated.crs_catalog", "crs_catalog_url"),
    ServiceSpec(
        "crs_conversion", "osdu_python_client.generated.crs_conversion", "crs_converter_url"
    ),
    ServiceSpec("wellbore_ddms", "osdu_python_client.generated.wellbore_ddms", "wellbore_ddms_url"),
    ServiceSpec(
        "workflow", "osdu_python_client.generated.ingestion_workflow_service", "workflow_url"
    ),
)

SERVICE_BY_ATTR: dict[str, ServiceSpec] = {s.attr: s for s in SERVICE_REGISTRY}


def import_target(target: str) -> Any:
    module_path, _, qualname = target.partition(":")
    obj: Any = importlib.import_module(module_path)
    if qualname:
        for part in qualname.split("."):
            obj = getattr(obj, part)
    return obj


def load_authenticated_client(spec: ServiceSpec) -> type:
    module = importlib.import_module(f"{spec.module}.client")
    return module.AuthenticatedClient
