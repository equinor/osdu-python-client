from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MaxMisLocation")


@_attrs_define
class MaxMisLocation:
    """
    Attributes:
        d_i (float | Unset):
        d_j (float | Unset):
    """

    d_i: float | Unset = UNSET
    d_j: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        d_i = self.d_i

        d_j = self.d_j

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if d_i is not UNSET:
            field_dict["dI"] = d_i
        if d_j is not UNSET:
            field_dict["dJ"] = d_j

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        d_i = d.pop("dI", UNSET)

        d_j = d.pop("dJ", UNSET)

        max_mis_location = cls(
            d_i=d_i,
            d_j=d_j,
        )

        max_mis_location.additional_properties = d
        return max_mis_location

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
