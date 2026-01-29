from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.body_evaluate_policy_api_policy_v1_evaluations_query_post import (
    BodyEvaluatePolicyApiPolicyV1EvaluationsQueryPost,
)
from ...models.detail import Detail
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: BodyEvaluatePolicyApiPolicyV1EvaluationsQueryPost,
    policy_id: str,
    include_auth: bool | Unset = False,
    cache: bool | Unset = True,
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

    params["policy_id"] = policy_id

    params["include_auth"] = include_auth

    params["cache"] = cache

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/policy/v1/evaluations/query",
        "params": params,
    }

    _kwargs["files"] = body.to_multipart()

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | Detail | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = response.json()
        return response_200

    if response.status_code == 400:
        response_400 = Detail.from_dict(response.json())

        return response_400

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422

    if response.status_code == 500:
        response_500 = Detail.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = Detail.from_dict(response.json())

        return response_503

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
    body: BodyEvaluatePolicyApiPolicyV1EvaluationsQueryPost,
    policy_id: str,
    include_auth: bool | Unset = False,
    cache: bool | Unset = True,
    correlation_id: str | Unset = UNSET,
    user_agent: str | Unset = UNSET,
    data_partition_id: str | Unset = UNSET,
    x_user_id: str | Unset = UNSET,
) -> Response[Any | Detail | HTTPValidationError]:
    r"""Evaluate Policy

     ## Evaulate Policies
    This API is to help you evaluate policies.

    If include_auth is True, then in your file data token, xuserid and data partition id will be ignored
    in the file and information from the headers
    of the request will be used for this information.

    ### Example:
    For example file data for policy dataauthz.rego:
    Where XXXX is the data partition and YYYY is a legal tag
    ```json
    {
        \"input\": {
            \"operation\": \"update\",
            \"records\": [
                {
                    \"id\":\"XXXX:test:1.4.1654807204111\",
                    \"kind\":\"XXXX:bulkupdate:test:1.1.1654807204111\",
                    \"legal\":{
                        \"legaltags\":[
                            \"YYYY\"
                        ],
                        \"otherRelevantDataCountries\":[\"US\"],
                        \"status\":\"compliant\"
                    },
                    \"acls\":{
                        \"viewers\":[\"data.default.viewers@XXXX.group\"],
                        \"owners\":[\"data.default.owners@XXXX.group\"]
                    }
                }
            ]
        }
    }
    ```

    ### Permission required to use this API:

    `policy.service.user` or `policy.service.admin`

    Setting cache to disable is intended for testing policies, in particular policies that do caching in
    OPA.

    Args:
        policy_id (str):
        include_auth (bool | Unset): Update posted data to include auth (token, xuserid and data
            partition id) from headers Default: False.
        cache (bool | Unset): Use cache (if enabled) on policy service. Default: True.
        correlation_id (str | Unset):
        user_agent (str | Unset):
        data_partition_id (str | Unset): identifier of the data partition to query
        x_user_id (str | Unset): identifier the user in the query
        body (BodyEvaluatePolicyApiPolicyV1EvaluationsQueryPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Detail | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        body=body,
        policy_id=policy_id,
        include_auth=include_auth,
        cache=cache,
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
    body: BodyEvaluatePolicyApiPolicyV1EvaluationsQueryPost,
    policy_id: str,
    include_auth: bool | Unset = False,
    cache: bool | Unset = True,
    correlation_id: str | Unset = UNSET,
    user_agent: str | Unset = UNSET,
    data_partition_id: str | Unset = UNSET,
    x_user_id: str | Unset = UNSET,
) -> Any | Detail | HTTPValidationError | None:
    r"""Evaluate Policy

     ## Evaulate Policies
    This API is to help you evaluate policies.

    If include_auth is True, then in your file data token, xuserid and data partition id will be ignored
    in the file and information from the headers
    of the request will be used for this information.

    ### Example:
    For example file data for policy dataauthz.rego:
    Where XXXX is the data partition and YYYY is a legal tag
    ```json
    {
        \"input\": {
            \"operation\": \"update\",
            \"records\": [
                {
                    \"id\":\"XXXX:test:1.4.1654807204111\",
                    \"kind\":\"XXXX:bulkupdate:test:1.1.1654807204111\",
                    \"legal\":{
                        \"legaltags\":[
                            \"YYYY\"
                        ],
                        \"otherRelevantDataCountries\":[\"US\"],
                        \"status\":\"compliant\"
                    },
                    \"acls\":{
                        \"viewers\":[\"data.default.viewers@XXXX.group\"],
                        \"owners\":[\"data.default.owners@XXXX.group\"]
                    }
                }
            ]
        }
    }
    ```

    ### Permission required to use this API:

    `policy.service.user` or `policy.service.admin`

    Setting cache to disable is intended for testing policies, in particular policies that do caching in
    OPA.

    Args:
        policy_id (str):
        include_auth (bool | Unset): Update posted data to include auth (token, xuserid and data
            partition id) from headers Default: False.
        cache (bool | Unset): Use cache (if enabled) on policy service. Default: True.
        correlation_id (str | Unset):
        user_agent (str | Unset):
        data_partition_id (str | Unset): identifier of the data partition to query
        x_user_id (str | Unset): identifier the user in the query
        body (BodyEvaluatePolicyApiPolicyV1EvaluationsQueryPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Detail | HTTPValidationError
    """

    return sync_detailed(
        client=client,
        body=body,
        policy_id=policy_id,
        include_auth=include_auth,
        cache=cache,
        correlation_id=correlation_id,
        user_agent=user_agent,
        data_partition_id=data_partition_id,
        x_user_id=x_user_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: BodyEvaluatePolicyApiPolicyV1EvaluationsQueryPost,
    policy_id: str,
    include_auth: bool | Unset = False,
    cache: bool | Unset = True,
    correlation_id: str | Unset = UNSET,
    user_agent: str | Unset = UNSET,
    data_partition_id: str | Unset = UNSET,
    x_user_id: str | Unset = UNSET,
) -> Response[Any | Detail | HTTPValidationError]:
    r"""Evaluate Policy

     ## Evaulate Policies
    This API is to help you evaluate policies.

    If include_auth is True, then in your file data token, xuserid and data partition id will be ignored
    in the file and information from the headers
    of the request will be used for this information.

    ### Example:
    For example file data for policy dataauthz.rego:
    Where XXXX is the data partition and YYYY is a legal tag
    ```json
    {
        \"input\": {
            \"operation\": \"update\",
            \"records\": [
                {
                    \"id\":\"XXXX:test:1.4.1654807204111\",
                    \"kind\":\"XXXX:bulkupdate:test:1.1.1654807204111\",
                    \"legal\":{
                        \"legaltags\":[
                            \"YYYY\"
                        ],
                        \"otherRelevantDataCountries\":[\"US\"],
                        \"status\":\"compliant\"
                    },
                    \"acls\":{
                        \"viewers\":[\"data.default.viewers@XXXX.group\"],
                        \"owners\":[\"data.default.owners@XXXX.group\"]
                    }
                }
            ]
        }
    }
    ```

    ### Permission required to use this API:

    `policy.service.user` or `policy.service.admin`

    Setting cache to disable is intended for testing policies, in particular policies that do caching in
    OPA.

    Args:
        policy_id (str):
        include_auth (bool | Unset): Update posted data to include auth (token, xuserid and data
            partition id) from headers Default: False.
        cache (bool | Unset): Use cache (if enabled) on policy service. Default: True.
        correlation_id (str | Unset):
        user_agent (str | Unset):
        data_partition_id (str | Unset): identifier of the data partition to query
        x_user_id (str | Unset): identifier the user in the query
        body (BodyEvaluatePolicyApiPolicyV1EvaluationsQueryPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Detail | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        body=body,
        policy_id=policy_id,
        include_auth=include_auth,
        cache=cache,
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
    body: BodyEvaluatePolicyApiPolicyV1EvaluationsQueryPost,
    policy_id: str,
    include_auth: bool | Unset = False,
    cache: bool | Unset = True,
    correlation_id: str | Unset = UNSET,
    user_agent: str | Unset = UNSET,
    data_partition_id: str | Unset = UNSET,
    x_user_id: str | Unset = UNSET,
) -> Any | Detail | HTTPValidationError | None:
    r"""Evaluate Policy

     ## Evaulate Policies
    This API is to help you evaluate policies.

    If include_auth is True, then in your file data token, xuserid and data partition id will be ignored
    in the file and information from the headers
    of the request will be used for this information.

    ### Example:
    For example file data for policy dataauthz.rego:
    Where XXXX is the data partition and YYYY is a legal tag
    ```json
    {
        \"input\": {
            \"operation\": \"update\",
            \"records\": [
                {
                    \"id\":\"XXXX:test:1.4.1654807204111\",
                    \"kind\":\"XXXX:bulkupdate:test:1.1.1654807204111\",
                    \"legal\":{
                        \"legaltags\":[
                            \"YYYY\"
                        ],
                        \"otherRelevantDataCountries\":[\"US\"],
                        \"status\":\"compliant\"
                    },
                    \"acls\":{
                        \"viewers\":[\"data.default.viewers@XXXX.group\"],
                        \"owners\":[\"data.default.owners@XXXX.group\"]
                    }
                }
            ]
        }
    }
    ```

    ### Permission required to use this API:

    `policy.service.user` or `policy.service.admin`

    Setting cache to disable is intended for testing policies, in particular policies that do caching in
    OPA.

    Args:
        policy_id (str):
        include_auth (bool | Unset): Update posted data to include auth (token, xuserid and data
            partition id) from headers Default: False.
        cache (bool | Unset): Use cache (if enabled) on policy service. Default: True.
        correlation_id (str | Unset):
        user_agent (str | Unset):
        data_partition_id (str | Unset): identifier of the data partition to query
        x_user_id (str | Unset): identifier the user in the query
        body (BodyEvaluatePolicyApiPolicyV1EvaluationsQueryPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Detail | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            policy_id=policy_id,
            include_auth=include_auth,
            cache=cache,
            correlation_id=correlation_id,
            user_agent=user_agent,
            data_partition_id=data_partition_id,
            x_user_id=x_user_id,
        )
    ).parsed
