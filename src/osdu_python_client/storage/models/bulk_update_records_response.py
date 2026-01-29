from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BulkUpdateRecordsResponse")


@_attrs_define
class BulkUpdateRecordsResponse:
    """
    Attributes:
        record_count (int | Unset):
        record_ids (list[str] | Unset):
        not_found_record_ids (list[str] | Unset):
        un_authorized_record_ids (list[str] | Unset):
        locked_record_ids (list[str] | Unset):
    """

    record_count: int | Unset = UNSET
    record_ids: list[str] | Unset = UNSET
    not_found_record_ids: list[str] | Unset = UNSET
    un_authorized_record_ids: list[str] | Unset = UNSET
    locked_record_ids: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        record_count = self.record_count

        record_ids: list[str] | Unset = UNSET
        if not isinstance(self.record_ids, Unset):
            record_ids = self.record_ids

        not_found_record_ids: list[str] | Unset = UNSET
        if not isinstance(self.not_found_record_ids, Unset):
            not_found_record_ids = self.not_found_record_ids

        un_authorized_record_ids: list[str] | Unset = UNSET
        if not isinstance(self.un_authorized_record_ids, Unset):
            un_authorized_record_ids = self.un_authorized_record_ids

        locked_record_ids: list[str] | Unset = UNSET
        if not isinstance(self.locked_record_ids, Unset):
            locked_record_ids = self.locked_record_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if record_count is not UNSET:
            field_dict["recordCount"] = record_count
        if record_ids is not UNSET:
            field_dict["recordIds"] = record_ids
        if not_found_record_ids is not UNSET:
            field_dict["notFoundRecordIds"] = not_found_record_ids
        if un_authorized_record_ids is not UNSET:
            field_dict["unAuthorizedRecordIds"] = un_authorized_record_ids
        if locked_record_ids is not UNSET:
            field_dict["lockedRecordIds"] = locked_record_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        record_count = d.pop("recordCount", UNSET)

        record_ids = cast(list[str], d.pop("recordIds", UNSET))

        not_found_record_ids = cast(list[str], d.pop("notFoundRecordIds", UNSET))

        un_authorized_record_ids = cast(
            list[str], d.pop("unAuthorizedRecordIds", UNSET)
        )

        locked_record_ids = cast(list[str], d.pop("lockedRecordIds", UNSET))

        bulk_update_records_response = cls(
            record_count=record_count,
            record_ids=record_ids,
            not_found_record_ids=not_found_record_ids,
            un_authorized_record_ids=un_authorized_record_ids,
            locked_record_ids=locked_record_ids,
        )

        bulk_update_records_response.additional_properties = d
        return bulk_update_records_response

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
