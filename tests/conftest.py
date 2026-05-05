# tests/conftest.py

from tests.config import config
from tests.auth_fixture import msal_token_cache, access_token
from tests.osdu_fixture import osdu, osdu_config, static_token_provider

__all__ = [
    "access_token",
    "config",
    "msal_token_cache",
    "osdu",
    "osdu_config",
    "static_token_provider",
]
