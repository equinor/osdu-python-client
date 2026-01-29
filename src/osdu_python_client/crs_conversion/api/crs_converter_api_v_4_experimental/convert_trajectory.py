from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.convert_trajectory_request_v4 import ConvertTrajectoryRequestV4
from ...models.convert_trajectory_response_v4 import ConvertTrajectoryResponseV4
from ...types import Response


def _get_kwargs(
    *,
    body: ConvertTrajectoryRequestV4,
    data_partition_id: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["data-partition-id"] = data_partition_id

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v4/convertTrajectory",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ConvertTrajectoryResponseV4 | None:
    if response.status_code == 200:
        response_200 = ConvertTrajectoryResponseV4.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ConvertTrajectoryResponseV4]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: ConvertTrajectoryRequestV4,
    data_partition_id: str,
) -> Response[ConvertTrajectoryResponseV4]:
    """Convert trajectory stations

     Convert a list of trajectory stations, given the unit and spatial context and a reference point in
    3D where MD==0

    Args:
        data_partition_id (str):
        body (ConvertTrajectoryRequestV4):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConvertTrajectoryResponseV4]
    """

    kwargs = _get_kwargs(
        body=body,
        data_partition_id=data_partition_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: ConvertTrajectoryRequestV4,
    data_partition_id: str,
) -> ConvertTrajectoryResponseV4 | None:
    """Convert trajectory stations

     Convert a list of trajectory stations, given the unit and spatial context and a reference point in
    3D where MD==0

    Args:
        data_partition_id (str):
        body (ConvertTrajectoryRequestV4):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConvertTrajectoryResponseV4
    """

    return sync_detailed(
        client=client,
        body=body,
        data_partition_id=data_partition_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: ConvertTrajectoryRequestV4,
    data_partition_id: str,
) -> Response[ConvertTrajectoryResponseV4]:
    """Convert trajectory stations

     Convert a list of trajectory stations, given the unit and spatial context and a reference point in
    3D where MD==0

    Args:
        data_partition_id (str):
        body (ConvertTrajectoryRequestV4):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConvertTrajectoryResponseV4]
    """

    kwargs = _get_kwargs(
        body=body,
        data_partition_id=data_partition_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: ConvertTrajectoryRequestV4,
    data_partition_id: str,
) -> ConvertTrajectoryResponseV4 | None:
    """Convert trajectory stations

     Convert a list of trajectory stations, given the unit and spatial context and a reference point in
    3D where MD==0

    Args:
        data_partition_id (str):
        body (ConvertTrajectoryRequestV4):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConvertTrajectoryResponseV4
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            data_partition_id=data_partition_id,
        )
    ).parsed
