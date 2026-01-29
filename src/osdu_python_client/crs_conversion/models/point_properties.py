from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PointProperties")


@_attrs_define
class PointProperties:
    """
    Attributes:
        label (str | Unset):
        inline (int | Unset):
        crossline (int | Unset):
    """

    label: str | Unset = UNSET
    inline: int | Unset = UNSET
    crossline: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        label = self.label

        inline = self.inline

        crossline = self.crossline

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if label is not UNSET:
            field_dict["Label"] = label
        if inline is not UNSET:
            field_dict["Inline"] = inline
        if crossline is not UNSET:
            field_dict["Crossline"] = crossline

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        label = d.pop("Label", UNSET)

        inline = d.pop("Inline", UNSET)

        crossline = d.pop("Crossline", UNSET)

        point_properties = cls(
            label=label,
            inline=inline,
            crossline=crossline,
        )

        point_properties.additional_properties = d
        return point_properties

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
