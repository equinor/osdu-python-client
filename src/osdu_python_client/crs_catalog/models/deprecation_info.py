from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DeprecationInfo")


@_attrs_define
class DeprecationInfo:
    """
    Attributes:
        deprecation_state (str | Unset):
        remarks (str | Unset):
    """

    deprecation_state: str | Unset = UNSET
    remarks: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        deprecation_state = self.deprecation_state

        remarks = self.remarks

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if deprecation_state is not UNSET:
            field_dict["deprecationState"] = deprecation_state
        if remarks is not UNSET:
            field_dict["remarks"] = remarks

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        deprecation_state = d.pop("deprecationState", UNSET)

        remarks = d.pop("remarks", UNSET)

        deprecation_info = cls(
            deprecation_state=deprecation_state,
            remarks=remarks,
        )

        deprecation_info.additional_properties = d
        return deprecation_info

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
