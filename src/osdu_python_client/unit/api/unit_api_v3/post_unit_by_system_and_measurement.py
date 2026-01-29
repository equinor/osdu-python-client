from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.app_error import AppError
from ...models.measurement_request import MeasurementRequest
from ...models.unit import Unit
from ...types import UNSET, Response


def _get_kwargs(
    *,
    body: MeasurementRequest,
    unit_system_name: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["unitSystemName"] = unit_system_name

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v3/unit/unitsystem",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AppError | Unit | None:
    if response.status_code == 200:
        response_200 = Unit.from_dict(response.json())

        return response_200

    if response.status_code == 201:
        response_201 = Unit.from_dict(response.json())

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
) -> Response[AppError | Unit]:
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
    unit_system_name: str,
) -> Response[AppError | Unit]:
    """postUnitBySystemAndMeasurement

     Post Unit By System And Measurement Using POST

    Args:
        unit_system_name (str):
        body (MeasurementRequest): Request to get a specific measurement given a persistable
            reference string or measurement essence structure.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppError | Unit]
    """

    kwargs = _get_kwargs(
        body=body,
        unit_system_name=unit_system_name,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: MeasurementRequest,
    unit_system_name: str,
) -> AppError | Unit | None:
    """postUnitBySystemAndMeasurement

     Post Unit By System And Measurement Using POST

    Args:
        unit_system_name (str):
        body (MeasurementRequest): Request to get a specific measurement given a persistable
            reference string or measurement essence structure.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppError | Unit
    """

    return sync_detailed(
        client=client,
        body=body,
        unit_system_name=unit_system_name,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: MeasurementRequest,
    unit_system_name: str,
) -> Response[AppError | Unit]:
    """postUnitBySystemAndMeasurement

     Post Unit By System And Measurement Using POST

    Args:
        unit_system_name (str):
        body (MeasurementRequest): Request to get a specific measurement given a persistable
            reference string or measurement essence structure.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppError | Unit]
    """

    kwargs = _get_kwargs(
        body=body,
        unit_system_name=unit_system_name,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: MeasurementRequest,
    unit_system_name: str,
) -> AppError | Unit | None:
    """postUnitBySystemAndMeasurement

     Post Unit By System And Measurement Using POST

    Args:
        unit_system_name (str):
        body (MeasurementRequest): Request to get a specific measurement given a persistable
            reference string or measurement essence structure.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppError | Unit
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            unit_system_name=unit_system_name,
        )
    ).parsed
