from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.app_error import AppError
from ...models.unit_system import UnitSystem
from ...models.unit_system_request import UnitSystemRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: UnitSystemRequest,
    offset: int | Unset = 0,
    limit: int | Unset = 100,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["offset"] = offset

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v2/unitsystem",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AppError | UnitSystem | None:
    if response.status_code == 200:
        response_200 = UnitSystem.from_dict(response.json())

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
) -> Response[AppError | UnitSystem]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: UnitSystemRequest,
    offset: int | Unset = 0,
    limit: int | Unset = 100,
) -> Response[AppError | UnitSystem]:
    """Get all Units assigned to the UnitSystem

     Get all unit assignments for the given unit system essence.

    Args:
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 100.
        body (UnitSystemRequest): Request to get all unit assignments for the given unit system

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppError | UnitSystem]
    """

    kwargs = _get_kwargs(
        body=body,
        offset=offset,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: UnitSystemRequest,
    offset: int | Unset = 0,
    limit: int | Unset = 100,
) -> AppError | UnitSystem | None:
    """Get all Units assigned to the UnitSystem

     Get all unit assignments for the given unit system essence.

    Args:
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 100.
        body (UnitSystemRequest): Request to get all unit assignments for the given unit system

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppError | UnitSystem
    """

    return sync_detailed(
        client=client,
        body=body,
        offset=offset,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: UnitSystemRequest,
    offset: int | Unset = 0,
    limit: int | Unset = 100,
) -> Response[AppError | UnitSystem]:
    """Get all Units assigned to the UnitSystem

     Get all unit assignments for the given unit system essence.

    Args:
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 100.
        body (UnitSystemRequest): Request to get all unit assignments for the given unit system

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppError | UnitSystem]
    """

    kwargs = _get_kwargs(
        body=body,
        offset=offset,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: UnitSystemRequest,
    offset: int | Unset = 0,
    limit: int | Unset = 100,
) -> AppError | UnitSystem | None:
    """Get all Units assigned to the UnitSystem

     Get all unit assignments for the given unit system essence.

    Args:
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 100.
        body (UnitSystemRequest): Request to get all unit assignments for the given unit system

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppError | UnitSystem
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            offset=offset,
            limit=limit,
        )
    ).parsed
