from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.app_error import AppError
from ...models.map_ import Map
from ...types import Response


def _get_kwargs(
    partition_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/partitions/{partition_id}".format(
            partition_id=quote(str(partition_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AppError | Map | None:
    if response.status_code == 200:
        response_200 = Map.from_dict(response.json())

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
) -> Response[AppError | Map]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    partition_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[AppError | Map]:
    """Get Partition Info

     Get all properties and their values for a given data partition id

    Args:
        partition_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppError | Map]
    """

    kwargs = _get_kwargs(
        partition_id=partition_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    partition_id: str,
    *,
    client: AuthenticatedClient,
) -> AppError | Map | None:
    """Get Partition Info

     Get all properties and their values for a given data partition id

    Args:
        partition_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppError | Map
    """

    return sync_detailed(
        partition_id=partition_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    partition_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[AppError | Map]:
    """Get Partition Info

     Get all properties and their values for a given data partition id

    Args:
        partition_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppError | Map]
    """

    kwargs = _get_kwargs(
        partition_id=partition_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    partition_id: str,
    *,
    client: AuthenticatedClient,
) -> AppError | Map | None:
    """Get Partition Info

     Get all properties and their values for a given data partition id

    Args:
        partition_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppError | Map
    """

    return (
        await asyncio_detailed(
            partition_id=partition_id,
            client=client,
        )
    ).parsed
