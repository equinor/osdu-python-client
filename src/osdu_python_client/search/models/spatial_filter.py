from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.by_bounding_box import ByBoundingBox
    from ..models.by_distance import ByDistance
    from ..models.by_geo_polygon import ByGeoPolygon
    from ..models.by_intersection import ByIntersection
    from ..models.by_within_polygon import ByWithinPolygon


T = TypeVar("T", bound="SpatialFilter")


@_attrs_define
class SpatialFilter:
    """
    Attributes:
        field (str):
        by_bounding_box (ByBoundingBox | Unset):
        by_distance (ByDistance | Unset):
        by_geo_polygon (ByGeoPolygon | Unset):
        by_intersection (ByIntersection | Unset):
        by_within_polygon (ByWithinPolygon | Unset):
    """

    field: str
    by_bounding_box: ByBoundingBox | Unset = UNSET
    by_distance: ByDistance | Unset = UNSET
    by_geo_polygon: ByGeoPolygon | Unset = UNSET
    by_intersection: ByIntersection | Unset = UNSET
    by_within_polygon: ByWithinPolygon | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field = self.field

        by_bounding_box: dict[str, Any] | Unset = UNSET
        if not isinstance(self.by_bounding_box, Unset):
            by_bounding_box = self.by_bounding_box.to_dict()

        by_distance: dict[str, Any] | Unset = UNSET
        if not isinstance(self.by_distance, Unset):
            by_distance = self.by_distance.to_dict()

        by_geo_polygon: dict[str, Any] | Unset = UNSET
        if not isinstance(self.by_geo_polygon, Unset):
            by_geo_polygon = self.by_geo_polygon.to_dict()

        by_intersection: dict[str, Any] | Unset = UNSET
        if not isinstance(self.by_intersection, Unset):
            by_intersection = self.by_intersection.to_dict()

        by_within_polygon: dict[str, Any] | Unset = UNSET
        if not isinstance(self.by_within_polygon, Unset):
            by_within_polygon = self.by_within_polygon.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "field": field,
            }
        )
        if by_bounding_box is not UNSET:
            field_dict["byBoundingBox"] = by_bounding_box
        if by_distance is not UNSET:
            field_dict["byDistance"] = by_distance
        if by_geo_polygon is not UNSET:
            field_dict["byGeoPolygon"] = by_geo_polygon
        if by_intersection is not UNSET:
            field_dict["byIntersection"] = by_intersection
        if by_within_polygon is not UNSET:
            field_dict["byWithinPolygon"] = by_within_polygon

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.by_bounding_box import ByBoundingBox
        from ..models.by_distance import ByDistance
        from ..models.by_geo_polygon import ByGeoPolygon
        from ..models.by_intersection import ByIntersection
        from ..models.by_within_polygon import ByWithinPolygon

        d = dict(src_dict)
        field = d.pop("field")

        _by_bounding_box = d.pop("byBoundingBox", UNSET)
        by_bounding_box: ByBoundingBox | Unset
        if isinstance(_by_bounding_box, Unset):
            by_bounding_box = UNSET
        else:
            by_bounding_box = ByBoundingBox.from_dict(_by_bounding_box)

        _by_distance = d.pop("byDistance", UNSET)
        by_distance: ByDistance | Unset
        if isinstance(_by_distance, Unset):
            by_distance = UNSET
        else:
            by_distance = ByDistance.from_dict(_by_distance)

        _by_geo_polygon = d.pop("byGeoPolygon", UNSET)
        by_geo_polygon: ByGeoPolygon | Unset
        if isinstance(_by_geo_polygon, Unset):
            by_geo_polygon = UNSET
        else:
            by_geo_polygon = ByGeoPolygon.from_dict(_by_geo_polygon)

        _by_intersection = d.pop("byIntersection", UNSET)
        by_intersection: ByIntersection | Unset
        if isinstance(_by_intersection, Unset):
            by_intersection = UNSET
        else:
            by_intersection = ByIntersection.from_dict(_by_intersection)

        _by_within_polygon = d.pop("byWithinPolygon", UNSET)
        by_within_polygon: ByWithinPolygon | Unset
        if isinstance(_by_within_polygon, Unset):
            by_within_polygon = UNSET
        else:
            by_within_polygon = ByWithinPolygon.from_dict(_by_within_polygon)

        spatial_filter = cls(
            field=field,
            by_bounding_box=by_bounding_box,
            by_distance=by_distance,
            by_geo_polygon=by_geo_polygon,
            by_intersection=by_intersection,
            by_within_polygon=by_within_polygon,
        )

        spatial_filter.additional_properties = d
        return spatial_filter

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
