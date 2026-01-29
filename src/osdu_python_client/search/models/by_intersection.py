from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.polygon import Polygon


T = TypeVar("T", bound="ByIntersection")


@_attrs_define
class ByIntersection:
    """
    Attributes:
        polygons (list[Polygon]):
    """

    polygons: list[Polygon]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        polygons = []
        for polygons_item_data in self.polygons:
            polygons_item = polygons_item_data.to_dict()
            polygons.append(polygons_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "polygons": polygons,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.polygon import Polygon

        d = dict(src_dict)
        polygons = []
        _polygons = d.pop("polygons")
        for polygons_item_data in _polygons:
            polygons_item = Polygon.from_dict(polygons_item_data)

            polygons.append(polygons_item)

        by_intersection = cls(
            polygons=polygons,
        )

        by_intersection.additional_properties = d
        return by_intersection

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
