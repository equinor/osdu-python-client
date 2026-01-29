from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.app_error import AppError
from ...models.late_bound_crs import LateBoundCRS
from ...models.late_bound_crs_request import LateBoundCRSRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: LateBoundCRSRequest,
    mode: str | Unset = "persistableReference",
    data_partition_id: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["data-partition-id"] = data_partition_id

    params: dict[str, Any] = {}

    params["mode"] = mode

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v2/lateboundcrs",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AppError | LateBoundCRS | None:
    if response.status_code == 200:
        response_200 = LateBoundCRS.from_dict(response.json())

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
) -> Response[AppError | LateBoundCRS]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: LateBoundCRSRequest,
    mode: str | Unset = "persistableReference",
    data_partition_id: str,
) -> Response[AppError | LateBoundCRS]:
    """Get one LateBoundCRS

     Get one LateBoundCRS given its persistable reference string or essence structure.

    Args:
        mode (str | Unset):  Default: 'persistableReference'.
        data_partition_id (str):
        body (LateBoundCRSRequest): Request to get one LateBoundCRS given its
            'persistableReference' (serialized essence) or 'essence' structure. Only one,
            persistableReference or essence must be provided. If both are provided, essence takes
            precedence.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppError | LateBoundCRS]
    """

    kwargs = _get_kwargs(
        body=body,
        mode=mode,
        data_partition_id=data_partition_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: LateBoundCRSRequest,
    mode: str | Unset = "persistableReference",
    data_partition_id: str,
) -> AppError | LateBoundCRS | None:
    """Get one LateBoundCRS

     Get one LateBoundCRS given its persistable reference string or essence structure.

    Args:
        mode (str | Unset):  Default: 'persistableReference'.
        data_partition_id (str):
        body (LateBoundCRSRequest): Request to get one LateBoundCRS given its
            'persistableReference' (serialized essence) or 'essence' structure. Only one,
            persistableReference or essence must be provided. If both are provided, essence takes
            precedence.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppError | LateBoundCRS
    """

    return sync_detailed(
        client=client,
        body=body,
        mode=mode,
        data_partition_id=data_partition_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: LateBoundCRSRequest,
    mode: str | Unset = "persistableReference",
    data_partition_id: str,
) -> Response[AppError | LateBoundCRS]:
    """Get one LateBoundCRS

     Get one LateBoundCRS given its persistable reference string or essence structure.

    Args:
        mode (str | Unset):  Default: 'persistableReference'.
        data_partition_id (str):
        body (LateBoundCRSRequest): Request to get one LateBoundCRS given its
            'persistableReference' (serialized essence) or 'essence' structure. Only one,
            persistableReference or essence must be provided. If both are provided, essence takes
            precedence.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppError | LateBoundCRS]
    """

    kwargs = _get_kwargs(
        body=body,
        mode=mode,
        data_partition_id=data_partition_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: LateBoundCRSRequest,
    mode: str | Unset = "persistableReference",
    data_partition_id: str,
) -> AppError | LateBoundCRS | None:
    """Get one LateBoundCRS

     Get one LateBoundCRS given its persistable reference string or essence structure.

    Args:
        mode (str | Unset):  Default: 'persistableReference'.
        data_partition_id (str):
        body (LateBoundCRSRequest): Request to get one LateBoundCRS given its
            'persistableReference' (serialized essence) or 'essence' structure. Only one,
            persistableReference or essence must be provided. If both are provided, essence takes
            precedence.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppError | LateBoundCRS
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            mode=mode,
            data_partition_id=data_partition_id,
        )
    ).parsed
