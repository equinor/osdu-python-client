from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.app_error import AppError
from ...models.record_merge_patch_request import RecordMergePatchRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    body: RecordMergePatchRequest,
    x_collaboration: str | Unset = UNSET,
    data_partition_id: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_collaboration, Unset):
        headers["x-collaboration"] = x_collaboration

    headers["data-partition-id"] = data_partition_id

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/records/{id}".format(
            id=quote(str(id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/merge-patch+json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AppError | str | None:
    if response.status_code == 200:
        response_200 = cast(str, response.json())
        return response_200

    if response.status_code == 400:
        response_400 = AppError.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = AppError.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = AppError.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = AppError.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = AppError.from_dict(response.json())

        return response_500

    if response.status_code == 502:
        response_502 = AppError.from_dict(response.json())

        return response_502

    if response.status_code == 503:
        response_503 = AppError.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AppError | str]:
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
    body: RecordMergePatchRequest,
    x_collaboration: str | Unset = UNSET,
    data_partition_id: str,
) -> Response[AppError | str]:
    """Patch record with merge-patch operations

     The API allows partial updates to a record using JSON Merge Patch (RFC 7396) format. It supports
    updating record fields like ACL, legal information, data and tags. Only the fields specified in the
    request body will be modified, leaving other fields unchanged. The API can also handle soft
    delete/undelete operations by setting the 'deleted' field.
    Allowed roles: `service.storage.creator` and `service.storage.admin`.

    Args:
        id (str):
        x_collaboration (str | Unset):
        data_partition_id (str):
        body (RecordMergePatchRequest): Data to be patched Example: {'acl': {'viewers':
            ['data.viewer@tenant.com'], 'owners': ['data.owner@tenant.com']}, 'legal': {'legaltags':
            ['tenant-public-usa-dataset-1'], 'otherRelevantDataCountries': ['US']}, 'data':
            {'wellName': 'Updated Well Name', 'status': 'active'}, 'tags': {'environment':
            'production'}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppError | str]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
        x_collaboration=x_collaboration,
        data_partition_id=data_partition_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
    body: RecordMergePatchRequest,
    x_collaboration: str | Unset = UNSET,
    data_partition_id: str,
) -> AppError | str | None:
    """Patch record with merge-patch operations

     The API allows partial updates to a record using JSON Merge Patch (RFC 7396) format. It supports
    updating record fields like ACL, legal information, data and tags. Only the fields specified in the
    request body will be modified, leaving other fields unchanged. The API can also handle soft
    delete/undelete operations by setting the 'deleted' field.
    Allowed roles: `service.storage.creator` and `service.storage.admin`.

    Args:
        id (str):
        x_collaboration (str | Unset):
        data_partition_id (str):
        body (RecordMergePatchRequest): Data to be patched Example: {'acl': {'viewers':
            ['data.viewer@tenant.com'], 'owners': ['data.owner@tenant.com']}, 'legal': {'legaltags':
            ['tenant-public-usa-dataset-1'], 'otherRelevantDataCountries': ['US']}, 'data':
            {'wellName': 'Updated Well Name', 'status': 'active'}, 'tags': {'environment':
            'production'}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppError | str
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
        x_collaboration=x_collaboration,
        data_partition_id=data_partition_id,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    body: RecordMergePatchRequest,
    x_collaboration: str | Unset = UNSET,
    data_partition_id: str,
) -> Response[AppError | str]:
    """Patch record with merge-patch operations

     The API allows partial updates to a record using JSON Merge Patch (RFC 7396) format. It supports
    updating record fields like ACL, legal information, data and tags. Only the fields specified in the
    request body will be modified, leaving other fields unchanged. The API can also handle soft
    delete/undelete operations by setting the 'deleted' field.
    Allowed roles: `service.storage.creator` and `service.storage.admin`.

    Args:
        id (str):
        x_collaboration (str | Unset):
        data_partition_id (str):
        body (RecordMergePatchRequest): Data to be patched Example: {'acl': {'viewers':
            ['data.viewer@tenant.com'], 'owners': ['data.owner@tenant.com']}, 'legal': {'legaltags':
            ['tenant-public-usa-dataset-1'], 'otherRelevantDataCountries': ['US']}, 'data':
            {'wellName': 'Updated Well Name', 'status': 'active'}, 'tags': {'environment':
            'production'}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppError | str]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
        x_collaboration=x_collaboration,
        data_partition_id=data_partition_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    body: RecordMergePatchRequest,
    x_collaboration: str | Unset = UNSET,
    data_partition_id: str,
) -> AppError | str | None:
    """Patch record with merge-patch operations

     The API allows partial updates to a record using JSON Merge Patch (RFC 7396) format. It supports
    updating record fields like ACL, legal information, data and tags. Only the fields specified in the
    request body will be modified, leaving other fields unchanged. The API can also handle soft
    delete/undelete operations by setting the 'deleted' field.
    Allowed roles: `service.storage.creator` and `service.storage.admin`.

    Args:
        id (str):
        x_collaboration (str | Unset):
        data_partition_id (str):
        body (RecordMergePatchRequest): Data to be patched Example: {'acl': {'viewers':
            ['data.viewer@tenant.com'], 'owners': ['data.owner@tenant.com']}, 'legal': {'legaltags':
            ['tenant-public-usa-dataset-1'], 'otherRelevantDataCountries': ['US']}, 'data':
            {'wellName': 'Updated Well Name', 'status': 'active'}, 'tags': {'environment':
            'production'}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppError | str
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
            x_collaboration=x_collaboration,
            data_partition_id=data_partition_id,
        )
    ).parsed
