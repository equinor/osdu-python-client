from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.app_error import AppError
from ...models.unit import Unit
from ...types import Response


def _get_kwargs(
    unit_system_name: str,
    ancestry: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v2/unit/unitsystem/{unit_system_name}/{ancestry}".format(
            unit_system_name=quote(str(unit_system_name), safe=""),
            ancestry=quote(str(ancestry), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AppError | Unit | None:
    if response.status_code == 200:
        response_200 = Unit.from_dict(response.json())

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
) -> Response[AppError | Unit]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    unit_system_name: str,
    ancestry: str,
    *,
    client: AuthenticatedClient,
) -> Response[AppError | Unit]:
    """Get a unique Unit for the given Measurement ancestry in the named UnitSystem

     Get a unique unit given a unit system name and dot separated measurement ancestry, e.g.
    Time_Per_Length.Acoustic_Slowness.

    Args:
        unit_system_name (str):
        ancestry (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppError | Unit]
    """

    kwargs = _get_kwargs(
        unit_system_name=unit_system_name,
        ancestry=ancestry,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    unit_system_name: str,
    ancestry: str,
    *,
    client: AuthenticatedClient,
) -> AppError | Unit | None:
    """Get a unique Unit for the given Measurement ancestry in the named UnitSystem

     Get a unique unit given a unit system name and dot separated measurement ancestry, e.g.
    Time_Per_Length.Acoustic_Slowness.

    Args:
        unit_system_name (str):
        ancestry (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppError | Unit
    """

    return sync_detailed(
        unit_system_name=unit_system_name,
        ancestry=ancestry,
        client=client,
    ).parsed


async def asyncio_detailed(
    unit_system_name: str,
    ancestry: str,
    *,
    client: AuthenticatedClient,
) -> Response[AppError | Unit]:
    """Get a unique Unit for the given Measurement ancestry in the named UnitSystem

     Get a unique unit given a unit system name and dot separated measurement ancestry, e.g.
    Time_Per_Length.Acoustic_Slowness.

    Args:
        unit_system_name (str):
        ancestry (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppError | Unit]
    """

    kwargs = _get_kwargs(
        unit_system_name=unit_system_name,
        ancestry=ancestry,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    unit_system_name: str,
    ancestry: str,
    *,
    client: AuthenticatedClient,
) -> AppError | Unit | None:
    """Get a unique Unit for the given Measurement ancestry in the named UnitSystem

     Get a unique unit given a unit system name and dot separated measurement ancestry, e.g.
    Time_Per_Length.Acoustic_Slowness.

    Args:
        unit_system_name (str):
        ancestry (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppError | Unit
    """

    return (
        await asyncio_detailed(
            unit_system_name=unit_system_name,
            ancestry=ancestry,
            client=client,
        )
    ).parsed
