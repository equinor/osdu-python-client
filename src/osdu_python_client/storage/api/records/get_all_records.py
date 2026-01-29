import datetime
from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.app_error import AppError
from ...models.get_all_records_sort_order import GetAllRecordsSortOrder
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    limit: int | Unset = 20,
    kind: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
    deleted: bool | Unset = False,
    modified_after_date: datetime.datetime | Unset = UNSET,
    sort_order: GetAllRecordsSortOrder | Unset = GetAllRecordsSortOrder.DESC,
    x_collaboration: str | Unset = UNSET,
    data_partition_id: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_collaboration, Unset):
        headers["x-collaboration"] = x_collaboration

    headers["data-partition-id"] = data_partition_id

    params: dict[str, Any] = {}

    params["limit"] = limit

    params["kind"] = kind

    params["cursor"] = cursor

    params["deleted"] = deleted

    json_modified_after_date: str | Unset = UNSET
    if not isinstance(modified_after_date, Unset):
        json_modified_after_date = modified_after_date.isoformat()
    params["modifiedAfterDate"] = json_modified_after_date

    json_sort_order: str | Unset = UNSET
    if not isinstance(sort_order, Unset):
        json_sort_order = sort_order.value

    params["sortOrder"] = json_sort_order

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/records",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AppError | str | None:
    if response.status_code == 200:
        response_200 = cast(str, response.json())
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
) -> Response[AppError | str]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 20,
    kind: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
    deleted: bool | Unset = False,
    modified_after_date: datetime.datetime | Unset = UNSET,
    sort_order: GetAllRecordsSortOrder | Unset = GetAllRecordsSortOrder.DESC,
    x_collaboration: str | Unset = UNSET,
    data_partition_id: str,
) -> Response[AppError | str]:
    """Fetch All records

     This API retrieves multiple records in a single request with support for filtering by kind, deleted
    status and lastModifiedDate. It is paginated, using a cursor parameter to fetch subsequent pages.The
    default page size is 20, configurable via the limit parameter.
    Allowed roles: `service.storage.viewer`,`service.storage.creator` and `service.storage.admin`.

    Args:
        limit (int | Unset):  Default: 20.
        kind (str | Unset):
        cursor (str | Unset):
        deleted (bool | Unset):  Default: False.
        modified_after_date (datetime.datetime | Unset):
        sort_order (GetAllRecordsSortOrder | Unset):  Default: GetAllRecordsSortOrder.DESC.
        x_collaboration (str | Unset):
        data_partition_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppError | str]
    """

    kwargs = _get_kwargs(
        limit=limit,
        kind=kind,
        cursor=cursor,
        deleted=deleted,
        modified_after_date=modified_after_date,
        sort_order=sort_order,
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
    limit: int | Unset = 20,
    kind: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
    deleted: bool | Unset = False,
    modified_after_date: datetime.datetime | Unset = UNSET,
    sort_order: GetAllRecordsSortOrder | Unset = GetAllRecordsSortOrder.DESC,
    x_collaboration: str | Unset = UNSET,
    data_partition_id: str,
) -> AppError | str | None:
    """Fetch All records

     This API retrieves multiple records in a single request with support for filtering by kind, deleted
    status and lastModifiedDate. It is paginated, using a cursor parameter to fetch subsequent pages.The
    default page size is 20, configurable via the limit parameter.
    Allowed roles: `service.storage.viewer`,`service.storage.creator` and `service.storage.admin`.

    Args:
        limit (int | Unset):  Default: 20.
        kind (str | Unset):
        cursor (str | Unset):
        deleted (bool | Unset):  Default: False.
        modified_after_date (datetime.datetime | Unset):
        sort_order (GetAllRecordsSortOrder | Unset):  Default: GetAllRecordsSortOrder.DESC.
        x_collaboration (str | Unset):
        data_partition_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppError | str
    """

    return sync_detailed(
        client=client,
        limit=limit,
        kind=kind,
        cursor=cursor,
        deleted=deleted,
        modified_after_date=modified_after_date,
        sort_order=sort_order,
        x_collaboration=x_collaboration,
        data_partition_id=data_partition_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 20,
    kind: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
    deleted: bool | Unset = False,
    modified_after_date: datetime.datetime | Unset = UNSET,
    sort_order: GetAllRecordsSortOrder | Unset = GetAllRecordsSortOrder.DESC,
    x_collaboration: str | Unset = UNSET,
    data_partition_id: str,
) -> Response[AppError | str]:
    """Fetch All records

     This API retrieves multiple records in a single request with support for filtering by kind, deleted
    status and lastModifiedDate. It is paginated, using a cursor parameter to fetch subsequent pages.The
    default page size is 20, configurable via the limit parameter.
    Allowed roles: `service.storage.viewer`,`service.storage.creator` and `service.storage.admin`.

    Args:
        limit (int | Unset):  Default: 20.
        kind (str | Unset):
        cursor (str | Unset):
        deleted (bool | Unset):  Default: False.
        modified_after_date (datetime.datetime | Unset):
        sort_order (GetAllRecordsSortOrder | Unset):  Default: GetAllRecordsSortOrder.DESC.
        x_collaboration (str | Unset):
        data_partition_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppError | str]
    """

    kwargs = _get_kwargs(
        limit=limit,
        kind=kind,
        cursor=cursor,
        deleted=deleted,
        modified_after_date=modified_after_date,
        sort_order=sort_order,
        x_collaboration=x_collaboration,
        data_partition_id=data_partition_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 20,
    kind: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
    deleted: bool | Unset = False,
    modified_after_date: datetime.datetime | Unset = UNSET,
    sort_order: GetAllRecordsSortOrder | Unset = GetAllRecordsSortOrder.DESC,
    x_collaboration: str | Unset = UNSET,
    data_partition_id: str,
) -> AppError | str | None:
    """Fetch All records

     This API retrieves multiple records in a single request with support for filtering by kind, deleted
    status and lastModifiedDate. It is paginated, using a cursor parameter to fetch subsequent pages.The
    default page size is 20, configurable via the limit parameter.
    Allowed roles: `service.storage.viewer`,`service.storage.creator` and `service.storage.admin`.

    Args:
        limit (int | Unset):  Default: 20.
        kind (str | Unset):
        cursor (str | Unset):
        deleted (bool | Unset):  Default: False.
        modified_after_date (datetime.datetime | Unset):
        sort_order (GetAllRecordsSortOrder | Unset):  Default: GetAllRecordsSortOrder.DESC.
        x_collaboration (str | Unset):
        data_partition_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppError | str
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            kind=kind,
            cursor=cursor,
            deleted=deleted,
            modified_after_date=modified_after_date,
            sort_order=sort_order,
            x_collaboration=x_collaboration,
            data_partition_id=data_partition_id,
        )
    ).parsed
