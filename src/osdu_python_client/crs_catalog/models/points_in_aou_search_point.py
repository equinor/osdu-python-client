from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.point import Point


T = TypeVar("T", bound="PointsInAouSearchPoint")


@_attrs_define
class PointsInAouSearchPoint:
    """A point that didn't land in the bounding box for area of use search

    Attributes:
        point (Point | Unset): Lat, long point
        index (int | Unset): A zero-based index of the point in the input "points" array
        approximate_km_distance_outside (int | Unset): Kilometers outside the record's bounding box
    """

    point: Point | Unset = UNSET
    index: int | Unset = UNSET
    approximate_km_distance_outside: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        point: dict[str, Any] | Unset = UNSET
        if not isinstance(self.point, Unset):
            point = self.point.to_dict()

        index = self.index

        approximate_km_distance_outside = self.approximate_km_distance_outside

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if point is not UNSET:
            field_dict["point"] = point
        if index is not UNSET:
            field_dict["index"] = index
        if approximate_km_distance_outside is not UNSET:
            field_dict["approximateKmDistanceOutside"] = approximate_km_distance_outside

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.point import Point

        d = dict(src_dict)
        _point = d.pop("point", UNSET)
        point: Point | Unset
        if isinstance(_point, Unset):
            point = UNSET
        else:
            point = Point.from_dict(_point)

        index = d.pop("index", UNSET)

        approximate_km_distance_outside = d.pop("approximateKmDistanceOutside", UNSET)

        points_in_aou_search_point = cls(
            point=point,
            index=index,
            approximate_km_distance_outside=approximate_km_distance_outside,
        )

        points_in_aou_search_point.additional_properties = d
        return points_in_aou_search_point

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
