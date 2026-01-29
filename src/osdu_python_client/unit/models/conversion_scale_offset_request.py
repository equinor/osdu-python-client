from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.unit_essence_impl import UnitEssenceImpl


T = TypeVar("T", bound="ConversionScaleOffsetRequest")


@_attrs_define
class ConversionScaleOffsetRequest:
    """A scale offset unit conversion request. The requested units are either passed as persistable reference strings (JSON
    serialized Unit 'essence') or as Unit essence structure.

        Attributes:
            from_unit (UnitEssenceImpl | Unset): The essence of a unit parameterization
            to_unit (UnitEssenceImpl | Unset): The essence of a unit parameterization
            from_unit_persistable_reference (str | Unset): The persistable reference string (JSON serialized Unit 'essence')
                representing toe 'from Unit'. Either 'fromUnitPersistableReference' or 'fromUnit' must be populated.
            to_unit_persistable_reference (str | Unset): The persistable reference string (JSON serialized Unit 'essence')
                representing toe 'to Unit'. Either 'toUnitPersistableReference' or 'toUnit' must be populated.
    """

    from_unit: UnitEssenceImpl | Unset = UNSET
    to_unit: UnitEssenceImpl | Unset = UNSET
    from_unit_persistable_reference: str | Unset = UNSET
    to_unit_persistable_reference: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from_unit: dict[str, Any] | Unset = UNSET
        if not isinstance(self.from_unit, Unset):
            from_unit = self.from_unit.to_dict()

        to_unit: dict[str, Any] | Unset = UNSET
        if not isinstance(self.to_unit, Unset):
            to_unit = self.to_unit.to_dict()

        from_unit_persistable_reference = self.from_unit_persistable_reference

        to_unit_persistable_reference = self.to_unit_persistable_reference

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if from_unit is not UNSET:
            field_dict["fromUnit"] = from_unit
        if to_unit is not UNSET:
            field_dict["toUnit"] = to_unit
        if from_unit_persistable_reference is not UNSET:
            field_dict["fromUnitPersistableReference"] = from_unit_persistable_reference
        if to_unit_persistable_reference is not UNSET:
            field_dict["toUnitPersistableReference"] = to_unit_persistable_reference

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.unit_essence_impl import UnitEssenceImpl

        d = dict(src_dict)
        _from_unit = d.pop("fromUnit", UNSET)
        from_unit: UnitEssenceImpl | Unset
        if isinstance(_from_unit, Unset):
            from_unit = UNSET
        else:
            from_unit = UnitEssenceImpl.from_dict(_from_unit)

        _to_unit = d.pop("toUnit", UNSET)
        to_unit: UnitEssenceImpl | Unset
        if isinstance(_to_unit, Unset):
            to_unit = UNSET
        else:
            to_unit = UnitEssenceImpl.from_dict(_to_unit)

        from_unit_persistable_reference = d.pop("fromUnitPersistableReference", UNSET)

        to_unit_persistable_reference = d.pop("toUnitPersistableReference", UNSET)

        conversion_scale_offset_request = cls(
            from_unit=from_unit,
            to_unit=to_unit,
            from_unit_persistable_reference=from_unit_persistable_reference,
            to_unit_persistable_reference=to_unit_persistable_reference,
        )

        conversion_scale_offset_request.additional_properties = d
        return conversion_scale_offset_request

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
