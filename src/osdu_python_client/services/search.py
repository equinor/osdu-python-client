from __future__ import annotations

from typing import Any

from osdu_python_client.errors import OsduError
from osdu_python_client.generated.search.api.search_api import (
    close_cursor,
    query_records,
    query_with_cursor,
)
from osdu_python_client.generated.search.client import AuthenticatedClient
from osdu_python_client.generated.search.models.app_error import AppError
from osdu_python_client.generated.search.models.cursor_query_request import CursorQueryRequest
from osdu_python_client.generated.search.models.cursor_query_response import CursorQueryResponse
from osdu_python_client.generated.search.models.query_request import QueryRequest
from osdu_python_client.generated.search.models.query_response import QueryResponse
from osdu_python_client.generated.search.types import Response


def _unwrap(result: Response[Any]) -> Any:
    if 200 <= result.status_code.value < 300:
        return result.parsed
    detail: Any = result.parsed if isinstance(result.parsed, AppError) else None
    raise OsduError(
        f"Search request failed: status={result.status_code.value} detail={detail}"
    )


class _ServiceBase:
    """Forward unknown attributes to the wrapped generated client.

    Lets callers still use ``service.get_httpx_client()`` etc. when needed.
    """

    _client: AuthenticatedClient

    def __getattr__(self, name: str) -> Any:
        return getattr(self._client, name)


class SearchService(_ServiceBase):
    def __init__(self, client: AuthenticatedClient, data_partition_id: str) -> None:
        self._client = client
        self._partition = data_partition_id

    def query(self, body: QueryRequest) -> QueryResponse:
        return _unwrap(self.query_detailed(body))

    def query_detailed(
        self, body: QueryRequest
    ) -> Response[AppError | QueryResponse]:
        return query_records.sync_detailed(
            client=self._client, body=body, data_partition_id=self._partition
        )

    def query_cursor(
        self, body: CursorQueryRequest, search_after: bool = False
    ) -> CursorQueryResponse:
        return _unwrap(self.query_cursor_detailed(body, search_after=search_after))

    def query_cursor_detailed(
        self, body: CursorQueryRequest, search_after: bool = False
    ) -> Response[AppError | CursorQueryResponse]:
        return query_with_cursor.sync_detailed(
            client=self._client,
            body=body,
            search_after=search_after,
            data_partition_id=self._partition,
        )

    def close_cursor(self, cursor: str, search_after: bool = False) -> None:
        result = close_cursor.sync_detailed(
            cursor,
            client=self._client,
            search_after=search_after,
            data_partition_id=self._partition,
        )
        _unwrap(result)


class AsyncSearchService(_ServiceBase):
    def __init__(self, client: AuthenticatedClient, data_partition_id: str) -> None:
        self._client = client
        self._partition = data_partition_id

    async def query(self, body: QueryRequest) -> QueryResponse:
        return _unwrap(await self.query_detailed(body))

    async def query_detailed(
        self, body: QueryRequest
    ) -> Response[AppError | QueryResponse]:
        return await query_records.asyncio_detailed(
            client=self._client, body=body, data_partition_id=self._partition
        )

    async def query_cursor(
        self, body: CursorQueryRequest, search_after: bool = False
    ) -> CursorQueryResponse:
        return _unwrap(
            await self.query_cursor_detailed(body, search_after=search_after)
        )

    async def query_cursor_detailed(
        self, body: CursorQueryRequest, search_after: bool = False
    ) -> Response[AppError | CursorQueryResponse]:
        return await query_with_cursor.asyncio_detailed(
            client=self._client,
            body=body,
            search_after=search_after,
            data_partition_id=self._partition,
        )

    async def close_cursor(self, cursor: str, search_after: bool = False) -> None:
        result = await close_cursor.asyncio_detailed(
            cursor,
            client=self._client,
            search_after=search_after,
            data_partition_id=self._partition,
        )
        _unwrap(result)
