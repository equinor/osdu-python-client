from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.minimum_depth_interval import MinimumDepthInterval
    from ..models.point import Point
    from ..models.trajectory_station_in_v4 import TrajectoryStationInV4


T = TypeVar("T", bound="ConvertTrajectoryRequestV4")


@_attrs_define
class ConvertTrajectoryRequestV4:
    r"""
    Attributes:
        trajectory_crs (str): Coordinate reference system for the reference point; typically the CRS is a projected CRS;
            if a geographic CRS is provided, the unitXY must be defined and the azimuthReference must be TRUE_NORTH.
            Example: "{"wkt":"PROJCS[\"WGS_1984_UTM_Zone_31N\",GEOGCS[\"GCS_WGS_1984\",DATUM[\"D_WGS_1984\",SPHEROID[\"WGS_1
            984\",6378137.0,298.257223563]],PRIMEM[\"Greenwich\",0.0],UNIT[\"Degree\",0.0174532925199433]],PROJECTION[\"Tran
            sverse_Mercator\"],PARAMETER[\"False_Easting\",500000.0],PARAMETER[\"False_Northing\",0.0],PARAMETER[\"Central_M
            eridian\",3.0],PARAMETER[\"Scale_Factor\",0.9996],PARAMETER[\"Latitude_Of_Origin\",0.0],UNIT[\"Meter\",1.0],AUTH
            ORITY[\"EPSG\",32631]]","ver":"PE_10_3_1","name":"WGS_1984_UTM_Zone_31N","authCode":{"auth":"EPSG","code":"32631
            "},"type":"LBC"}".
        unit_z (str): The vertical unit of the dz in the input trajectory stations; the unit must be a length unit in
            'persistable model' format, see example. Example: "{"scaleOffset":{"scale":1.0,"offset":0.0},"symbol":"m","baseM
            easurement":{"ancestry":"Length","type":"UM"},"type":"USO"}".
        input_stations (list[TrajectoryStationInV4]): The array of input trajectory stations
        method (str): The computation method - 'AzimuthalEquidistant' (default) or 'LMP' (Lee's modified proposal
            SPE96813) Example: AzimuthalEquidistant.
        azimuth_reference (str | Unset): azimuth reference for the input trajectory station azimuth values (TRUE_NORTH
            or GridNorth) Example: TRUE_NORTH.
        unit_xy (str | Unset): The horizontal unit of the dx, dy in the input trajectory stations; the unit must be a
            length unit in 'persistable model' format, see example. Example: "{"scaleOffset":{"scale":1.0,"offset":0.0},"sym
            bol":"m","baseMeasurement":{"ancestry":"Length","type":"UM"},"type":"USO"}".
        reference_point (Point | Unset): Point representation for CRS operations
        input_kind (str | Unset): The kind of input; one of MD_Inclination_Azimuth (default), MD_X_Y_Z, MD_dX_dY_dZ,
            X_Y_Z, dX_dY_dZ. MD stands for measured depth; MD_X_Y_Z/X_Y_Z stand for absolute coordinates in the reference
            CRS, MD_dX_dY_dZ/dX_dY_dZ stand for deviations relative to the reference point. Example: MD_Inclination_Azimuth.
        interpolate (bool | Unset): Perform trajectory interpolation on demand; default is true. Example: True.
        md_i (MinimumDepthInterval | Unset): Minimum depth interval record; context is provided by the container.
        unit_md (str | Unset):
    """

    trajectory_crs: str
    unit_z: str
    input_stations: list[TrajectoryStationInV4]
    method: str
    azimuth_reference: str | Unset = UNSET
    unit_xy: str | Unset = UNSET
    reference_point: Point | Unset = UNSET
    input_kind: str | Unset = UNSET
    interpolate: bool | Unset = UNSET
    md_i: MinimumDepthInterval | Unset = UNSET
    unit_md: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        trajectory_crs = self.trajectory_crs

        unit_z = self.unit_z

        input_stations = []
        for input_stations_item_data in self.input_stations:
            input_stations_item = input_stations_item_data.to_dict()
            input_stations.append(input_stations_item)

        method = self.method

        azimuth_reference = self.azimuth_reference

        unit_xy = self.unit_xy

        reference_point: dict[str, Any] | Unset = UNSET
        if not isinstance(self.reference_point, Unset):
            reference_point = self.reference_point.to_dict()

        input_kind = self.input_kind

        interpolate = self.interpolate

        md_i: dict[str, Any] | Unset = UNSET
        if not isinstance(self.md_i, Unset):
            md_i = self.md_i.to_dict()

        unit_md = self.unit_md

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "trajectoryCRS": trajectory_crs,
                "unitZ": unit_z,
                "inputStations": input_stations,
                "method": method,
            }
        )
        if azimuth_reference is not UNSET:
            field_dict["azimuthReference"] = azimuth_reference
        if unit_xy is not UNSET:
            field_dict["unitXY"] = unit_xy
        if reference_point is not UNSET:
            field_dict["referencePoint"] = reference_point
        if input_kind is not UNSET:
            field_dict["inputKind"] = input_kind
        if interpolate is not UNSET:
            field_dict["interpolate"] = interpolate
        if md_i is not UNSET:
            field_dict["MD_i"] = md_i
        if unit_md is not UNSET:
            field_dict["unitMD"] = unit_md

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.minimum_depth_interval import MinimumDepthInterval
        from ..models.point import Point
        from ..models.trajectory_station_in_v4 import TrajectoryStationInV4

        d = dict(src_dict)
        trajectory_crs = d.pop("trajectoryCRS")

        unit_z = d.pop("unitZ")

        input_stations = []
        _input_stations = d.pop("inputStations")
        for input_stations_item_data in _input_stations:
            input_stations_item = TrajectoryStationInV4.from_dict(
                input_stations_item_data
            )

            input_stations.append(input_stations_item)

        method = d.pop("method")

        azimuth_reference = d.pop("azimuthReference", UNSET)

        unit_xy = d.pop("unitXY", UNSET)

        _reference_point = d.pop("referencePoint", UNSET)
        reference_point: Point | Unset
        if isinstance(_reference_point, Unset):
            reference_point = UNSET
        else:
            reference_point = Point.from_dict(_reference_point)

        input_kind = d.pop("inputKind", UNSET)

        interpolate = d.pop("interpolate", UNSET)

        _md_i = d.pop("MD_i", UNSET)
        md_i: MinimumDepthInterval | Unset
        if isinstance(_md_i, Unset):
            md_i = UNSET
        else:
            md_i = MinimumDepthInterval.from_dict(_md_i)

        unit_md = d.pop("unitMD", UNSET)

        convert_trajectory_request_v4 = cls(
            trajectory_crs=trajectory_crs,
            unit_z=unit_z,
            input_stations=input_stations,
            method=method,
            azimuth_reference=azimuth_reference,
            unit_xy=unit_xy,
            reference_point=reference_point,
            input_kind=input_kind,
            interpolate=interpolate,
            md_i=md_i,
            unit_md=unit_md,
        )

        convert_trajectory_request_v4.additional_properties = d
        return convert_trajectory_request_v4

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
