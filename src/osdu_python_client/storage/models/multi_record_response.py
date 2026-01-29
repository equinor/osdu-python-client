from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.conversion_status import ConversionStatus


T = TypeVar("T", bound="MultiRecordResponse")


@_attrs_define
class MultiRecordResponse:
    """
    Attributes:
        records (list[str] | Unset):
        not_found (list[str] | Unset):
        conversion_statuses (list[ConversionStatus] | Unset):
    """

    records: list[str] | Unset = UNSET
    not_found: list[str] | Unset = UNSET
    conversion_statuses: list[ConversionStatus] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        records: list[str] | Unset = UNSET
        if not isinstance(self.records, Unset):
            records = self.records

        not_found: list[str] | Unset = UNSET
        if not isinstance(self.not_found, Unset):
            not_found = self.not_found

        conversion_statuses: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.conversion_statuses, Unset):
            conversion_statuses = []
            for conversion_statuses_item_data in self.conversion_statuses:
                conversion_statuses_item = conversion_statuses_item_data.to_dict()
                conversion_statuses.append(conversion_statuses_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if records is not UNSET:
            field_dict["records"] = records
        if not_found is not UNSET:
            field_dict["notFound"] = not_found
        if conversion_statuses is not UNSET:
            field_dict["conversionStatuses"] = conversion_statuses

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.conversion_status import ConversionStatus

        d = dict(src_dict)
        records = cast(list[str], d.pop("records", UNSET))

        not_found = cast(list[str], d.pop("notFound", UNSET))

        _conversion_statuses = d.pop("conversionStatuses", UNSET)
        conversion_statuses: list[ConversionStatus] | Unset = UNSET
        if _conversion_statuses is not UNSET:
            conversion_statuses = []
            for conversion_statuses_item_data in _conversion_statuses:
                conversion_statuses_item = ConversionStatus.from_dict(
                    conversion_statuses_item_data
                )

                conversion_statuses.append(conversion_statuses_item)

        multi_record_response = cls(
            records=records,
            not_found=not_found,
            conversion_statuses=conversion_statuses,
        )

        multi_record_response.additional_properties = d
        return multi_record_response

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
