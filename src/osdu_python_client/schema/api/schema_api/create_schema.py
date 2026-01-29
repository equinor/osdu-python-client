from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.app_error import AppError
from ...models.schema_info import SchemaInfo
from ...models.schema_request import SchemaRequest
from ...types import Response


def _get_kwargs(
    *,
    body: SchemaRequest,
    data_partition_id: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["data-partition-id"] = data_partition_id

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/schema",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AppError | SchemaInfo | None:
    if response.status_code == 201:
        response_201 = SchemaInfo.from_dict(response.json())

        return response_201

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
) -> Response[AppError | SchemaInfo]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: SchemaRequest,
    data_partition_id: str,
) -> Response[AppError | SchemaInfo]:
    """Adds a schema to the schema repository.

     Adds a schema to the schema repository. The schemaIdentity must be unique. The `authority`, `source`
    and `entityType` will be registered if not present. <p>If lower minor versions are registered the
    service validates the new schema against breaking changes; if breaking changes are discovered the
    request fails.</p> <p>**Note:** The schema must not reference other schemas with status
    `DEVELOPMENT`. Scope to a schema will be set by system based on partition id (`SHARED` for common
    tenant and `INTERNAL` for private tenant). </p><p>Required roles : `service.schema-service.editors`
    groups to create schema.</p>

    Args:
        data_partition_id (str):
        body (SchemaRequest): Represents a model to Schema Request

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppError | SchemaInfo]
    """

    kwargs = _get_kwargs(
        body=body,
        data_partition_id=data_partition_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: SchemaRequest,
    data_partition_id: str,
) -> AppError | SchemaInfo | None:
    """Adds a schema to the schema repository.

     Adds a schema to the schema repository. The schemaIdentity must be unique. The `authority`, `source`
    and `entityType` will be registered if not present. <p>If lower minor versions are registered the
    service validates the new schema against breaking changes; if breaking changes are discovered the
    request fails.</p> <p>**Note:** The schema must not reference other schemas with status
    `DEVELOPMENT`. Scope to a schema will be set by system based on partition id (`SHARED` for common
    tenant and `INTERNAL` for private tenant). </p><p>Required roles : `service.schema-service.editors`
    groups to create schema.</p>

    Args:
        data_partition_id (str):
        body (SchemaRequest): Represents a model to Schema Request

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppError | SchemaInfo
    """

    return sync_detailed(
        client=client,
        body=body,
        data_partition_id=data_partition_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: SchemaRequest,
    data_partition_id: str,
) -> Response[AppError | SchemaInfo]:
    """Adds a schema to the schema repository.

     Adds a schema to the schema repository. The schemaIdentity must be unique. The `authority`, `source`
    and `entityType` will be registered if not present. <p>If lower minor versions are registered the
    service validates the new schema against breaking changes; if breaking changes are discovered the
    request fails.</p> <p>**Note:** The schema must not reference other schemas with status
    `DEVELOPMENT`. Scope to a schema will be set by system based on partition id (`SHARED` for common
    tenant and `INTERNAL` for private tenant). </p><p>Required roles : `service.schema-service.editors`
    groups to create schema.</p>

    Args:
        data_partition_id (str):
        body (SchemaRequest): Represents a model to Schema Request

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppError | SchemaInfo]
    """

    kwargs = _get_kwargs(
        body=body,
        data_partition_id=data_partition_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: SchemaRequest,
    data_partition_id: str,
) -> AppError | SchemaInfo | None:
    """Adds a schema to the schema repository.

     Adds a schema to the schema repository. The schemaIdentity must be unique. The `authority`, `source`
    and `entityType` will be registered if not present. <p>If lower minor versions are registered the
    service validates the new schema against breaking changes; if breaking changes are discovered the
    request fails.</p> <p>**Note:** The schema must not reference other schemas with status
    `DEVELOPMENT`. Scope to a schema will be set by system based on partition id (`SHARED` for common
    tenant and `INTERNAL` for private tenant). </p><p>Required roles : `service.schema-service.editors`
    groups to create schema.</p>

    Args:
        data_partition_id (str):
        body (SchemaRequest): Represents a model to Schema Request

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppError | SchemaInfo
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            data_partition_id=data_partition_id,
        )
    ).parsed
