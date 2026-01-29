from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.app_error import AppError
from ...models.schema_info_response import SchemaInfoResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    authority: str | Unset = UNSET,
    source: str | Unset = UNSET,
    entity_type: str | Unset = UNSET,
    schema_version_major: str | Unset = UNSET,
    schema_version_minor: str | Unset = UNSET,
    schema_version_patch: str | Unset = UNSET,
    status: str | Unset = UNSET,
    scope: str | Unset = UNSET,
    latest_version: str | Unset = UNSET,
    limit: str | Unset = UNSET,
    offset: str | Unset = UNSET,
    data_partition_id: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["data-partition-id"] = data_partition_id

    params: dict[str, Any] = {}

    params["authority"] = authority

    params["source"] = source

    params["entityType"] = entity_type

    params["schemaVersionMajor"] = schema_version_major

    params["schemaVersionMinor"] = schema_version_minor

    params["schemaVersionPatch"] = schema_version_patch

    params["status"] = status

    params["scope"] = scope

    params["latestVersion"] = latest_version

    params["limit"] = limit

    params["offset"] = offset

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/schema",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AppError | SchemaInfoResponse | None:
    if response.status_code == 200:
        response_200 = SchemaInfoResponse.from_dict(response.json())

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
) -> Response[AppError | SchemaInfoResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    authority: str | Unset = UNSET,
    source: str | Unset = UNSET,
    entity_type: str | Unset = UNSET,
    schema_version_major: str | Unset = UNSET,
    schema_version_minor: str | Unset = UNSET,
    schema_version_patch: str | Unset = UNSET,
    status: str | Unset = UNSET,
    scope: str | Unset = UNSET,
    latest_version: str | Unset = UNSET,
    limit: str | Unset = UNSET,
    offset: str | Unset = UNSET,
    data_partition_id: str,
) -> Response[AppError | SchemaInfoResponse]:
    """Searches SchemaInfo repository

     Searches for information of available schema (SchemaInfo) in schema repository. Support options to
    filter out the search contents. <p>Required roles:  `service.schema-service.viewers` groups to get
    the schema.</p>

    Args:
        authority (str | Unset):
        source (str | Unset):
        entity_type (str | Unset):
        schema_version_major (str | Unset):
        schema_version_minor (str | Unset):
        schema_version_patch (str | Unset):
        status (str | Unset):
        scope (str | Unset):
        latest_version (str | Unset):
        limit (str | Unset):
        offset (str | Unset):
        data_partition_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppError | SchemaInfoResponse]
    """

    kwargs = _get_kwargs(
        authority=authority,
        source=source,
        entity_type=entity_type,
        schema_version_major=schema_version_major,
        schema_version_minor=schema_version_minor,
        schema_version_patch=schema_version_patch,
        status=status,
        scope=scope,
        latest_version=latest_version,
        limit=limit,
        offset=offset,
        data_partition_id=data_partition_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    authority: str | Unset = UNSET,
    source: str | Unset = UNSET,
    entity_type: str | Unset = UNSET,
    schema_version_major: str | Unset = UNSET,
    schema_version_minor: str | Unset = UNSET,
    schema_version_patch: str | Unset = UNSET,
    status: str | Unset = UNSET,
    scope: str | Unset = UNSET,
    latest_version: str | Unset = UNSET,
    limit: str | Unset = UNSET,
    offset: str | Unset = UNSET,
    data_partition_id: str,
) -> AppError | SchemaInfoResponse | None:
    """Searches SchemaInfo repository

     Searches for information of available schema (SchemaInfo) in schema repository. Support options to
    filter out the search contents. <p>Required roles:  `service.schema-service.viewers` groups to get
    the schema.</p>

    Args:
        authority (str | Unset):
        source (str | Unset):
        entity_type (str | Unset):
        schema_version_major (str | Unset):
        schema_version_minor (str | Unset):
        schema_version_patch (str | Unset):
        status (str | Unset):
        scope (str | Unset):
        latest_version (str | Unset):
        limit (str | Unset):
        offset (str | Unset):
        data_partition_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppError | SchemaInfoResponse
    """

    return sync_detailed(
        client=client,
        authority=authority,
        source=source,
        entity_type=entity_type,
        schema_version_major=schema_version_major,
        schema_version_minor=schema_version_minor,
        schema_version_patch=schema_version_patch,
        status=status,
        scope=scope,
        latest_version=latest_version,
        limit=limit,
        offset=offset,
        data_partition_id=data_partition_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    authority: str | Unset = UNSET,
    source: str | Unset = UNSET,
    entity_type: str | Unset = UNSET,
    schema_version_major: str | Unset = UNSET,
    schema_version_minor: str | Unset = UNSET,
    schema_version_patch: str | Unset = UNSET,
    status: str | Unset = UNSET,
    scope: str | Unset = UNSET,
    latest_version: str | Unset = UNSET,
    limit: str | Unset = UNSET,
    offset: str | Unset = UNSET,
    data_partition_id: str,
) -> Response[AppError | SchemaInfoResponse]:
    """Searches SchemaInfo repository

     Searches for information of available schema (SchemaInfo) in schema repository. Support options to
    filter out the search contents. <p>Required roles:  `service.schema-service.viewers` groups to get
    the schema.</p>

    Args:
        authority (str | Unset):
        source (str | Unset):
        entity_type (str | Unset):
        schema_version_major (str | Unset):
        schema_version_minor (str | Unset):
        schema_version_patch (str | Unset):
        status (str | Unset):
        scope (str | Unset):
        latest_version (str | Unset):
        limit (str | Unset):
        offset (str | Unset):
        data_partition_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppError | SchemaInfoResponse]
    """

    kwargs = _get_kwargs(
        authority=authority,
        source=source,
        entity_type=entity_type,
        schema_version_major=schema_version_major,
        schema_version_minor=schema_version_minor,
        schema_version_patch=schema_version_patch,
        status=status,
        scope=scope,
        latest_version=latest_version,
        limit=limit,
        offset=offset,
        data_partition_id=data_partition_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    authority: str | Unset = UNSET,
    source: str | Unset = UNSET,
    entity_type: str | Unset = UNSET,
    schema_version_major: str | Unset = UNSET,
    schema_version_minor: str | Unset = UNSET,
    schema_version_patch: str | Unset = UNSET,
    status: str | Unset = UNSET,
    scope: str | Unset = UNSET,
    latest_version: str | Unset = UNSET,
    limit: str | Unset = UNSET,
    offset: str | Unset = UNSET,
    data_partition_id: str,
) -> AppError | SchemaInfoResponse | None:
    """Searches SchemaInfo repository

     Searches for information of available schema (SchemaInfo) in schema repository. Support options to
    filter out the search contents. <p>Required roles:  `service.schema-service.viewers` groups to get
    the schema.</p>

    Args:
        authority (str | Unset):
        source (str | Unset):
        entity_type (str | Unset):
        schema_version_major (str | Unset):
        schema_version_minor (str | Unset):
        schema_version_patch (str | Unset):
        status (str | Unset):
        scope (str | Unset):
        latest_version (str | Unset):
        limit (str | Unset):
        offset (str | Unset):
        data_partition_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppError | SchemaInfoResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            authority=authority,
            source=source,
            entity_type=entity_type,
            schema_version_major=schema_version_major,
            schema_version_minor=schema_version_minor,
            schema_version_patch=schema_version_patch,
            status=status,
            scope=scope,
            latest_version=latest_version,
            limit=limit,
            offset=offset,
            data_partition_id=data_partition_id,
        )
    ).parsed
