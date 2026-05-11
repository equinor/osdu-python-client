"""GCP auth providers (placeholder).

OSDU-on-GCP deployments typically authenticate via Google Cloud IAM, using
service-account JSON keys, Application Default Credentials, or workload
identity. A real implementation should:

1. Add ``google-auth`` under ``[project.optional-dependencies].gcp``.
2. Implement a ``TokenProvider`` that wraps ``google.auth.default()`` or
   ``google.oauth2.service_account.Credentials.from_service_account_file()``,
   calls ``credentials.refresh(google.auth.transport.requests.Request())``,
   and returns ``credentials.token``.
3. Replace the placeholder ``_factory`` below.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from osdu_python_client.auth._base import TokenProvider, register_provider

if TYPE_CHECKING:
    from osdu_python_client.config import OsduConfig


def _factory(_config: "OsduConfig") -> TokenProvider:
    raise NotImplementedError(
        "auth_provider='gcp_iam' is not yet implemented. "
        "Implement a TokenProvider for your GCP auth flow and either "
        "register it via osdu_python_client.auth.register_provider() "
        "or pass it directly to OsduClient(token_provider=...)."
    )


register_provider("gcp_iam", _factory)
