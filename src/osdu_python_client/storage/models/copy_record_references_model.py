from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.record_version_model import RecordVersionModel


T = TypeVar("T", bound="CopyRecordReferencesModel")


@_attrs_define
class CopyRecordReferencesModel:
    """
    Attributes:
        target (str | Unset):
        records (list[RecordVersionModel] | Unset):
    """

    target: str | Unset = UNSET
    records: list[RecordVersionModel] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        target = self.target

        records: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.records, Unset):
            records = []
            for records_item_data in self.records:
                records_item = records_item_data.to_dict()
                records.append(records_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if target is not UNSET:
            field_dict["target"] = target
        if records is not UNSET:
            field_dict["records"] = records

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.record_version_model import RecordVersionModel

        d = dict(src_dict)
        target = d.pop("target", UNSET)

        _records = d.pop("records", UNSET)
        records: list[RecordVersionModel] | Unset = UNSET
        if _records is not UNSET:
            records = []
            for records_item_data in _records:
                records_item = RecordVersionModel.from_dict(records_item_data)

                records.append(records_item)

        copy_record_references_model = cls(
            target=target,
            records=records,
        )

        copy_record_references_model.additional_properties = d
        return copy_record_references_model

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
