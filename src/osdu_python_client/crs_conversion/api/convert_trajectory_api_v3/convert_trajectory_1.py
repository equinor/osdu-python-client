from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.convert_trajectory_request import ConvertTrajectoryRequest
from ...types import Response


def _get_kwargs(
    *,
    body: ConvertTrajectoryRequest,
    data_partition_id: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["data-partition-id"] = data_partition_id

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v3/convertTrajectory",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | None:
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: ConvertTrajectoryRequest,
    data_partition_id: str,
) -> Response[Any]:
    """Convert trajectory stations

     Convert a list of trajectory stations, given the unit and spatial context and a reference point in
    3D where MD==0.
     + Note: To get WGS 84 output the trajectoryCRS needs to be a BoundCRS (unless it is WGS 84 based)

    Args:
        data_partition_id (str):
        body (ConvertTrajectoryRequest): Input trajectory data structure; contains the context
            (crs, units, azimuth reference, method)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        body=body,
        data_partition_id=data_partition_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: ConvertTrajectoryRequest,
    data_partition_id: str,
) -> Response[Any]:
    """Convert trajectory stations

     Convert a list of trajectory stations, given the unit and spatial context and a reference point in
    3D where MD==0.
     + Note: To get WGS 84 output the trajectoryCRS needs to be a BoundCRS (unless it is WGS 84 based)

    Args:
        data_partition_id (str):
        body (ConvertTrajectoryRequest): Input trajectory data structure; contains the context
            (crs, units, azimuth reference, method)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        body=body,
        data_partition_id=data_partition_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
