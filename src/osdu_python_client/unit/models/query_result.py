from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.map_state import MapState
    from ..models.measurement import Measurement
    from ..models.measurement_map_item import MeasurementMapItem
    from ..models.unit import Unit
    from ..models.unit_map_item import UnitMapItem


T = TypeVar("T", bound="QueryResult")


@_attrs_define
class QueryResult:
    """
    Attributes:
        offset (int | Unset):
        count (int | Unset):
        units (list[Unit] | Unset):
        unit_map_items (list[UnitMapItem] | Unset):
        measurement_map_items (list[MeasurementMapItem] | Unset):
        measurements (list[Measurement] | Unset):
        map_states (list[MapState] | Unset):
        total_count (int | Unset):
    """

    offset: int | Unset = UNSET
    count: int | Unset = UNSET
    units: list[Unit] | Unset = UNSET
    unit_map_items: list[UnitMapItem] | Unset = UNSET
    measurement_map_items: list[MeasurementMapItem] | Unset = UNSET
    measurements: list[Measurement] | Unset = UNSET
    map_states: list[MapState] | Unset = UNSET
    total_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        offset = self.offset

        count = self.count

        units: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.units, Unset):
            units = []
            for units_item_data in self.units:
                units_item = units_item_data.to_dict()
                units.append(units_item)

        unit_map_items: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.unit_map_items, Unset):
            unit_map_items = []
            for unit_map_items_item_data in self.unit_map_items:
                unit_map_items_item = unit_map_items_item_data.to_dict()
                unit_map_items.append(unit_map_items_item)

        measurement_map_items: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.measurement_map_items, Unset):
            measurement_map_items = []
            for measurement_map_items_item_data in self.measurement_map_items:
                measurement_map_items_item = measurement_map_items_item_data.to_dict()
                measurement_map_items.append(measurement_map_items_item)

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

        total_count = self.total_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if offset is not UNSET:
            field_dict["offset"] = offset
        if count is not UNSET:
            field_dict["count"] = count
        if units is not UNSET:
            field_dict["units"] = units
        if unit_map_items is not UNSET:
            field_dict["unitMapItems"] = unit_map_items
        if measurement_map_items is not UNSET:
            field_dict["measurementMapItems"] = measurement_map_items
        if measurements is not UNSET:
            field_dict["measurements"] = measurements
        if map_states is not UNSET:
            field_dict["mapStates"] = map_states
        if total_count is not UNSET:
            field_dict["totalCount"] = total_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.map_state import MapState
        from ..models.measurement import Measurement
        from ..models.measurement_map_item import MeasurementMapItem
        from ..models.unit import Unit
        from ..models.unit_map_item import UnitMapItem

        d = dict(src_dict)
        offset = d.pop("offset", UNSET)

        count = d.pop("count", UNSET)

        _units = d.pop("units", UNSET)
        units: list[Unit] | Unset = UNSET
        if _units is not UNSET:
            units = []
            for units_item_data in _units:
                units_item = Unit.from_dict(units_item_data)

                units.append(units_item)

        _unit_map_items = d.pop("unitMapItems", UNSET)
        unit_map_items: list[UnitMapItem] | Unset = UNSET
        if _unit_map_items is not UNSET:
            unit_map_items = []
            for unit_map_items_item_data in _unit_map_items:
                unit_map_items_item = UnitMapItem.from_dict(unit_map_items_item_data)

                unit_map_items.append(unit_map_items_item)

        _measurement_map_items = d.pop("measurementMapItems", UNSET)
        measurement_map_items: list[MeasurementMapItem] | Unset = UNSET
        if _measurement_map_items is not UNSET:
            measurement_map_items = []
            for measurement_map_items_item_data in _measurement_map_items:
                measurement_map_items_item = MeasurementMapItem.from_dict(
                    measurement_map_items_item_data
                )

                measurement_map_items.append(measurement_map_items_item)

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

        total_count = d.pop("totalCount", UNSET)

        query_result = cls(
            offset=offset,
            count=count,
            units=units,
            unit_map_items=unit_map_items,
            measurement_map_items=measurement_map_items,
            measurements=measurements,
            map_states=map_states,
            total_count=total_count,
        )

        query_result.additional_properties = d
        return query_result

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
