from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.point import Point


T = TypeVar("T", bound="InPolygonQuery")


@_attrs_define
class InPolygonQuery:
    """Coordinate Transformations

    Attributes:
        record_id (str | Unset): Record of CRS or CT to check points against
        data_id (str | Unset): Searches on id for CRS records
        points (list[Point] | Unset): List of points to check against CRS or CT bounding boxes
        offset (int | Unset): Corresponds to offset on search service
        limit (int | Unset): Corresponds to limit on search service. Default is to return all found entities.
        returned_fields (list[str] | Unset):
    """

    record_id: str | Unset = UNSET
    data_id: str | Unset = UNSET
    points: list[Point] | Unset = UNSET
    offset: int | Unset = UNSET
    limit: int | Unset = UNSET
    returned_fields: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        record_id = self.record_id

        data_id = self.data_id

        points: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.points, Unset):
            points = []
            for points_item_data in self.points:
                points_item = points_item_data.to_dict()
                points.append(points_item)

        offset = self.offset

        limit = self.limit

        returned_fields: list[str] | Unset = UNSET
        if not isinstance(self.returned_fields, Unset):
            returned_fields = self.returned_fields

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if record_id is not UNSET:
            field_dict["recordId"] = record_id
        if data_id is not UNSET:
            field_dict["dataId"] = data_id
        if points is not UNSET:
            field_dict["points"] = points
        if offset is not UNSET:
            field_dict["offset"] = offset
        if limit is not UNSET:
            field_dict["limit"] = limit
        if returned_fields is not UNSET:
            field_dict["returnedFields"] = returned_fields

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.point import Point

        d = dict(src_dict)
        record_id = d.pop("recordId", UNSET)

        data_id = d.pop("dataId", UNSET)

        _points = d.pop("points", UNSET)
        points: list[Point] | Unset = UNSET
        if _points is not UNSET:
            points = []
            for points_item_data in _points:
                points_item = Point.from_dict(points_item_data)

                points.append(points_item)

        offset = d.pop("offset", UNSET)

        limit = d.pop("limit", UNSET)

        returned_fields = cast(list[str], d.pop("returnedFields", UNSET))

        in_polygon_query = cls(
            record_id=record_id,
            data_id=data_id,
            points=points,
            offset=offset,
            limit=limit,
            returned_fields=returned_fields,
        )

        in_polygon_query.additional_properties = d
        return in_polygon_query

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
