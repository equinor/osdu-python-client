from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.app_error import AppError
from ...models.measurement_request import MeasurementRequest
from ...models.query_result import QueryResult
from ...types import Response


def _get_kwargs(
    *,
    body: MeasurementRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v3/unit/measurement/preferred",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AppError | QueryResult | None:
    if response.status_code == 200:
        response_200 = QueryResult.from_dict(response.json())

        return response_200

    if response.status_code == 201:
        response_201 = QueryResult.from_dict(response.json())

        return response_201

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
) -> Response[AppError | QueryResult]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: MeasurementRequest,
) -> Response[AppError | QueryResult]:
    """postPreferredUnitsByMeasurement

     Post Preferred Units By Measurement Using POST

    Args:
        body (MeasurementRequest): Request to get a specific measurement given a persistable
            reference string or measurement essence structure.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppError | QueryResult]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: MeasurementRequest,
) -> AppError | QueryResult | None:
    """postPreferredUnitsByMeasurement

     Post Preferred Units By Measurement Using POST

    Args:
        body (MeasurementRequest): Request to get a specific measurement given a persistable
            reference string or measurement essence structure.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppError | QueryResult
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: MeasurementRequest,
) -> Response[AppError | QueryResult]:
    """postPreferredUnitsByMeasurement

     Post Preferred Units By Measurement Using POST

    Args:
        body (MeasurementRequest): Request to get a specific measurement given a persistable
            reference string or measurement essence structure.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppError | QueryResult]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: MeasurementRequest,
) -> AppError | QueryResult | None:
    """postPreferredUnitsByMeasurement

     Post Preferred Units By Measurement Using POST

    Args:
        body (MeasurementRequest): Request to get a specific measurement given a persistable
            reference string or measurement essence structure.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppError | QueryResult
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
