from __future__ import annotations

from collections.abc import Iterator
from typing import Any

import pytest

from osdu_python_client import OsduClient, OsduConfig
from osdu_python_client.auth import TokenProvider


class _StaticTokenProvider:
    def __init__(self, token: str) -> None:
        self._token = token

    def get_token(self, force_refresh: bool = False) -> str:
        return self._token


@pytest.fixture(scope="session")
def osdu_config() -> OsduConfig:
    return OsduConfig()


@pytest.fixture(scope="session")
def static_token_provider(access_token: str) -> TokenProvider:
    return _StaticTokenProvider(access_token)


@pytest.fixture(scope="session")
def osdu(
    osdu_config: OsduConfig, static_token_provider: TokenProvider
) -> Iterator[OsduClient]:
    client = OsduClient(config=osdu_config, token_provider=static_token_provider)
    try:
        yield client
    finally:
        client.close()
