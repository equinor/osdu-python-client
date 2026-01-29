from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.abcd import ABCD
    from ..models.measurement_essence import MeasurementEssence
    from ..models.scale_offset import ScaleOffset


T = TypeVar("T", bound="UnitEssence")


@_attrs_define
class UnitEssence:
    """
    Attributes:
        type_ (str | Unset):
        symbol (str | Unset):
        abcd (ABCD | Unset):
        scale_offset (ScaleOffset | Unset):
        base_measurement_essence (MeasurementEssence | Unset):
    """

    type_: str | Unset = UNSET
    symbol: str | Unset = UNSET
    abcd: ABCD | Unset = UNSET
    scale_offset: ScaleOffset | Unset = UNSET
    base_measurement_essence: MeasurementEssence | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        symbol = self.symbol

        abcd: dict[str, Any] | Unset = UNSET
        if not isinstance(self.abcd, Unset):
            abcd = self.abcd.to_dict()

        scale_offset: dict[str, Any] | Unset = UNSET
        if not isinstance(self.scale_offset, Unset):
            scale_offset = self.scale_offset.to_dict()

        base_measurement_essence: dict[str, Any] | Unset = UNSET
        if not isinstance(self.base_measurement_essence, Unset):
            base_measurement_essence = self.base_measurement_essence.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if symbol is not UNSET:
            field_dict["symbol"] = symbol
        if abcd is not UNSET:
            field_dict["abcd"] = abcd
        if scale_offset is not UNSET:
            field_dict["scaleOffset"] = scale_offset
        if base_measurement_essence is not UNSET:
            field_dict["baseMeasurementEssence"] = base_measurement_essence

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.abcd import ABCD
        from ..models.measurement_essence import MeasurementEssence
        from ..models.scale_offset import ScaleOffset

        d = dict(src_dict)
        type_ = d.pop("type", UNSET)

        symbol = d.pop("symbol", UNSET)

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

        _base_measurement_essence = d.pop("baseMeasurementEssence", UNSET)
        base_measurement_essence: MeasurementEssence | Unset
        if isinstance(_base_measurement_essence, Unset):
            base_measurement_essence = UNSET
        else:
            base_measurement_essence = MeasurementEssence.from_dict(
                _base_measurement_essence
            )

        unit_essence = cls(
            type_=type_,
            symbol=symbol,
            abcd=abcd,
            scale_offset=scale_offset,
            base_measurement_essence=base_measurement_essence,
        )

        unit_essence.additional_properties = d
        return unit_essence

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
