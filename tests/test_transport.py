from __future__ import annotations

import httpx
import pytest

from osdu_python_client.errors import OsduRetryExhausted
from osdu_python_client.transport import RetryTransport


class FakeProvider:
    def __init__(self, tokens: list[str]) -> None:
        self._tokens = list(tokens)
        self.calls: list[bool] = []

    def get_token(self, force_refresh: bool = False) -> str:
        self.calls.append(force_refresh)
        return self._tokens.pop(0) if self._tokens else "default"


def _mock(handler) -> httpx.MockTransport:
    return httpx.MockTransport(handler)


def test_auth_header_injected_on_success():
    seen: list[str] = []

    def handler(request: httpx.Request) -> httpx.Response:
        seen.append(request.headers["Authorization"])
        return httpx.Response(200, json={"ok": True})

    provider = FakeProvider(["t1"])
    transport = RetryTransport(provider, inner=_mock(handler), sleep=lambda _: None)
    client = httpx.Client(transport=transport, base_url="https://x")

    r = client.get("/")
    assert r.status_code == 200
    assert seen == ["Bearer t1"]
    assert provider.calls == [False]


def test_401_triggers_one_force_refresh_then_succeeds():
    sequence = [
        httpx.Response(401, json={"error": "expired"}),
        httpx.Response(200, json={"ok": True}),
    ]
    auth_seen: list[str] = []

    def handler(request: httpx.Request) -> httpx.Response:
        auth_seen.append(request.headers["Authorization"])
        return sequence.pop(0)

    provider = FakeProvider(["stale", "fresh"])
    transport = RetryTransport(provider, inner=_mock(handler), sleep=lambda _: None)
    client = httpx.Client(transport=transport, base_url="https://x")

    r = client.get("/")
    assert r.status_code == 200
    assert auth_seen == ["Bearer stale", "Bearer fresh"]
    assert provider.calls == [False, True]


def test_429_with_retry_after_is_honoured_and_retries_succeed():
    sequence = [
        httpx.Response(429, headers={"Retry-After": "0"}),
        httpx.Response(200, json={"ok": True}),
    ]
    sleeps: list[float] = []

    def handler(_: httpx.Request) -> httpx.Response:
        return sequence.pop(0)

    provider = FakeProvider(["t1"])
    transport = RetryTransport(
        provider, inner=_mock(handler), sleep=sleeps.append, max_attempts=3
    )
    client = httpx.Client(transport=transport, base_url="https://x")

    r = client.get("/")
    assert r.status_code == 200
    assert sleeps == [0.0]


def test_retries_exhausted_raises():
    def handler(_: httpx.Request) -> httpx.Response:
        return httpx.Response(503, headers={"Retry-After": "0"})

    provider = FakeProvider(["t"] * 5)
    transport = RetryTransport(
        provider, inner=_mock(handler), sleep=lambda _: None, max_attempts=3
    )
    client = httpx.Client(transport=transport, base_url="https://x")

    # On the final attempt the transport returns the response rather than raising.
    r = client.get("/")
    assert r.status_code == 503


def test_non_retryable_status_returned_immediately():
    calls = {"n": 0}

    def handler(_: httpx.Request) -> httpx.Response:
        calls["n"] += 1
        return httpx.Response(404, json={"error": "nope"})

    provider = FakeProvider(["t"])
    transport = RetryTransport(provider, inner=_mock(handler), sleep=lambda _: None)
    client = httpx.Client(transport=transport, base_url="https://x")

    r = client.get("/")
    assert r.status_code == 404
    assert calls["n"] == 1


def test_401_then_still_401_returns_response_not_loops():
    def handler(_: httpx.Request) -> httpx.Response:
        return httpx.Response(401, json={"error": "still bad"})

    provider = FakeProvider(["a", "b", "c"])
    transport = RetryTransport(
        provider, inner=_mock(handler), sleep=lambda _: None, max_attempts=3
    )
    client = httpx.Client(transport=transport, base_url="https://x")

    r = client.get("/")
    assert r.status_code == 401
    # First call is normal, second is force_refresh after 401, then no further refresh
    assert provider.calls == [False, True]


def test_partition_default_does_not_override_explicit_header():
    from osdu_python_client.hooks import partition_hook

    seen: dict[str, str] = {}

    def handler(request: httpx.Request) -> httpx.Response:
        seen["partition"] = request.headers["data-partition-id"]
        return httpx.Response(200)

    provider = FakeProvider(["t"])
    transport = RetryTransport(provider, inner=_mock(handler), sleep=lambda _: None)
    client = httpx.Client(
        transport=transport,
        base_url="https://x",
        event_hooks={"request": [partition_hook("default-partition")]},
    )

    client.get("/", headers={"data-partition-id": "explicit"})
    assert seen["partition"] == "explicit"

    client.get("/")
    assert seen["partition"] == "default-partition"


@pytest.mark.asyncio
async def test_async_401_force_refresh_then_succeeds():
    from osdu_python_client.transport import AsyncRetryTransport

    sequence = [
        httpx.Response(401, json={"error": "expired"}),
        httpx.Response(200, json={"ok": True}),
    ]
    auth_seen: list[str] = []

    def handler(request: httpx.Request) -> httpx.Response:
        auth_seen.append(request.headers["Authorization"])
        return sequence.pop(0)

    provider = FakeProvider(["stale", "fresh"])
    transport = AsyncRetryTransport(
        provider, inner=httpx.MockTransport(handler), max_attempts=3
    )
    async with httpx.AsyncClient(transport=transport, base_url="https://x") as client:
        r = await client.get("/")
    assert r.status_code == 200
    assert auth_seen == ["Bearer stale", "Bearer fresh"]
    assert provider.calls == [False, True]


@pytest.mark.asyncio
async def test_async_429_with_retry_after_succeeds():
    from osdu_python_client.transport import AsyncRetryTransport

    sequence = [
        httpx.Response(429, headers={"Retry-After": "0"}),
        httpx.Response(200, json={"ok": True}),
    ]

    def handler(_: httpx.Request) -> httpx.Response:
        return sequence.pop(0)

    provider = FakeProvider(["t"])
    transport = AsyncRetryTransport(
        provider, inner=httpx.MockTransport(handler), max_attempts=3, base_delay=0.0
    )
    async with httpx.AsyncClient(transport=transport, base_url="https://x") as client:
        r = await client.get("/")
    assert r.status_code == 200
