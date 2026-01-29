from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.app_error import AppError
from ...models.conversion_result import ConversionResult
from ...types import Response


def _get_kwargs(
    namespaces: str,
    from_symbol: str,
    to_symbol: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v2/conversion/abcd/{namespaces}/{from_symbol}/{to_symbol}".format(
            namespaces=quote(str(namespaces), safe=""),
            from_symbol=quote(str(from_symbol), safe=""),
            to_symbol=quote(str(to_symbol), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AppError | ConversionResult | None:
    if response.status_code == 200:
        response_200 = ConversionResult.from_dict(response.json())

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
) -> Response[AppError | ConversionResult]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    namespaces: str,
    from_symbol: str,
    to_symbol: str,
    *,
    client: AuthenticatedClient,
) -> Response[AppError | ConversionResult]:
    """Get Abcd Unit conversion parameters given two Unit specifications

     'Get the Energistics style unit parameters given the ''from'' and ''to'' unit symbols and the
    namespace(-list) to disambiguate the unit symbols. Example for a prioritized namespaces list:
    ''LIS,RP66,ECL,Energistics_UoM'' - this will prioritize the units in the LIS namespace over other
    namespaces.'

    Args:
        namespaces (str):
        from_symbol (str):
        to_symbol (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppError | ConversionResult]
    """

    kwargs = _get_kwargs(
        namespaces=namespaces,
        from_symbol=from_symbol,
        to_symbol=to_symbol,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    namespaces: str,
    from_symbol: str,
    to_symbol: str,
    *,
    client: AuthenticatedClient,
) -> AppError | ConversionResult | None:
    """Get Abcd Unit conversion parameters given two Unit specifications

     'Get the Energistics style unit parameters given the ''from'' and ''to'' unit symbols and the
    namespace(-list) to disambiguate the unit symbols. Example for a prioritized namespaces list:
    ''LIS,RP66,ECL,Energistics_UoM'' - this will prioritize the units in the LIS namespace over other
    namespaces.'

    Args:
        namespaces (str):
        from_symbol (str):
        to_symbol (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppError | ConversionResult
    """

    return sync_detailed(
        namespaces=namespaces,
        from_symbol=from_symbol,
        to_symbol=to_symbol,
        client=client,
    ).parsed


async def asyncio_detailed(
    namespaces: str,
    from_symbol: str,
    to_symbol: str,
    *,
    client: AuthenticatedClient,
) -> Response[AppError | ConversionResult]:
    """Get Abcd Unit conversion parameters given two Unit specifications

     'Get the Energistics style unit parameters given the ''from'' and ''to'' unit symbols and the
    namespace(-list) to disambiguate the unit symbols. Example for a prioritized namespaces list:
    ''LIS,RP66,ECL,Energistics_UoM'' - this will prioritize the units in the LIS namespace over other
    namespaces.'

    Args:
        namespaces (str):
        from_symbol (str):
        to_symbol (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppError | ConversionResult]
    """

    kwargs = _get_kwargs(
        namespaces=namespaces,
        from_symbol=from_symbol,
        to_symbol=to_symbol,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    namespaces: str,
    from_symbol: str,
    to_symbol: str,
    *,
    client: AuthenticatedClient,
) -> AppError | ConversionResult | None:
    """Get Abcd Unit conversion parameters given two Unit specifications

     'Get the Energistics style unit parameters given the ''from'' and ''to'' unit symbols and the
    namespace(-list) to disambiguate the unit symbols. Example for a prioritized namespaces list:
    ''LIS,RP66,ECL,Energistics_UoM'' - this will prioritize the units in the LIS namespace over other
    namespaces.'

    Args:
        namespaces (str):
        from_symbol (str):
        to_symbol (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppError | ConversionResult
    """

    return (
        await asyncio_detailed(
            namespaces=namespaces,
            from_symbol=from_symbol,
            to_symbol=to_symbol,
            client=client,
        )
    ).parsed
