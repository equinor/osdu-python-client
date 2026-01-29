from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MeasurementEssenceImpl")


@_attrs_define
class MeasurementEssenceImpl:
    """The essence of a measurement definition

    Attributes:
        base_measurement_code (str | Unset):
        ancestry (str | Unset): The measurement ancestry, i.e. the parent codes separated by a period symbol.
        type_ (str | Unset): The type string for this measurement
    """

    base_measurement_code: str | Unset = UNSET
    ancestry: str | Unset = UNSET
    type_: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        base_measurement_code = self.base_measurement_code

        ancestry = self.ancestry

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if base_measurement_code is not UNSET:
            field_dict["baseMeasurementCode"] = base_measurement_code
        if ancestry is not UNSET:
            field_dict["ancestry"] = ancestry
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        base_measurement_code = d.pop("baseMeasurementCode", UNSET)

        ancestry = d.pop("ancestry", UNSET)

        type_ = d.pop("type", UNSET)

        measurement_essence_impl = cls(
            base_measurement_code=base_measurement_code,
            ancestry=ancestry,
            type_=type_,
        )

        measurement_essence_impl.additional_properties = d
        return measurement_essence_impl

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
