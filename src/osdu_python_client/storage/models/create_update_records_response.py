from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateUpdateRecordsResponse")


@_attrs_define
class CreateUpdateRecordsResponse:
    """
    Attributes:
        record_count (int | Unset):
        record_ids (list[str] | Unset):
        skipped_record_ids (list[str] | Unset):
        record_id_versions (list[str] | Unset):
    """

    record_count: int | Unset = UNSET
    record_ids: list[str] | Unset = UNSET
    skipped_record_ids: list[str] | Unset = UNSET
    record_id_versions: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        record_count = self.record_count

        record_ids: list[str] | Unset = UNSET
        if not isinstance(self.record_ids, Unset):
            record_ids = self.record_ids

        skipped_record_ids: list[str] | Unset = UNSET
        if not isinstance(self.skipped_record_ids, Unset):
            skipped_record_ids = self.skipped_record_ids

        record_id_versions: list[str] | Unset = UNSET
        if not isinstance(self.record_id_versions, Unset):
            record_id_versions = self.record_id_versions

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if record_count is not UNSET:
            field_dict["recordCount"] = record_count
        if record_ids is not UNSET:
            field_dict["recordIds"] = record_ids
        if skipped_record_ids is not UNSET:
            field_dict["skippedRecordIds"] = skipped_record_ids
        if record_id_versions is not UNSET:
            field_dict["recordIdVersions"] = record_id_versions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        record_count = d.pop("recordCount", UNSET)

        record_ids = cast(list[str], d.pop("recordIds", UNSET))

        skipped_record_ids = cast(list[str], d.pop("skippedRecordIds", UNSET))

        record_id_versions = cast(list[str], d.pop("recordIdVersions", UNSET))

        create_update_records_response = cls(
            record_count=record_count,
            record_ids=record_ids,
            skipped_record_ids=skipped_record_ids,
            record_id_versions=record_id_versions,
        )

        create_update_records_response.additional_properties = d
        return create_update_records_response

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
