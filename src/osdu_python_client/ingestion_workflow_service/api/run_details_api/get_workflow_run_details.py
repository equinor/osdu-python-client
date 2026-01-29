from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.app_error import AppError
from ...models.get_workflow_run_details_response_200 import (
    GetWorkflowRunDetailsResponse200,
)
from ...types import Response


def _get_kwargs(
    workflow_name: str,
    run_id: str,
    *,
    data_partition_id: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["data-partition-id"] = data_partition_id

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/workflow/{workflow_name}/workflowRun/{run_id}/latestInfo".format(
            workflow_name=quote(str(workflow_name), safe=""),
            run_id=quote(str(run_id), safe=""),
        ),
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AppError | GetWorkflowRunDetailsResponse200 | None:
    if response.status_code == 200:
        response_200 = GetWorkflowRunDetailsResponse200.from_dict(response.json())

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
) -> Response[AppError | GetWorkflowRunDetailsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    workflow_name: str,
    run_id: str,
    *,
    client: AuthenticatedClient,
    data_partition_id: str,
) -> Response[AppError | GetWorkflowRunDetailsResponse200]:
    """Get execution details for the latest workflow task.

     Get execution details for the latest workflow task. **Required roles** - 'service.workflow.viewer'
    and ownership of requested workflow run.

    Args:
        workflow_name (str):
        run_id (str):
        data_partition_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppError | GetWorkflowRunDetailsResponse200]
    """

    kwargs = _get_kwargs(
        workflow_name=workflow_name,
        run_id=run_id,
        data_partition_id=data_partition_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    workflow_name: str,
    run_id: str,
    *,
    client: AuthenticatedClient,
    data_partition_id: str,
) -> AppError | GetWorkflowRunDetailsResponse200 | None:
    """Get execution details for the latest workflow task.

     Get execution details for the latest workflow task. **Required roles** - 'service.workflow.viewer'
    and ownership of requested workflow run.

    Args:
        workflow_name (str):
        run_id (str):
        data_partition_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppError | GetWorkflowRunDetailsResponse200
    """

    return sync_detailed(
        workflow_name=workflow_name,
        run_id=run_id,
        client=client,
        data_partition_id=data_partition_id,
    ).parsed


async def asyncio_detailed(
    workflow_name: str,
    run_id: str,
    *,
    client: AuthenticatedClient,
    data_partition_id: str,
) -> Response[AppError | GetWorkflowRunDetailsResponse200]:
    """Get execution details for the latest workflow task.

     Get execution details for the latest workflow task. **Required roles** - 'service.workflow.viewer'
    and ownership of requested workflow run.

    Args:
        workflow_name (str):
        run_id (str):
        data_partition_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppError | GetWorkflowRunDetailsResponse200]
    """

    kwargs = _get_kwargs(
        workflow_name=workflow_name,
        run_id=run_id,
        data_partition_id=data_partition_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workflow_name: str,
    run_id: str,
    *,
    client: AuthenticatedClient,
    data_partition_id: str,
) -> AppError | GetWorkflowRunDetailsResponse200 | None:
    """Get execution details for the latest workflow task.

     Get execution details for the latest workflow task. **Required roles** - 'service.workflow.viewer'
    and ownership of requested workflow run.

    Args:
        workflow_name (str):
        run_id (str):
        data_partition_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppError | GetWorkflowRunDetailsResponse200
    """

    return (
        await asyncio_detailed(
            workflow_name=workflow_name,
            run_id=run_id,
            client=client,
            data_partition_id=data_partition_id,
        )
    ).parsed
