"""AWS auth providers (placeholder).

OSDU-on-AWS deployments typically authenticate via Cognito user pools or
direct AWS IAM signing. This module is a stub for the registry; a real
implementation should:

1. Add ``boto3`` (or ``warrant``/``pycognito`` for SRP-based user-pool flows)
   under ``[project.optional-dependencies].aws`` in ``pyproject.toml``.
2. Define an AWS-specific settings class similar to ``AzureMsalConfig``
   (e.g. ``AwsCognitoConfig`` with ``region``, ``user_pool_id``, ``client_id``,
   ``username``, ``password`` env vars).
3. Implement a ``TokenProvider`` that returns a usable bearer token — typically
   the Cognito ID token, exchanged for a fresh one on ``force_refresh``.
4. Replace the placeholder ``_factory`` below with the real one.

Until that's done, selecting ``auth_provider="aws_cognito"`` will fail with
the message below at provider-build time, not import time.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from osdu_python_client.auth._base import TokenProvider, register_provider

if TYPE_CHECKING:
    from osdu_python_client.config import OsduConfig


def _factory(_config: "OsduConfig") -> TokenProvider:
    raise NotImplementedError(
        "auth_provider='aws_cognito' is not yet implemented. "
        "Implement a TokenProvider for your AWS auth flow and either "
        "register it via osdu_python_client.auth.register_provider() "
        "or pass it directly to OsduClient(token_provider=...)."
    )


register_provider("aws_cognito", _factory)
