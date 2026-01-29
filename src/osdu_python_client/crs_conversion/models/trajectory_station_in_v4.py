from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TrajectoryStationInV4")


@_attrs_define
class TrajectoryStationInV4:
    """Input trajectory station record; context is provided by the container.

    Attributes:
        md (float | Unset): MD (measured depth) from vertical reference point in 'unitZ'. Example: 2563.56.
        inclination (float | Unset): Inclination angle in degrees of arc, 0.0 is vertical, 90.0 is horizontal. Example:
            15.0.
        azimuth (float | Unset): Azimuth angle in degrees of arc, 0.0/360.0 is North; reference given by
            azimuthReference (TRUE_NORTH or GridNorth). Example: 355.0.
        dx (float | Unset): E-W deviation in the local Cartesian engineering CRS from the well reference point; unit is
            given by container's 'unitXY' or projected 'trajectoryCRS'. Example: 55.9.
        dy (float | Unset): N-S deviation in the local Cartesian engineering CRS from the well reference point; Y is
            aligned with azimuth reference (TRUE_NORTH or projected GridNorth); unit is given by container's 'unitXY' or
            projected 'trajectoryCRS'. Example: -145.3.
        dz (float | Unset): True vertical deviation in the local Cartesian engineering CRS from the well reference
            point; unit is given by container's unitZ; downwards positive. Example: 1965.6.
    """

    md: float | Unset = UNSET
    inclination: float | Unset = UNSET
    azimuth: float | Unset = UNSET
    dx: float | Unset = UNSET
    dy: float | Unset = UNSET
    dz: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        md = self.md

        inclination = self.inclination

        azimuth = self.azimuth

        dx = self.dx

        dy = self.dy

        dz = self.dz

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if md is not UNSET:
            field_dict["md"] = md
        if inclination is not UNSET:
            field_dict["inclination"] = inclination
        if azimuth is not UNSET:
            field_dict["azimuth"] = azimuth
        if dx is not UNSET:
            field_dict["dx"] = dx
        if dy is not UNSET:
            field_dict["dy"] = dy
        if dz is not UNSET:
            field_dict["dz"] = dz

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        md = d.pop("md", UNSET)

        inclination = d.pop("inclination", UNSET)

        azimuth = d.pop("azimuth", UNSET)

        dx = d.pop("dx", UNSET)

        dy = d.pop("dy", UNSET)

        dz = d.pop("dz", UNSET)

        trajectory_station_in_v4 = cls(
            md=md,
            inclination=inclination,
            azimuth=azimuth,
            dx=dx,
            dy=dy,
            dz=dz,
        )

        trajectory_station_in_v4.additional_properties = d
        return trajectory_station_in_v4

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
