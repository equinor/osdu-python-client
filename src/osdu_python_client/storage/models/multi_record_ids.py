from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MultiRecordIds")


@_attrs_define
class MultiRecordIds:
    """Record ids

    Attributes:
        records (list[str] | Unset):
        attributes (list[str] | Unset):
    """

    records: list[str] | Unset = UNSET
    attributes: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        records: list[str] | Unset = UNSET
        if not isinstance(self.records, Unset):
            records = self.records

        attributes: list[str] | Unset = UNSET
        if not isinstance(self.attributes, Unset):
            attributes = self.attributes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if records is not UNSET:
            field_dict["records"] = records
        if attributes is not UNSET:
            field_dict["attributes"] = attributes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        records = cast(list[str], d.pop("records", UNSET))

        attributes = cast(list[str], d.pop("attributes", UNSET))

        multi_record_ids = cls(
            records=records,
            attributes=attributes,
        )

        multi_record_ids.additional_properties = d
        return multi_record_ids

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
