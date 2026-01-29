from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.abstract_spatial_location import AbstractSpatialLocation


T = TypeVar("T", bound="AbstractBinGrid")


@_attrs_define
class AbstractBinGrid:
    """
    Attributes:
        bin_grid_name (str | Unset):
        bin_grid_type_id (str | Unset):
        source_bin_grid_id (int | Unset):
        source_bin_grid_app_id (str | Unset):
        coverage_percent (float | Unset):
        bin_grid_definition_method_type_id (str | Unset):
        p6_transformation_method (int | Unset):
        p6_bin_grid_origin_i (float | Unset):
        p6_bin_grid_origin_j (float | Unset):
        p6_bin_grid_origin_easting (float | Unset):
        p6_bin_grid_origin_northing (float | Unset):
        p6_scale_factor_of_bin_grid (float | Unset):
        p6_bin_width_on_iaxis (float | Unset):
        p6_bin_width_on_jaxis (float | Unset):
        p6_map_grid_bearing_of_bin_grid_jaxis (float | Unset):
        p6_bin_node_increment_on_iaxis (int | Unset):
        p6_bin_node_increment_on_jaxis (int | Unset):
        abcd_bin_grid_spatial_location (AbstractSpatialLocation | Unset):
    """

    bin_grid_name: str | Unset = UNSET
    bin_grid_type_id: str | Unset = UNSET
    source_bin_grid_id: int | Unset = UNSET
    source_bin_grid_app_id: str | Unset = UNSET
    coverage_percent: float | Unset = UNSET
    bin_grid_definition_method_type_id: str | Unset = UNSET
    p6_transformation_method: int | Unset = UNSET
    p6_bin_grid_origin_i: float | Unset = UNSET
    p6_bin_grid_origin_j: float | Unset = UNSET
    p6_bin_grid_origin_easting: float | Unset = UNSET
    p6_bin_grid_origin_northing: float | Unset = UNSET
    p6_scale_factor_of_bin_grid: float | Unset = UNSET
    p6_bin_width_on_iaxis: float | Unset = UNSET
    p6_bin_width_on_jaxis: float | Unset = UNSET
    p6_map_grid_bearing_of_bin_grid_jaxis: float | Unset = UNSET
    p6_bin_node_increment_on_iaxis: int | Unset = UNSET
    p6_bin_node_increment_on_jaxis: int | Unset = UNSET
    abcd_bin_grid_spatial_location: AbstractSpatialLocation | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bin_grid_name = self.bin_grid_name

        bin_grid_type_id = self.bin_grid_type_id

        source_bin_grid_id = self.source_bin_grid_id

        source_bin_grid_app_id = self.source_bin_grid_app_id

        coverage_percent = self.coverage_percent

        bin_grid_definition_method_type_id = self.bin_grid_definition_method_type_id

        p6_transformation_method = self.p6_transformation_method

        p6_bin_grid_origin_i = self.p6_bin_grid_origin_i

        p6_bin_grid_origin_j = self.p6_bin_grid_origin_j

        p6_bin_grid_origin_easting = self.p6_bin_grid_origin_easting

        p6_bin_grid_origin_northing = self.p6_bin_grid_origin_northing

        p6_scale_factor_of_bin_grid = self.p6_scale_factor_of_bin_grid

        p6_bin_width_on_iaxis = self.p6_bin_width_on_iaxis

        p6_bin_width_on_jaxis = self.p6_bin_width_on_jaxis

        p6_map_grid_bearing_of_bin_grid_jaxis = (
            self.p6_map_grid_bearing_of_bin_grid_jaxis
        )

        p6_bin_node_increment_on_iaxis = self.p6_bin_node_increment_on_iaxis

        p6_bin_node_increment_on_jaxis = self.p6_bin_node_increment_on_jaxis

        abcd_bin_grid_spatial_location: dict[str, Any] | Unset = UNSET
        if not isinstance(self.abcd_bin_grid_spatial_location, Unset):
            abcd_bin_grid_spatial_location = (
                self.abcd_bin_grid_spatial_location.to_dict()
            )

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bin_grid_name is not UNSET:
            field_dict["BinGridName"] = bin_grid_name
        if bin_grid_type_id is not UNSET:
            field_dict["BinGridTypeID"] = bin_grid_type_id
        if source_bin_grid_id is not UNSET:
            field_dict["SourceBinGridID"] = source_bin_grid_id
        if source_bin_grid_app_id is not UNSET:
            field_dict["SourceBinGridAppID"] = source_bin_grid_app_id
        if coverage_percent is not UNSET:
            field_dict["CoveragePercent"] = coverage_percent
        if bin_grid_definition_method_type_id is not UNSET:
            field_dict["BinGridDefinitionMethodTypeID"] = (
                bin_grid_definition_method_type_id
            )
        if p6_transformation_method is not UNSET:
            field_dict["P6TransformationMethod"] = p6_transformation_method
        if p6_bin_grid_origin_i is not UNSET:
            field_dict["P6BinGridOriginI"] = p6_bin_grid_origin_i
        if p6_bin_grid_origin_j is not UNSET:
            field_dict["P6BinGridOriginJ"] = p6_bin_grid_origin_j
        if p6_bin_grid_origin_easting is not UNSET:
            field_dict["P6BinGridOriginEasting"] = p6_bin_grid_origin_easting
        if p6_bin_grid_origin_northing is not UNSET:
            field_dict["P6BinGridOriginNorthing"] = p6_bin_grid_origin_northing
        if p6_scale_factor_of_bin_grid is not UNSET:
            field_dict["P6ScaleFactorOfBinGrid"] = p6_scale_factor_of_bin_grid
        if p6_bin_width_on_iaxis is not UNSET:
            field_dict["P6BinWidthOnIaxis"] = p6_bin_width_on_iaxis
        if p6_bin_width_on_jaxis is not UNSET:
            field_dict["P6BinWidthOnJaxis"] = p6_bin_width_on_jaxis
        if p6_map_grid_bearing_of_bin_grid_jaxis is not UNSET:
            field_dict["P6MapGridBearingOfBinGridJaxis"] = (
                p6_map_grid_bearing_of_bin_grid_jaxis
            )
        if p6_bin_node_increment_on_iaxis is not UNSET:
            field_dict["P6BinNodeIncrementOnIaxis"] = p6_bin_node_increment_on_iaxis
        if p6_bin_node_increment_on_jaxis is not UNSET:
            field_dict["P6BinNodeIncrementOnJaxis"] = p6_bin_node_increment_on_jaxis
        if abcd_bin_grid_spatial_location is not UNSET:
            field_dict["ABCDBinGridSpatialLocation"] = abcd_bin_grid_spatial_location

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.abstract_spatial_location import AbstractSpatialLocation

        d = dict(src_dict)
        bin_grid_name = d.pop("BinGridName", UNSET)

        bin_grid_type_id = d.pop("BinGridTypeID", UNSET)

        source_bin_grid_id = d.pop("SourceBinGridID", UNSET)

        source_bin_grid_app_id = d.pop("SourceBinGridAppID", UNSET)

        coverage_percent = d.pop("CoveragePercent", UNSET)

        bin_grid_definition_method_type_id = d.pop(
            "BinGridDefinitionMethodTypeID", UNSET
        )

        p6_transformation_method = d.pop("P6TransformationMethod", UNSET)

        p6_bin_grid_origin_i = d.pop("P6BinGridOriginI", UNSET)

        p6_bin_grid_origin_j = d.pop("P6BinGridOriginJ", UNSET)

        p6_bin_grid_origin_easting = d.pop("P6BinGridOriginEasting", UNSET)

        p6_bin_grid_origin_northing = d.pop("P6BinGridOriginNorthing", UNSET)

        p6_scale_factor_of_bin_grid = d.pop("P6ScaleFactorOfBinGrid", UNSET)

        p6_bin_width_on_iaxis = d.pop("P6BinWidthOnIaxis", UNSET)

        p6_bin_width_on_jaxis = d.pop("P6BinWidthOnJaxis", UNSET)

        p6_map_grid_bearing_of_bin_grid_jaxis = d.pop(
            "P6MapGridBearingOfBinGridJaxis", UNSET
        )

        p6_bin_node_increment_on_iaxis = d.pop("P6BinNodeIncrementOnIaxis", UNSET)

        p6_bin_node_increment_on_jaxis = d.pop("P6BinNodeIncrementOnJaxis", UNSET)

        _abcd_bin_grid_spatial_location = d.pop("ABCDBinGridSpatialLocation", UNSET)
        abcd_bin_grid_spatial_location: AbstractSpatialLocation | Unset
        if isinstance(_abcd_bin_grid_spatial_location, Unset):
            abcd_bin_grid_spatial_location = UNSET
        else:
            abcd_bin_grid_spatial_location = AbstractSpatialLocation.from_dict(
                _abcd_bin_grid_spatial_location
            )

        abstract_bin_grid = cls(
            bin_grid_name=bin_grid_name,
            bin_grid_type_id=bin_grid_type_id,
            source_bin_grid_id=source_bin_grid_id,
            source_bin_grid_app_id=source_bin_grid_app_id,
            coverage_percent=coverage_percent,
            bin_grid_definition_method_type_id=bin_grid_definition_method_type_id,
            p6_transformation_method=p6_transformation_method,
            p6_bin_grid_origin_i=p6_bin_grid_origin_i,
            p6_bin_grid_origin_j=p6_bin_grid_origin_j,
            p6_bin_grid_origin_easting=p6_bin_grid_origin_easting,
            p6_bin_grid_origin_northing=p6_bin_grid_origin_northing,
            p6_scale_factor_of_bin_grid=p6_scale_factor_of_bin_grid,
            p6_bin_width_on_iaxis=p6_bin_width_on_iaxis,
            p6_bin_width_on_jaxis=p6_bin_width_on_jaxis,
            p6_map_grid_bearing_of_bin_grid_jaxis=p6_map_grid_bearing_of_bin_grid_jaxis,
            p6_bin_node_increment_on_iaxis=p6_bin_node_increment_on_iaxis,
            p6_bin_node_increment_on_jaxis=p6_bin_node_increment_on_jaxis,
            abcd_bin_grid_spatial_location=abcd_bin_grid_spatial_location,
        )

        abstract_bin_grid.additional_properties = d
        return abstract_bin_grid

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
