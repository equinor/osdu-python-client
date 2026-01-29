from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.geo_json_feature_collection_geo_json_variant_internal import (
    GeoJsonFeatureCollectionGeoJsonVariantInternal,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.geo_json_feature import GeoJsonFeature
    from ..models.geo_json_feature_collection_properties import (
        GeoJsonFeatureCollectionProperties,
    )


T = TypeVar("T", bound="GeoJsonFeatureCollection")


@_attrs_define
class GeoJsonFeatureCollection:
    """The converted GeoJSON FeatureCollection or AnyCrsFeatureCollection with 'toCRS' context; length and order of the
    structure is the same as in the request. Points, which failed to convert, are returned as NaN.

        Attributes:
            type_ (str):
            features (list[GeoJsonFeature]):
            geo_json_variant_internal (GeoJsonFeatureCollectionGeoJsonVariantInternal | Unset):
            bbox (list[float] | Unset):
            properties (GeoJsonFeatureCollectionProperties | Unset):
            persistable_reference_crs (str | Unset):
            coordinate_reference_system_id (str | Unset):
            vertical_unit_id (str | Unset):
            persistable_reference_unit_z (str | Unset):
    """

    type_: str
    features: list[GeoJsonFeature]
    geo_json_variant_internal: (
        GeoJsonFeatureCollectionGeoJsonVariantInternal | Unset
    ) = UNSET
    bbox: list[float] | Unset = UNSET
    properties: GeoJsonFeatureCollectionProperties | Unset = UNSET
    persistable_reference_crs: str | Unset = UNSET
    coordinate_reference_system_id: str | Unset = UNSET
    vertical_unit_id: str | Unset = UNSET
    persistable_reference_unit_z: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        features = []
        for features_item_data in self.features:
            features_item = features_item_data.to_dict()
            features.append(features_item)

        geo_json_variant_internal: str | Unset = UNSET
        if not isinstance(self.geo_json_variant_internal, Unset):
            geo_json_variant_internal = self.geo_json_variant_internal.value

        bbox: list[float] | Unset = UNSET
        if not isinstance(self.bbox, Unset):
            bbox = self.bbox

        properties: dict[str, Any] | Unset = UNSET
        if not isinstance(self.properties, Unset):
            properties = self.properties.to_dict()

        persistable_reference_crs = self.persistable_reference_crs

        coordinate_reference_system_id = self.coordinate_reference_system_id

        vertical_unit_id = self.vertical_unit_id

        persistable_reference_unit_z = self.persistable_reference_unit_z

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "features": features,
            }
        )
        if geo_json_variant_internal is not UNSET:
            field_dict["geoJsonVariantInternal"] = geo_json_variant_internal
        if bbox is not UNSET:
            field_dict["bbox"] = bbox
        if properties is not UNSET:
            field_dict["properties"] = properties
        if persistable_reference_crs is not UNSET:
            field_dict["persistableReferenceCrs"] = persistable_reference_crs
        if coordinate_reference_system_id is not UNSET:
            field_dict["CoordinateReferenceSystemID"] = coordinate_reference_system_id
        if vertical_unit_id is not UNSET:
            field_dict["VerticalUnitID"] = vertical_unit_id
        if persistable_reference_unit_z is not UNSET:
            field_dict["persistableReferenceUnitZ"] = persistable_reference_unit_z

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.geo_json_feature import GeoJsonFeature
        from ..models.geo_json_feature_collection_properties import (
            GeoJsonFeatureCollectionProperties,
        )

        d = dict(src_dict)
        type_ = d.pop("type")

        features = []
        _features = d.pop("features")
        for features_item_data in _features:
            features_item = GeoJsonFeature.from_dict(features_item_data)

            features.append(features_item)

        _geo_json_variant_internal = d.pop("geoJsonVariantInternal", UNSET)
        geo_json_variant_internal: (
            GeoJsonFeatureCollectionGeoJsonVariantInternal | Unset
        )
        if isinstance(_geo_json_variant_internal, Unset):
            geo_json_variant_internal = UNSET
        else:
            geo_json_variant_internal = GeoJsonFeatureCollectionGeoJsonVariantInternal(
                _geo_json_variant_internal
            )

        bbox = cast(list[float], d.pop("bbox", UNSET))

        _properties = d.pop("properties", UNSET)
        properties: GeoJsonFeatureCollectionProperties | Unset
        if isinstance(_properties, Unset):
            properties = UNSET
        else:
            properties = GeoJsonFeatureCollectionProperties.from_dict(_properties)

        persistable_reference_crs = d.pop("persistableReferenceCrs", UNSET)

        coordinate_reference_system_id = d.pop("CoordinateReferenceSystemID", UNSET)

        vertical_unit_id = d.pop("VerticalUnitID", UNSET)

        persistable_reference_unit_z = d.pop("persistableReferenceUnitZ", UNSET)

        geo_json_feature_collection = cls(
            type_=type_,
            features=features,
            geo_json_variant_internal=geo_json_variant_internal,
            bbox=bbox,
            properties=properties,
            persistable_reference_crs=persistable_reference_crs,
            coordinate_reference_system_id=coordinate_reference_system_id,
            vertical_unit_id=vertical_unit_id,
            persistable_reference_unit_z=persistable_reference_unit_z,
        )

        geo_json_feature_collection.additional_properties = d
        return geo_json_feature_collection

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
