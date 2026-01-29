from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    expiry_time: str | Unset = UNSET,
    data_partition_id: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["data-partition-id"] = data_partition_id

    params: dict[str, Any] = {}

    params["expiryTime"] = expiry_time

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v2/files/{id}/downloadURL".format(
            id=quote(str(id), safe=""),
        ),
        "params": params,
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
    *,
    client: AuthenticatedClient,
    expiry_time: str | Unset = UNSET,
    data_partition_id: str,
) -> Response[Any]:
    """Gets a URL to download the file

     Gets a URL for downloading the file associated with the unique `id`.By default, the download URL is
    valid for `1 Hour` and it is `7 Days` maximum.<p> **Required roles**: `service.file.viewers`. Users
    added to groups `users.datalake.viewers`,`users.datalake.editors`, `users.datalake.admins`,
    `users.datalake.ops` would be added to group `service.file.viewers` by default.</p>

    Args:
        id (str):
        expiry_time (str | Unset):
        data_partition_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        id=id,
        expiry_time=expiry_time,
        data_partition_id=data_partition_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    expiry_time: str | Unset = UNSET,
    data_partition_id: str,
) -> Response[Any]:
    """Gets a URL to download the file

     Gets a URL for downloading the file associated with the unique `id`.By default, the download URL is
    valid for `1 Hour` and it is `7 Days` maximum.<p> **Required roles**: `service.file.viewers`. Users
    added to groups `users.datalake.viewers`,`users.datalake.editors`, `users.datalake.admins`,
    `users.datalake.ops` would be added to group `service.file.viewers` by default.</p>

    Args:
        id (str):
        expiry_time (str | Unset):
        data_partition_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        id=id,
        expiry_time=expiry_time,
        data_partition_id=data_partition_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
