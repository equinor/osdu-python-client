from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.point_properties import PointProperties


T = TypeVar("T", bound="PropertiesBinGridCorners")


@_attrs_define
class PropertiesBinGridCorners:
    """
    Attributes:
        kind (str | Unset):
        point_properties (list[PointProperties] | Unset):
    """

    kind: str | Unset = UNSET
    point_properties: list[PointProperties] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        kind = self.kind

        point_properties: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.point_properties, Unset):
            point_properties = []
            for point_properties_item_data in self.point_properties:
                point_properties_item = point_properties_item_data.to_dict()
                point_properties.append(point_properties_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if kind is not UNSET:
            field_dict["Kind"] = kind
        if point_properties is not UNSET:
            field_dict["PointProperties"] = point_properties

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.point_properties import PointProperties

        d = dict(src_dict)
        kind = d.pop("Kind", UNSET)

        _point_properties = d.pop("PointProperties", UNSET)
        point_properties: list[PointProperties] | Unset = UNSET
        if _point_properties is not UNSET:
            point_properties = []
            for point_properties_item_data in _point_properties:
                point_properties_item = PointProperties.from_dict(
                    point_properties_item_data
                )

                point_properties.append(point_properties_item)

        properties_bin_grid_corners = cls(
            kind=kind,
            point_properties=point_properties,
        )

        properties_bin_grid_corners.additional_properties = d
        return properties_bin_grid_corners

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
