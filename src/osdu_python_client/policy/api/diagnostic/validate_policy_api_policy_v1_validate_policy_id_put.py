from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.body_validate_policy_api_policy_v1_validate_policy_id_put import (
    BodyValidatePolicyApiPolicyV1ValidatePolicyIdPut,
)
from ...models.detail import Detail
from ...types import UNSET, Response, Unset


def _get_kwargs(
    policy_id: str,
    *,
    body: BodyValidatePolicyApiPolicyV1ValidatePolicyIdPut,
    template: bool | Unset = False,
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

    params["template"] = template

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/policy/v1/validate/{policy_id}".format(
            policy_id=quote(str(policy_id), safe=""),
        ),
        "params": params,
    }

    _kwargs["files"] = body.to_multipart()

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | Detail | None:
    if response.status_code == 200:
        response_200 = response.json()
        return response_200

    if response.status_code == 400:
        response_400 = Detail.from_dict(response.json())

        return response_400

    if response.status_code == 422:
        response_422 = Detail.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | Detail]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    policy_id: str,
    *,
    client: AuthenticatedClient,
    body: BodyValidatePolicyApiPolicyV1ValidatePolicyIdPut,
    template: bool | Unset = False,
    correlation_id: str | Unset = UNSET,
    user_agent: str | Unset = UNSET,
    data_partition_id: str | Unset = UNSET,
    x_user_id: str | Unset = UNSET,
) -> Response[Any | Detail]:
    r"""Validate Policy

     # Validate Policy
    This API checks to make sure the rego is valid and the naming of the policy package is acceptable.

    If template parameter is True, then the incoming file will automatically replace the following
    during validation:
    - data_partition
    - DATA_PARTITION
    - name with policy_id without \".rego\" suffix

    Args:
        policy_id (str):
        template (bool | Unset):  Default: False.
        correlation_id (str | Unset):
        user_agent (str | Unset):
        data_partition_id (str | Unset): identifier of the data partition to query
        x_user_id (str | Unset): identifier the user in the query
        body (BodyValidatePolicyApiPolicyV1ValidatePolicyIdPut):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Detail]
    """

    kwargs = _get_kwargs(
        policy_id=policy_id,
        body=body,
        template=template,
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
    policy_id: str,
    *,
    client: AuthenticatedClient,
    body: BodyValidatePolicyApiPolicyV1ValidatePolicyIdPut,
    template: bool | Unset = False,
    correlation_id: str | Unset = UNSET,
    user_agent: str | Unset = UNSET,
    data_partition_id: str | Unset = UNSET,
    x_user_id: str | Unset = UNSET,
) -> Any | Detail | None:
    r"""Validate Policy

     # Validate Policy
    This API checks to make sure the rego is valid and the naming of the policy package is acceptable.

    If template parameter is True, then the incoming file will automatically replace the following
    during validation:
    - data_partition
    - DATA_PARTITION
    - name with policy_id without \".rego\" suffix

    Args:
        policy_id (str):
        template (bool | Unset):  Default: False.
        correlation_id (str | Unset):
        user_agent (str | Unset):
        data_partition_id (str | Unset): identifier of the data partition to query
        x_user_id (str | Unset): identifier the user in the query
        body (BodyValidatePolicyApiPolicyV1ValidatePolicyIdPut):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Detail
    """

    return sync_detailed(
        policy_id=policy_id,
        client=client,
        body=body,
        template=template,
        correlation_id=correlation_id,
        user_agent=user_agent,
        data_partition_id=data_partition_id,
        x_user_id=x_user_id,
    ).parsed


async def asyncio_detailed(
    policy_id: str,
    *,
    client: AuthenticatedClient,
    body: BodyValidatePolicyApiPolicyV1ValidatePolicyIdPut,
    template: bool | Unset = False,
    correlation_id: str | Unset = UNSET,
    user_agent: str | Unset = UNSET,
    data_partition_id: str | Unset = UNSET,
    x_user_id: str | Unset = UNSET,
) -> Response[Any | Detail]:
    r"""Validate Policy

     # Validate Policy
    This API checks to make sure the rego is valid and the naming of the policy package is acceptable.

    If template parameter is True, then the incoming file will automatically replace the following
    during validation:
    - data_partition
    - DATA_PARTITION
    - name with policy_id without \".rego\" suffix

    Args:
        policy_id (str):
        template (bool | Unset):  Default: False.
        correlation_id (str | Unset):
        user_agent (str | Unset):
        data_partition_id (str | Unset): identifier of the data partition to query
        x_user_id (str | Unset): identifier the user in the query
        body (BodyValidatePolicyApiPolicyV1ValidatePolicyIdPut):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Detail]
    """

    kwargs = _get_kwargs(
        policy_id=policy_id,
        body=body,
        template=template,
        correlation_id=correlation_id,
        user_agent=user_agent,
        data_partition_id=data_partition_id,
        x_user_id=x_user_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    policy_id: str,
    *,
    client: AuthenticatedClient,
    body: BodyValidatePolicyApiPolicyV1ValidatePolicyIdPut,
    template: bool | Unset = False,
    correlation_id: str | Unset = UNSET,
    user_agent: str | Unset = UNSET,
    data_partition_id: str | Unset = UNSET,
    x_user_id: str | Unset = UNSET,
) -> Any | Detail | None:
    r"""Validate Policy

     # Validate Policy
    This API checks to make sure the rego is valid and the naming of the policy package is acceptable.

    If template parameter is True, then the incoming file will automatically replace the following
    during validation:
    - data_partition
    - DATA_PARTITION
    - name with policy_id without \".rego\" suffix

    Args:
        policy_id (str):
        template (bool | Unset):  Default: False.
        correlation_id (str | Unset):
        user_agent (str | Unset):
        data_partition_id (str | Unset): identifier of the data partition to query
        x_user_id (str | Unset): identifier the user in the query
        body (BodyValidatePolicyApiPolicyV1ValidatePolicyIdPut):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Detail
    """

    return (
        await asyncio_detailed(
            policy_id=policy_id,
            client=client,
            body=body,
            template=template,
            correlation_id=correlation_id,
            user_agent=user_agent,
            data_partition_id=data_partition_id,
            x_user_id=x_user_id,
        )
    ).parsed
