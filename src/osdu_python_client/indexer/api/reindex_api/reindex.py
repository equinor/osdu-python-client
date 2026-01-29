from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.record_reindex_request import RecordReindexRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: RecordReindexRequest,
    force_clean: bool | Unset = False,
    data_partition_id: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["data-partition-id"] = data_partition_id

    params: dict[str, Any] = {}

    params["force_clean"] = force_clean

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/reindex",
        "params": params,
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
    body: RecordReindexRequest,
    force_clean: bool | Unset = False,
    data_partition_id: str,
) -> Response[Any]:
    """Re-index given 'kind'

     This API allows users to re-index a 'kind' without re-ingesting the records via storage API.
    Required roles: `service.search.admin`

    Args:
        force_clean (bool | Unset):  Default: False.
        data_partition_id (str):
        body (RecordReindexRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        body=body,
        force_clean=force_clean,
        data_partition_id=data_partition_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: RecordReindexRequest,
    force_clean: bool | Unset = False,
    data_partition_id: str,
) -> Response[Any]:
    """Re-index given 'kind'

     This API allows users to re-index a 'kind' without re-ingesting the records via storage API.
    Required roles: `service.search.admin`

    Args:
        force_clean (bool | Unset):  Default: False.
        data_partition_id (str):
        body (RecordReindexRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        body=body,
        force_clean=force_clean,
        data_partition_id=data_partition_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
