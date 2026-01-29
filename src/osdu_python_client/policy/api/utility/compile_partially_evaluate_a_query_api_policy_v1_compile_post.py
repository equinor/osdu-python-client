from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.body_compile_partially_evaluate_a_query_api_policy_v1_compile_post import (
    BodyCompilePartiallyEvaluateAQueryApiPolicyV1CompilePost,
)
from ...models.detail import Detail
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: BodyCompilePartiallyEvaluateAQueryApiPolicyV1CompilePost,
    metrics: bool | Unset = False,
    instrument: bool | Unset = False,
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

    params["metrics"] = metrics

    params["instrument"] = instrument

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/policy/v1/compile",
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
    *,
    client: AuthenticatedClient,
    body: BodyCompilePartiallyEvaluateAQueryApiPolicyV1CompilePost,
    metrics: bool | Unset = False,
    instrument: bool | Unset = False,
    correlation_id: str | Unset = UNSET,
    user_agent: str | Unset = UNSET,
    data_partition_id: str | Unset = UNSET,
    x_user_id: str | Unset = UNSET,
) -> Response[Any | Detail]:
    """Compile Partially Evaluate A Query

     # Compile - Partially evaluate a query.
    The Compile API allows you to partially evaluate Rego queries and obtain a simplified version of the
    policy.

    ### Metrics
    When query parameter metrics=true, the API response will include detailed performance metrics from
    OPA.
    OPA currently supports the following query performance metrics:

        timer_rego_input_parse_ns: time taken (in nanoseconds) to parse the input
        timer_rego_query_parse_ns: time taken (in nanonseconds) to parse the query.
        timer_rego_query_compile_ns: time taken (in nanonseconds) to compile the query.
        timer_rego_query_eval_ns: time taken (in nanonseconds) to evaluate the query.
        timer_rego_module_parse_ns: time taken (in nanoseconds) to parse the input policy module.
        timer_rego_module_compile_ns: time taken (in nanoseconds) to compile the loaded policy modules.
        timer_server_handler_ns: time take (in nanoseconds) to handle the API request.

    ### Instrumentation
    To enable query instrumentation, specify metrics=true and instrument=true query parameters when
    executing the API call.
    Query instrumentation can help diagnose performance problems, however, it can add significant
    overhead to query evaluation.
    We recommend leaving query instrumentation off unless you are debugging a performance problem.

    ### Permission required to use this API:

        policy.service.admin

    Args:
        metrics (bool | Unset): Include report detailed performance metrics on requested on
            individual API call. Returned inline with the API response Default: False.
        instrument (bool | Unset): Include instrumentation data wth detailed performance metrics
            on requested on individual API call. Returned inline with the API response Default: False.
        correlation_id (str | Unset):
        user_agent (str | Unset):
        data_partition_id (str | Unset): identifier of the data partition to query
        x_user_id (str | Unset): identifier the user in the query
        body (BodyCompilePartiallyEvaluateAQueryApiPolicyV1CompilePost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Detail]
    """

    kwargs = _get_kwargs(
        body=body,
        metrics=metrics,
        instrument=instrument,
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
    body: BodyCompilePartiallyEvaluateAQueryApiPolicyV1CompilePost,
    metrics: bool | Unset = False,
    instrument: bool | Unset = False,
    correlation_id: str | Unset = UNSET,
    user_agent: str | Unset = UNSET,
    data_partition_id: str | Unset = UNSET,
    x_user_id: str | Unset = UNSET,
) -> Any | Detail | None:
    """Compile Partially Evaluate A Query

     # Compile - Partially evaluate a query.
    The Compile API allows you to partially evaluate Rego queries and obtain a simplified version of the
    policy.

    ### Metrics
    When query parameter metrics=true, the API response will include detailed performance metrics from
    OPA.
    OPA currently supports the following query performance metrics:

        timer_rego_input_parse_ns: time taken (in nanoseconds) to parse the input
        timer_rego_query_parse_ns: time taken (in nanonseconds) to parse the query.
        timer_rego_query_compile_ns: time taken (in nanonseconds) to compile the query.
        timer_rego_query_eval_ns: time taken (in nanonseconds) to evaluate the query.
        timer_rego_module_parse_ns: time taken (in nanoseconds) to parse the input policy module.
        timer_rego_module_compile_ns: time taken (in nanoseconds) to compile the loaded policy modules.
        timer_server_handler_ns: time take (in nanoseconds) to handle the API request.

    ### Instrumentation
    To enable query instrumentation, specify metrics=true and instrument=true query parameters when
    executing the API call.
    Query instrumentation can help diagnose performance problems, however, it can add significant
    overhead to query evaluation.
    We recommend leaving query instrumentation off unless you are debugging a performance problem.

    ### Permission required to use this API:

        policy.service.admin

    Args:
        metrics (bool | Unset): Include report detailed performance metrics on requested on
            individual API call. Returned inline with the API response Default: False.
        instrument (bool | Unset): Include instrumentation data wth detailed performance metrics
            on requested on individual API call. Returned inline with the API response Default: False.
        correlation_id (str | Unset):
        user_agent (str | Unset):
        data_partition_id (str | Unset): identifier of the data partition to query
        x_user_id (str | Unset): identifier the user in the query
        body (BodyCompilePartiallyEvaluateAQueryApiPolicyV1CompilePost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Detail
    """

    return sync_detailed(
        client=client,
        body=body,
        metrics=metrics,
        instrument=instrument,
        correlation_id=correlation_id,
        user_agent=user_agent,
        data_partition_id=data_partition_id,
        x_user_id=x_user_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: BodyCompilePartiallyEvaluateAQueryApiPolicyV1CompilePost,
    metrics: bool | Unset = False,
    instrument: bool | Unset = False,
    correlation_id: str | Unset = UNSET,
    user_agent: str | Unset = UNSET,
    data_partition_id: str | Unset = UNSET,
    x_user_id: str | Unset = UNSET,
) -> Response[Any | Detail]:
    """Compile Partially Evaluate A Query

     # Compile - Partially evaluate a query.
    The Compile API allows you to partially evaluate Rego queries and obtain a simplified version of the
    policy.

    ### Metrics
    When query parameter metrics=true, the API response will include detailed performance metrics from
    OPA.
    OPA currently supports the following query performance metrics:

        timer_rego_input_parse_ns: time taken (in nanoseconds) to parse the input
        timer_rego_query_parse_ns: time taken (in nanonseconds) to parse the query.
        timer_rego_query_compile_ns: time taken (in nanonseconds) to compile the query.
        timer_rego_query_eval_ns: time taken (in nanonseconds) to evaluate the query.
        timer_rego_module_parse_ns: time taken (in nanoseconds) to parse the input policy module.
        timer_rego_module_compile_ns: time taken (in nanoseconds) to compile the loaded policy modules.
        timer_server_handler_ns: time take (in nanoseconds) to handle the API request.

    ### Instrumentation
    To enable query instrumentation, specify metrics=true and instrument=true query parameters when
    executing the API call.
    Query instrumentation can help diagnose performance problems, however, it can add significant
    overhead to query evaluation.
    We recommend leaving query instrumentation off unless you are debugging a performance problem.

    ### Permission required to use this API:

        policy.service.admin

    Args:
        metrics (bool | Unset): Include report detailed performance metrics on requested on
            individual API call. Returned inline with the API response Default: False.
        instrument (bool | Unset): Include instrumentation data wth detailed performance metrics
            on requested on individual API call. Returned inline with the API response Default: False.
        correlation_id (str | Unset):
        user_agent (str | Unset):
        data_partition_id (str | Unset): identifier of the data partition to query
        x_user_id (str | Unset): identifier the user in the query
        body (BodyCompilePartiallyEvaluateAQueryApiPolicyV1CompilePost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Detail]
    """

    kwargs = _get_kwargs(
        body=body,
        metrics=metrics,
        instrument=instrument,
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
    body: BodyCompilePartiallyEvaluateAQueryApiPolicyV1CompilePost,
    metrics: bool | Unset = False,
    instrument: bool | Unset = False,
    correlation_id: str | Unset = UNSET,
    user_agent: str | Unset = UNSET,
    data_partition_id: str | Unset = UNSET,
    x_user_id: str | Unset = UNSET,
) -> Any | Detail | None:
    """Compile Partially Evaluate A Query

     # Compile - Partially evaluate a query.
    The Compile API allows you to partially evaluate Rego queries and obtain a simplified version of the
    policy.

    ### Metrics
    When query parameter metrics=true, the API response will include detailed performance metrics from
    OPA.
    OPA currently supports the following query performance metrics:

        timer_rego_input_parse_ns: time taken (in nanoseconds) to parse the input
        timer_rego_query_parse_ns: time taken (in nanonseconds) to parse the query.
        timer_rego_query_compile_ns: time taken (in nanonseconds) to compile the query.
        timer_rego_query_eval_ns: time taken (in nanonseconds) to evaluate the query.
        timer_rego_module_parse_ns: time taken (in nanoseconds) to parse the input policy module.
        timer_rego_module_compile_ns: time taken (in nanoseconds) to compile the loaded policy modules.
        timer_server_handler_ns: time take (in nanoseconds) to handle the API request.

    ### Instrumentation
    To enable query instrumentation, specify metrics=true and instrument=true query parameters when
    executing the API call.
    Query instrumentation can help diagnose performance problems, however, it can add significant
    overhead to query evaluation.
    We recommend leaving query instrumentation off unless you are debugging a performance problem.

    ### Permission required to use this API:

        policy.service.admin

    Args:
        metrics (bool | Unset): Include report detailed performance metrics on requested on
            individual API call. Returned inline with the API response Default: False.
        instrument (bool | Unset): Include instrumentation data wth detailed performance metrics
            on requested on individual API call. Returned inline with the API response Default: False.
        correlation_id (str | Unset):
        user_agent (str | Unset):
        data_partition_id (str | Unset): identifier of the data partition to query
        x_user_id (str | Unset): identifier the user in the query
        body (BodyCompilePartiallyEvaluateAQueryApiPolicyV1CompilePost):

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
            metrics=metrics,
            instrument=instrument,
            correlation_id=correlation_id,
            user_agent=user_agent,
            data_partition_id=data_partition_id,
            x_user_id=x_user_id,
        )
    ).parsed
