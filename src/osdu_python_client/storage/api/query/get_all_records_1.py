from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.app_error import AppError
from ...models.datastore_query_result import DatastoreQueryResult
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    cursor: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    kind: str,
    x_collaboration: str | Unset = UNSET,
    data_partition_id: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_collaboration, Unset):
        headers["x-collaboration"] = x_collaboration

    headers["data-partition-id"] = data_partition_id

    params: dict[str, Any] = {}

    params["cursor"] = cursor

    params["limit"] = limit

    params["kind"] = kind

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/query/records",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AppError | DatastoreQueryResult | None:
    if response.status_code == 200:
        response_200 = DatastoreQueryResult.from_dict(response.json())

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
) -> Response[AppError | DatastoreQueryResult]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    cursor: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    kind: str,
    x_collaboration: str | Unset = UNSET,
    data_partition_id: str,
) -> Response[AppError | DatastoreQueryResult]:
    """Get all record from kind

     The API returns a list of all record ids which belong to the specified kind.
    Allowed roles: `service.storage.admin`.

    Args:
        cursor (str | Unset):
        limit (int | Unset):
        kind (str):
        x_collaboration (str | Unset):
        data_partition_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppError | DatastoreQueryResult]
    """

    kwargs = _get_kwargs(
        cursor=cursor,
        limit=limit,
        kind=kind,
        x_collaboration=x_collaboration,
        data_partition_id=data_partition_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    cursor: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    kind: str,
    x_collaboration: str | Unset = UNSET,
    data_partition_id: str,
) -> AppError | DatastoreQueryResult | None:
    """Get all record from kind

     The API returns a list of all record ids which belong to the specified kind.
    Allowed roles: `service.storage.admin`.

    Args:
        cursor (str | Unset):
        limit (int | Unset):
        kind (str):
        x_collaboration (str | Unset):
        data_partition_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppError | DatastoreQueryResult
    """

    return sync_detailed(
        client=client,
        cursor=cursor,
        limit=limit,
        kind=kind,
        x_collaboration=x_collaboration,
        data_partition_id=data_partition_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    cursor: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    kind: str,
    x_collaboration: str | Unset = UNSET,
    data_partition_id: str,
) -> Response[AppError | DatastoreQueryResult]:
    """Get all record from kind

     The API returns a list of all record ids which belong to the specified kind.
    Allowed roles: `service.storage.admin`.

    Args:
        cursor (str | Unset):
        limit (int | Unset):
        kind (str):
        x_collaboration (str | Unset):
        data_partition_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppError | DatastoreQueryResult]
    """

    kwargs = _get_kwargs(
        cursor=cursor,
        limit=limit,
        kind=kind,
        x_collaboration=x_collaboration,
        data_partition_id=data_partition_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    cursor: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    kind: str,
    x_collaboration: str | Unset = UNSET,
    data_partition_id: str,
) -> AppError | DatastoreQueryResult | None:
    """Get all record from kind

     The API returns a list of all record ids which belong to the specified kind.
    Allowed roles: `service.storage.admin`.

    Args:
        cursor (str | Unset):
        limit (int | Unset):
        kind (str):
        x_collaboration (str | Unset):
        data_partition_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppError | DatastoreQueryResult
    """

    return (
        await asyncio_detailed(
            client=client,
            cursor=cursor,
            limit=limit,
            kind=kind,
            x_collaboration=x_collaboration,
            data_partition_id=data_partition_id,
        )
    ).parsed
