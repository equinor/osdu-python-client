from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
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
        "url": "/v2/files/uploadURL",
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
    *,
    client: AuthenticatedClient,
    expiry_time: str | Unset = UNSET,
    data_partition_id: str,
) -> Response[Any]:
    """Get a location in Landing Zone to upload a file.

     Gets a temporary signed URL to upload a file (Service does not upload the file by itself, User needs
    to use this URL to upload the file). The generated URL is time bound and by default expires by 7
    days maximum. <p> User will receive a FileSource in the response.This is the relative path where the
    uploaded file will persist. Once the file is uploaded, FileSource can then be used to post metadata
    of the file.</p> <p> **Required roles**: `service.file.editors`. Users added to groups
    `users.datalake.editors`, `users.datalake.admins`, `users.datalake.ops` would be added to group
    `service.file.editors` by default.</p>

    Args:
        expiry_time (str | Unset):
        data_partition_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        expiry_time=expiry_time,
        data_partition_id=data_partition_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    expiry_time: str | Unset = UNSET,
    data_partition_id: str,
) -> Response[Any]:
    """Get a location in Landing Zone to upload a file.

     Gets a temporary signed URL to upload a file (Service does not upload the file by itself, User needs
    to use this URL to upload the file). The generated URL is time bound and by default expires by 7
    days maximum. <p> User will receive a FileSource in the response.This is the relative path where the
    uploaded file will persist. Once the file is uploaded, FileSource can then be used to post metadata
    of the file.</p> <p> **Required roles**: `service.file.editors`. Users added to groups
    `users.datalake.editors`, `users.datalake.admins`, `users.datalake.ops` would be added to group
    `service.file.editors` by default.</p>

    Args:
        expiry_time (str | Unset):
        data_partition_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        expiry_time=expiry_time,
        data_partition_id=data_partition_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
