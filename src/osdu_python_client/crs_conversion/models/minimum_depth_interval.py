from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MinimumDepthInterval")


@_attrs_define
class MinimumDepthInterval:
    """Minimum depth interval record; context is provided by the container.

    Attributes:
        md_i (list[float] | Unset): MD_I (measured depth) Example: 200.
        md_interval (float | Unset): MD_INTERVAL (measured depth interval) Example: 1.0.
    """

    md_i: list[float] | Unset = UNSET
    md_interval: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        md_i: list[float] | Unset = UNSET
        if not isinstance(self.md_i, Unset):
            md_i = self.md_i

        md_interval = self.md_interval

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if md_i is not UNSET:
            field_dict["md_i"] = md_i
        if md_interval is not UNSET:
            field_dict["md_interval"] = md_interval

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        md_i = cast(list[float], d.pop("md_i", UNSET))

        md_interval = d.pop("md_interval", UNSET)

        minimum_depth_interval = cls(
            md_i=md_i,
            md_interval=md_interval,
        )

        minimum_depth_interval.additional_properties = d
        return minimum_depth_interval

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
