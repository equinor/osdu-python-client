from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.convert_bin_grid_request import ConvertBinGridRequest
from ...types import Response


def _get_kwargs(
    *,
    body: ConvertBinGridRequest,
    data_partition_id: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["data-partition-id"] = data_partition_id

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v3/convertBinGrid",
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
    body: ConvertBinGridRequest,
    data_partition_id: str,
) -> Response[Any]:
    """CRS Convert service is an OSDU platform standard method for QC and conversion of Bin Grids,
    associated in particular with ingested seismic volumes, that describe the `real world` (Easting,
    Northing) of bin grid centers at (inline, crossline) local coordinates

     QC check of the `squareness` of a Bin Grid defined using 4 corner points.
     + Coordinate conversion of a Bin Grid to a new CRS and `square it up` (if target CRS is same as
    original CRS then conversion is omitted, and the squareness test is done in the original CRS).
     + Calculate derived P6 parameters from the input 4 corners.
     + Calculate WGS 84 coordinates at the corners
     + Returns converted Bin Grid and a QC of squareness of the bin grid

    Args:
        data_partition_id (str):
        body (ConvertBinGridRequest):

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
    body: ConvertBinGridRequest,
    data_partition_id: str,
) -> Response[Any]:
    """CRS Convert service is an OSDU platform standard method for QC and conversion of Bin Grids,
    associated in particular with ingested seismic volumes, that describe the `real world` (Easting,
    Northing) of bin grid centers at (inline, crossline) local coordinates

     QC check of the `squareness` of a Bin Grid defined using 4 corner points.
     + Coordinate conversion of a Bin Grid to a new CRS and `square it up` (if target CRS is same as
    original CRS then conversion is omitted, and the squareness test is done in the original CRS).
     + Calculate derived P6 parameters from the input 4 corners.
     + Calculate WGS 84 coordinates at the corners
     + Returns converted Bin Grid and a QC of squareness of the bin grid

    Args:
        data_partition_id (str):
        body (ConvertBinGridRequest):

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
