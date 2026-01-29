from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.app_error import AppError
from ...models.in_polygon_query import InPolygonQuery
from ...models.points_in_aou_search_result import PointsInAouSearchResult
from ...types import Response


def _get_kwargs(
    *,
    body: InPolygonQuery,
    data_partition_id: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["data-partition-id"] = data_partition_id

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v3/points-in-aou",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AppError | PointsInAouSearchResult | None:
    if response.status_code == 200:
        response_200 = PointsInAouSearchResult.from_dict(response.json())

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
) -> Response[AppError | PointsInAouSearchResult]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: InPolygonQuery,
    data_partition_id: str,
) -> Response[AppError | PointsInAouSearchResult]:
    """Coordinate Transformations

     Coordinate Transformations

    Args:
        data_partition_id (str):
        body (InPolygonQuery): Coordinate Transformations

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppError | PointsInAouSearchResult]
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
    body: InPolygonQuery,
    data_partition_id: str,
) -> AppError | PointsInAouSearchResult | None:
    """Coordinate Transformations

     Coordinate Transformations

    Args:
        data_partition_id (str):
        body (InPolygonQuery): Coordinate Transformations

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppError | PointsInAouSearchResult
    """

    return sync_detailed(
        client=client,
        body=body,
        data_partition_id=data_partition_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: InPolygonQuery,
    data_partition_id: str,
) -> Response[AppError | PointsInAouSearchResult]:
    """Coordinate Transformations

     Coordinate Transformations

    Args:
        data_partition_id (str):
        body (InPolygonQuery): Coordinate Transformations

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppError | PointsInAouSearchResult]
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
    body: InPolygonQuery,
    data_partition_id: str,
) -> AppError | PointsInAouSearchResult | None:
    """Coordinate Transformations

     Coordinate Transformations

    Args:
        data_partition_id (str):
        body (InPolygonQuery): Coordinate Transformations

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppError | PointsInAouSearchResult
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            data_partition_id=data_partition_id,
        )
    ).parsed
