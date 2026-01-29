from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ABCDImpl")


@_attrs_define
class ABCDImpl:
    """Energistics standard parameterization y = (A+Bx)/(C+Dx)

    Attributes:
        a (float | Unset): Coefficient A in the Energistics unit parameterization y = (A+Bx)/(C+Dx)
        b (float | Unset): Coefficient B in the Energistics unit parameterization y = (A+Bx)/(C+Dx)
        c (float | Unset): Coefficient C in the Energistics unit parameterization y = (A+Bx)/(C+Dx)
        d (float | Unset): Coefficient D in the Energistics unit parameterization y = (A+Bx)/(C+Dx)
    """

    a: float | Unset = UNSET
    b: float | Unset = UNSET
    c: float | Unset = UNSET
    d: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        a = self.a

        b = self.b

        c = self.c

        d = self.d

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if a is not UNSET:
            field_dict["a"] = a
        if b is not UNSET:
            field_dict["b"] = b
        if c is not UNSET:
            field_dict["c"] = c
        if d is not UNSET:
            field_dict["d"] = d

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        a = d.pop("a", UNSET)

        b = d.pop("b", UNSET)

        c = d.pop("c", UNSET)

        d = d.pop("d", UNSET)

        abcd_impl = cls(
            a=a,
            b=b,
            c=c,
            d=d,
        )

        abcd_impl.additional_properties = d
        return abcd_impl

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
