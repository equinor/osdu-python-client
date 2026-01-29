from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.app_error import AppError
from ...models.replay_status_response import ReplayStatusResponse
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    data_partition_id: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["data-partition-id"] = data_partition_id

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/replay/status/{id}".format(
            id=quote(str(id), safe=""),
        ),
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AppError | ReplayStatusResponse | None:
    if response.status_code == 200:
        response_200 = ReplayStatusResponse.from_dict(response.json())

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
) -> Response[AppError | ReplayStatusResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    data_partition_id: str,
) -> Response[AppError | ReplayStatusResponse]:
    """Get Replay Status.

     The API fetches replay status based on replay id.
    Required roles: `users.datalake.ops`.

    Args:
        id (str):
        data_partition_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppError | ReplayStatusResponse]
    """

    kwargs = _get_kwargs(
        id=id,
        data_partition_id=data_partition_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
    data_partition_id: str,
) -> AppError | ReplayStatusResponse | None:
    """Get Replay Status.

     The API fetches replay status based on replay id.
    Required roles: `users.datalake.ops`.

    Args:
        id (str):
        data_partition_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppError | ReplayStatusResponse
    """

    return sync_detailed(
        id=id,
        client=client,
        data_partition_id=data_partition_id,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    data_partition_id: str,
) -> Response[AppError | ReplayStatusResponse]:
    """Get Replay Status.

     The API fetches replay status based on replay id.
    Required roles: `users.datalake.ops`.

    Args:
        id (str):
        data_partition_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppError | ReplayStatusResponse]
    """

    kwargs = _get_kwargs(
        id=id,
        data_partition_id=data_partition_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    data_partition_id: str,
) -> AppError | ReplayStatusResponse | None:
    """Get Replay Status.

     The API fetches replay status based on replay id.
    Required roles: `users.datalake.ops`.

    Args:
        id (str):
        data_partition_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppError | ReplayStatusResponse
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            data_partition_id=data_partition_id,
        )
    ).parsed
