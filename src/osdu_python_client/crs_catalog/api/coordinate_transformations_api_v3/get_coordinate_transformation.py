from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.app_error import AppError
from ...models.search_response import SearchResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    record_id: str | Unset = UNSET,
    data_id: str | Unset = UNSET,
    data_partition_id: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["data-partition-id"] = data_partition_id

    params: dict[str, Any] = {}

    params["recordId"] = record_id

    params["dataId"] = data_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v3/coordinate-transformation",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AppError | SearchResponse | None:
    if response.status_code == 200:
        response_200 = SearchResponse.from_dict(response.json())

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

    if response.status_code == 409:
        response_409 = AppError.from_dict(response.json())

        return response_409

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
) -> Response[AppError | SearchResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    record_id: str | Unset = UNSET,
    data_id: str | Unset = UNSET,
    data_partition_id: str,
) -> Response[AppError | SearchResponse]:
    """Coordinate Transformations

     Coordinate Transformations

    Args:
        record_id (str | Unset):
        data_id (str | Unset):
        data_partition_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppError | SearchResponse]
    """

    kwargs = _get_kwargs(
        record_id=record_id,
        data_id=data_id,
        data_partition_id=data_partition_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    record_id: str | Unset = UNSET,
    data_id: str | Unset = UNSET,
    data_partition_id: str,
) -> AppError | SearchResponse | None:
    """Coordinate Transformations

     Coordinate Transformations

    Args:
        record_id (str | Unset):
        data_id (str | Unset):
        data_partition_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppError | SearchResponse
    """

    return sync_detailed(
        client=client,
        record_id=record_id,
        data_id=data_id,
        data_partition_id=data_partition_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    record_id: str | Unset = UNSET,
    data_id: str | Unset = UNSET,
    data_partition_id: str,
) -> Response[AppError | SearchResponse]:
    """Coordinate Transformations

     Coordinate Transformations

    Args:
        record_id (str | Unset):
        data_id (str | Unset):
        data_partition_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppError | SearchResponse]
    """

    kwargs = _get_kwargs(
        record_id=record_id,
        data_id=data_id,
        data_partition_id=data_partition_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    record_id: str | Unset = UNSET,
    data_id: str | Unset = UNSET,
    data_partition_id: str,
) -> AppError | SearchResponse | None:
    """Coordinate Transformations

     Coordinate Transformations

    Args:
        record_id (str | Unset):
        data_id (str | Unset):
        data_partition_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppError | SearchResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            record_id=record_id,
            data_id=data_id,
            data_partition_id=data_partition_id,
        )
    ).parsed
