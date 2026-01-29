from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.app_error import AppError
from ...models.convert_points_request import ConvertPointsRequest
from ...models.convert_points_response import ConvertPointsResponse
from ...types import Response


def _get_kwargs(
    *,
    body: ConvertPointsRequest,
    data_partition_id: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["data-partition-id"] = data_partition_id

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v3/convert",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AppError | ConvertPointsResponse | None:
    if response.status_code == 200:
        response_200 = ConvertPointsResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = AppError.from_dict(response.json())

        return response_400

    if response.status_code == 500:
        response_500 = AppError.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = AppError.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AppError | ConvertPointsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: ConvertPointsRequest,
    data_partition_id: str,
) -> Response[AppError | ConvertPointsResponse]:
    """Convert a list of points

     Convert a list of points

    Args:
        data_partition_id (str):
        body (ConvertPointsRequest): Request to convert a set of points from a source CRS to a
            target CRS

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppError | ConvertPointsResponse]
    """

    kwargs = _get_kwargs(
        body=body,
        data_partition_id=data_partition_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: ConvertPointsRequest,
    data_partition_id: str,
) -> AppError | ConvertPointsResponse | None:
    """Convert a list of points

     Convert a list of points

    Args:
        data_partition_id (str):
        body (ConvertPointsRequest): Request to convert a set of points from a source CRS to a
            target CRS

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppError | ConvertPointsResponse
    """

    return sync_detailed(
        client=client,
        body=body,
        data_partition_id=data_partition_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: ConvertPointsRequest,
    data_partition_id: str,
) -> Response[AppError | ConvertPointsResponse]:
    """Convert a list of points

     Convert a list of points

    Args:
        data_partition_id (str):
        body (ConvertPointsRequest): Request to convert a set of points from a source CRS to a
            target CRS

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppError | ConvertPointsResponse]
    """

    kwargs = _get_kwargs(
        body=body,
        data_partition_id=data_partition_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: ConvertPointsRequest,
    data_partition_id: str,
) -> AppError | ConvertPointsResponse | None:
    """Convert a list of points

     Convert a list of points

    Args:
        data_partition_id (str):
        body (ConvertPointsRequest): Request to convert a set of points from a source CRS to a
            target CRS

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppError | ConvertPointsResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            data_partition_id=data_partition_id,
        )
    ).parsed
