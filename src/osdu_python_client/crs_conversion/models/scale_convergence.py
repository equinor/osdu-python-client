from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ScaleConvergence")


@_attrs_define
class ScaleConvergence:
    """scaleConvergence

    Attributes:
        scalefactor (float | Unset): Scalefactor
        convergence (float | Unset): convergence
        point (float | Unset): Point representation for CRS operations
    """

    scalefactor: float | Unset = UNSET
    convergence: float | Unset = UNSET
    point: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        scalefactor = self.scalefactor

        convergence = self.convergence

        point = self.point

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if scalefactor is not UNSET:
            field_dict["scalefactor"] = scalefactor
        if convergence is not UNSET:
            field_dict["convergence"] = convergence
        if point is not UNSET:
            field_dict["point"] = point

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        scalefactor = d.pop("scalefactor", UNSET)

        convergence = d.pop("convergence", UNSET)

        point = d.pop("point", UNSET)

        scale_convergence = cls(
            scalefactor=scalefactor,
            convergence=convergence,
            point=point,
        )

        scale_convergence.additional_properties = d
        return scale_convergence

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
