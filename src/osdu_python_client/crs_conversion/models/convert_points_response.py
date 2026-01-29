from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.point import Point


T = TypeVar("T", bound="ConvertPointsResponse")


@_attrs_define
class ConvertPointsResponse:
    """Response of a CRS conversion/transformation operation

    Attributes:
        success_count (int | Unset): Number of points successfully converted. If the number is less than the request
            array length conversion/transformation failures occurred.
        points (list[Point] | Unset): Converted points; length and order of the array is the same as in the request.
            Points, which failed to convert, are returned as NaN.
        operations_applied (list[str] | Unset): The list of operations performed on the points as a list of strings
    """

    success_count: int | Unset = UNSET
    points: list[Point] | Unset = UNSET
    operations_applied: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success_count = self.success_count

        points: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.points, Unset):
            points = []
            for points_item_data in self.points:
                points_item = points_item_data.to_dict()
                points.append(points_item)

        operations_applied: list[str] | Unset = UNSET
        if not isinstance(self.operations_applied, Unset):
            operations_applied = self.operations_applied

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if success_count is not UNSET:
            field_dict["successCount"] = success_count
        if points is not UNSET:
            field_dict["points"] = points
        if operations_applied is not UNSET:
            field_dict["operationsApplied"] = operations_applied

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.point import Point

        d = dict(src_dict)
        success_count = d.pop("successCount", UNSET)

        _points = d.pop("points", UNSET)
        points: list[Point] | Unset = UNSET
        if _points is not UNSET:
            points = []
            for points_item_data in _points:
                points_item = Point.from_dict(points_item_data)

                points.append(points_item)

        operations_applied = cast(list[str], d.pop("operationsApplied", UNSET))

        convert_points_response = cls(
            success_count=success_count,
            points=points,
            operations_applied=operations_applied,
        )

        convert_points_response.additional_properties = d
        return convert_points_response

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
