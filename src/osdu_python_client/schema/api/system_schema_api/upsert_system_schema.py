from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.app_error import AppError
from ...models.schema_request import SchemaRequest
from ...types import Response


def _get_kwargs(
    *,
    body: SchemaRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/schemas/system",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AppError | None:
    if response.status_code == 400:
        response_400 = AppError.from_dict(response.json())

        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AppError]:
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
) -> Response[AppError]:
    """Creates/Updates a schema in development status

     Creates a new schema or updates an already existing schema with status `DEVELOPMENT` in the schema
    repository. If a user tries to create a schema with status other than `DEVELOPMENT`, API will not
    throw an exception. <p>The update of schema without `DEVELOPMENT` status would cause error. Any
    schema instance with the same schemaIdentity is replaced. A schema state can also be changed from
    `DEVELOPMENT` to `PUBLISHED` or `OBSOLETE` while updating schema content or by providing the same
    schema content.</p> <p>**Note:** The schema may refer to other schema definitions in `DEVELOPMENT`
    state. If those schemas are updated themselves, it is the developer's responsibility to PUT the
    dependent schemas again to update the schema. Scope for a schema will be SHARED for all the schemas
    created using this API.</p><p>Service principal authorization is required to call thi API.</p>

    Args:
        body (SchemaRequest): Represents a model to Schema Request

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppError]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: SchemaRequest,
) -> AppError | None:
    """Creates/Updates a schema in development status

     Creates a new schema or updates an already existing schema with status `DEVELOPMENT` in the schema
    repository. If a user tries to create a schema with status other than `DEVELOPMENT`, API will not
    throw an exception. <p>The update of schema without `DEVELOPMENT` status would cause error. Any
    schema instance with the same schemaIdentity is replaced. A schema state can also be changed from
    `DEVELOPMENT` to `PUBLISHED` or `OBSOLETE` while updating schema content or by providing the same
    schema content.</p> <p>**Note:** The schema may refer to other schema definitions in `DEVELOPMENT`
    state. If those schemas are updated themselves, it is the developer's responsibility to PUT the
    dependent schemas again to update the schema. Scope for a schema will be SHARED for all the schemas
    created using this API.</p><p>Service principal authorization is required to call thi API.</p>

    Args:
        body (SchemaRequest): Represents a model to Schema Request

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppError
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: SchemaRequest,
) -> Response[AppError]:
    """Creates/Updates a schema in development status

     Creates a new schema or updates an already existing schema with status `DEVELOPMENT` in the schema
    repository. If a user tries to create a schema with status other than `DEVELOPMENT`, API will not
    throw an exception. <p>The update of schema without `DEVELOPMENT` status would cause error. Any
    schema instance with the same schemaIdentity is replaced. A schema state can also be changed from
    `DEVELOPMENT` to `PUBLISHED` or `OBSOLETE` while updating schema content or by providing the same
    schema content.</p> <p>**Note:** The schema may refer to other schema definitions in `DEVELOPMENT`
    state. If those schemas are updated themselves, it is the developer's responsibility to PUT the
    dependent schemas again to update the schema. Scope for a schema will be SHARED for all the schemas
    created using this API.</p><p>Service principal authorization is required to call thi API.</p>

    Args:
        body (SchemaRequest): Represents a model to Schema Request

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppError]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: SchemaRequest,
) -> AppError | None:
    """Creates/Updates a schema in development status

     Creates a new schema or updates an already existing schema with status `DEVELOPMENT` in the schema
    repository. If a user tries to create a schema with status other than `DEVELOPMENT`, API will not
    throw an exception. <p>The update of schema without `DEVELOPMENT` status would cause error. Any
    schema instance with the same schemaIdentity is replaced. A schema state can also be changed from
    `DEVELOPMENT` to `PUBLISHED` or `OBSOLETE` while updating schema content or by providing the same
    schema content.</p> <p>**Note:** The schema may refer to other schema definitions in `DEVELOPMENT`
    state. If those schemas are updated themselves, it is the developer's responsibility to PUT the
    dependent schemas again to update the schema. Scope for a schema will be SHARED for all the schemas
    created using this API.</p><p>Service principal authorization is required to call thi API.</p>

    Args:
        body (SchemaRequest): Represents a model to Schema Request

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppError
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
