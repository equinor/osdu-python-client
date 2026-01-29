from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.json_patch import JsonPatch
    from ..models.record_query_patch import RecordQueryPatch


T = TypeVar("T", bound="PatchRecordsRequestModel")


@_attrs_define
class PatchRecordsRequestModel:
    """Records to be patched

    Example:
        {'query': {'ids': ['common:work-product-component--wellLog:123456']}, 'ops': [{'op': 'remove', 'path':
            '/acl/viewers/0'}]}

    Attributes:
        query (RecordQueryPatch): Represents a model for Record Query Patch Example: {'ids': ['common:work-product-
            component--wellLog:123456']}.
        ops (JsonPatch): Record patch operations.
    """

    query: RecordQueryPatch
    ops: JsonPatch
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        query = self.query.to_dict()

        ops = self.ops.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "query": query,
                "ops": ops,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.json_patch import JsonPatch
        from ..models.record_query_patch import RecordQueryPatch

        d = dict(src_dict)
        query = RecordQueryPatch.from_dict(d.pop("query"))

        ops = JsonPatch.from_dict(d.pop("ops"))

        patch_records_request_model = cls(
            query=query,
            ops=ops,
        )

        patch_records_request_model.additional_properties = d
        return patch_records_request_model

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
