from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.geo_json_feature_collection import GeoJsonFeatureCollection


T = TypeVar("T", bound="ConvertGeoJsonResponse")


@_attrs_define
class ConvertGeoJsonResponse:
    """Response of a CRS conversion/transformation operation involving GeoJSON FeatureCollection or
    AnyCrsFeatureCollection.

        Attributes:
            success_count (int | Unset): The number of coordinates in the GeoJSON FeatureCollection or
                AnyCrsFeatureCollection successfully converted/transformed. If this number is less than totalCount then
                conversion/transformation errors have occurred.
            total_count (int | Unset): The total number of coordinates in the GeoJSON FeatureCollection or
                AnyCrsFeatureCollection.
            feature_collection (GeoJsonFeatureCollection | Unset): The converted GeoJSON FeatureCollection or
                AnyCrsFeatureCollection with 'toCRS' context; length and order of the structure is the same as in the request.
                Points, which failed to convert, are returned as NaN.
            operations_applied (list[str] | Unset): The list of operations performed on the points as a list of strings
    """

    success_count: int | Unset = UNSET
    total_count: int | Unset = UNSET
    feature_collection: GeoJsonFeatureCollection | Unset = UNSET
    operations_applied: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success_count = self.success_count

        total_count = self.total_count

        feature_collection: dict[str, Any] | Unset = UNSET
        if not isinstance(self.feature_collection, Unset):
            feature_collection = self.feature_collection.to_dict()

        operations_applied: list[str] | Unset = UNSET
        if not isinstance(self.operations_applied, Unset):
            operations_applied = self.operations_applied

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if success_count is not UNSET:
            field_dict["successCount"] = success_count
        if total_count is not UNSET:
            field_dict["totalCount"] = total_count
        if feature_collection is not UNSET:
            field_dict["featureCollection"] = feature_collection
        if operations_applied is not UNSET:
            field_dict["operationsApplied"] = operations_applied

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.geo_json_feature_collection import GeoJsonFeatureCollection

        d = dict(src_dict)
        success_count = d.pop("successCount", UNSET)

        total_count = d.pop("totalCount", UNSET)

        _feature_collection = d.pop("featureCollection", UNSET)
        feature_collection: GeoJsonFeatureCollection | Unset
        if isinstance(_feature_collection, Unset):
            feature_collection = UNSET
        else:
            feature_collection = GeoJsonFeatureCollection.from_dict(_feature_collection)

        operations_applied = cast(list[str], d.pop("operationsApplied", UNSET))

        convert_geo_json_response = cls(
            success_count=success_count,
            total_count=total_count,
            feature_collection=feature_collection,
            operations_applied=operations_applied,
        )

        convert_geo_json_response.additional_properties = d
        return convert_geo_json_response

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
