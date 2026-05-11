from __future__ import annotations

from types import SimpleNamespace
from typing import Any

import httpx
import pytest

from osdu_python_client.errors import OsduError
from osdu_python_client.services.facade import Endpoint, ServiceFacade, _unwrap


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


def _install_mock_transport(client: Any, handler: Any) -> None:
    client._transport._inner = httpx.MockTransport(handler)


def _fake_response(status: int, parsed: Any = None) -> SimpleNamespace:
    return SimpleNamespace(status_code=status, parsed=parsed)


def _fake_op(*, sync_response=None, async_response=None, accepts_partition: bool = True):
    captured: dict[str, Any] = {"sync": [], "async": []}

    def sync_detailed(*, client, data_partition_id=None, body=None):
        captured["sync"].append({"client": client, "partition": data_partition_id, "body": body})
        return sync_response

    async def asyncio_detailed(*, client, data_partition_id=None, body=None):
        captured["async"].append({"client": client, "partition": data_partition_id, "body": body})
        return async_response

    if not accepts_partition:
        def sync_detailed(*, client, body=None):  # type: ignore[no-redef]
            captured["sync"].append({"client": client, "body": body})
            return sync_response

        async def asyncio_detailed(*, client, body=None):  # type: ignore[no-redef]
            captured["async"].append({"client": client, "body": body})
            return async_response

    mod = SimpleNamespace(sync_detailed=sync_detailed, asyncio_detailed=asyncio_detailed)
    mod.__name__ = "fake_op"
    return mod, captured


def test_endpoint_default_call_unwraps_and_binds():
    mod, captured = _fake_op(sync_response=_fake_response(200, parsed={"ok": True}))
    ep = Endpoint(mod, client="C", partition="P", is_async=False)

    result = ep(body="REQ")
    assert result == {"ok": True}
    assert captured["sync"] == [{"client": "C", "partition": "P", "body": "REQ"}]


def test_endpoint_default_call_raises_on_non_2xx():
    mod, _ = _fake_op(sync_response=_fake_response(404, parsed={"error": "nope"}))
    ep = Endpoint(mod, client="C", partition="P", is_async=False)
    with pytest.raises(OsduError):
        ep(body="REQ")


def test_unwrap_falls_back_to_response_content_when_parsed_is_none():
    response = SimpleNamespace(
        status_code=401,
        parsed=None,
        content=b'{"code":401,"reason":"Unauthorized","message":"token expired"}',
    )
    mod, _ = _fake_op(sync_response=response)
    ep = Endpoint(mod, client="C", partition="P", is_async=False)
    with pytest.raises(OsduError, match="token expired"):
        ep(body="REQ")


def test_endpoint_detailed_returns_envelope():
    response = _fake_response(500, parsed={"error": "boom"})
    mod, _ = _fake_op(sync_response=response)
    ep = Endpoint(mod, client="C", partition="P", is_async=False)

    assert ep.detailed(body="REQ") is response


def test_endpoint_explicit_partition_is_not_overridden():
    mod, captured = _fake_op(sync_response=_fake_response(200, parsed=None))
    ep = Endpoint(mod, client="C", partition="DEFAULT", is_async=False)
    ep(body="REQ", data_partition_id="EXPLICIT")
    assert captured["sync"][0]["partition"] == "EXPLICIT"


def test_endpoint_skips_partition_for_ops_that_dont_accept_it():
    mod, captured = _fake_op(
        sync_response=_fake_response(200, parsed=None), accepts_partition=False
    )
    ep = Endpoint(mod, client="C", partition="P", is_async=False)
    ep(body="REQ")
    assert captured["sync"][0] == {"client": "C", "body": "REQ"}


async def test_endpoint_async_call_unwraps():
    mod, captured = _fake_op(async_response=_fake_response(200, parsed="DTO"))
    ep = Endpoint(mod, client="C", partition="P", is_async=True)

    result = await ep(body="REQ")
    assert result == "DTO"
    assert captured["async"] == [{"client": "C", "partition": "P", "body": "REQ"}]


def test_unwrap_accepts_enum_status_code():
    class Code:
        value = 200

    assert _unwrap(SimpleNamespace(status_code=Code(), parsed="x")) == "x"


def test_unwrap_accepts_int_status_code():
    assert _unwrap(SimpleNamespace(status_code=204, parsed=None)) is None


def test_service_facade_falls_through_to_client_for_unknown_names():
    facade = ServiceFacade(
        "osdu_python_client.generated.search",
        client=SimpleNamespace(get_httpx_client=lambda: "the-client"),
        partition="P",
        is_async=False,
    )
    assert facade.get_httpx_client() == "the-client"


def test_service_facade_resolves_endpoint_by_name():
    from osdu_python_client.client import OsduClient
    from osdu_python_client.config import OsduConfig

    osdu = OsduClient(config=OsduConfig(), token_provider=StaticProvider())
    try:
        ep = osdu.search.query_records
        assert isinstance(ep, Endpoint)
    finally:
        osdu.close()


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


def test_endpoint_overrides_replace_default_endpoint():
    from osdu_python_client import OsduClient, OsduConfig

    config = OsduConfig(endpoint_overrides={"search": "/api/search/v3"})
    osdu = OsduClient(config=config, token_provider=StaticProvider())
    try:
        assert str(osdu.search.get_httpx_client().base_url).rstrip("/") == (
            "https://example.invalid/api/search/v3"
        )
    finally:
        osdu.close()


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
