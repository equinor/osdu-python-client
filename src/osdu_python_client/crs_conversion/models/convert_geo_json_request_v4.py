from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.geo_json_feature_collection import GeoJsonFeatureCollection


T = TypeVar("T", bound="ConvertGeoJsonRequestV4")


@_attrs_define
class ConvertGeoJsonRequestV4:
    r""" Request to convert a GeoJSON FeatureCollection or AnyCrsFeatureCollection from WGS 84 or
    'AnyCrsFeatureCollection.persistableReferenceCrs to a target CRS.' to a target CRS

        Attributes:
            to_crs (str): Target CRS as persistable reference string Example: "{"authCode":{"auth":"EPSG","code":"4326"},"na
                me":"GCS_WGS_1984","type":"LBC","ver":"PE_10_3_1","wkt":"GEOGCS[\"GCS_WGS_1984\",DATUM[\"D_WGS_1984\",SPHEROID[\
                "WGS_1984\",6378137.0,298.257223563]],PRIMEM[\"Greenwich\",0.0],UNIT[\"Degree\",0.0174532925199433],AUTHORITY[\"
                EPSG\",4326]]"}".
            feature_collection (GeoJsonFeatureCollection): The converted GeoJSON FeatureCollection or
                AnyCrsFeatureCollection with 'toCRS' context; length and order of the structure is the same as in the request.
                Points, which failed to convert, are returned as NaN.
            to_unit_z (str | Unset): Optional: the target Z-unit for the z-axis scaling. Example: "{"baseMeasurement":{"ance
                stry":"Length","type":"UM"},"scaleOffset":{"offset":0.0,"scale":1.0},"symbol":"m","type":"USO"}".
            transformation (str | Unset): Explicit Transformation as persistable reference string or record id, its optional
                and if given it will override Bound Transformation  Example: osdu:reference-data--
                CoordinateTransformation:EPSG::15851:.
     """

    to_crs: str
    feature_collection: GeoJsonFeatureCollection
    to_unit_z: str | Unset = UNSET
    transformation: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        to_crs = self.to_crs

        feature_collection = self.feature_collection.to_dict()

        to_unit_z = self.to_unit_z

        transformation = self.transformation

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "toCRS": to_crs,
                "featureCollection": feature_collection,
            }
        )
        if to_unit_z is not UNSET:
            field_dict["toUnitZ"] = to_unit_z
        if transformation is not UNSET:
            field_dict["transformation"] = transformation

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.geo_json_feature_collection import GeoJsonFeatureCollection

        d = dict(src_dict)
        to_crs = d.pop("toCRS")

        feature_collection = GeoJsonFeatureCollection.from_dict(
            d.pop("featureCollection")
        )

        to_unit_z = d.pop("toUnitZ", UNSET)

        transformation = d.pop("transformation", UNSET)

        convert_geo_json_request_v4 = cls(
            to_crs=to_crs,
            feature_collection=feature_collection,
            to_unit_z=to_unit_z,
            transformation=transformation,
        )

        convert_geo_json_request_v4.additional_properties = d
        return convert_geo_json_request_v4

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
