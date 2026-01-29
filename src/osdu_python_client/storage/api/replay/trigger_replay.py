from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.app_error import AppError
from ...models.replay_request import ReplayRequest
from ...models.replay_response import ReplayResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: ReplayRequest,
    x_collaboration: str | Unset = UNSET,
    data_partition_id: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_collaboration, Unset):
        headers["x-collaboration"] = x_collaboration

    headers["data-partition-id"] = data_partition_id

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/replay",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AppError | ReplayResponse | None:
    if response.status_code == 202:
        response_202 = ReplayResponse.from_dict(response.json())

        return response_202

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
) -> Response[AppError | ReplayResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: ReplayRequest,
    x_collaboration: str | Unset = UNSET,
    data_partition_id: str,
) -> Response[AppError | ReplayResponse]:
    """Replay Based on Filter.

     The API trigger the replay based on operation and filter.
    Required roles: `users.datalake.ops`.

    Args:
        x_collaboration (str | Unset):
        data_partition_id (str):
        body (ReplayRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppError | ReplayResponse]
    """

    kwargs = _get_kwargs(
        body=body,
        x_collaboration=x_collaboration,
        data_partition_id=data_partition_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: ReplayRequest,
    x_collaboration: str | Unset = UNSET,
    data_partition_id: str,
) -> AppError | ReplayResponse | None:
    """Replay Based on Filter.

     The API trigger the replay based on operation and filter.
    Required roles: `users.datalake.ops`.

    Args:
        x_collaboration (str | Unset):
        data_partition_id (str):
        body (ReplayRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppError | ReplayResponse
    """

    return sync_detailed(
        client=client,
        body=body,
        x_collaboration=x_collaboration,
        data_partition_id=data_partition_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: ReplayRequest,
    x_collaboration: str | Unset = UNSET,
    data_partition_id: str,
) -> Response[AppError | ReplayResponse]:
    """Replay Based on Filter.

     The API trigger the replay based on operation and filter.
    Required roles: `users.datalake.ops`.

    Args:
        x_collaboration (str | Unset):
        data_partition_id (str):
        body (ReplayRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppError | ReplayResponse]
    """

    kwargs = _get_kwargs(
        body=body,
        x_collaboration=x_collaboration,
        data_partition_id=data_partition_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: ReplayRequest,
    x_collaboration: str | Unset = UNSET,
    data_partition_id: str,
) -> AppError | ReplayResponse | None:
    """Replay Based on Filter.

     The API trigger the replay based on operation and filter.
    Required roles: `users.datalake.ops`.

    Args:
        x_collaboration (str | Unset):
        data_partition_id (str):
        body (ReplayRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppError | ReplayResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            x_collaboration=x_collaboration,
            data_partition_id=data_partition_id,
        )
    ).parsed
