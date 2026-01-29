from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.app_error import AppError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    x_collaboration: str | Unset = UNSET,
    data_partition_id: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_collaboration, Unset):
        headers["x-collaboration"] = x_collaboration

    headers["data-partition-id"] = data_partition_id

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/records/{id}:delete".format(
            id=quote(str(id), safe=""),
        ),
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | AppError | None:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

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
) -> Response[Any | AppError]:
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
    x_collaboration: str | Unset = UNSET,
    data_partition_id: str,
) -> Response[Any | AppError]:
    """Delete Record

     The API performs a logical deletion of the record using recordId. This operation can be reverted
    later.
    Allowed roles: `service.storage.creator` and `service.storage.admin` who is the OWNER of the record.

    Args:
        id (str):
        x_collaboration (str | Unset):
        data_partition_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | AppError]
    """

    kwargs = _get_kwargs(
        id=id,
        x_collaboration=x_collaboration,
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
    x_collaboration: str | Unset = UNSET,
    data_partition_id: str,
) -> Any | AppError | None:
    """Delete Record

     The API performs a logical deletion of the record using recordId. This operation can be reverted
    later.
    Allowed roles: `service.storage.creator` and `service.storage.admin` who is the OWNER of the record.

    Args:
        id (str):
        x_collaboration (str | Unset):
        data_partition_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | AppError
    """

    return sync_detailed(
        id=id,
        client=client,
        x_collaboration=x_collaboration,
        data_partition_id=data_partition_id,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    x_collaboration: str | Unset = UNSET,
    data_partition_id: str,
) -> Response[Any | AppError]:
    """Delete Record

     The API performs a logical deletion of the record using recordId. This operation can be reverted
    later.
    Allowed roles: `service.storage.creator` and `service.storage.admin` who is the OWNER of the record.

    Args:
        id (str):
        x_collaboration (str | Unset):
        data_partition_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | AppError]
    """

    kwargs = _get_kwargs(
        id=id,
        x_collaboration=x_collaboration,
        data_partition_id=data_partition_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    x_collaboration: str | Unset = UNSET,
    data_partition_id: str,
) -> Any | AppError | None:
    """Delete Record

     The API performs a logical deletion of the record using recordId. This operation can be reverted
    later.
    Allowed roles: `service.storage.creator` and `service.storage.admin` who is the OWNER of the record.

    Args:
        id (str):
        x_collaboration (str | Unset):
        data_partition_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | AppError
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            x_collaboration=x_collaboration,
            data_partition_id=data_partition_id,
        )
    ).parsed
