from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.points_in_aou_search_point import PointsInAouSearchPoint


T = TypeVar("T", bound="PointsInAouSearchResult")


@_attrs_define
class PointsInAouSearchResult:
    """List of failed points, ones that aren't in bounding box

    Attributes:
        bbox_failed_points (list[PointsInAouSearchPoint] | Unset): A point that didn't land in the bounding box for area
            of use search
        max_dist_km_outside_b_box (int | Unset): Point distance with highest km outside bounding box
    """

    bbox_failed_points: list[PointsInAouSearchPoint] | Unset = UNSET
    max_dist_km_outside_b_box: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bbox_failed_points: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.bbox_failed_points, Unset):
            bbox_failed_points = []
            for bbox_failed_points_item_data in self.bbox_failed_points:
                bbox_failed_points_item = bbox_failed_points_item_data.to_dict()
                bbox_failed_points.append(bbox_failed_points_item)

        max_dist_km_outside_b_box = self.max_dist_km_outside_b_box

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bbox_failed_points is not UNSET:
            field_dict["bboxFailedPoints"] = bbox_failed_points
        if max_dist_km_outside_b_box is not UNSET:
            field_dict["maxDistKmOutsideBBox"] = max_dist_km_outside_b_box

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.points_in_aou_search_point import PointsInAouSearchPoint

        d = dict(src_dict)
        _bbox_failed_points = d.pop("bboxFailedPoints", UNSET)
        bbox_failed_points: list[PointsInAouSearchPoint] | Unset = UNSET
        if _bbox_failed_points is not UNSET:
            bbox_failed_points = []
            for bbox_failed_points_item_data in _bbox_failed_points:
                bbox_failed_points_item = PointsInAouSearchPoint.from_dict(
                    bbox_failed_points_item_data
                )

                bbox_failed_points.append(bbox_failed_points_item)

        max_dist_km_outside_b_box = d.pop("maxDistKmOutsideBBox", UNSET)

        points_in_aou_search_result = cls(
            bbox_failed_points=bbox_failed_points,
            max_dist_km_outside_b_box=max_dist_km_outside_b_box,
        )

        points_in_aou_search_result.additional_properties = d
        return points_in_aou_search_result

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
