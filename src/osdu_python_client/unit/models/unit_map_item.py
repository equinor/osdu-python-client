from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.unit import Unit


T = TypeVar("T", bound="UnitMapItem")


@_attrs_define
class UnitMapItem:
    """
    Attributes:
        state (str | Unset):
        from_namespace (str | Unset):
        to_namespace (str | Unset):
        from_unit (Unit | Unset):
        to_unit (Unit | Unset):
        note (str | Unset):
    """

    state: str | Unset = UNSET
    from_namespace: str | Unset = UNSET
    to_namespace: str | Unset = UNSET
    from_unit: Unit | Unset = UNSET
    to_unit: Unit | Unset = UNSET
    note: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        state = self.state

        from_namespace = self.from_namespace

        to_namespace = self.to_namespace

        from_unit: dict[str, Any] | Unset = UNSET
        if not isinstance(self.from_unit, Unset):
            from_unit = self.from_unit.to_dict()

        to_unit: dict[str, Any] | Unset = UNSET
        if not isinstance(self.to_unit, Unset):
            to_unit = self.to_unit.to_dict()

        note = self.note

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if state is not UNSET:
            field_dict["state"] = state
        if from_namespace is not UNSET:
            field_dict["fromNamespace"] = from_namespace
        if to_namespace is not UNSET:
            field_dict["toNamespace"] = to_namespace
        if from_unit is not UNSET:
            field_dict["fromUnit"] = from_unit
        if to_unit is not UNSET:
            field_dict["toUnit"] = to_unit
        if note is not UNSET:
            field_dict["note"] = note

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.unit import Unit

        d = dict(src_dict)
        state = d.pop("state", UNSET)

        from_namespace = d.pop("fromNamespace", UNSET)

        to_namespace = d.pop("toNamespace", UNSET)

        _from_unit = d.pop("fromUnit", UNSET)
        from_unit: Unit | Unset
        if isinstance(_from_unit, Unset):
            from_unit = UNSET
        else:
            from_unit = Unit.from_dict(_from_unit)

        _to_unit = d.pop("toUnit", UNSET)
        to_unit: Unit | Unset
        if isinstance(_to_unit, Unset):
            to_unit = UNSET
        else:
            to_unit = Unit.from_dict(_to_unit)

        note = d.pop("note", UNSET)

        unit_map_item = cls(
            state=state,
            from_namespace=from_namespace,
            to_namespace=to_namespace,
            from_unit=from_unit,
            to_unit=to_unit,
            note=note,
        )

        unit_map_item.additional_properties = d
        return unit_map_item

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
