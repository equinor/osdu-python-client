from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SphericalBoundingBox")


@_attrs_define
class SphericalBoundingBox:
    """
    Attributes:
        longitude_left (float | Unset):
        latitude_lower (float | Unset):
        longitude_right (float | Unset):
        latitude_upper (float | Unset):
    """

    longitude_left: float | Unset = UNSET
    latitude_lower: float | Unset = UNSET
    longitude_right: float | Unset = UNSET
    latitude_upper: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        longitude_left = self.longitude_left

        latitude_lower = self.latitude_lower

        longitude_right = self.longitude_right

        latitude_upper = self.latitude_upper

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if longitude_left is not UNSET:
            field_dict["longitudeLeft"] = longitude_left
        if latitude_lower is not UNSET:
            field_dict["latitudeLower"] = latitude_lower
        if longitude_right is not UNSET:
            field_dict["longitudeRight"] = longitude_right
        if latitude_upper is not UNSET:
            field_dict["latitudeUpper"] = latitude_upper

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        longitude_left = d.pop("longitudeLeft", UNSET)

        latitude_lower = d.pop("latitudeLower", UNSET)

        longitude_right = d.pop("longitudeRight", UNSET)

        latitude_upper = d.pop("latitudeUpper", UNSET)

        spherical_bounding_box = cls(
            longitude_left=longitude_left,
            latitude_lower=latitude_lower,
            longitude_right=longitude_right,
            latitude_upper=latitude_upper,
        )

        spherical_bounding_box.additional_properties = d
        return spherical_bounding_box

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
