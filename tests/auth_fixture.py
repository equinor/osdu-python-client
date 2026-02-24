import os
import pathlib
from typing import Any

import pytest
from msal import PublicClientApplication

from tests.config import CoreConfig


def _token_cache_path() -> pathlib.Path:
    return pathlib.Path(".msal_token_cache.bin")


@pytest.fixture(scope="session")
def msal_token_cache() -> Any:
    """
    Persistent MSAL cache across test runs (in the repo root).
    """
    cache = os.environ.get("OSDU_MSAL_CACHE_PATH")
    path = pathlib.Path(cache) if cache else _token_cache_path()

    try:
        from msal import SerializableTokenCache  # type: ignore
    except Exception as exc:  # pragma: no cover
        raise RuntimeError("msal is required. Install the `dev` extras.") from exc

    token_cache = SerializableTokenCache()
    if path.exists():
        token_cache.deserialize(path.read_text(encoding="utf-8"))

    yield token_cache

    if token_cache.has_state_changed:
        path.write_text(token_cache.serialize(), encoding="utf-8")


@pytest.fixture(scope="session")
def access_token(config: CoreConfig, msal_token_cache: Any) -> str:
    """
    Acquire an access token using MSAL interactive login.
    Tries cache first, then falls back to interactive.
    """
    app = PublicClientApplication(
        client_id=config.client_id,
        authority=config.authority,
        token_cache=msal_token_cache,
    )

    scopes = config.scopes.split()
    accounts = app.get_accounts()
    result: dict[str, Any] | None = None

    if accounts:
        result = app.acquire_token_silent(scopes=scopes, account=accounts[0])

    if not result or "access_token" not in result:
        result = app.acquire_token_interactive(scopes=scopes)

    token = result.get("access_token") if isinstance(result, dict) else None
    if not token:
        raise RuntimeError(f"Authentication failed: {result}")

    return token
