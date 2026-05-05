from __future__ import annotations

import os

import httpx
import pytest


@pytest.fixture(autouse=True)
def _env(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("SERVER", "https://example.invalid")
    monkeypatch.setenv("DATA_PARTITION_ID", "test-partition")
    monkeypatch.setenv("AUTHORITY", "https://login.example/tenant")
    monkeypatch.setenv("SCOPES", "scope/.default")
    monkeypatch.setenv("CLIENT_ID", "client-id")
    monkeypatch.setenv("AUTH_MODE", "interactive")
    monkeypatch.delenv("OSDU_MSAL_CACHE_PATH", raising=False)


class StaticProvider:
    def get_token(self, force_refresh: bool = False) -> str:
        return "tok"


def _install_mock_transport(client, handler) -> None:
    """Replace the wrapped inner transport on the OsduClient's RetryTransport."""
    client._transport._inner = httpx.MockTransport(handler)


def test_with_headers_scopes_to_one_service():
    from osdu_python_client import OsduClient, OsduConfig

    seen: list[dict[str, str]] = []

    def handler(request: httpx.Request) -> httpx.Response:
        seen.append(dict(request.headers))
        return httpx.Response(200, json={})

    osdu = OsduClient(config=OsduConfig(), token_provider=StaticProvider())
    _install_mock_transport(osdu, handler)
    try:
        osdu.search.get_httpx_client().get("/q")
        osdu.storage.get_httpx_client().get("/r")

        with osdu.with_headers(service="search", **{"frame-of-reference": "units=SI"}):
            osdu.search.get_httpx_client().get("/q")
            osdu.storage.get_httpx_client().get("/r")

        osdu.search.get_httpx_client().get("/q")
    finally:
        osdu.close()

    # 5 requests captured, in order:
    # 0: search no header
    # 1: storage no header
    # 2: search WITH header (scoped)
    # 3: storage no header (scoped to search only)
    # 4: search no header (restored)
    assert "frame-of-reference" not in seen[0]
    assert "frame-of-reference" not in seen[1]
    assert seen[2]["frame-of-reference"] == "units=SI"
    assert "frame-of-reference" not in seen[3]
    assert "frame-of-reference" not in seen[4]


def test_with_headers_global_applies_to_all_built_clients():
    from osdu_python_client import OsduClient, OsduConfig

    seen: list[dict[str, str]] = []

    def handler(request: httpx.Request) -> httpx.Response:
        seen.append(dict(request.headers))
        return httpx.Response(200, json={})

    osdu = OsduClient(config=OsduConfig(), token_provider=StaticProvider())
    _install_mock_transport(osdu, handler)
    try:
        osdu.search.get_httpx_client().get("/q")
        osdu.storage.get_httpx_client().get("/r")

        with osdu.with_headers(**{"x-correlation-id": "abc"}):
            osdu.search.get_httpx_client().get("/q")
            osdu.storage.get_httpx_client().get("/r")
    finally:
        osdu.close()

    assert seen[0].get("x-correlation-id") is None
    assert seen[1].get("x-correlation-id") is None
    assert seen[2]["x-correlation-id"] == "abc"
    assert seen[3]["x-correlation-id"] == "abc"


def test_partition_header_is_default_injected():
    from osdu_python_client import OsduClient, OsduConfig

    seen: list[str] = []

    def handler(request: httpx.Request) -> httpx.Response:
        seen.append(request.headers["data-partition-id"])
        return httpx.Response(200, json={})

    osdu = OsduClient(config=OsduConfig(), token_provider=StaticProvider())
    _install_mock_transport(osdu, handler)
    try:
        osdu.search.get_httpx_client().get("/q")
    finally:
        osdu.close()

    assert seen == ["test-partition"]


async def test_async_with_headers_scoped():
    from osdu_python_client import AsyncOsduClient, OsduConfig

    seen: list[dict[str, str]] = []

    def handler(request: httpx.Request) -> httpx.Response:
        seen.append(dict(request.headers))
        return httpx.Response(200, json={})

    osdu = AsyncOsduClient(config=OsduConfig(), token_provider=StaticProvider())
    osdu._transport._inner = httpx.MockTransport(handler)
    try:
        await osdu.search.get_async_httpx_client().get("/q")
        async with osdu.with_headers(service="search", **{"frame-of-reference": "units=SI"}):
            await osdu.search.get_async_httpx_client().get("/q")
        await osdu.search.get_async_httpx_client().get("/q")
    finally:
        await osdu.aclose()

    assert "frame-of-reference" not in seen[0]
    assert seen[1]["frame-of-reference"] == "units=SI"
    assert "frame-of-reference" not in seen[2]
