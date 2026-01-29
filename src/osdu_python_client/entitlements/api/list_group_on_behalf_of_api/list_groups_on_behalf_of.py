from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    member_email: str,
    *,
    type_: str,
    appid: str | Unset = UNSET,
    role_required: bool | Unset = False,
    data_partition_id: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["data-partition-id"] = data_partition_id

    params: dict[str, Any] = {}

    params["type"] = type_

    params["appid"] = appid

    params["roleRequired"] = role_required

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/members/{member_email}/groups".format(
            member_email=quote(str(member_email), safe=""),
        ),
        "params": params,
    }

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
    member_email: str,
    *,
    client: AuthenticatedClient,
    type_: str,
    appid: str | Unset = UNSET,
    role_required: bool | Unset = False,
    data_partition_id: str,
) -> Response[Any]:
    """List Group On Behalf Of

     List Group On Behalf Of

    Args:
        member_email (str):
        type_ (str):
        appid (str | Unset):
        role_required (bool | Unset):  Default: False.
        data_partition_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        member_email=member_email,
        type_=type_,
        appid=appid,
        role_required=role_required,
        data_partition_id=data_partition_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    member_email: str,
    *,
    client: AuthenticatedClient,
    type_: str,
    appid: str | Unset = UNSET,
    role_required: bool | Unset = False,
    data_partition_id: str,
) -> Response[Any]:
    """List Group On Behalf Of

     List Group On Behalf Of

    Args:
        member_email (str):
        type_ (str):
        appid (str | Unset):
        role_required (bool | Unset):  Default: False.
        data_partition_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        member_email=member_email,
        type_=type_,
        appid=appid,
        role_required=role_required,
        data_partition_id=data_partition_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
