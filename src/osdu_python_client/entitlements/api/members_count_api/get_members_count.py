from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_members_count_role import GetMembersCountRole
from ...types import UNSET, Response, Unset


def _get_kwargs(
    group_email: str,
    *,
    role: GetMembersCountRole | Unset = UNSET,
    data_partition_id: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["data-partition-id"] = data_partition_id

    params: dict[str, Any] = {}

    json_role: str | Unset = UNSET
    if not isinstance(role, Unset):
        json_role = role.value

    params["role"] = json_role

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/groups/{group_email}/membersCount".format(
            group_email=quote(str(group_email), safe=""),
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
    group_email: str,
    *,
    client: AuthenticatedClient,
    role: GetMembersCountRole | Unset = UNSET,
    data_partition_id: str,
) -> Response[Any]:
    """Count Members of a group

     Count Members of a group

    Args:
        group_email (str):
        role (GetMembersCountRole | Unset):
        data_partition_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        group_email=group_email,
        role=role,
        data_partition_id=data_partition_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    group_email: str,
    *,
    client: AuthenticatedClient,
    role: GetMembersCountRole | Unset = UNSET,
    data_partition_id: str,
) -> Response[Any]:
    """Count Members of a group

     Count Members of a group

    Args:
        group_email (str):
        role (GetMembersCountRole | Unset):
        data_partition_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        group_email=group_email,
        role=role,
        data_partition_id=data_partition_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
