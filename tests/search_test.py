import os

import pytest

from osdu_python_client.search.api.search_api import query_records
from osdu_python_client.search.client import AuthenticatedClient
from osdu_python_client.search.models.query_request import QueryRequest
from tests.config import CoreConfig


@pytest.fixture(scope="session")
def search_client(config: CoreConfig, access_token: str) -> AuthenticatedClient:
    return AuthenticatedClient(base_url=config.search_url, token=access_token)


def test_search_query_records(
    config: CoreConfig, search_client: AuthenticatedClient
):
    kind_data = os.getenv("OSDU_SEARCH_KIND", "osdu:wks:work-product-component--WellLog:*")
    query_text = os.getenv("OSDU_SEARCH_QUERY", "*")
    limit = int(os.getenv("OSDU_SEARCH_LIMIT", "5"))

    request = QueryRequest(
        kind=kind_data,
        query=query_text,
        limit=limit,
        returned_fields=["id", "kind","createTime"]
    )

    result = query_records.sync_detailed(
        client=search_client,
        body=request,
        data_partition_id=config.data_partition_id,
    )

    assert result is not None
    assert result.status_code.value == 200

    dto = result.parsed
    assert dto is not None

    assert hasattr(dto, "results")
    for record in dto.results:
        print(record.additional_properties)


def test_search_wellbores_for_given_field(
    config: CoreConfig, search_client: AuthenticatedClient
):
    request = QueryRequest(
        kind="osdu:wks:master-data--Field:*",
        query='data.FieldName:"AASTA HANSTEEN"',
        limit=1,
        returned_fields=["id", ]
    )

    result = query_records.sync_detailed(
        client=search_client,
        body=request,
        data_partition_id=config.data_partition_id,
    )

    assert result is not None
    assert result.status_code.value == 200

    dto = result.parsed
    assert dto is not None

    assert hasattr(dto, "results")
    field_id = dto.results[0].additional_properties["id"]
    print("Field ID: " + field_id)

    request = QueryRequest(
        kind="osdu:wks:master-data--Wellbore:*",
        query=f'nested(data.GeoContexts, (FieldID:"{field_id}"))',
        limit=100,
        returned_fields=["id", "kind","createTime"]
    )

    result = query_records.sync_detailed(
        client=search_client,
        body=request,
        data_partition_id=config.data_partition_id,
    )

    assert result is not None
    assert result.status_code.value == 200

    dto = result.parsed
    assert dto is not None

    assert hasattr(dto, "results")
    for record in dto.results:
        print(record.additional_properties)
