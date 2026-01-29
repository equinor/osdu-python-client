from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.abstract_any_crs_feature_collection import (
        AbstractAnyCrsFeatureCollection,
    )
    from ..models.abstract_feature_collection import AbstractFeatureCollection


T = TypeVar("T", bound="AbstractSpatialLocation")


@_attrs_define
class AbstractSpatialLocation:
    """
    Attributes:
        spatial_location_coordinates_date (str | Unset):
        quantitative_accuracy_band_id (str | Unset):
        qualitative_spatial_accuracy_type_id (str | Unset):
        coordinate_quality_check_performed_by (str | Unset):
        coordinate_quality_check_date_time (str | Unset):
        coordinate_quality_check_remarks (list[str] | Unset):
        applied_operations (list[str] | Unset):
        spatial_parameter_type_id (str | Unset):
        spatial_geometry_type_id (str | Unset):
        as_ingested_coordinates (AbstractAnyCrsFeatureCollection | Unset):
        wgs_84_coordinates (AbstractFeatureCollection | Unset):
    """

    spatial_location_coordinates_date: str | Unset = UNSET
    quantitative_accuracy_band_id: str | Unset = UNSET
    qualitative_spatial_accuracy_type_id: str | Unset = UNSET
    coordinate_quality_check_performed_by: str | Unset = UNSET
    coordinate_quality_check_date_time: str | Unset = UNSET
    coordinate_quality_check_remarks: list[str] | Unset = UNSET
    applied_operations: list[str] | Unset = UNSET
    spatial_parameter_type_id: str | Unset = UNSET
    spatial_geometry_type_id: str | Unset = UNSET
    as_ingested_coordinates: AbstractAnyCrsFeatureCollection | Unset = UNSET
    wgs_84_coordinates: AbstractFeatureCollection | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        spatial_location_coordinates_date = self.spatial_location_coordinates_date

        quantitative_accuracy_band_id = self.quantitative_accuracy_band_id

        qualitative_spatial_accuracy_type_id = self.qualitative_spatial_accuracy_type_id

        coordinate_quality_check_performed_by = (
            self.coordinate_quality_check_performed_by
        )

        coordinate_quality_check_date_time = self.coordinate_quality_check_date_time

        coordinate_quality_check_remarks: list[str] | Unset = UNSET
        if not isinstance(self.coordinate_quality_check_remarks, Unset):
            coordinate_quality_check_remarks = self.coordinate_quality_check_remarks

        applied_operations: list[str] | Unset = UNSET
        if not isinstance(self.applied_operations, Unset):
            applied_operations = self.applied_operations

        spatial_parameter_type_id = self.spatial_parameter_type_id

        spatial_geometry_type_id = self.spatial_geometry_type_id

        as_ingested_coordinates: dict[str, Any] | Unset = UNSET
        if not isinstance(self.as_ingested_coordinates, Unset):
            as_ingested_coordinates = self.as_ingested_coordinates.to_dict()

        wgs_84_coordinates: dict[str, Any] | Unset = UNSET
        if not isinstance(self.wgs_84_coordinates, Unset):
            wgs_84_coordinates = self.wgs_84_coordinates.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if spatial_location_coordinates_date is not UNSET:
            field_dict["SpatialLocationCoordinatesDate"] = (
                spatial_location_coordinates_date
            )
        if quantitative_accuracy_band_id is not UNSET:
            field_dict["QuantitativeAccuracyBandID"] = quantitative_accuracy_band_id
        if qualitative_spatial_accuracy_type_id is not UNSET:
            field_dict["QualitativeSpatialAccuracyTypeID"] = (
                qualitative_spatial_accuracy_type_id
            )
        if coordinate_quality_check_performed_by is not UNSET:
            field_dict["CoordinateQualityCheckPerformedBy"] = (
                coordinate_quality_check_performed_by
            )
        if coordinate_quality_check_date_time is not UNSET:
            field_dict["CoordinateQualityCheckDateTime"] = (
                coordinate_quality_check_date_time
            )
        if coordinate_quality_check_remarks is not UNSET:
            field_dict["CoordinateQualityCheckRemarks"] = (
                coordinate_quality_check_remarks
            )
        if applied_operations is not UNSET:
            field_dict["AppliedOperations"] = applied_operations
        if spatial_parameter_type_id is not UNSET:
            field_dict["SpatialParameterTypeID"] = spatial_parameter_type_id
        if spatial_geometry_type_id is not UNSET:
            field_dict["SpatialGeometryTypeID"] = spatial_geometry_type_id
        if as_ingested_coordinates is not UNSET:
            field_dict["AsIngestedCoordinates"] = as_ingested_coordinates
        if wgs_84_coordinates is not UNSET:
            field_dict["Wgs84Coordinates"] = wgs_84_coordinates

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.abstract_any_crs_feature_collection import (
            AbstractAnyCrsFeatureCollection,
        )
        from ..models.abstract_feature_collection import AbstractFeatureCollection

        d = dict(src_dict)
        spatial_location_coordinates_date = d.pop(
            "SpatialLocationCoordinatesDate", UNSET
        )

        quantitative_accuracy_band_id = d.pop("QuantitativeAccuracyBandID", UNSET)

        qualitative_spatial_accuracy_type_id = d.pop(
            "QualitativeSpatialAccuracyTypeID", UNSET
        )

        coordinate_quality_check_performed_by = d.pop(
            "CoordinateQualityCheckPerformedBy", UNSET
        )

        coordinate_quality_check_date_time = d.pop(
            "CoordinateQualityCheckDateTime", UNSET
        )

        coordinate_quality_check_remarks = cast(
            list[str], d.pop("CoordinateQualityCheckRemarks", UNSET)
        )

        applied_operations = cast(list[str], d.pop("AppliedOperations", UNSET))

        spatial_parameter_type_id = d.pop("SpatialParameterTypeID", UNSET)

        spatial_geometry_type_id = d.pop("SpatialGeometryTypeID", UNSET)

        _as_ingested_coordinates = d.pop("AsIngestedCoordinates", UNSET)
        as_ingested_coordinates: AbstractAnyCrsFeatureCollection | Unset
        if isinstance(_as_ingested_coordinates, Unset):
            as_ingested_coordinates = UNSET
        else:
            as_ingested_coordinates = AbstractAnyCrsFeatureCollection.from_dict(
                _as_ingested_coordinates
            )

        _wgs_84_coordinates = d.pop("Wgs84Coordinates", UNSET)
        wgs_84_coordinates: AbstractFeatureCollection | Unset
        if isinstance(_wgs_84_coordinates, Unset):
            wgs_84_coordinates = UNSET
        else:
            wgs_84_coordinates = AbstractFeatureCollection.from_dict(
                _wgs_84_coordinates
            )

        abstract_spatial_location = cls(
            spatial_location_coordinates_date=spatial_location_coordinates_date,
            quantitative_accuracy_band_id=quantitative_accuracy_band_id,
            qualitative_spatial_accuracy_type_id=qualitative_spatial_accuracy_type_id,
            coordinate_quality_check_performed_by=coordinate_quality_check_performed_by,
            coordinate_quality_check_date_time=coordinate_quality_check_date_time,
            coordinate_quality_check_remarks=coordinate_quality_check_remarks,
            applied_operations=applied_operations,
            spatial_parameter_type_id=spatial_parameter_type_id,
            spatial_geometry_type_id=spatial_geometry_type_id,
            as_ingested_coordinates=as_ingested_coordinates,
            wgs_84_coordinates=wgs_84_coordinates,
        )

        abstract_spatial_location.additional_properties = d
        return abstract_spatial_location

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
