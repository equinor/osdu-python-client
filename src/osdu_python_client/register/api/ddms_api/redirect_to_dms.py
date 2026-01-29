from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import Response


def _get_kwargs(
    id: str,
    type_: str,
    localid: str,
    *,
    data_partition_id: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["data-partition-id"] = data_partition_id

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/ddms/{id}/{type_}/{localid}".format(
            id=quote(str(id), safe=""),
            type_=quote(str(type_), safe=""),
            localid=quote(str(localid), safe=""),
        ),
    }

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
    id: str,
    type_: str,
    localid: str,
    *,
    client: AuthenticatedClient,
    data_partition_id: str,
) -> Response[Any]:
    """Retrieves Single Entity record id

     Get a Single DDMS record id. Required roles: `users.datalake.ops` or `users.datalake.admins` or
    `users.datalake.editors` or `users.datalake.viewers`

    Args:
        id (str):
        type_ (str):
        localid (str):
        data_partition_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        id=id,
        type_=type_,
        localid=localid,
        data_partition_id=data_partition_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    id: str,
    type_: str,
    localid: str,
    *,
    client: AuthenticatedClient,
    data_partition_id: str,
) -> Response[Any]:
    """Retrieves Single Entity record id

     Get a Single DDMS record id. Required roles: `users.datalake.ops` or `users.datalake.admins` or
    `users.datalake.editors` or `users.datalake.viewers`

    Args:
        id (str):
        type_ (str):
        localid (str):
        data_partition_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        id=id,
        type_=type_,
        localid=localid,
        data_partition_id=data_partition_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
