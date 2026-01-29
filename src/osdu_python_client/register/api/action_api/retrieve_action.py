from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.json_node import JsonNode
from ...types import Response


def _get_kwargs(
    *,
    body: JsonNode,
    data_partition_id: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["data-partition-id"] = data_partition_id

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/action:retrieve",
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
    body: JsonNode,
    data_partition_id: str,
) -> Response[Any]:
    """Query for action registrations and substitutes any action with the given parameters

     Retrieve an action registration. Required roles: `users.datalake.ops` or `users.datalake.admins` or
    `users.datalake.editors` or `users.datalake.viewers`

    Args:
        data_partition_id (str):
        body (JsonNode): testPayload Example: {'id': 'common:regularheightfield:123456', 'kind':
            'common:petrel:regularheightfield:1.0.0', 'data': {'uri': 'https://myproj.com/abc123'}}.

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
    body: JsonNode,
    data_partition_id: str,
) -> Response[Any]:
    """Query for action registrations and substitutes any action with the given parameters

     Retrieve an action registration. Required roles: `users.datalake.ops` or `users.datalake.admins` or
    `users.datalake.editors` or `users.datalake.viewers`

    Args:
        data_partition_id (str):
        body (JsonNode): testPayload Example: {'id': 'common:regularheightfield:123456', 'kind':
            'common:petrel:regularheightfield:1.0.0', 'data': {'uri': 'https://myproj.com/abc123'}}.

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
