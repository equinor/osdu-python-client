from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.detail import Detail
from ...models.http_validation_error import HTTPValidationError
from ...models.info_out import InfoOut
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
        "url": "/api/policy/v1/info",
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Detail | HTTPValidationError | InfoOut | None:
    if response.status_code == 200:
        response_200 = InfoOut.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = Detail.from_dict(response.json())

        return response_400

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422

    if response.status_code == 503:
        response_503 = Detail.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Detail | HTTPValidationError | InfoOut]:
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
) -> Response[Detail | HTTPValidationError | InfoOut]:
    r"""Return Version Info

     Return Service version information.
    Expected returned JSON is in \"InfoOut\" schema, which include Services and ServiceDetail schemas.

    ### Permission required to use this API:

        None

    Args:
        correlation_id (str | Unset):
        user_agent (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Detail | HTTPValidationError | InfoOut]
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
) -> Detail | HTTPValidationError | InfoOut | None:
    r"""Return Version Info

     Return Service version information.
    Expected returned JSON is in \"InfoOut\" schema, which include Services and ServiceDetail schemas.

    ### Permission required to use this API:

        None

    Args:
        correlation_id (str | Unset):
        user_agent (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Detail | HTTPValidationError | InfoOut
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
) -> Response[Detail | HTTPValidationError | InfoOut]:
    r"""Return Version Info

     Return Service version information.
    Expected returned JSON is in \"InfoOut\" schema, which include Services and ServiceDetail schemas.

    ### Permission required to use this API:

        None

    Args:
        correlation_id (str | Unset):
        user_agent (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Detail | HTTPValidationError | InfoOut]
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
) -> Detail | HTTPValidationError | InfoOut | None:
    r"""Return Version Info

     Return Service version information.
    Expected returned JSON is in \"InfoOut\" schema, which include Services and ServiceDetail schemas.

    ### Permission required to use this API:

        None

    Args:
        correlation_id (str | Unset):
        user_agent (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Detail | HTTPValidationError | InfoOut
    """

    return (
        await asyncio_detailed(
            client=client,
            correlation_id=correlation_id,
            user_agent=user_agent,
        )
    ).parsed
