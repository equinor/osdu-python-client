from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ct import CT


T = TypeVar("T", bound="CTDeprecationInfo")


@_attrs_define
class CTDeprecationInfo:
    """
    Attributes:
        superseded_by_ct (CT | Unset):
        deprecation_state (str | Unset):
        remarks (str | Unset):
    """

    superseded_by_ct: CT | Unset = UNSET
    deprecation_state: str | Unset = UNSET
    remarks: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        superseded_by_ct: dict[str, Any] | Unset = UNSET
        if not isinstance(self.superseded_by_ct, Unset):
            superseded_by_ct = self.superseded_by_ct.to_dict()

        deprecation_state = self.deprecation_state

        remarks = self.remarks

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if superseded_by_ct is not UNSET:
            field_dict["supersededByCT"] = superseded_by_ct
        if deprecation_state is not UNSET:
            field_dict["deprecationState"] = deprecation_state
        if remarks is not UNSET:
            field_dict["remarks"] = remarks

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ct import CT

        d = dict(src_dict)
        _superseded_by_ct = d.pop("supersededByCT", UNSET)
        superseded_by_ct: CT | Unset
        if isinstance(_superseded_by_ct, Unset):
            superseded_by_ct = UNSET
        else:
            superseded_by_ct = CT.from_dict(_superseded_by_ct)

        deprecation_state = d.pop("deprecationState", UNSET)

        remarks = d.pop("remarks", UNSET)

        ct_deprecation_info = cls(
            superseded_by_ct=superseded_by_ct,
            deprecation_state=deprecation_state,
            remarks=remarks,
        )

        ct_deprecation_info.additional_properties = d
        return ct_deprecation_info

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
