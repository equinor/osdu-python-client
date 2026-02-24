import os
import pytest

from osdu_python_client.entitlements.api.list_group_on_behalf_of_api import (
    list_all_partition_groups,
)
from osdu_python_client.entitlements.client import AuthenticatedClient
from tests.config import CoreConfig


@pytest.fixture(scope="session")
def entitlements_client(config: CoreConfig, access_token: str) -> AuthenticatedClient:
    return AuthenticatedClient(base_url=config.entitlements_url, token=access_token)

def test_list_all_entitlement_groups(
        config: CoreConfig, entitlements_client: AuthenticatedClient
):
    group_type = os.getenv("OSDU_GROUP_TYPE", "NONE")

    # sync_detailed returns a Response object wrapper
    result = list_all_partition_groups.sync_detailed(
        client=entitlements_client,
        data_partition_id=config.data_partition_id,
        type_=group_type,
    )

    assert result is not None
    assert result.status_code.value == 200

    # The generated client parses the JSON for you into 'parsed'
    dto = result.parsed
    assert dto is not None

    # Access the groups property on the DTO directly
    assert hasattr(dto, "groups")
    for group in dto.groups:
        print(group.name + " - " + group.email)
