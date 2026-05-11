import os

from osdu_python_client import OsduClient, enable_debug_logging
from osdu_python_client.generated.search.models.query_request import QueryRequest



def test_search_query_records(osdu: OsduClient):
    request = QueryRequest(
        kind=os.getenv("OSDU_SEARCH_KIND", "osdu:wks:work-product-component--WellLog:*"),
        query=os.getenv("OSDU_SEARCH_QUERY", "*"),
        limit=int(os.getenv("OSDU_SEARCH_LIMIT", "5")),
        returned_fields=["id", "kind", "createTime"],
    )

    dto = osdu.search.query_records(body=request)

    assert dto is not None
    assert hasattr(dto, "results")
    for record in dto.results:
        print(record.additional_properties)


def test_search_wellbores_for_given_field(osdu: OsduClient):
    enable_debug_logging(include_bodies=True)

    field = osdu.search.query_records(
        body=QueryRequest(
            kind="osdu:wks:master-data--Field:*",
            query='data.FieldName:"AASTA HANSTEEN"',
            limit=1,
            returned_fields=["id"],
        )
    )
    assert field.results, "No matching field returned"
    field_id = field.results[0].additional_properties["id"]
    print("Field ID: " + field_id)

    wellbores = osdu.search.query_records(
        body=QueryRequest(
            kind="osdu:wks:master-data--Wellbore:*",
            query=f'nested(data.GeoContexts, (FieldID:"{field_id}"))',
            limit=100,
            returned_fields=["id", "kind", "createTime"],
        )
    )
    assert wellbores is not None
    for record in wellbores.results:
        print(record.additional_properties)
