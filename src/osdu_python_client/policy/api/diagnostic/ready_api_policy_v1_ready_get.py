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
    correlation_id: str | Unset = UNSET,
    user_agent: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(correlation_id, Unset):
        headers["correlation-id"] = correlation_id

    if not isinstance(user_agent, Unset):
        headers["user-agent"] = user_agent

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/policy/v1/ready",
    }

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

    if response.status_code == 501:
        response_501 = Detail.from_dict(response.json())

        return response_501

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
    client: AuthenticatedClient | Client,
    correlation_id: str | Unset = UNSET,
    user_agent: str | Unset = UNSET,
) -> Response[Any | Detail | HTTPValidationError]:
    """Ready

     ## Health check endpoint, which depends on OPA being available and healthy.
    This API does not require any headers or authentication.

    ### Possible http return status codes:
    * 200 - no error
    * 501 - not implemented
    * 503 - service not available

    The /ready endpoint responds with a 200 HTTP status code if the overall application works.
    The endpoint indicates that the service is ready to serve requests.

    ### Permission required to use this API:

        None

    Args:
        correlation_id (str | Unset):
        user_agent (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Detail | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        correlation_id=correlation_id,
        user_agent=user_agent,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    correlation_id: str | Unset = UNSET,
    user_agent: str | Unset = UNSET,
) -> Any | Detail | HTTPValidationError | None:
    """Ready

     ## Health check endpoint, which depends on OPA being available and healthy.
    This API does not require any headers or authentication.

    ### Possible http return status codes:
    * 200 - no error
    * 501 - not implemented
    * 503 - service not available

    The /ready endpoint responds with a 200 HTTP status code if the overall application works.
    The endpoint indicates that the service is ready to serve requests.

    ### Permission required to use this API:

        None

    Args:
        correlation_id (str | Unset):
        user_agent (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Detail | HTTPValidationError
    """

    return sync_detailed(
        client=client,
        correlation_id=correlation_id,
        user_agent=user_agent,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    correlation_id: str | Unset = UNSET,
    user_agent: str | Unset = UNSET,
) -> Response[Any | Detail | HTTPValidationError]:
    """Ready

     ## Health check endpoint, which depends on OPA being available and healthy.
    This API does not require any headers or authentication.

    ### Possible http return status codes:
    * 200 - no error
    * 501 - not implemented
    * 503 - service not available

    The /ready endpoint responds with a 200 HTTP status code if the overall application works.
    The endpoint indicates that the service is ready to serve requests.

    ### Permission required to use this API:

        None

    Args:
        correlation_id (str | Unset):
        user_agent (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Detail | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        correlation_id=correlation_id,
        user_agent=user_agent,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    correlation_id: str | Unset = UNSET,
    user_agent: str | Unset = UNSET,
) -> Any | Detail | HTTPValidationError | None:
    """Ready

     ## Health check endpoint, which depends on OPA being available and healthy.
    This API does not require any headers or authentication.

    ### Possible http return status codes:
    * 200 - no error
    * 501 - not implemented
    * 503 - service not available

    The /ready endpoint responds with a 200 HTTP status code if the overall application works.
    The endpoint indicates that the service is ready to serve requests.

    ### Permission required to use this API:

        None

    Args:
        correlation_id (str | Unset):
        user_agent (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Detail | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            client=client,
            correlation_id=correlation_id,
            user_agent=user_agent,
        )
    ).parsed
