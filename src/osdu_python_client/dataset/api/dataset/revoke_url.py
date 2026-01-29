from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.revoke_url_body import RevokeURLBody
from ...types import UNSET, Response


def _get_kwargs(
    *,
    body: RevokeURLBody,
    kind_sub_type: str,
    data_partition_id: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["data-partition-id"] = data_partition_id

    params: dict[str, Any] = {}

    params["kindSubType"] = kind_sub_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/revokeURL",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | None:
    if response.status_code == 204:
        return None

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
    body: RevokeURLBody,
    kind_sub_type: str,
    data_partition_id: str,
) -> Response[Any]:
    """Revoke previously generated URLs for Dataset

     Revoke previously generated URLs associated with a specific dataset kind subtype(Eg - dataset--
    File.Generic).
    Required roles: `service.dataset.admin`.

    Args:
        kind_sub_type (str):
        data_partition_id (str):
        body (RevokeURLBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        body=body,
        kind_sub_type=kind_sub_type,
        data_partition_id=data_partition_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: RevokeURLBody,
    kind_sub_type: str,
    data_partition_id: str,
) -> Response[Any]:
    """Revoke previously generated URLs for Dataset

     Revoke previously generated URLs associated with a specific dataset kind subtype(Eg - dataset--
    File.Generic).
    Required roles: `service.dataset.admin`.

    Args:
        kind_sub_type (str):
        data_partition_id (str):
        body (RevokeURLBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        body=body,
        kind_sub_type=kind_sub_type,
        data_partition_id=data_partition_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
