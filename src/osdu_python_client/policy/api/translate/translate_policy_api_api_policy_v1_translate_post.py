from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.detail import Detail
from ...models.translate_item import TranslateItem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: TranslateItem,
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

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/policy/v1/translate",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

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

    if response.status_code == 404:
        response_404 = Detail.from_dict(response.json())

        return response_404

    if response.status_code == 406:
        response_406 = Detail.from_dict(response.json())

        return response_406

    if response.status_code == 422:
        response_422 = Detail.from_dict(response.json())

        return response_422

    if response.status_code == 500:
        response_500 = Detail.from_dict(response.json())

        return response_500

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
    *,
    client: AuthenticatedClient,
    body: TranslateItem,
    correlation_id: str | Unset = UNSET,
    user_agent: str | Unset = UNSET,
    data_partition_id: str | Unset = UNSET,
    x_user_id: str | Unset = UNSET,
) -> Response[Any | Detail]:
    r"""Translate Policy Api

     ## Translate policy
    Given an OPA query that should be partially evaluated, return an ElasticSearch request body

    In the body of the request the JSON schema should match \"TranslateItem\".
    Please note: xuserid, token and datapartitionid are now actively inserted into input request

    ### Permission required to use this API:

    `policy.service.user` or `policy.service.admin`

    Args:
        correlation_id (str | Unset):
        user_agent (str | Unset):
        data_partition_id (str | Unset): identifier of the data partition to query
        x_user_id (str | Unset): identifier the user in the query
        body (TranslateItem):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Detail]
    """

    kwargs = _get_kwargs(
        body=body,
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
    body: TranslateItem,
    correlation_id: str | Unset = UNSET,
    user_agent: str | Unset = UNSET,
    data_partition_id: str | Unset = UNSET,
    x_user_id: str | Unset = UNSET,
) -> Any | Detail | None:
    r"""Translate Policy Api

     ## Translate policy
    Given an OPA query that should be partially evaluated, return an ElasticSearch request body

    In the body of the request the JSON schema should match \"TranslateItem\".
    Please note: xuserid, token and datapartitionid are now actively inserted into input request

    ### Permission required to use this API:

    `policy.service.user` or `policy.service.admin`

    Args:
        correlation_id (str | Unset):
        user_agent (str | Unset):
        data_partition_id (str | Unset): identifier of the data partition to query
        x_user_id (str | Unset): identifier the user in the query
        body (TranslateItem):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Detail
    """

    return sync_detailed(
        client=client,
        body=body,
        correlation_id=correlation_id,
        user_agent=user_agent,
        data_partition_id=data_partition_id,
        x_user_id=x_user_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: TranslateItem,
    correlation_id: str | Unset = UNSET,
    user_agent: str | Unset = UNSET,
    data_partition_id: str | Unset = UNSET,
    x_user_id: str | Unset = UNSET,
) -> Response[Any | Detail]:
    r"""Translate Policy Api

     ## Translate policy
    Given an OPA query that should be partially evaluated, return an ElasticSearch request body

    In the body of the request the JSON schema should match \"TranslateItem\".
    Please note: xuserid, token and datapartitionid are now actively inserted into input request

    ### Permission required to use this API:

    `policy.service.user` or `policy.service.admin`

    Args:
        correlation_id (str | Unset):
        user_agent (str | Unset):
        data_partition_id (str | Unset): identifier of the data partition to query
        x_user_id (str | Unset): identifier the user in the query
        body (TranslateItem):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Detail]
    """

    kwargs = _get_kwargs(
        body=body,
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
    body: TranslateItem,
    correlation_id: str | Unset = UNSET,
    user_agent: str | Unset = UNSET,
    data_partition_id: str | Unset = UNSET,
    x_user_id: str | Unset = UNSET,
) -> Any | Detail | None:
    r"""Translate Policy Api

     ## Translate policy
    Given an OPA query that should be partially evaluated, return an ElasticSearch request body

    In the body of the request the JSON schema should match \"TranslateItem\".
    Please note: xuserid, token and datapartitionid are now actively inserted into input request

    ### Permission required to use this API:

    `policy.service.user` or `policy.service.admin`

    Args:
        correlation_id (str | Unset):
        user_agent (str | Unset):
        data_partition_id (str | Unset): identifier of the data partition to query
        x_user_id (str | Unset): identifier the user in the query
        body (TranslateItem):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Detail
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            correlation_id=correlation_id,
            user_agent=user_agent,
            data_partition_id=data_partition_id,
            x_user_id=x_user_id,
        )
    ).parsed
