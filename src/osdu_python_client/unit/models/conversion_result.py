from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.abcd import ABCD
    from ..models.scale_offset import ScaleOffset
    from ..models.unit import Unit


T = TypeVar("T", bound="ConversionResult")


@_attrs_define
class ConversionResult:
    """
    Attributes:
        abcd (ABCD | Unset):
        scale_offset (ScaleOffset | Unset):
        from_unit (Unit | Unset):
        to_unit (Unit | Unset):
    """

    abcd: ABCD | Unset = UNSET
    scale_offset: ScaleOffset | Unset = UNSET
    from_unit: Unit | Unset = UNSET
    to_unit: Unit | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        abcd: dict[str, Any] | Unset = UNSET
        if not isinstance(self.abcd, Unset):
            abcd = self.abcd.to_dict()

        scale_offset: dict[str, Any] | Unset = UNSET
        if not isinstance(self.scale_offset, Unset):
            scale_offset = self.scale_offset.to_dict()

        from_unit: dict[str, Any] | Unset = UNSET
        if not isinstance(self.from_unit, Unset):
            from_unit = self.from_unit.to_dict()

        to_unit: dict[str, Any] | Unset = UNSET
        if not isinstance(self.to_unit, Unset):
            to_unit = self.to_unit.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if abcd is not UNSET:
            field_dict["abcd"] = abcd
        if scale_offset is not UNSET:
            field_dict["scaleOffset"] = scale_offset
        if from_unit is not UNSET:
            field_dict["fromUnit"] = from_unit
        if to_unit is not UNSET:
            field_dict["toUnit"] = to_unit

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.abcd import ABCD
        from ..models.scale_offset import ScaleOffset
        from ..models.unit import Unit

        d = dict(src_dict)
        _abcd = d.pop("abcd", UNSET)
        abcd: ABCD | Unset
        if isinstance(_abcd, Unset):
            abcd = UNSET
        else:
            abcd = ABCD.from_dict(_abcd)

        _scale_offset = d.pop("scaleOffset", UNSET)
        scale_offset: ScaleOffset | Unset
        if isinstance(_scale_offset, Unset):
            scale_offset = UNSET
        else:
            scale_offset = ScaleOffset.from_dict(_scale_offset)

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

        conversion_result = cls(
            abcd=abcd,
            scale_offset=scale_offset,
            from_unit=from_unit,
            to_unit=to_unit,
        )

        conversion_result.additional_properties = d
        return conversion_result

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
