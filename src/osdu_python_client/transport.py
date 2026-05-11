from __future__ import annotations

import logging
import random
import time
from typing import Iterable, Mapping

import httpx

from osdu_python_client.auth import TokenProvider
from osdu_python_client.errors import OsduRetryExhausted

DEFAULT_RETRY_STATUSES: frozenset[int] = frozenset({429, 502, 503, 504})

log = logging.getLogger(__name__)
body_log = logging.getLogger(__name__ + ".body")
# Off by default — opt in via enable_debug_logging(include_bodies=True) or by
# setting this logger's level directly. Keeps payloads (often PII-heavy) out
# of logs unless explicitly requested, even when the parent logger is at DEBUG.
body_log.setLevel(logging.WARNING)

_SENSITIVE_HEADERS: frozenset[str] = frozenset(
    {"authorization", "cookie", "proxy-authorization", "set-cookie"}
)
_BODY_LOG_MAX = 2048


def _redact_headers(headers: Mapping[str, str]) -> dict[str, str]:
    return {
        k: ("***REDACTED***" if k.lower() in _SENSITIVE_HEADERS else v)
        for k, v in headers.items()
    }


def _truncate_body(content: bytes | str | None) -> str:
    if content is None:
        return "<none>"
    if isinstance(content, bytes):
        text = content.decode("utf-8", errors="replace")
    else:
        text = content
    if len(text) > _BODY_LOG_MAX:
        return f"{text[:_BODY_LOG_MAX]}... [truncated {len(text) - _BODY_LOG_MAX} bytes]"
    return text


def _log_request(request: httpx.Request) -> None:
    log.debug("→ %s %s", request.method, request.url)
    if log.isEnabledFor(logging.DEBUG):
        log.debug("  headers=%s", _redact_headers(request.headers))
    if body_log.isEnabledFor(logging.DEBUG):
        body_log.debug("→ %s %s body=%s", request.method, request.url, _truncate_body(request.content))


def _log_response(request: httpx.Request, response: httpx.Response, elapsed_ms: float) -> None:
    log.debug(
        "← %d %s %s (%.1fms)",
        response.status_code, request.method, request.url, elapsed_ms,
    )


def _log_response_body(response: httpx.Response) -> None:
    # Only safe to call when the caller has already materialized the response
    # (we call .read() before retrying, so this is OK on retry paths).
    if body_log.isEnabledFor(logging.DEBUG):
        body_log.debug("← body=%s", _truncate_body(response.content))


class RetryTransport(httpx.BaseTransport):
    def __init__(
        self,
        token_provider: TokenProvider,
        inner: httpx.BaseTransport | None = None,
        max_attempts: int = 3,
        base_delay: float = 0.5,
        retry_statuses: Iterable[int] = DEFAULT_RETRY_STATUSES,
        sleep: callable = time.sleep,
    ) -> None:
        self._provider = token_provider
        self._inner = inner or httpx.HTTPTransport(retries=2)
        self._max_attempts = max_attempts
        self._base_delay = base_delay
        self._retry_statuses = frozenset(retry_statuses)
        self._sleep = sleep

    def _set_auth(self, request: httpx.Request, force_refresh: bool) -> None:
        token = self._provider.get_token(force_refresh=force_refresh)
        request.headers["Authorization"] = f"Bearer {token}"

    def _backoff(self, attempt: int, response: httpx.Response | None) -> float:
        if response is not None:
            retry_after = response.headers.get("Retry-After")
            if retry_after:
                try:
                    return max(0.0, float(retry_after))
                except ValueError:
                    pass
        return self._base_delay * (2**attempt) + random.uniform(0, self._base_delay)

    def handle_request(self, request: httpx.Request) -> httpx.Response:
        self._set_auth(request, force_refresh=False)
        _log_request(request)

        last_response: httpx.Response | None = None
        refreshed_for_401 = False

        for attempt in range(self._max_attempts):
            started = time.perf_counter()
            response = self._inner.handle_request(request)
            elapsed_ms = (time.perf_counter() - started) * 1000.0
            _log_response(request, response, elapsed_ms)

            if response.status_code == 401 and not refreshed_for_401:
                response.read()
                _log_response_body(response)
                response.close()
                log.info("401 from %s — forcing token refresh", request.url)
                self._set_auth(request, force_refresh=True)
                refreshed_for_401 = True
                continue

            if response.status_code in self._retry_statuses:
                last_response = response
                if attempt == self._max_attempts - 1:
                    response.read()
                    _log_response_body(response)
                    log.warning(
                        "retries exhausted after %d attempts, last status %d for %s",
                        self._max_attempts, response.status_code, request.url,
                    )
                    return response
                delay = self._backoff(attempt, response)
                response.read()
                _log_response_body(response)
                response.close()
                log.info(
                    "retryable status %d (attempt %d/%d) — sleeping %.2fs",
                    response.status_code, attempt + 1, self._max_attempts, delay,
                )
                self._sleep(delay)
                continue

            if body_log.isEnabledFor(logging.DEBUG):
                response.read()
                _log_response_body(response)
            return response

        if last_response is not None:
            raise OsduRetryExhausted(
                f"Retries exhausted ({self._max_attempts}) — last status {last_response.status_code}",
                status_code=last_response.status_code,
            )
        raise OsduRetryExhausted(f"Retries exhausted ({self._max_attempts})")

    def close(self) -> None:
        self._inner.close()


class AsyncRetryTransport(httpx.AsyncBaseTransport):
    def __init__(
        self,
        token_provider: TokenProvider,
        inner: httpx.AsyncBaseTransport | None = None,
        max_attempts: int = 3,
        base_delay: float = 0.5,
        retry_statuses: Iterable[int] = DEFAULT_RETRY_STATUSES,
    ) -> None:
        self._provider = token_provider
        self._inner = inner or httpx.AsyncHTTPTransport(retries=2)
        self._max_attempts = max_attempts
        self._base_delay = base_delay
        self._retry_statuses = frozenset(retry_statuses)

    def _set_auth(self, request: httpx.Request, force_refresh: bool) -> None:
        token = self._provider.get_token(force_refresh=force_refresh)
        request.headers["Authorization"] = f"Bearer {token}"

    def _backoff(self, attempt: int, response: httpx.Response | None) -> float:
        if response is not None:
            retry_after = response.headers.get("Retry-After")
            if retry_after:
                try:
                    return max(0.0, float(retry_after))
                except ValueError:
                    pass
        return self._base_delay * (2**attempt) + random.uniform(0, self._base_delay)

    async def handle_async_request(self, request: httpx.Request) -> httpx.Response:
        import asyncio

        self._set_auth(request, force_refresh=False)
        _log_request(request)
        last_response: httpx.Response | None = None
        refreshed_for_401 = False

        for attempt in range(self._max_attempts):
            started = time.perf_counter()
            response = await self._inner.handle_async_request(request)
            elapsed_ms = (time.perf_counter() - started) * 1000.0
            _log_response(request, response, elapsed_ms)

            if response.status_code == 401 and not refreshed_for_401:
                await response.aread()
                _log_response_body(response)
                await response.aclose()
                log.info("401 from %s — forcing token refresh", request.url)
                self._set_auth(request, force_refresh=True)
                refreshed_for_401 = True
                continue

            if response.status_code in self._retry_statuses:
                last_response = response
                if attempt == self._max_attempts - 1:
                    await response.aread()
                    _log_response_body(response)
                    log.warning(
                        "retries exhausted after %d attempts, last status %d for %s",
                        self._max_attempts, response.status_code, request.url,
                    )
                    return response
                delay = self._backoff(attempt, response)
                await response.aread()
                _log_response_body(response)
                await response.aclose()
                log.info(
                    "retryable status %d (attempt %d/%d) — sleeping %.2fs",
                    response.status_code, attempt + 1, self._max_attempts, delay,
                )
                await asyncio.sleep(delay)
                continue

            if body_log.isEnabledFor(logging.DEBUG):
                await response.aread()
                _log_response_body(response)
            return response

        if last_response is not None:
            raise OsduRetryExhausted(
                f"Retries exhausted ({self._max_attempts}) — last status {last_response.status_code}",
                status_code=last_response.status_code,
            )
        raise OsduRetryExhausted(f"Retries exhausted ({self._max_attempts})")

    async def aclose(self) -> None:
        await self._inner.aclose()
