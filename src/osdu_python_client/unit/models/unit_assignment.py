from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.measurement import Measurement
    from ..models.unit import Unit


T = TypeVar("T", bound="UnitAssignment")


@_attrs_define
class UnitAssignment:
    """
    Attributes:
        last_modified (str | Unset):
        measurement (Measurement | Unset):
        unit (Unit | Unset):
    """

    last_modified: str | Unset = UNSET
    measurement: Measurement | Unset = UNSET
    unit: Unit | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        last_modified = self.last_modified

        measurement: dict[str, Any] | Unset = UNSET
        if not isinstance(self.measurement, Unset):
            measurement = self.measurement.to_dict()

        unit: dict[str, Any] | Unset = UNSET
        if not isinstance(self.unit, Unset):
            unit = self.unit.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if last_modified is not UNSET:
            field_dict["lastModified"] = last_modified
        if measurement is not UNSET:
            field_dict["measurement"] = measurement
        if unit is not UNSET:
            field_dict["unit"] = unit

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.measurement import Measurement
        from ..models.unit import Unit

        d = dict(src_dict)
        last_modified = d.pop("lastModified", UNSET)

        _measurement = d.pop("measurement", UNSET)
        measurement: Measurement | Unset
        if isinstance(_measurement, Unset):
            measurement = UNSET
        else:
            measurement = Measurement.from_dict(_measurement)

        _unit = d.pop("unit", UNSET)
        unit: Unit | Unset
        if isinstance(_unit, Unset):
            unit = UNSET
        else:
            unit = Unit.from_dict(_unit)

        unit_assignment = cls(
            last_modified=last_modified,
            measurement=measurement,
            unit=unit,
        )

        unit_assignment.additional_properties = d
        return unit_assignment

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
