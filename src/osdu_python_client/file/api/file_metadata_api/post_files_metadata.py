from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.file_metadata import FileMetadata
from ...types import Response


def _get_kwargs(
    *,
    body: FileMetadata,
    data_partition_id: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["data-partition-id"] = data_partition_id

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v2/files/metadata",
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
    body: FileMetadata,
    data_partition_id: str,
) -> Response[Any]:
    """Creates a metadata for a file

     This API creates a metadata record for a file that is already uploaded. The Metadata is linked to
    the file via `FileSource` provided in the request body. <p> If `FileSource` attribute is missing in
    the request body or there is no file present, then the request fails with an error. </p><p> When
    metadata is successfully updated in the system, it returns the `Id` of the file metadata record.
    </p><p> **Required roles**: `service.file.editors`. Users added to groups `users.datalake.editors`,
    `users.datalake.admins`, `users.datalake.ops` would be added to group `service.file.editors` by
    default.</p>

    Args:
        data_partition_id (str):
        body (FileMetadata): File metadata record.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        body=body,
        data_partition_id=data_partition_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: FileMetadata,
    data_partition_id: str,
) -> Response[Any]:
    """Creates a metadata for a file

     This API creates a metadata record for a file that is already uploaded. The Metadata is linked to
    the file via `FileSource` provided in the request body. <p> If `FileSource` attribute is missing in
    the request body or there is no file present, then the request fails with an error. </p><p> When
    metadata is successfully updated in the system, it returns the `Id` of the file metadata record.
    </p><p> **Required roles**: `service.file.editors`. Users added to groups `users.datalake.editors`,
    `users.datalake.admins`, `users.datalake.ops` would be added to group `service.file.editors` by
    default.</p>

    Args:
        data_partition_id (str):
        body (FileMetadata): File metadata record.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        body=body,
        data_partition_id=data_partition_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
