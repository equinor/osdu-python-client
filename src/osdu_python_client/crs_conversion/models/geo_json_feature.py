from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.geo_json_feature_geo_json_variant_internal import (
    GeoJsonFeatureGeoJsonVariantInternal,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.geo_json_base import GeoJsonBase
    from ..models.geo_json_feature_properties import GeoJsonFeatureProperties


T = TypeVar("T", bound="GeoJsonFeature")


@_attrs_define
class GeoJsonFeature:
    """
    Attributes:
        type_ (str):
        geometry (GeoJsonBase):
        geo_json_variant_internal (GeoJsonFeatureGeoJsonVariantInternal | Unset):
        bbox (list[float] | Unset):
        properties (GeoJsonFeatureProperties | Unset):
    """

    type_: str
    geometry: GeoJsonBase
    geo_json_variant_internal: GeoJsonFeatureGeoJsonVariantInternal | Unset = UNSET
    bbox: list[float] | Unset = UNSET
    properties: GeoJsonFeatureProperties | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        geometry = self.geometry.to_dict()

        geo_json_variant_internal: str | Unset = UNSET
        if not isinstance(self.geo_json_variant_internal, Unset):
            geo_json_variant_internal = self.geo_json_variant_internal.value

        bbox: list[float] | Unset = UNSET
        if not isinstance(self.bbox, Unset):
            bbox = self.bbox

        properties: dict[str, Any] | Unset = UNSET
        if not isinstance(self.properties, Unset):
            properties = self.properties.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "geometry": geometry,
            }
        )
        if geo_json_variant_internal is not UNSET:
            field_dict["geoJsonVariantInternal"] = geo_json_variant_internal
        if bbox is not UNSET:
            field_dict["bbox"] = bbox
        if properties is not UNSET:
            field_dict["properties"] = properties

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.geo_json_base import GeoJsonBase
        from ..models.geo_json_feature_properties import GeoJsonFeatureProperties

        d = dict(src_dict)
        type_ = d.pop("type")

        geometry = GeoJsonBase.from_dict(d.pop("geometry"))

        _geo_json_variant_internal = d.pop("geoJsonVariantInternal", UNSET)
        geo_json_variant_internal: GeoJsonFeatureGeoJsonVariantInternal | Unset
        if isinstance(_geo_json_variant_internal, Unset):
            geo_json_variant_internal = UNSET
        else:
            geo_json_variant_internal = GeoJsonFeatureGeoJsonVariantInternal(
                _geo_json_variant_internal
            )

        bbox = cast(list[float], d.pop("bbox", UNSET))

        _properties = d.pop("properties", UNSET)
        properties: GeoJsonFeatureProperties | Unset
        if isinstance(_properties, Unset):
            properties = UNSET
        else:
            properties = GeoJsonFeatureProperties.from_dict(_properties)

        geo_json_feature = cls(
            type_=type_,
            geometry=geometry,
            geo_json_variant_internal=geo_json_variant_internal,
            bbox=bbox,
            properties=properties,
        )

        geo_json_feature.additional_properties = d
        return geo_json_feature

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
