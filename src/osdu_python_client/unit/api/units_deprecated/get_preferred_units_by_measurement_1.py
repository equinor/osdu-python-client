from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.app_error import AppError
from ...models.query_result import QueryResult
from ...types import Response


def _get_kwargs(
    ancestry: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v2/unit/measurement/preferred/{ancestry}".format(
            ancestry=quote(str(ancestry), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AppError | QueryResult | None:
    if response.status_code == 200:
        response_200 = QueryResult.from_dict(response.json())

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
) -> Response[AppError | QueryResult]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    ancestry: str,
    *,
    client: AuthenticatedClient,
) -> Response[AppError | QueryResult]:
    """Get preferred Units for a Measurement by ancestry

     Get the preferred units given dot separated ancestry, e.g. Time_Per_Length.Acoustic_Slowness.

    Args:
        ancestry (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppError | QueryResult]
    """

    kwargs = _get_kwargs(
        ancestry=ancestry,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    ancestry: str,
    *,
    client: AuthenticatedClient,
) -> AppError | QueryResult | None:
    """Get preferred Units for a Measurement by ancestry

     Get the preferred units given dot separated ancestry, e.g. Time_Per_Length.Acoustic_Slowness.

    Args:
        ancestry (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppError | QueryResult
    """

    return sync_detailed(
        ancestry=ancestry,
        client=client,
    ).parsed


async def asyncio_detailed(
    ancestry: str,
    *,
    client: AuthenticatedClient,
) -> Response[AppError | QueryResult]:
    """Get preferred Units for a Measurement by ancestry

     Get the preferred units given dot separated ancestry, e.g. Time_Per_Length.Acoustic_Slowness.

    Args:
        ancestry (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppError | QueryResult]
    """

    kwargs = _get_kwargs(
        ancestry=ancestry,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    ancestry: str,
    *,
    client: AuthenticatedClient,
) -> AppError | QueryResult | None:
    """Get preferred Units for a Measurement by ancestry

     Get the preferred units given dot separated ancestry, e.g. Time_Per_Length.Acoustic_Slowness.

    Args:
        ancestry (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppError | QueryResult
    """

    return (
        await asyncio_detailed(
            ancestry=ancestry,
            client=client,
        )
    ).parsed
