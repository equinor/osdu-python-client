import logging
import os

import pytest

from osdu_python_client import OsduClient, enable_debug_logging


@pytest.fixture(autouse=True)
def _debug_logging(caplog: pytest.LogCaptureFixture):
    enable_debug_logging(include_bodies=True)
    caplog.set_level(logging.DEBUG, logger="osdu_python_client")


def test_list_my_entitlement_groups(osdu: OsduClient):
    member_email = os.environ["OSDU_MEMBER_EMAIL"]
    group_type = os.getenv("OSDU_GROUP_TYPE", "none")
    print(f"member_email: {member_email!r}")
    print(f"group_type: {group_type!r}")
    print(f"entitlements URL: {osdu.entitlements.get_httpx_client().base_url}")

    dto = osdu.entitlements.list_groups_on_behalf_of(
        member_email=member_email,
        type_=group_type,
    )

    assert dto is not None
    assert hasattr(dto, "groups")
    print(f"\nGroups for {member_email}:")
    for group in dto.groups:
        print(f"  {group.name} - {group.email}")
