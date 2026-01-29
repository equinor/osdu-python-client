from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.scale_convergence import ScaleConvergence
    from ..models.trajectory_station_out import TrajectoryStationOut


T = TypeVar("T", bound="ConvertTrajectoryResponseV4")


@_attrs_define
class ConvertTrajectoryResponseV4:
    r""" Trajectory response data structure; contains the context (crs, units).

        Attributes:
            trajectory_crs (str): Coordinate reference system for the reference point; typically the CRS is a projected CRS;
                if a geographic CRS is provided, the unitXY must be defined and the azimuthReference must be TRUE_NORTH.
                Example: {"authCode":{"auth":"SLB","code":"30200002"},"lateBoundCRS":{"authCode":{"auth":"EPSG","code":"30200"},
                "name":"Trinidad_1903_Trinidad_Grid","type":"LBC","ver":"PE_10_3_1","wkt":"PROJCS[\"Trinidad_1903_Trinidad_Grid\
                ",GEOGCS[\"GCS_Trinidad_1903\",DATUM[\"D_Trinidad_1903\",SPHEROID[\"Clarke_1858\",6378293.64520876,294.260676369
                ]],PRIMEM[\"Greenwich\",0.0],UNIT[\"Degree\",0.0174532925199433]],PROJECTION[\"Cassini\"],PARAMETER[\"False_East
                ing\",430000.0],PARAMETER[\"False_Northing\",325000.0],PARAMETER[\"Central_Meridian\",-
                61.3333333333333],PARAMETER[\"Scale_Factor\",1.0],PARAMETER[\"Latitude_Of_Origin\",10.4416666666667],UNIT[\"Link
                _Clarke\",0.201166195164],AUTHORITY[\"EPSG\",30200]]"},"name":"Trinidad 1903 * EOG-Tto Trin / Trinidad Grid [302
                00,10085]","singleCT":{"authCode":{"auth":"EPSG","code":"10085"},"name":"Trinidad_1903_To_WGS_1984_2","type":"ST
                ","ver":"PE_10_3_1","wkt":"GEOGTRAN[\"Trinidad_1903_To_WGS_1984_2\",GEOGCS[\"GCS_Trinidad_1903\",DATUM[\"D_Trini
                dad_1903\",SPHEROID[\"Clarke_1858\",6378293.64520876,294.260676369]],PRIMEM[\"Greenwich\",0.0],UNIT[\"Degree\",0
                .0174532925199433]],GEOGCS[\"GCS_WGS_1984\",DATUM[\"D_WGS_1984\",SPHEROID[\"WGS_1984\",6378137.0,298.257223563]]
                ,PRIMEM[\"Greenwich\",0.0],UNIT[\"Degree\",0.0174532925199433]],METHOD[\"Geocentric_Translation\"],PARAMETER[\"X
                _Axis_Translation\",-
                61.0],PARAMETER[\"Y_Axis_Translation\",285.2],PARAMETER[\"Z_Axis_Translation\",471.6],AUTHORITY[\"EPSG\",10085]]
                "},"type":"EBC","ver":"PE_10_3_1"}.
            unit_xy (str): The horizontal unit of the dx, dy in the output trajectory stations. Example: {"scaleOffset":{"sc
                ale":1.0,"offset":0.0},"symbol":"m","baseMeasurement":{"ancestry":"Length","type":"UM"},"type":"USO"}.
            unit_z (str): The vertical unit of the dz in the output trajectory stations. Example: {"scaleOffset":{"scale":1.
                0,"offset":0.0},"symbol":"m","baseMeasurement":{"ancestry":"Length","type":"UM"},"type":"USO"}.
            unit_dls (str): The unit of the dog leg severity (DLS) in the output trajectory stations. Example: %7B%22ScaleOf
                fset%22%3A%7B%22Scale%22%3A5.72614583987641E-
                4%2C%22Offset%22%3A0.0%7D%2C%22Symbol%22%3A%22deg%2F100ft%22%2C%22BaseMeasurement%22%3A%22%257B%2522Ancestry%252
                2%253A%2522Rotation_Per_Length%2522%257D%22%7D.
            stations (list[TrajectoryStationOut]): Computed trajectory stations.
            local_crs (str): Coordinate Reference System for the local, True North oriented, true distance, engineering CRS
                with origin at the well's surface location. Example: {"authCode":{"auth":"SLB","code":"30200002"},"lateBoundCRS"
                :{"authCode":{"auth":"EPSG","code":"30200"},"name":"Trinidad_1903_Trinidad_Grid","type":"LBC","ver":"PE_10_3_1",
                "wkt":"PROJCS[\"Trinidad_1903_Trinidad_Grid\",GEOGCS[\"GCS_Trinidad_1903\",DATUM[\"D_Trinidad_1903\",SPHEROID[\"
                Clarke_1858\",6378293.64520876,294.260676369]],PRIMEM[\"Greenwich\",0.0],UNIT[\"Degree\",0.0174532925199433]],PR
                OJECTION[\"Cassini\"],PARAMETER[\"False_Easting\",430000.0],PARAMETER[\"False_Northing\",325000.0],PARAMETER[\"C
                entral_Meridian\",-
                61.3333333333333],PARAMETER[\"Scale_Factor\",1.0],PARAMETER[\"Latitude_Of_Origin\",10.4416666666667],UNIT[\"Link
                _Clarke\",0.201166195164],AUTHORITY[\"EPSG\",30200]]"},"name":"Trinidad 1903 * EOG-Tto Trin / Trinidad Grid [302
                00,10085]","singleCT":{"authCode":{"auth":"EPSG","code":"10085"},"name":"Trinidad_1903_To_WGS_1984_2","type":"ST
                ","ver":"PE_10_3_1","wkt":"GEOGTRAN[\"Trinidad_1903_To_WGS_1984_2\",GEOGCS[\"GCS_Trinidad_1903\",DATUM[\"D_Trini
                dad_1903\",SPHEROID[\"Clarke_1858\",6378293.64520876,294.260676369]],PRIMEM[\"Greenwich\",0.0],UNIT[\"Degree\",0
                .0174532925199433]],GEOGCS[\"GCS_WGS_1984\",DATUM[\"D_WGS_1984\",SPHEROID[\"WGS_1984\",6378137.0,298.257223563]]
                ,PRIMEM[\"Greenwich\",0.0],UNIT[\"Degree\",0.0174532925199433]],METHOD[\"Geocentric_Translation\"],PARAMETER[\"X
                _Axis_Translation\",-
                61.0],PARAMETER[\"Y_Axis_Translation\",285.2],PARAMETER[\"Z_Axis_Translation\",471.6],AUTHORITY[\"EPSG\",10085]]
                "},"type":"EBC","ver":"PE_10_3_1"}.
            method (str): The computation method used - 'AzimuthalEquidistant' (default) or 'LMP' (Lee's modified proposal
                SPE96813). Example: AzimuthalEquidistant.
            unit_md (str | Unset): unitMD
            operations_applied (list[str] | Unset): The list of operations performed on the points as a list of strings
            stations_i (list[TrajectoryStationOut] | Unset): Computed trajectory stations i.
            scale_convergence_list (list[ScaleConvergence] | Unset): scaleConvergence
            input_kind (str | Unset): The kind of input; one of MD_Inclination_Azimuth (default), MD_X_Y_Z, MD_dX_dY_dZ,
                X_Y_Z, dX_dY_dZ. MD stands for measured depth; MD_X_Y_Z/X_Y_Z stand for absolute coordinates in the reference
                CRS, MD_dX_dY_dZ/dX_dY_dZ stand for deviations relative to the reference point. Example: MD_Inclination_Azimuth.
     """

    trajectory_crs: str
    unit_xy: str
    unit_z: str
    unit_dls: str
    stations: list[TrajectoryStationOut]
    local_crs: str
    method: str
    unit_md: str | Unset = UNSET
    operations_applied: list[str] | Unset = UNSET
    stations_i: list[TrajectoryStationOut] | Unset = UNSET
    scale_convergence_list: list[ScaleConvergence] | Unset = UNSET
    input_kind: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        trajectory_crs = self.trajectory_crs

        unit_xy = self.unit_xy

        unit_z = self.unit_z

        unit_dls = self.unit_dls

        stations = []
        for stations_item_data in self.stations:
            stations_item = stations_item_data.to_dict()
            stations.append(stations_item)

        local_crs = self.local_crs

        method = self.method

        unit_md = self.unit_md

        operations_applied: list[str] | Unset = UNSET
        if not isinstance(self.operations_applied, Unset):
            operations_applied = self.operations_applied

        stations_i: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.stations_i, Unset):
            stations_i = []
            for stations_i_item_data in self.stations_i:
                stations_i_item = stations_i_item_data.to_dict()
                stations_i.append(stations_i_item)

        scale_convergence_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.scale_convergence_list, Unset):
            scale_convergence_list = []
            for scale_convergence_list_item_data in self.scale_convergence_list:
                scale_convergence_list_item = scale_convergence_list_item_data.to_dict()
                scale_convergence_list.append(scale_convergence_list_item)

        input_kind = self.input_kind

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "trajectoryCRS": trajectory_crs,
                "unitXY": unit_xy,
                "unitZ": unit_z,
                "unitDls": unit_dls,
                "stations": stations,
                "localCRS": local_crs,
                "method": method,
            }
        )
        if unit_md is not UNSET:
            field_dict["unitMD"] = unit_md
        if operations_applied is not UNSET:
            field_dict["operationsApplied"] = operations_applied
        if stations_i is not UNSET:
            field_dict["stations_i"] = stations_i
        if scale_convergence_list is not UNSET:
            field_dict["scaleConvergenceList"] = scale_convergence_list
        if input_kind is not UNSET:
            field_dict["inputKind"] = input_kind

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.scale_convergence import ScaleConvergence
        from ..models.trajectory_station_out import TrajectoryStationOut

        d = dict(src_dict)
        trajectory_crs = d.pop("trajectoryCRS")

        unit_xy = d.pop("unitXY")

        unit_z = d.pop("unitZ")

        unit_dls = d.pop("unitDls")

        stations = []
        _stations = d.pop("stations")
        for stations_item_data in _stations:
            stations_item = TrajectoryStationOut.from_dict(stations_item_data)

            stations.append(stations_item)

        local_crs = d.pop("localCRS")

        method = d.pop("method")

        unit_md = d.pop("unitMD", UNSET)

        operations_applied = cast(list[str], d.pop("operationsApplied", UNSET))

        _stations_i = d.pop("stations_i", UNSET)
        stations_i: list[TrajectoryStationOut] | Unset = UNSET
        if _stations_i is not UNSET:
            stations_i = []
            for stations_i_item_data in _stations_i:
                stations_i_item = TrajectoryStationOut.from_dict(stations_i_item_data)

                stations_i.append(stations_i_item)

        _scale_convergence_list = d.pop("scaleConvergenceList", UNSET)
        scale_convergence_list: list[ScaleConvergence] | Unset = UNSET
        if _scale_convergence_list is not UNSET:
            scale_convergence_list = []
            for scale_convergence_list_item_data in _scale_convergence_list:
                scale_convergence_list_item = ScaleConvergence.from_dict(
                    scale_convergence_list_item_data
                )

                scale_convergence_list.append(scale_convergence_list_item)

        input_kind = d.pop("inputKind", UNSET)

        convert_trajectory_response_v4 = cls(
            trajectory_crs=trajectory_crs,
            unit_xy=unit_xy,
            unit_z=unit_z,
            unit_dls=unit_dls,
            stations=stations,
            local_crs=local_crs,
            method=method,
            unit_md=unit_md,
            operations_applied=operations_applied,
            stations_i=stations_i,
            scale_convergence_list=scale_convergence_list,
            input_kind=input_kind,
        )

        convert_trajectory_response_v4.additional_properties = d
        return convert_trajectory_response_v4

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
