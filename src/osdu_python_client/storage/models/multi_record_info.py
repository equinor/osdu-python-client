from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.record import Record


T = TypeVar("T", bound="MultiRecordInfo")


@_attrs_define
class MultiRecordInfo:
    """
    Attributes:
        records (list[Record] | Unset):
        invalid_records (list[str] | Unset):
        retry_records (list[str] | Unset):
    """

    records: list[Record] | Unset = UNSET
    invalid_records: list[str] | Unset = UNSET
    retry_records: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        records: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.records, Unset):
            records = []
            for records_item_data in self.records:
                records_item = records_item_data.to_dict()
                records.append(records_item)

        invalid_records: list[str] | Unset = UNSET
        if not isinstance(self.invalid_records, Unset):
            invalid_records = self.invalid_records

        retry_records: list[str] | Unset = UNSET
        if not isinstance(self.retry_records, Unset):
            retry_records = self.retry_records

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if records is not UNSET:
            field_dict["records"] = records
        if invalid_records is not UNSET:
            field_dict["invalidRecords"] = invalid_records
        if retry_records is not UNSET:
            field_dict["retryRecords"] = retry_records

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.record import Record

        d = dict(src_dict)
        _records = d.pop("records", UNSET)
        records: list[Record] | Unset = UNSET
        if _records is not UNSET:
            records = []
            for records_item_data in _records:
                records_item = Record.from_dict(records_item_data)

                records.append(records_item)

        invalid_records = cast(list[str], d.pop("invalidRecords", UNSET))

        retry_records = cast(list[str], d.pop("retryRecords", UNSET))

        multi_record_info = cls(
            records=records,
            invalid_records=invalid_records,
            retry_records=retry_records,
        )

        multi_record_info.additional_properties = d
        return multi_record_info

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
