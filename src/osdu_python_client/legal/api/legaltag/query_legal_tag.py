from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.query_legal_tag import QueryLegalTag
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: QueryLegalTag,
    valid: bool | Unset = True,
    data_partition_id: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["data-partition-id"] = data_partition_id

    params: dict[str, Any] = {}

    params["valid"] = valid

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/legaltags:query",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | None:
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: QueryLegalTag,
    valid: bool | Unset = True,
    data_partition_id: str,
) -> Response[Any]:
    """Retrieves the legaltags which matches query criteria or none if there is no match.

     This allows query for specific attributes of legaltags including the attributes of
    extensionproperties. See [https://osdu.pages.opengroup.org/platform/security-and-
    compliance/legal/api/#legal-query](https://osdu.pages.opengroup.org/platform/security-and-
    compliance/legal/api/#legal-query) for more details.

    Args:
        valid (bool | Unset):  Default: True.
        data_partition_id (str):
        body (QueryLegalTag): Represents the Search Query objects for Legaltags.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        body=body,
        valid=valid,
        data_partition_id=data_partition_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: QueryLegalTag,
    valid: bool | Unset = True,
    data_partition_id: str,
) -> Response[Any]:
    """Retrieves the legaltags which matches query criteria or none if there is no match.

     This allows query for specific attributes of legaltags including the attributes of
    extensionproperties. See [https://osdu.pages.opengroup.org/platform/security-and-
    compliance/legal/api/#legal-query](https://osdu.pages.opengroup.org/platform/security-and-
    compliance/legal/api/#legal-query) for more details.

    Args:
        valid (bool | Unset):  Default: True.
        data_partition_id (str):
        body (QueryLegalTag): Represents the Search Query objects for Legaltags.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        body=body,
        valid=valid,
        data_partition_id=data_partition_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
