from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.measurement import Measurement


T = TypeVar("T", bound="MeasurementMapItem")


@_attrs_define
class MeasurementMapItem:
    """
    Attributes:
        state (str | Unset):
        from_namespace (str | Unset):
        to_namespace (str | Unset):
        from_measurement (Measurement | Unset):
        note (str | Unset):
        to_measurement (Measurement | Unset):
    """

    state: str | Unset = UNSET
    from_namespace: str | Unset = UNSET
    to_namespace: str | Unset = UNSET
    from_measurement: Measurement | Unset = UNSET
    note: str | Unset = UNSET
    to_measurement: Measurement | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        state = self.state

        from_namespace = self.from_namespace

        to_namespace = self.to_namespace

        from_measurement: dict[str, Any] | Unset = UNSET
        if not isinstance(self.from_measurement, Unset):
            from_measurement = self.from_measurement.to_dict()

        note = self.note

        to_measurement: dict[str, Any] | Unset = UNSET
        if not isinstance(self.to_measurement, Unset):
            to_measurement = self.to_measurement.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if state is not UNSET:
            field_dict["state"] = state
        if from_namespace is not UNSET:
            field_dict["fromNamespace"] = from_namespace
        if to_namespace is not UNSET:
            field_dict["toNamespace"] = to_namespace
        if from_measurement is not UNSET:
            field_dict["fromMeasurement"] = from_measurement
        if note is not UNSET:
            field_dict["note"] = note
        if to_measurement is not UNSET:
            field_dict["toMeasurement"] = to_measurement

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.measurement import Measurement

        d = dict(src_dict)
        state = d.pop("state", UNSET)

        from_namespace = d.pop("fromNamespace", UNSET)

        to_namespace = d.pop("toNamespace", UNSET)

        _from_measurement = d.pop("fromMeasurement", UNSET)
        from_measurement: Measurement | Unset
        if isinstance(_from_measurement, Unset):
            from_measurement = UNSET
        else:
            from_measurement = Measurement.from_dict(_from_measurement)

        note = d.pop("note", UNSET)

        _to_measurement = d.pop("toMeasurement", UNSET)
        to_measurement: Measurement | Unset
        if isinstance(_to_measurement, Unset):
            to_measurement = UNSET
        else:
            to_measurement = Measurement.from_dict(_to_measurement)

        measurement_map_item = cls(
            state=state,
            from_namespace=from_namespace,
            to_namespace=to_namespace,
            from_measurement=from_measurement,
            note=note,
            to_measurement=to_measurement,
        )

        measurement_map_item.additional_properties = d
        return measurement_map_item

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
