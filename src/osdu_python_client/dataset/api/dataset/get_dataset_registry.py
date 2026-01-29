from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_dataset_registry_request import GetDatasetRegistryRequest
from ...types import Response


def _get_kwargs(
    *,
    body: GetDatasetRegistryRequest,
    data_partition_id: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["data-partition-id"] = data_partition_id

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/getDatasetRegistry",
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
    body: GetDatasetRegistryRequest,
    data_partition_id: str,
) -> Response[Any]:
    """Get Dataset Registries

     Get Dataset Registries.
    **Required roles:  `service.storage.creator` or `service.storage.admin` or `service.storage.viewer`.

    Args:
        data_partition_id (str):
        body (GetDatasetRegistryRequest): Dataset registry ids

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
    body: GetDatasetRegistryRequest,
    data_partition_id: str,
) -> Response[Any]:
    """Get Dataset Registries

     Get Dataset Registries.
    **Required roles:  `service.storage.creator` or `service.storage.admin` or `service.storage.viewer`.

    Args:
        data_partition_id (str):
        body (GetDatasetRegistryRequest): Dataset registry ids

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
