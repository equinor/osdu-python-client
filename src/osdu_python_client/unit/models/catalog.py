from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.map_state import MapState
    from ..models.measurement import Measurement
    from ..models.measurement_map import MeasurementMap
    from ..models.unit import Unit
    from ..models.unit_map import UnitMap
    from ..models.unit_system_info import UnitSystemInfo


T = TypeVar("T", bound="Catalog")


@_attrs_define
class Catalog:
    """
    Attributes:
        units (list[Unit] | Unset):
        last_modified (str | Unset):
        unit_maps (list[UnitMap] | Unset):
        measurement_maps (list[MeasurementMap] | Unset):
        unit_system_infos (list[UnitSystemInfo] | Unset):
        total_unit_count (int | Unset):
        total_measurement_count (int | Unset):
        total_unit_system_count (int | Unset):
        total_unit_map_count (int | Unset):
        total_measurement_map_count (int | Unset):
        total_map_state_count (int | Unset):
        measurements (list[Measurement] | Unset):
        map_states (list[MapState] | Unset):
    """

    units: list[Unit] | Unset = UNSET
    last_modified: str | Unset = UNSET
    unit_maps: list[UnitMap] | Unset = UNSET
    measurement_maps: list[MeasurementMap] | Unset = UNSET
    unit_system_infos: list[UnitSystemInfo] | Unset = UNSET
    total_unit_count: int | Unset = UNSET
    total_measurement_count: int | Unset = UNSET
    total_unit_system_count: int | Unset = UNSET
    total_unit_map_count: int | Unset = UNSET
    total_measurement_map_count: int | Unset = UNSET
    total_map_state_count: int | Unset = UNSET
    measurements: list[Measurement] | Unset = UNSET
    map_states: list[MapState] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        units: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.units, Unset):
            units = []
            for units_item_data in self.units:
                units_item = units_item_data.to_dict()
                units.append(units_item)

        last_modified = self.last_modified

        unit_maps: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.unit_maps, Unset):
            unit_maps = []
            for unit_maps_item_data in self.unit_maps:
                unit_maps_item = unit_maps_item_data.to_dict()
                unit_maps.append(unit_maps_item)

        measurement_maps: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.measurement_maps, Unset):
            measurement_maps = []
            for measurement_maps_item_data in self.measurement_maps:
                measurement_maps_item = measurement_maps_item_data.to_dict()
                measurement_maps.append(measurement_maps_item)

        unit_system_infos: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.unit_system_infos, Unset):
            unit_system_infos = []
            for unit_system_infos_item_data in self.unit_system_infos:
                unit_system_infos_item = unit_system_infos_item_data.to_dict()
                unit_system_infos.append(unit_system_infos_item)

        total_unit_count = self.total_unit_count

        total_measurement_count = self.total_measurement_count

        total_unit_system_count = self.total_unit_system_count

        total_unit_map_count = self.total_unit_map_count

        total_measurement_map_count = self.total_measurement_map_count

        total_map_state_count = self.total_map_state_count

        measurements: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.measurements, Unset):
            measurements = []
            for measurements_item_data in self.measurements:
                measurements_item = measurements_item_data.to_dict()
                measurements.append(measurements_item)

        map_states: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.map_states, Unset):
            map_states = []
            for map_states_item_data in self.map_states:
                map_states_item = map_states_item_data.to_dict()
                map_states.append(map_states_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if units is not UNSET:
            field_dict["units"] = units
        if last_modified is not UNSET:
            field_dict["lastModified"] = last_modified
        if unit_maps is not UNSET:
            field_dict["unitMaps"] = unit_maps
        if measurement_maps is not UNSET:
            field_dict["measurementMaps"] = measurement_maps
        if unit_system_infos is not UNSET:
            field_dict["unitSystemInfos"] = unit_system_infos
        if total_unit_count is not UNSET:
            field_dict["totalUnitCount"] = total_unit_count
        if total_measurement_count is not UNSET:
            field_dict["totalMeasurementCount"] = total_measurement_count
        if total_unit_system_count is not UNSET:
            field_dict["totalUnitSystemCount"] = total_unit_system_count
        if total_unit_map_count is not UNSET:
            field_dict["totalUnitMapCount"] = total_unit_map_count
        if total_measurement_map_count is not UNSET:
            field_dict["totalMeasurementMapCount"] = total_measurement_map_count
        if total_map_state_count is not UNSET:
            field_dict["totalMapStateCount"] = total_map_state_count
        if measurements is not UNSET:
            field_dict["measurements"] = measurements
        if map_states is not UNSET:
            field_dict["mapStates"] = map_states

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.map_state import MapState
        from ..models.measurement import Measurement
        from ..models.measurement_map import MeasurementMap
        from ..models.unit import Unit
        from ..models.unit_map import UnitMap
        from ..models.unit_system_info import UnitSystemInfo

        d = dict(src_dict)
        _units = d.pop("units", UNSET)
        units: list[Unit] | Unset = UNSET
        if _units is not UNSET:
            units = []
            for units_item_data in _units:
                units_item = Unit.from_dict(units_item_data)

                units.append(units_item)

        last_modified = d.pop("lastModified", UNSET)

        _unit_maps = d.pop("unitMaps", UNSET)
        unit_maps: list[UnitMap] | Unset = UNSET
        if _unit_maps is not UNSET:
            unit_maps = []
            for unit_maps_item_data in _unit_maps:
                unit_maps_item = UnitMap.from_dict(unit_maps_item_data)

                unit_maps.append(unit_maps_item)

        _measurement_maps = d.pop("measurementMaps", UNSET)
        measurement_maps: list[MeasurementMap] | Unset = UNSET
        if _measurement_maps is not UNSET:
            measurement_maps = []
            for measurement_maps_item_data in _measurement_maps:
                measurement_maps_item = MeasurementMap.from_dict(
                    measurement_maps_item_data
                )

                measurement_maps.append(measurement_maps_item)

        _unit_system_infos = d.pop("unitSystemInfos", UNSET)
        unit_system_infos: list[UnitSystemInfo] | Unset = UNSET
        if _unit_system_infos is not UNSET:
            unit_system_infos = []
            for unit_system_infos_item_data in _unit_system_infos:
                unit_system_infos_item = UnitSystemInfo.from_dict(
                    unit_system_infos_item_data
                )

                unit_system_infos.append(unit_system_infos_item)

        total_unit_count = d.pop("totalUnitCount", UNSET)

        total_measurement_count = d.pop("totalMeasurementCount", UNSET)

        total_unit_system_count = d.pop("totalUnitSystemCount", UNSET)

        total_unit_map_count = d.pop("totalUnitMapCount", UNSET)

        total_measurement_map_count = d.pop("totalMeasurementMapCount", UNSET)

        total_map_state_count = d.pop("totalMapStateCount", UNSET)

        _measurements = d.pop("measurements", UNSET)
        measurements: list[Measurement] | Unset = UNSET
        if _measurements is not UNSET:
            measurements = []
            for measurements_item_data in _measurements:
                measurements_item = Measurement.from_dict(measurements_item_data)

                measurements.append(measurements_item)

        _map_states = d.pop("mapStates", UNSET)
        map_states: list[MapState] | Unset = UNSET
        if _map_states is not UNSET:
            map_states = []
            for map_states_item_data in _map_states:
                map_states_item = MapState.from_dict(map_states_item_data)

                map_states.append(map_states_item)

        catalog = cls(
            units=units,
            last_modified=last_modified,
            unit_maps=unit_maps,
            measurement_maps=measurement_maps,
            unit_system_infos=unit_system_infos,
            total_unit_count=total_unit_count,
            total_measurement_count=total_measurement_count,
            total_unit_system_count=total_unit_system_count,
            total_unit_map_count=total_unit_map_count,
            total_measurement_map_count=total_measurement_map_count,
            total_map_state_count=total_map_state_count,
            measurements=measurements,
            map_states=map_states,
        )

        catalog.additional_properties = d
        return catalog

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
