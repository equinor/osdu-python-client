import json
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
    limit = int(os.getenv("OSDU_SEARCH_LIMIT", "10"))

    request = QueryRequest(
        kind=kind_data,
        query=query_text,
        limit=limit,
    )

    # sync_detailed returns a Response object wrapper
    result = query_records.sync_detailed(
        client=search_client,
        body=request,
        data_partition_id=config.data_partition_id,
    )

    assert result is not None
    assert result.status_code.value == 200

    # The generated client parses the JSON for you into 'parsed'
    dto = result.parsed
    assert dto is not None

    # QueryResponse should expose results (may be empty depending on query/kind)
    assert hasattr(dto, "results")
    print(dto.results)
