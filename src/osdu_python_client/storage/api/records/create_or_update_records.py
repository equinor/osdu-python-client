from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.app_error import AppError
from ...models.create_update_records_response import CreateUpdateRecordsResponse
from ...models.record import Record
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: list[Record],
    skipdupes: bool | Unset = UNSET,
    x_collaboration: str | Unset = UNSET,
    data_partition_id: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_collaboration, Unset):
        headers["x-collaboration"] = x_collaboration

    headers["data-partition-id"] = data_partition_id

    params: dict[str, Any] = {}

    params["skipdupes"] = skipdupes

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/records",
        "params": params,
    }

    _kwargs["json"] = []
    for body_item_data in body:
        body_item = body_item_data.to_dict()
        _kwargs["json"].append(body_item)

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AppError | CreateUpdateRecordsResponse | None:
    if response.status_code == 201:
        response_201 = CreateUpdateRecordsResponse.from_dict(response.json())

        return response_201

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
) -> Response[AppError | CreateUpdateRecordsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: list[Record],
    skipdupes: bool | Unset = UNSET,
    x_collaboration: str | Unset = UNSET,
    data_partition_id: str,
) -> Response[AppError | CreateUpdateRecordsResponse]:
    """Create or Update Records

     The API represents the main injection mechanism into the Data Ecosystem.
    It allows records creation and/or update.When no record id is provided or when the provided id is
    not already present in the Data Ecosystem then a new record is created.
     If the id is related to an existing record in the Data Ecosystem then an update operation takes
    place and a new version of the record is created.

    Args:
        skipdupes (bool | Unset):
        x_collaboration (str | Unset):
        data_partition_id (str):
        body (list[Record]): Records to be created/updated

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppError | CreateUpdateRecordsResponse]
    """

    kwargs = _get_kwargs(
        body=body,
        skipdupes=skipdupes,
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
    body: list[Record],
    skipdupes: bool | Unset = UNSET,
    x_collaboration: str | Unset = UNSET,
    data_partition_id: str,
) -> AppError | CreateUpdateRecordsResponse | None:
    """Create or Update Records

     The API represents the main injection mechanism into the Data Ecosystem.
    It allows records creation and/or update.When no record id is provided or when the provided id is
    not already present in the Data Ecosystem then a new record is created.
     If the id is related to an existing record in the Data Ecosystem then an update operation takes
    place and a new version of the record is created.

    Args:
        skipdupes (bool | Unset):
        x_collaboration (str | Unset):
        data_partition_id (str):
        body (list[Record]): Records to be created/updated

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppError | CreateUpdateRecordsResponse
    """

    return sync_detailed(
        client=client,
        body=body,
        skipdupes=skipdupes,
        x_collaboration=x_collaboration,
        data_partition_id=data_partition_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: list[Record],
    skipdupes: bool | Unset = UNSET,
    x_collaboration: str | Unset = UNSET,
    data_partition_id: str,
) -> Response[AppError | CreateUpdateRecordsResponse]:
    """Create or Update Records

     The API represents the main injection mechanism into the Data Ecosystem.
    It allows records creation and/or update.When no record id is provided or when the provided id is
    not already present in the Data Ecosystem then a new record is created.
     If the id is related to an existing record in the Data Ecosystem then an update operation takes
    place and a new version of the record is created.

    Args:
        skipdupes (bool | Unset):
        x_collaboration (str | Unset):
        data_partition_id (str):
        body (list[Record]): Records to be created/updated

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppError | CreateUpdateRecordsResponse]
    """

    kwargs = _get_kwargs(
        body=body,
        skipdupes=skipdupes,
        x_collaboration=x_collaboration,
        data_partition_id=data_partition_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: list[Record],
    skipdupes: bool | Unset = UNSET,
    x_collaboration: str | Unset = UNSET,
    data_partition_id: str,
) -> AppError | CreateUpdateRecordsResponse | None:
    """Create or Update Records

     The API represents the main injection mechanism into the Data Ecosystem.
    It allows records creation and/or update.When no record id is provided or when the provided id is
    not already present in the Data Ecosystem then a new record is created.
     If the id is related to an existing record in the Data Ecosystem then an update operation takes
    place and a new version of the record is created.

    Args:
        skipdupes (bool | Unset):
        x_collaboration (str | Unset):
        data_partition_id (str):
        body (list[Record]): Records to be created/updated

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppError | CreateUpdateRecordsResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            skipdupes=skipdupes,
            x_collaboration=x_collaboration,
            data_partition_id=data_partition_id,
        )
    ).parsed
