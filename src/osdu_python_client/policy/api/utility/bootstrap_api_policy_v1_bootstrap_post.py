from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.detail import Detail
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    force: bool | Unset = False,
    correlation_id: str | Unset = UNSET,
    user_agent: str | Unset = UNSET,
    data_partition_id: str | Unset = UNSET,
    x_user_id: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(correlation_id, Unset):
        headers["correlation-id"] = correlation_id

    if not isinstance(user_agent, Unset):
        headers["user-agent"] = user_agent

    if not isinstance(data_partition_id, Unset):
        headers["data-partition-id"] = data_partition_id

    if not isinstance(x_user_id, Unset):
        headers["x-user-id"] = x_user_id

    params: dict[str, Any] = {}

    params["force"] = force

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/policy/v1/bootstrap",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | Detail | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = response.json()
        return response_200

    if response.status_code == 201:
        response_201 = Detail.from_dict(response.json())

        return response_201

    if response.status_code == 202:
        response_202 = Detail.from_dict(response.json())

        return response_202

    if response.status_code == 400:
        response_400 = Detail.from_dict(response.json())

        return response_400

    if response.status_code == 405:
        response_405 = Detail.from_dict(response.json())

        return response_405

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | Detail | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    force: bool | Unset = False,
    correlation_id: str | Unset = UNSET,
    user_agent: str | Unset = UNSET,
    data_partition_id: str | Unset = UNSET,
    x_user_id: str | Unset = UNSET,
) -> Response[Any | Detail | HTTPValidationError]:
    """Bootstrap

     ## Experimental bootstrap API for creating and updating bundle to default.

    This should be used when adding a partition to OSDU or when wanting to reset to a known good state.

    ### Without force:

    - This method is only allowed if the partition doesn't already have a bundle.
    - If the bundle already exists it will return 405 METHOD_NOT_ALLOWED.
    - Policy Service can be configured to ignore force.

    ### May return:

    - `HTTP_202_ACCEPTED` - updated
    - `HTTP_201_CREATED` - created
    - `HTTP_405_METHOD_NOT_ALLOWED` - not allowed
    - `HTTP_424_FAILED_DEPENDENCY` - bundle server caused failure

    ### Permission required to use this API on this system (configurable):

        service.policy.admin

    Args:
        force (bool | Unset):  Default: False.
        correlation_id (str | Unset):
        user_agent (str | Unset):
        data_partition_id (str | Unset): identifier of the data partition to query
        x_user_id (str | Unset): identifier the user in the query

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Detail | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        force=force,
        correlation_id=correlation_id,
        user_agent=user_agent,
        data_partition_id=data_partition_id,
        x_user_id=x_user_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    force: bool | Unset = False,
    correlation_id: str | Unset = UNSET,
    user_agent: str | Unset = UNSET,
    data_partition_id: str | Unset = UNSET,
    x_user_id: str | Unset = UNSET,
) -> Any | Detail | HTTPValidationError | None:
    """Bootstrap

     ## Experimental bootstrap API for creating and updating bundle to default.

    This should be used when adding a partition to OSDU or when wanting to reset to a known good state.

    ### Without force:

    - This method is only allowed if the partition doesn't already have a bundle.
    - If the bundle already exists it will return 405 METHOD_NOT_ALLOWED.
    - Policy Service can be configured to ignore force.

    ### May return:

    - `HTTP_202_ACCEPTED` - updated
    - `HTTP_201_CREATED` - created
    - `HTTP_405_METHOD_NOT_ALLOWED` - not allowed
    - `HTTP_424_FAILED_DEPENDENCY` - bundle server caused failure

    ### Permission required to use this API on this system (configurable):

        service.policy.admin

    Args:
        force (bool | Unset):  Default: False.
        correlation_id (str | Unset):
        user_agent (str | Unset):
        data_partition_id (str | Unset): identifier of the data partition to query
        x_user_id (str | Unset): identifier the user in the query

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Detail | HTTPValidationError
    """

    return sync_detailed(
        client=client,
        force=force,
        correlation_id=correlation_id,
        user_agent=user_agent,
        data_partition_id=data_partition_id,
        x_user_id=x_user_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    force: bool | Unset = False,
    correlation_id: str | Unset = UNSET,
    user_agent: str | Unset = UNSET,
    data_partition_id: str | Unset = UNSET,
    x_user_id: str | Unset = UNSET,
) -> Response[Any | Detail | HTTPValidationError]:
    """Bootstrap

     ## Experimental bootstrap API for creating and updating bundle to default.

    This should be used when adding a partition to OSDU or when wanting to reset to a known good state.

    ### Without force:

    - This method is only allowed if the partition doesn't already have a bundle.
    - If the bundle already exists it will return 405 METHOD_NOT_ALLOWED.
    - Policy Service can be configured to ignore force.

    ### May return:

    - `HTTP_202_ACCEPTED` - updated
    - `HTTP_201_CREATED` - created
    - `HTTP_405_METHOD_NOT_ALLOWED` - not allowed
    - `HTTP_424_FAILED_DEPENDENCY` - bundle server caused failure

    ### Permission required to use this API on this system (configurable):

        service.policy.admin

    Args:
        force (bool | Unset):  Default: False.
        correlation_id (str | Unset):
        user_agent (str | Unset):
        data_partition_id (str | Unset): identifier of the data partition to query
        x_user_id (str | Unset): identifier the user in the query

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Detail | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        force=force,
        correlation_id=correlation_id,
        user_agent=user_agent,
        data_partition_id=data_partition_id,
        x_user_id=x_user_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    force: bool | Unset = False,
    correlation_id: str | Unset = UNSET,
    user_agent: str | Unset = UNSET,
    data_partition_id: str | Unset = UNSET,
    x_user_id: str | Unset = UNSET,
) -> Any | Detail | HTTPValidationError | None:
    """Bootstrap

     ## Experimental bootstrap API for creating and updating bundle to default.

    This should be used when adding a partition to OSDU or when wanting to reset to a known good state.

    ### Without force:

    - This method is only allowed if the partition doesn't already have a bundle.
    - If the bundle already exists it will return 405 METHOD_NOT_ALLOWED.
    - Policy Service can be configured to ignore force.

    ### May return:

    - `HTTP_202_ACCEPTED` - updated
    - `HTTP_201_CREATED` - created
    - `HTTP_405_METHOD_NOT_ALLOWED` - not allowed
    - `HTTP_424_FAILED_DEPENDENCY` - bundle server caused failure

    ### Permission required to use this API on this system (configurable):

        service.policy.admin

    Args:
        force (bool | Unset):  Default: False.
        correlation_id (str | Unset):
        user_agent (str | Unset):
        data_partition_id (str | Unset): identifier of the data partition to query
        x_user_id (str | Unset): identifier the user in the query

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Detail | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            client=client,
            force=force,
            correlation_id=correlation_id,
            user_agent=user_agent,
            data_partition_id=data_partition_id,
            x_user_id=x_user_id,
        )
    ).parsed
