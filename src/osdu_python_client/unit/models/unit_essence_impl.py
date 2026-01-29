from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.abcd_impl import ABCDImpl
    from ..models.measurement_essence import MeasurementEssence
    from ..models.scale_offset_impl import ScaleOffsetImpl


T = TypeVar("T", bound="UnitEssenceImpl")


@_attrs_define
class UnitEssenceImpl:
    """The essence of a unit parameterization

    Attributes:
        abcd (ABCDImpl | Unset): Energistics standard parameterization y = (A+Bx)/(C+Dx)
        scale_offset (ScaleOffsetImpl | Unset): Unit in y = scale*(x-offset) parameterization
        symbol (str | Unset): Unit in y = scale*(x-offset) parameterization
        base_measurement (MeasurementEssence | Unset):
        type_ (str | Unset): The type string for this unit essence, either 'USO' for ScaleOffset or 'UAD' for Abcd
    """

    abcd: ABCDImpl | Unset = UNSET
    scale_offset: ScaleOffsetImpl | Unset = UNSET
    symbol: str | Unset = UNSET
    base_measurement: MeasurementEssence | Unset = UNSET
    type_: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        abcd: dict[str, Any] | Unset = UNSET
        if not isinstance(self.abcd, Unset):
            abcd = self.abcd.to_dict()

        scale_offset: dict[str, Any] | Unset = UNSET
        if not isinstance(self.scale_offset, Unset):
            scale_offset = self.scale_offset.to_dict()

        symbol = self.symbol

        base_measurement: dict[str, Any] | Unset = UNSET
        if not isinstance(self.base_measurement, Unset):
            base_measurement = self.base_measurement.to_dict()

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if abcd is not UNSET:
            field_dict["abcd"] = abcd
        if scale_offset is not UNSET:
            field_dict["scaleOffset"] = scale_offset
        if symbol is not UNSET:
            field_dict["symbol"] = symbol
        if base_measurement is not UNSET:
            field_dict["baseMeasurement"] = base_measurement
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.abcd_impl import ABCDImpl
        from ..models.measurement_essence import MeasurementEssence
        from ..models.scale_offset_impl import ScaleOffsetImpl

        d = dict(src_dict)
        _abcd = d.pop("abcd", UNSET)
        abcd: ABCDImpl | Unset
        if isinstance(_abcd, Unset):
            abcd = UNSET
        else:
            abcd = ABCDImpl.from_dict(_abcd)

        _scale_offset = d.pop("scaleOffset", UNSET)
        scale_offset: ScaleOffsetImpl | Unset
        if isinstance(_scale_offset, Unset):
            scale_offset = UNSET
        else:
            scale_offset = ScaleOffsetImpl.from_dict(_scale_offset)

        symbol = d.pop("symbol", UNSET)

        _base_measurement = d.pop("baseMeasurement", UNSET)
        base_measurement: MeasurementEssence | Unset
        if isinstance(_base_measurement, Unset):
            base_measurement = UNSET
        else:
            base_measurement = MeasurementEssence.from_dict(_base_measurement)

        type_ = d.pop("type", UNSET)

        unit_essence_impl = cls(
            abcd=abcd,
            scale_offset=scale_offset,
            symbol=symbol,
            base_measurement=base_measurement,
            type_=type_,
        )

        unit_essence_impl.additional_properties = d
        return unit_essence_impl

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
