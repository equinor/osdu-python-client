from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TrajectoryStationOut")


@_attrs_define
class TrajectoryStationOut:
    """Output trajectory station record; context is provided by the container.

    Attributes:
        md (float | Unset): MD (measured depth) from vertical reference point in 'unitZ'. Example: 2563.56.
        inclination (float | Unset): Inclination angle in degrees of arc, 0.0 is vertical, 90.0 is horizontal. Example:
            15.0.
        azimuth_tn (float | Unset): True North azimuth angle in degrees of arc, 0.0/360.0 is North. Example: 355.96.
        azimuth_gn (float | Unset): Grid North azimuth angle in degrees of arc, 0.0/360.0 is North. Example: 355.0.
        dx_tn (float | Unset): True E-W deviation in the local Cartesian engineering CRS from the well reference point;
            unit is given by container's 'unitXY'. Example: 55.9.
        dy_tn (float | Unset): True N-S deviation in the local Cartesian engineering CRS from the well reference point;
            Y is aligned with TRUE_NORTH; unit is given by container's 'unitXY'. Example: -145.3.
        point (float | Unset): Point representation for CRS operations
        wgs_84_longitude (float | Unset): WGS 84 longitude in dega
        wgs_84_latitude (float | Unset): WGS 84 latitude in dega
        dls (float | Unset): Curvature, Dog Leg Severity, measured in 'unitDls'.
        original (float | Unset): Original trajectory station if true, interpolated trajectory station if false.
        dz (float | Unset):
    """

    md: float | Unset = UNSET
    inclination: float | Unset = UNSET
    azimuth_tn: float | Unset = UNSET
    azimuth_gn: float | Unset = UNSET
    dx_tn: float | Unset = UNSET
    dy_tn: float | Unset = UNSET
    point: float | Unset = UNSET
    wgs_84_longitude: float | Unset = UNSET
    wgs_84_latitude: float | Unset = UNSET
    dls: float | Unset = UNSET
    original: float | Unset = UNSET
    dz: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        md = self.md

        inclination = self.inclination

        azimuth_tn = self.azimuth_tn

        azimuth_gn = self.azimuth_gn

        dx_tn = self.dx_tn

        dy_tn = self.dy_tn

        point = self.point

        wgs_84_longitude = self.wgs_84_longitude

        wgs_84_latitude = self.wgs_84_latitude

        dls = self.dls

        original = self.original

        dz = self.dz

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if md is not UNSET:
            field_dict["md"] = md
        if inclination is not UNSET:
            field_dict["inclination"] = inclination
        if azimuth_tn is not UNSET:
            field_dict["azimuthTN"] = azimuth_tn
        if azimuth_gn is not UNSET:
            field_dict["azimuthGN"] = azimuth_gn
        if dx_tn is not UNSET:
            field_dict["dxTN"] = dx_tn
        if dy_tn is not UNSET:
            field_dict["dyTN"] = dy_tn
        if point is not UNSET:
            field_dict["point"] = point
        if wgs_84_longitude is not UNSET:
            field_dict["wgs84Longitude"] = wgs_84_longitude
        if wgs_84_latitude is not UNSET:
            field_dict["wgs84Latitude"] = wgs_84_latitude
        if dls is not UNSET:
            field_dict["dls"] = dls
        if original is not UNSET:
            field_dict["original"] = original
        if dz is not UNSET:
            field_dict["dz"] = dz

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        md = d.pop("md", UNSET)

        inclination = d.pop("inclination", UNSET)

        azimuth_tn = d.pop("azimuthTN", UNSET)

        azimuth_gn = d.pop("azimuthGN", UNSET)

        dx_tn = d.pop("dxTN", UNSET)

        dy_tn = d.pop("dyTN", UNSET)

        point = d.pop("point", UNSET)

        wgs_84_longitude = d.pop("wgs84Longitude", UNSET)

        wgs_84_latitude = d.pop("wgs84Latitude", UNSET)

        dls = d.pop("dls", UNSET)

        original = d.pop("original", UNSET)

        dz = d.pop("dz", UNSET)

        trajectory_station_out = cls(
            md=md,
            inclination=inclination,
            azimuth_tn=azimuth_tn,
            azimuth_gn=azimuth_gn,
            dx_tn=dx_tn,
            dy_tn=dy_tn,
            point=point,
            wgs_84_longitude=wgs_84_longitude,
            wgs_84_latitude=wgs_84_latitude,
            dls=dls,
            original=original,
            dz=dz,
        )

        trajectory_station_out.additional_properties = d
        return trajectory_station_out

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
