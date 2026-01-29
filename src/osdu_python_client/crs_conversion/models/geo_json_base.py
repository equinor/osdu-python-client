from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.geo_json_base_geo_json_variant_internal import (
    GeoJsonBaseGeoJsonVariantInternal,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="GeoJsonBase")


@_attrs_define
class GeoJsonBase:
    """
    Attributes:
        type_ (str):
        geo_json_variant_internal (GeoJsonBaseGeoJsonVariantInternal | Unset):
        bbox (list[float] | Unset):
    """

    type_: str
    geo_json_variant_internal: GeoJsonBaseGeoJsonVariantInternal | Unset = UNSET
    bbox: list[float] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        geo_json_variant_internal: str | Unset = UNSET
        if not isinstance(self.geo_json_variant_internal, Unset):
            geo_json_variant_internal = self.geo_json_variant_internal.value

        bbox: list[float] | Unset = UNSET
        if not isinstance(self.bbox, Unset):
            bbox = self.bbox

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
            }
        )
        if geo_json_variant_internal is not UNSET:
            field_dict["geoJsonVariantInternal"] = geo_json_variant_internal
        if bbox is not UNSET:
            field_dict["bbox"] = bbox

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = d.pop("type")

        _geo_json_variant_internal = d.pop("geoJsonVariantInternal", UNSET)
        geo_json_variant_internal: GeoJsonBaseGeoJsonVariantInternal | Unset
        if isinstance(_geo_json_variant_internal, Unset):
            geo_json_variant_internal = UNSET
        else:
            geo_json_variant_internal = GeoJsonBaseGeoJsonVariantInternal(
                _geo_json_variant_internal
            )

        bbox = cast(list[float], d.pop("bbox", UNSET))

        geo_json_base = cls(
            type_=type_,
            geo_json_variant_internal=geo_json_variant_internal,
            bbox=bbox,
        )

        geo_json_base.additional_properties = d
        return geo_json_base

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
