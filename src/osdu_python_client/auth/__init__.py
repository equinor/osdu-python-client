"""Pluggable auth subsystem.

The core extension point is the :class:`TokenProvider` Protocol. CSP-specific
providers self-register on import. Built-in registry entries:

- ``azure_msal`` — fully implemented (MSAL).
- ``aws_cognito``, ``gcp_iam``, ``ibm_iam`` — stubs; ``_factory`` raises with
  guidance on how to implement.

For unsupported CSPs, pass your own ``TokenProvider`` to ``OsduClient`` and
ignore this whole machinery.
"""

from osdu_python_client.auth._base import (
    TokenProvider,
    TokenProviderFactory,
    provider_for,
    register_provider,
    registered_providers,
)

# Eager imports trigger registry side effects. Each module imports its CSP SDK
# lazily (only when the factory is called), so this is cheap and safe.
from osdu_python_client.auth import aws as _aws  # noqa: F401
from osdu_python_client.auth import azure as _azure  # noqa: F401
from osdu_python_client.auth import gcp as _gcp  # noqa: F401
from osdu_python_client.auth import ibm as _ibm  # noqa: F401
from osdu_python_client.auth.azure import (
    AzureMsalConfig,
    ClientCredentialsProvider,
    MsalDeviceFlowProvider,
    MsalInteractiveProvider,
)

__all__ = [
    "AzureMsalConfig",
    "ClientCredentialsProvider",
    "MsalDeviceFlowProvider",
    "MsalInteractiveProvider",
    "TokenProvider",
    "TokenProviderFactory",
    "provider_for",
    "register_provider",
    "registered_providers",
]
