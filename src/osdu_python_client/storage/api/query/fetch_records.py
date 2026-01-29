from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.app_error import AppError
from ...models.multi_record_request import MultiRecordRequest
from ...models.multi_record_response import MultiRecordResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: MultiRecordRequest,
    x_collaboration: str | Unset = UNSET,
    data_partition_id: str,
    frame_of_reference: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_collaboration, Unset):
        headers["x-collaboration"] = x_collaboration

    headers["data-partition-id"] = data_partition_id

    headers["frame-of-reference"] = frame_of_reference

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/query/records:batch",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AppError | MultiRecordResponse | None:
    if response.status_code == 200:
        response_200 = MultiRecordResponse.from_dict(response.json())

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
) -> Response[AppError | MultiRecordResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: MultiRecordRequest,
    x_collaboration: str | Unset = UNSET,
    data_partition_id: str,
    frame_of_reference: str,
) -> Response[AppError | MultiRecordResponse]:
    """Fetch multiple records

     The API fetches multiple records at once in the specific {data-partition-id}.The value of {frame-of-
    reference} indicates whether normalization is applied.
    Required roles: `users.datalake.viewers` or `users.datalake.editors` or `users.datalake.admins`.

    Args:
        x_collaboration (str | Unset):
        data_partition_id (str):
        frame_of_reference (str):
        body (MultiRecordRequest): Record ids

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppError | MultiRecordResponse]
    """

    kwargs = _get_kwargs(
        body=body,
        x_collaboration=x_collaboration,
        data_partition_id=data_partition_id,
        frame_of_reference=frame_of_reference,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: MultiRecordRequest,
    x_collaboration: str | Unset = UNSET,
    data_partition_id: str,
    frame_of_reference: str,
) -> AppError | MultiRecordResponse | None:
    """Fetch multiple records

     The API fetches multiple records at once in the specific {data-partition-id}.The value of {frame-of-
    reference} indicates whether normalization is applied.
    Required roles: `users.datalake.viewers` or `users.datalake.editors` or `users.datalake.admins`.

    Args:
        x_collaboration (str | Unset):
        data_partition_id (str):
        frame_of_reference (str):
        body (MultiRecordRequest): Record ids

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppError | MultiRecordResponse
    """

    return sync_detailed(
        client=client,
        body=body,
        x_collaboration=x_collaboration,
        data_partition_id=data_partition_id,
        frame_of_reference=frame_of_reference,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: MultiRecordRequest,
    x_collaboration: str | Unset = UNSET,
    data_partition_id: str,
    frame_of_reference: str,
) -> Response[AppError | MultiRecordResponse]:
    """Fetch multiple records

     The API fetches multiple records at once in the specific {data-partition-id}.The value of {frame-of-
    reference} indicates whether normalization is applied.
    Required roles: `users.datalake.viewers` or `users.datalake.editors` or `users.datalake.admins`.

    Args:
        x_collaboration (str | Unset):
        data_partition_id (str):
        frame_of_reference (str):
        body (MultiRecordRequest): Record ids

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppError | MultiRecordResponse]
    """

    kwargs = _get_kwargs(
        body=body,
        x_collaboration=x_collaboration,
        data_partition_id=data_partition_id,
        frame_of_reference=frame_of_reference,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: MultiRecordRequest,
    x_collaboration: str | Unset = UNSET,
    data_partition_id: str,
    frame_of_reference: str,
) -> AppError | MultiRecordResponse | None:
    """Fetch multiple records

     The API fetches multiple records at once in the specific {data-partition-id}.The value of {frame-of-
    reference} indicates whether normalization is applied.
    Required roles: `users.datalake.viewers` or `users.datalake.editors` or `users.datalake.admins`.

    Args:
        x_collaboration (str | Unset):
        data_partition_id (str):
        frame_of_reference (str):
        body (MultiRecordRequest): Record ids

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppError | MultiRecordResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            x_collaboration=x_collaboration,
            data_partition_id=data_partition_id,
            frame_of_reference=frame_of_reference,
        )
    ).parsed
