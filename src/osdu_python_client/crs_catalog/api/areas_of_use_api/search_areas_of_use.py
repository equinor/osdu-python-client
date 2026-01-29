from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.app_error import AppError
from ...models.area_of_use_results import AreaOfUseResults
from ...models.search_request import SearchRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: SearchRequest,
    longitude_left: float | Unset = -180.0,
    latitude_lower: float | Unset = -90.0,
    longitude_right: float | Unset = 180.0,
    latitude_upper: float | Unset = 90.0,
    offset: int | Unset = 0,
    limit: int | Unset = 100,
    mode: str | Unset = "persistableReference",
    data_partition_id: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["data-partition-id"] = data_partition_id

    params: dict[str, Any] = {}

    params["longitudeLeft"] = longitude_left

    params["latitudeLower"] = latitude_lower

    params["longitudeRight"] = longitude_right

    params["latitudeUpper"] = latitude_upper

    params["offset"] = offset

    params["limit"] = limit

    params["mode"] = mode

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v2/search/area",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AppError | AreaOfUseResults | None:
    if response.status_code == 200:
        response_200 = AreaOfUseResults.from_dict(response.json())

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
) -> Response[AppError | AreaOfUseResults]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: SearchRequest,
    longitude_left: float | Unset = -180.0,
    latitude_lower: float | Unset = -90.0,
    longitude_right: float | Unset = 180.0,
    latitude_upper: float | Unset = 90.0,
    offset: int | Unset = 0,
    limit: int | Unset = 100,
    mode: str | Unset = "persistableReference",
    data_partition_id: str,
) -> Response[AppError | AreaOfUseResults]:
    """Search Areas of Use

     Search Area of Use records by keywords and/or geographic area - returning named bounding box
    definitions in latitude and longitude. Geographical constraints are passed (optionally) as
    parameters via the query URL, search keywords are passed via the request body. Query syntax follows
    Lucene style, default operator for multiple expressions is AND. The following keywords are
    supported: ''name:'', ''description:'', ''authority:'', ''code:'', ''deprecationState:'',
    ''remarks:'' (deprecationState remarks), ''lastModified:''. Example ''name:*America*''.

    Args:
        longitude_left (float | Unset):  Default: -180.0.
        latitude_lower (float | Unset):  Default: -90.0.
        longitude_right (float | Unset):  Default: 180.0.
        latitude_upper (float | Unset):  Default: 90.0.
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 100.
        mode (str | Unset):  Default: 'persistableReference'.
        data_partition_id (str):
        body (SearchRequest): Request to containing a Lucene style query string.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppError | AreaOfUseResults]
    """

    kwargs = _get_kwargs(
        body=body,
        longitude_left=longitude_left,
        latitude_lower=latitude_lower,
        longitude_right=longitude_right,
        latitude_upper=latitude_upper,
        offset=offset,
        limit=limit,
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
    body: SearchRequest,
    longitude_left: float | Unset = -180.0,
    latitude_lower: float | Unset = -90.0,
    longitude_right: float | Unset = 180.0,
    latitude_upper: float | Unset = 90.0,
    offset: int | Unset = 0,
    limit: int | Unset = 100,
    mode: str | Unset = "persistableReference",
    data_partition_id: str,
) -> AppError | AreaOfUseResults | None:
    """Search Areas of Use

     Search Area of Use records by keywords and/or geographic area - returning named bounding box
    definitions in latitude and longitude. Geographical constraints are passed (optionally) as
    parameters via the query URL, search keywords are passed via the request body. Query syntax follows
    Lucene style, default operator for multiple expressions is AND. The following keywords are
    supported: ''name:'', ''description:'', ''authority:'', ''code:'', ''deprecationState:'',
    ''remarks:'' (deprecationState remarks), ''lastModified:''. Example ''name:*America*''.

    Args:
        longitude_left (float | Unset):  Default: -180.0.
        latitude_lower (float | Unset):  Default: -90.0.
        longitude_right (float | Unset):  Default: 180.0.
        latitude_upper (float | Unset):  Default: 90.0.
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 100.
        mode (str | Unset):  Default: 'persistableReference'.
        data_partition_id (str):
        body (SearchRequest): Request to containing a Lucene style query string.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppError | AreaOfUseResults
    """

    return sync_detailed(
        client=client,
        body=body,
        longitude_left=longitude_left,
        latitude_lower=latitude_lower,
        longitude_right=longitude_right,
        latitude_upper=latitude_upper,
        offset=offset,
        limit=limit,
        mode=mode,
        data_partition_id=data_partition_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: SearchRequest,
    longitude_left: float | Unset = -180.0,
    latitude_lower: float | Unset = -90.0,
    longitude_right: float | Unset = 180.0,
    latitude_upper: float | Unset = 90.0,
    offset: int | Unset = 0,
    limit: int | Unset = 100,
    mode: str | Unset = "persistableReference",
    data_partition_id: str,
) -> Response[AppError | AreaOfUseResults]:
    """Search Areas of Use

     Search Area of Use records by keywords and/or geographic area - returning named bounding box
    definitions in latitude and longitude. Geographical constraints are passed (optionally) as
    parameters via the query URL, search keywords are passed via the request body. Query syntax follows
    Lucene style, default operator for multiple expressions is AND. The following keywords are
    supported: ''name:'', ''description:'', ''authority:'', ''code:'', ''deprecationState:'',
    ''remarks:'' (deprecationState remarks), ''lastModified:''. Example ''name:*America*''.

    Args:
        longitude_left (float | Unset):  Default: -180.0.
        latitude_lower (float | Unset):  Default: -90.0.
        longitude_right (float | Unset):  Default: 180.0.
        latitude_upper (float | Unset):  Default: 90.0.
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 100.
        mode (str | Unset):  Default: 'persistableReference'.
        data_partition_id (str):
        body (SearchRequest): Request to containing a Lucene style query string.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppError | AreaOfUseResults]
    """

    kwargs = _get_kwargs(
        body=body,
        longitude_left=longitude_left,
        latitude_lower=latitude_lower,
        longitude_right=longitude_right,
        latitude_upper=latitude_upper,
        offset=offset,
        limit=limit,
        mode=mode,
        data_partition_id=data_partition_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: SearchRequest,
    longitude_left: float | Unset = -180.0,
    latitude_lower: float | Unset = -90.0,
    longitude_right: float | Unset = 180.0,
    latitude_upper: float | Unset = 90.0,
    offset: int | Unset = 0,
    limit: int | Unset = 100,
    mode: str | Unset = "persistableReference",
    data_partition_id: str,
) -> AppError | AreaOfUseResults | None:
    """Search Areas of Use

     Search Area of Use records by keywords and/or geographic area - returning named bounding box
    definitions in latitude and longitude. Geographical constraints are passed (optionally) as
    parameters via the query URL, search keywords are passed via the request body. Query syntax follows
    Lucene style, default operator for multiple expressions is AND. The following keywords are
    supported: ''name:'', ''description:'', ''authority:'', ''code:'', ''deprecationState:'',
    ''remarks:'' (deprecationState remarks), ''lastModified:''. Example ''name:*America*''.

    Args:
        longitude_left (float | Unset):  Default: -180.0.
        latitude_lower (float | Unset):  Default: -90.0.
        longitude_right (float | Unset):  Default: 180.0.
        latitude_upper (float | Unset):  Default: 90.0.
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 100.
        mode (str | Unset):  Default: 'persistableReference'.
        data_partition_id (str):
        body (SearchRequest): Request to containing a Lucene style query string.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppError | AreaOfUseResults
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            longitude_left=longitude_left,
            latitude_lower=latitude_lower,
            longitude_right=longitude_right,
            latitude_upper=latitude_upper,
            offset=offset,
            limit=limit,
            mode=mode,
            data_partition_id=data_partition_id,
        )
    ).parsed
