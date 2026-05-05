from __future__ import annotations

import random
import time
from typing import Iterable

import httpx

from osdu_python_client.auth import TokenProvider
from osdu_python_client.errors import OsduRetryExhausted

DEFAULT_RETRY_STATUSES: frozenset[int] = frozenset({429, 502, 503, 504})


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

        last_response: httpx.Response | None = None
        refreshed_for_401 = False

        for attempt in range(self._max_attempts):
            response = self._inner.handle_request(request)

            if response.status_code == 401 and not refreshed_for_401:
                response.read()
                response.close()
                self._set_auth(request, force_refresh=True)
                refreshed_for_401 = True
                continue

            if response.status_code in self._retry_statuses:
                last_response = response
                if attempt == self._max_attempts - 1:
                    return response
                delay = self._backoff(attempt, response)
                response.read()
                response.close()
                self._sleep(delay)
                continue

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
        last_response: httpx.Response | None = None
        refreshed_for_401 = False

        for attempt in range(self._max_attempts):
            response = await self._inner.handle_async_request(request)

            if response.status_code == 401 and not refreshed_for_401:
                await response.aread()
                await response.aclose()
                self._set_auth(request, force_refresh=True)
                refreshed_for_401 = True
                continue

            if response.status_code in self._retry_statuses:
                last_response = response
                if attempt == self._max_attempts - 1:
                    return response
                delay = self._backoff(attempt, response)
                await response.aread()
                await response.aclose()
                await asyncio.sleep(delay)
                continue

            return response

        if last_response is not None:
            raise OsduRetryExhausted(
                f"Retries exhausted ({self._max_attempts}) — last status {last_response.status_code}",
                status_code=last_response.status_code,
            )
        raise OsduRetryExhausted(f"Retries exhausted ({self._max_attempts})")

    async def aclose(self) -> None:
        await self._inner.aclose()
