from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.add_member_dto import AddMemberDto
from ...types import Response


def _get_kwargs(
    group_email: str,
    *,
    body: AddMemberDto,
    data_partition_id: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["data-partition-id"] = data_partition_id

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/groups/{group_email}/members".format(
            group_email=quote(str(group_email), safe=""),
        ),
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
    group_email: str,
    *,
    client: AuthenticatedClient,
    body: AddMemberDto,
    data_partition_id: str,
) -> Response[Any]:
    """Add Member

     Add Member

    Args:
        group_email (str):
        data_partition_id (str):
        body (AddMemberDto): Represents a model to add a member

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        group_email=group_email,
        body=body,
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
    body: AddMemberDto,
    data_partition_id: str,
) -> Response[Any]:
    """Add Member

     Add Member

    Args:
        group_email (str):
        data_partition_id (str):
        body (AddMemberDto): Represents a model to add a member

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        group_email=group_email,
        body=body,
        data_partition_id=data_partition_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
