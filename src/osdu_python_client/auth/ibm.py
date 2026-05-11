"""IBM Cloud auth providers (placeholder).

OSDU-on-IBM deployments typically authenticate via IBM Cloud IAM using an
API key that's exchanged for an access token. A real implementation should:

1. Add ``ibm-cloud-sdk-core`` under ``[project.optional-dependencies].ibm``.
2. Implement a ``TokenProvider`` that wraps ``IAMAuthenticator(apikey=...)``,
   calls ``authenticator.token_manager.get_token()`` (which caches and refreshes),
   and returns the token string.
3. Replace the placeholder ``_factory`` below.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from osdu_python_client.auth._base import TokenProvider, register_provider

if TYPE_CHECKING:
    from osdu_python_client.config import OsduConfig


def _factory(_config: "OsduConfig") -> TokenProvider:
    raise NotImplementedError(
        "auth_provider='ibm_iam' is not yet implemented. "
        "Implement a TokenProvider for your IBM Cloud auth flow and either "
        "register it via osdu_python_client.auth.register_provider() "
        "or pass it directly to OsduClient(token_provider=...)."
    )


register_provider("ibm_iam", _factory)
