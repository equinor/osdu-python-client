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
    version: int,
    *,
    attribute: list[str] | Unset = UNSET,
    x_collaboration: str | Unset = UNSET,
    data_partition_id: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_collaboration, Unset):
        headers["x-collaboration"] = x_collaboration

    headers["data-partition-id"] = data_partition_id

    params: dict[str, Any] = {}

    json_attribute: list[str] | Unset = UNSET
    if not isinstance(attribute, Unset):
        json_attribute = attribute

    params["attribute"] = json_attribute

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/records/{id}/{version}".format(
            id=quote(str(id), safe=""),
            version=quote(str(version), safe=""),
        ),
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
    id: str,
    version: int,
    *,
    client: AuthenticatedClient,
    attribute: list[str] | Unset = UNSET,
    x_collaboration: str | Unset = UNSET,
    data_partition_id: str,
) -> Response[AppError | str]:
    """Get Specific record

     The API retrieves the specific version of the given record.
    Allowed roles: `service.storage.viewer`, `service.storage.creator` and `service.storage.admin`.

    Args:
        id (str):
        version (int):
        attribute (list[str] | Unset):
        x_collaboration (str | Unset):
        data_partition_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppError | str]
    """

    kwargs = _get_kwargs(
        id=id,
        version=version,
        attribute=attribute,
        x_collaboration=x_collaboration,
        data_partition_id=data_partition_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    version: int,
    *,
    client: AuthenticatedClient,
    attribute: list[str] | Unset = UNSET,
    x_collaboration: str | Unset = UNSET,
    data_partition_id: str,
) -> AppError | str | None:
    """Get Specific record

     The API retrieves the specific version of the given record.
    Allowed roles: `service.storage.viewer`, `service.storage.creator` and `service.storage.admin`.

    Args:
        id (str):
        version (int):
        attribute (list[str] | Unset):
        x_collaboration (str | Unset):
        data_partition_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppError | str
    """

    return sync_detailed(
        id=id,
        version=version,
        client=client,
        attribute=attribute,
        x_collaboration=x_collaboration,
        data_partition_id=data_partition_id,
    ).parsed


async def asyncio_detailed(
    id: str,
    version: int,
    *,
    client: AuthenticatedClient,
    attribute: list[str] | Unset = UNSET,
    x_collaboration: str | Unset = UNSET,
    data_partition_id: str,
) -> Response[AppError | str]:
    """Get Specific record

     The API retrieves the specific version of the given record.
    Allowed roles: `service.storage.viewer`, `service.storage.creator` and `service.storage.admin`.

    Args:
        id (str):
        version (int):
        attribute (list[str] | Unset):
        x_collaboration (str | Unset):
        data_partition_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppError | str]
    """

    kwargs = _get_kwargs(
        id=id,
        version=version,
        attribute=attribute,
        x_collaboration=x_collaboration,
        data_partition_id=data_partition_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    version: int,
    *,
    client: AuthenticatedClient,
    attribute: list[str] | Unset = UNSET,
    x_collaboration: str | Unset = UNSET,
    data_partition_id: str,
) -> AppError | str | None:
    """Get Specific record

     The API retrieves the specific version of the given record.
    Allowed roles: `service.storage.viewer`, `service.storage.creator` and `service.storage.admin`.

    Args:
        id (str):
        version (int):
        attribute (list[str] | Unset):
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
            id=id,
            version=version,
            client=client,
            attribute=attribute,
            x_collaboration=x_collaboration,
            data_partition_id=data_partition_id,
        )
    ).parsed
