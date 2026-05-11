from __future__ import annotations

import logging
from typing import TYPE_CHECKING, Callable, Protocol, runtime_checkable

from osdu_python_client.errors import OsduConfigError

if TYPE_CHECKING:
    from osdu_python_client.config import OsduConfig

log = logging.getLogger(__name__)


@runtime_checkable
class TokenProvider(Protocol):
    """The single auth extension point.

    Implementations must return a non-empty bearer token string. ``force_refresh``
    is a hint: the transport sets it to ``True`` after a 401 to force a fresh
    fetch rather than reuse a cached token.
    """

    def get_token(self, force_refresh: bool = False) -> str: ...


TokenProviderFactory = Callable[["OsduConfig"], TokenProvider]

_REGISTRY: dict[str, TokenProviderFactory] = {}


def register_provider(name: str, factory: TokenProviderFactory) -> None:
    """Register a CSP-specific token provider factory under ``name``.

    Calling ``register_provider("azure_msal", factory)`` lets users select it
    via ``OsduConfig.auth_provider = "azure_msal"``. Built-in providers live
    in ``osdu_python_client.auth.<csp>`` and self-register on import.
    """
    if name in _REGISTRY:
        log.debug("re-registering auth provider %r", name)
    _REGISTRY[name] = factory


def registered_providers() -> list[str]:
    return sorted(_REGISTRY)


def provider_for(config: "OsduConfig") -> TokenProvider:
    """Build the provider selected by ``config.auth_provider``.

    Callers that want full control should bypass this and pass their own
    ``TokenProvider`` to ``OsduClient(token_provider=...)``.
    """
    factory = _REGISTRY.get(config.auth_provider)
    if factory is None:
        raise OsduConfigError(
            f"auth_provider={config.auth_provider!r} is not registered. "
            f"Available providers: {registered_providers()}. "
            f"For unsupported CSPs, pass token_provider=... to OsduClient directly."
        )
    return factory(config)
