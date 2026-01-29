from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.point import Point


T = TypeVar("T", bound="ByBoundingBox")


@_attrs_define
class ByBoundingBox:
    """
    Attributes:
        top_left (Point):
        bottom_right (Point):
    """

    top_left: Point
    bottom_right: Point
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        top_left = self.top_left.to_dict()

        bottom_right = self.bottom_right.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "topLeft": top_left,
                "bottomRight": bottom_right,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.point import Point

        d = dict(src_dict)
        top_left = Point.from_dict(d.pop("topLeft"))

        bottom_right = Point.from_dict(d.pop("bottomRight"))

        by_bounding_box = cls(
            top_left=top_left,
            bottom_right=bottom_right,
        )

        by_bounding_box.additional_properties = d
        return by_bounding_box

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
