from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.cursor_query_request import CursorQueryRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: CursorQueryRequest,
    search_after: bool | Unset = False,
    data_partition_id: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["data-partition-id"] = data_partition_id

    params: dict[str, Any] = {}

    params["search_after"] = search_after

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/query_with_cursor",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | None:
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: CursorQueryRequest,
    search_after: bool | Unset = False,
    data_partition_id: str,
) -> Response[Any]:
    """Queries the index using cursor for the input request criteria.

     The API supports full text search on string fields, range queries on date, numeric or string fields,
    along with geo-spatial search.
    Required roles: `users.datalake.viewers` or `users.datalake.editors` or `users.datalake.admins` or
    `users.datalake.ops`. In addition, users must be a member of data groups to access the data.
    It can be used to retrieve large numbers of results (or even all results) from a single search
    request, in much the same way as you would use a cursor on a traditional database.

    Args:
        search_after (bool | Unset):  Default: False.
        data_partition_id (str):
        body (CursorQueryRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        body=body,
        search_after=search_after,
        data_partition_id=data_partition_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: CursorQueryRequest,
    search_after: bool | Unset = False,
    data_partition_id: str,
) -> Response[Any]:
    """Queries the index using cursor for the input request criteria.

     The API supports full text search on string fields, range queries on date, numeric or string fields,
    along with geo-spatial search.
    Required roles: `users.datalake.viewers` or `users.datalake.editors` or `users.datalake.admins` or
    `users.datalake.ops`. In addition, users must be a member of data groups to access the data.
    It can be used to retrieve large numbers of results (or even all results) from a single search
    request, in much the same way as you would use a cursor on a traditional database.

    Args:
        search_after (bool | Unset):  Default: False.
        data_partition_id (str):
        body (CursorQueryRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        body=body,
        search_after=search_after,
        data_partition_id=data_partition_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
