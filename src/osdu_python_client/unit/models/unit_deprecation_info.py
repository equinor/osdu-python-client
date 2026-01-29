from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UnitDeprecationInfo")


@_attrs_define
class UnitDeprecationInfo:
    """
    Attributes:
        state (str | Unset):
        remarks (str | Unset):
        superseded_by_unit (str | Unset):
    """

    state: str | Unset = UNSET
    remarks: str | Unset = UNSET
    superseded_by_unit: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        state = self.state

        remarks = self.remarks

        superseded_by_unit = self.superseded_by_unit

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if state is not UNSET:
            field_dict["state"] = state
        if remarks is not UNSET:
            field_dict["remarks"] = remarks
        if superseded_by_unit is not UNSET:
            field_dict["supersededByUnit"] = superseded_by_unit

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        state = d.pop("state", UNSET)

        remarks = d.pop("remarks", UNSET)

        superseded_by_unit = d.pop("supersededByUnit", UNSET)

        unit_deprecation_info = cls(
            state=state,
            remarks=remarks,
            superseded_by_unit=superseded_by_unit,
        )

        unit_deprecation_info.additional_properties = d
        return unit_deprecation_info

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
