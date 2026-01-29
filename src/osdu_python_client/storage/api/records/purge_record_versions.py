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
    version_ids: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    from_: int | Unset = UNSET,
    x_collaboration: str | Unset = UNSET,
    data_partition_id: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_collaboration, Unset):
        headers["x-collaboration"] = x_collaboration

    headers["data-partition-id"] = data_partition_id

    params: dict[str, Any] = {}

    params["versionIds"] = version_ids

    params["limit"] = limit

    params["from"] = from_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/records/{id}/versions".format(
            id=quote(str(id), safe=""),
        ),
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | AppError | None:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

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
    version_ids: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    from_: int | Unset = UNSET,
    x_collaboration: str | Unset = UNSET,
    data_partition_id: str,
) -> Response[Any | AppError]:
    """Purge Record Versions

     The API for the given record id performs the permanent physical deletion of the record versions
    excluding latest version and any linked records or files if there are any.
     `versionIds` or `limit` or `from` request parameters used to delete the record versions.

    Args:
        id (str):
        version_ids (str | Unset):
        limit (int | Unset):
        from_ (int | Unset):
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
        version_ids=version_ids,
        limit=limit,
        from_=from_,
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
    version_ids: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    from_: int | Unset = UNSET,
    x_collaboration: str | Unset = UNSET,
    data_partition_id: str,
) -> Any | AppError | None:
    """Purge Record Versions

     The API for the given record id performs the permanent physical deletion of the record versions
    excluding latest version and any linked records or files if there are any.
     `versionIds` or `limit` or `from` request parameters used to delete the record versions.

    Args:
        id (str):
        version_ids (str | Unset):
        limit (int | Unset):
        from_ (int | Unset):
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
        version_ids=version_ids,
        limit=limit,
        from_=from_,
        x_collaboration=x_collaboration,
        data_partition_id=data_partition_id,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    version_ids: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    from_: int | Unset = UNSET,
    x_collaboration: str | Unset = UNSET,
    data_partition_id: str,
) -> Response[Any | AppError]:
    """Purge Record Versions

     The API for the given record id performs the permanent physical deletion of the record versions
    excluding latest version and any linked records or files if there are any.
     `versionIds` or `limit` or `from` request parameters used to delete the record versions.

    Args:
        id (str):
        version_ids (str | Unset):
        limit (int | Unset):
        from_ (int | Unset):
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
        version_ids=version_ids,
        limit=limit,
        from_=from_,
        x_collaboration=x_collaboration,
        data_partition_id=data_partition_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    version_ids: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    from_: int | Unset = UNSET,
    x_collaboration: str | Unset = UNSET,
    data_partition_id: str,
) -> Any | AppError | None:
    """Purge Record Versions

     The API for the given record id performs the permanent physical deletion of the record versions
    excluding latest version and any linked records or files if there are any.
     `versionIds` or `limit` or `from` request parameters used to delete the record versions.

    Args:
        id (str):
        version_ids (str | Unset):
        limit (int | Unset):
        from_ (int | Unset):
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
            version_ids=version_ids,
            limit=limit,
            from_=from_,
            x_collaboration=x_collaboration,
            data_partition_id=data_partition_id,
        )
    ).parsed
