from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.app_error import AppError
from ...models.conversion_result import ConversionResult
from ...types import UNSET, Response


def _get_kwargs(
    *,
    namespaces: str,
    from_symbol: str,
    to_symbol: str,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["namespaces"] = namespaces

    params["fromSymbol"] = from_symbol

    params["toSymbol"] = to_symbol

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v3/conversion/scale",
        "params": params,
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
    *,
    client: AuthenticatedClient,
    namespaces: str,
    from_symbol: str,
    to_symbol: str,
) -> Response[AppError | ConversionResult]:
    """getConversionScaleOffsetBySymbols

     Get Conversion Scale Offset By Symbols Using GET

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
    *,
    client: AuthenticatedClient,
    namespaces: str,
    from_symbol: str,
    to_symbol: str,
) -> AppError | ConversionResult | None:
    """getConversionScaleOffsetBySymbols

     Get Conversion Scale Offset By Symbols Using GET

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
        client=client,
        namespaces=namespaces,
        from_symbol=from_symbol,
        to_symbol=to_symbol,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    namespaces: str,
    from_symbol: str,
    to_symbol: str,
) -> Response[AppError | ConversionResult]:
    """getConversionScaleOffsetBySymbols

     Get Conversion Scale Offset By Symbols Using GET

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
    *,
    client: AuthenticatedClient,
    namespaces: str,
    from_symbol: str,
    to_symbol: str,
) -> AppError | ConversionResult | None:
    """getConversionScaleOffsetBySymbols

     Get Conversion Scale Offset By Symbols Using GET

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
            client=client,
            namespaces=namespaces,
            from_symbol=from_symbol,
            to_symbol=to_symbol,
        )
    ).parsed
