from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.geometry import Geometry
    from ..models.properties_bin_grid_corners import PropertiesBinGridCorners


T = TypeVar("T", bound="AbstractFeature")


@_attrs_define
class AbstractFeature:
    """
    Attributes:
        type_ (str | Unset):
        properties (PropertiesBinGridCorners | Unset):
        geometry (Geometry | Unset):
    """

    type_: str | Unset = UNSET
    properties: PropertiesBinGridCorners | Unset = UNSET
    geometry: Geometry | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        properties: dict[str, Any] | Unset = UNSET
        if not isinstance(self.properties, Unset):
            properties = self.properties.to_dict()

        geometry: dict[str, Any] | Unset = UNSET
        if not isinstance(self.geometry, Unset):
            geometry = self.geometry.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if properties is not UNSET:
            field_dict["properties"] = properties
        if geometry is not UNSET:
            field_dict["geometry"] = geometry

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.geometry import Geometry
        from ..models.properties_bin_grid_corners import PropertiesBinGridCorners

        d = dict(src_dict)
        type_ = d.pop("type", UNSET)

        _properties = d.pop("properties", UNSET)
        properties: PropertiesBinGridCorners | Unset
        if isinstance(_properties, Unset):
            properties = UNSET
        else:
            properties = PropertiesBinGridCorners.from_dict(_properties)

        _geometry = d.pop("geometry", UNSET)
        geometry: Geometry | Unset
        if isinstance(_geometry, Unset):
            geometry = UNSET
        else:
            geometry = Geometry.from_dict(_geometry)

        abstract_feature = cls(
            type_=type_,
            properties=properties,
            geometry=geometry,
        )

        abstract_feature.additional_properties = d
        return abstract_feature

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
