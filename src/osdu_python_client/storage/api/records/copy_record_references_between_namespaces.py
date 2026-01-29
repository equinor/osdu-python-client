from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.app_error import AppError
from ...models.copy_record_references_model import CopyRecordReferencesModel
from ...types import Response


def _get_kwargs(
    *,
    body: CopyRecordReferencesModel,
    x_collaboration: str,
    data_partition_id: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["x-collaboration"] = x_collaboration

    headers["data-partition-id"] = data_partition_id

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/records/copy",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AppError | CopyRecordReferencesModel | None:
    if response.status_code == 200:
        response_200 = CopyRecordReferencesModel.from_dict(response.json())

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

    if response.status_code == 409:
        response_409 = AppError.from_dict(response.json())

        return response_409

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
) -> Response[AppError | CopyRecordReferencesModel]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: CopyRecordReferencesModel,
    x_collaboration: str,
    data_partition_id: str,
) -> Response[AppError | CopyRecordReferencesModel]:
    """Copy Record references form one namespace to another

     This API attempts to copy all the Record references it is provided from the given source namespace
    to the target namespace. All references will be copied or all will fail as a transaction. If the
    target namespace does not et exist it will be created. It requires 'services.storage.admin'
    permission to call

    Args:
        x_collaboration (str):
        data_partition_id (str):
        body (CopyRecordReferencesModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppError | CopyRecordReferencesModel]
    """

    kwargs = _get_kwargs(
        body=body,
        x_collaboration=x_collaboration,
        data_partition_id=data_partition_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: CopyRecordReferencesModel,
    x_collaboration: str,
    data_partition_id: str,
) -> AppError | CopyRecordReferencesModel | None:
    """Copy Record references form one namespace to another

     This API attempts to copy all the Record references it is provided from the given source namespace
    to the target namespace. All references will be copied or all will fail as a transaction. If the
    target namespace does not et exist it will be created. It requires 'services.storage.admin'
    permission to call

    Args:
        x_collaboration (str):
        data_partition_id (str):
        body (CopyRecordReferencesModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppError | CopyRecordReferencesModel
    """

    return sync_detailed(
        client=client,
        body=body,
        x_collaboration=x_collaboration,
        data_partition_id=data_partition_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: CopyRecordReferencesModel,
    x_collaboration: str,
    data_partition_id: str,
) -> Response[AppError | CopyRecordReferencesModel]:
    """Copy Record references form one namespace to another

     This API attempts to copy all the Record references it is provided from the given source namespace
    to the target namespace. All references will be copied or all will fail as a transaction. If the
    target namespace does not et exist it will be created. It requires 'services.storage.admin'
    permission to call

    Args:
        x_collaboration (str):
        data_partition_id (str):
        body (CopyRecordReferencesModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppError | CopyRecordReferencesModel]
    """

    kwargs = _get_kwargs(
        body=body,
        x_collaboration=x_collaboration,
        data_partition_id=data_partition_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: CopyRecordReferencesModel,
    x_collaboration: str,
    data_partition_id: str,
) -> AppError | CopyRecordReferencesModel | None:
    """Copy Record references form one namespace to another

     This API attempts to copy all the Record references it is provided from the given source namespace
    to the target namespace. All references will be copied or all will fail as a transaction. If the
    target namespace does not et exist it will be created. It requires 'services.storage.admin'
    permission to call

    Args:
        x_collaboration (str):
        data_partition_id (str):
        body (CopyRecordReferencesModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppError | CopyRecordReferencesModel
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            x_collaboration=x_collaboration,
            data_partition_id=data_partition_id,
        )
    ).parsed
