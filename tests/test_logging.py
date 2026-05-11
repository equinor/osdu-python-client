from __future__ import annotations

import logging

import httpx
import pytest

from osdu_python_client import enable_debug_logging
from osdu_python_client.transport import (
    RetryTransport,
    _redact_headers,
    _truncate_body,
)


SECRET = "supersecret-token-value"


class FakeProvider:
    def __init__(self, tokens: list[str]) -> None:
        self._tokens = list(tokens)

    def get_token(self, force_refresh: bool = False) -> str:
        return self._tokens.pop(0) if self._tokens else SECRET


def _mock(handler) -> httpx.MockTransport:
    return httpx.MockTransport(handler)


def test_redact_headers_masks_sensitive_keys():
    headers = {
        "Authorization": "Bearer abc",
        "Cookie": "sessionid=xyz",
        "Set-Cookie": "id=1",
        "Proxy-Authorization": "Basic 123",
        "Content-Type": "application/json",
        "data-partition-id": "p",
    }
    redacted = _redact_headers(headers)
    assert redacted["Authorization"] == "***REDACTED***"
    assert redacted["Cookie"] == "***REDACTED***"
    assert redacted["Set-Cookie"] == "***REDACTED***"
    assert redacted["Proxy-Authorization"] == "***REDACTED***"
    assert redacted["Content-Type"] == "application/json"
    assert redacted["data-partition-id"] == "p"


def test_truncate_body_truncates_long_payloads():
    text = "x" * 5000
    out = _truncate_body(text)
    assert out.startswith("x" * 2048)
    assert "truncated" in out


def test_truncate_body_handles_bytes_and_none():
    assert _truncate_body(None) == "<none>"
    assert _truncate_body(b'{"k":"v"}') == '{"k":"v"}'


def test_no_token_appears_in_logs(caplog: pytest.LogCaptureFixture):
    """Critical: the bearer token must never appear in any emitted log
    record at any level, no matter what we do — request, response, retry."""

    sequence = [
        httpx.Response(429, headers={"Retry-After": "0"}),
        httpx.Response(401),
        httpx.Response(200, json={"ok": True}),
    ]

    def handler(_: httpx.Request) -> httpx.Response:
        return sequence.pop(0)

    provider = FakeProvider([SECRET, SECRET, SECRET])
    transport = RetryTransport(
        provider, inner=_mock(handler), sleep=lambda _: None, max_attempts=5
    )
    client = httpx.Client(transport=transport, base_url="https://x")

    caplog.set_level(logging.DEBUG, logger="osdu_python_client")
    logging.getLogger("osdu_python_client.transport.body").setLevel(logging.DEBUG)
    try:
        client.get("/")
    finally:
        logging.getLogger("osdu_python_client.transport.body").setLevel(logging.WARNING)

    all_log_text = "\n".join(r.getMessage() for r in caplog.records)
    assert SECRET not in all_log_text, "token leaked into logs!"
    # And specifically: redacted marker should appear
    assert "***REDACTED***" in all_log_text


def test_retry_decision_is_logged_at_info(caplog: pytest.LogCaptureFixture):
    sequence = [
        httpx.Response(503, headers={"Retry-After": "0"}),
        httpx.Response(200, json={"ok": True}),
    ]

    def handler(_: httpx.Request) -> httpx.Response:
        return sequence.pop(0)

    provider = FakeProvider(["t"])
    transport = RetryTransport(
        provider, inner=_mock(handler), sleep=lambda _: None, max_attempts=3
    )
    client = httpx.Client(transport=transport, base_url="https://x")

    caplog.set_level(logging.INFO, logger="osdu_python_client.transport")
    client.get("/")

    messages = [r.getMessage() for r in caplog.records]
    assert any("retryable status 503" in m for m in messages), messages


def test_401_force_refresh_is_logged_at_info(caplog: pytest.LogCaptureFixture):
    sequence = [
        httpx.Response(401),
        httpx.Response(200, json={"ok": True}),
    ]

    def handler(_: httpx.Request) -> httpx.Response:
        return sequence.pop(0)

    provider = FakeProvider(["stale", "fresh"])
    transport = RetryTransport(
        provider, inner=_mock(handler), sleep=lambda _: None, max_attempts=3
    )
    client = httpx.Client(transport=transport, base_url="https://x")

    caplog.set_level(logging.INFO, logger="osdu_python_client.transport")
    client.get("/")

    messages = [r.getMessage() for r in caplog.records]
    assert any("forcing token refresh" in m for m in messages), messages


def test_exhaustion_logged_at_warning(caplog: pytest.LogCaptureFixture):
    def handler(_: httpx.Request) -> httpx.Response:
        return httpx.Response(503, headers={"Retry-After": "0"})

    provider = FakeProvider(["t"] * 5)
    transport = RetryTransport(
        provider, inner=_mock(handler), sleep=lambda _: None, max_attempts=3
    )
    client = httpx.Client(transport=transport, base_url="https://x")

    caplog.set_level(logging.WARNING, logger="osdu_python_client.transport")
    client.get("/")

    warnings = [
        r for r in caplog.records
        if r.levelno == logging.WARNING and "retries exhausted" in r.getMessage()
    ]
    assert warnings, "expected a WARNING about retry exhaustion"


def test_enable_debug_logging_flips_levels():
    lib = logging.getLogger("osdu_python_client")
    body = logging.getLogger("osdu_python_client.transport.body")

    prior_lib_level = lib.level
    prior_lib_handlers = list(lib.handlers)
    prior_body_level = body.level
    try:
        enable_debug_logging(include_bodies=False)
        assert lib.level == logging.DEBUG
        assert body.level == logging.WARNING

        enable_debug_logging(include_bodies=True)
        assert body.level == logging.DEBUG
    finally:
        lib.setLevel(prior_lib_level)
        body.setLevel(prior_body_level)
        # Remove handlers we added
        for h in list(lib.handlers):
            if h not in prior_lib_handlers:
                lib.removeHandler(h)


def test_body_logger_off_by_default(caplog: pytest.LogCaptureFixture):
    """With only the parent logger at DEBUG (no include_bodies), bodies must
    stay out of the log stream — the body logger has its own level set."""

    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(429, headers={"Retry-After": "0"}, json={"err": "secret-payload"})

    provider = FakeProvider(["t"] * 5)
    transport = RetryTransport(
        provider, inner=_mock(handler), sleep=lambda _: None, max_attempts=2
    )
    client = httpx.Client(transport=transport, base_url="https://x")

    caplog.set_level(logging.DEBUG, logger="osdu_python_client")
    # Explicitly do NOT lift the body logger
    logging.getLogger("osdu_python_client.transport.body").setLevel(logging.WARNING)

    client.post("/q", json={"private": "data"})

    all_log_text = "\n".join(r.getMessage() for r in caplog.records)
    assert "secret-payload" not in all_log_text
    assert "private" not in all_log_text
