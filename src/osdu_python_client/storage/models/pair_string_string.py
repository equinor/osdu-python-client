from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PairStringString")


@_attrs_define
class PairStringString:
    """
    Attributes:
        value (str | Unset):
        key (str | Unset):
        left (str | Unset):
        right (str | Unset):
    """

    value: str | Unset = UNSET
    key: str | Unset = UNSET
    left: str | Unset = UNSET
    right: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        value = self.value

        key = self.key

        left = self.left

        right = self.right

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if value is not UNSET:
            field_dict["value"] = value
        if key is not UNSET:
            field_dict["key"] = key
        if left is not UNSET:
            field_dict["left"] = left
        if right is not UNSET:
            field_dict["right"] = right

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        value = d.pop("value", UNSET)

        key = d.pop("key", UNSET)

        left = d.pop("left", UNSET)

        right = d.pop("right", UNSET)

        pair_string_string = cls(
            value=value,
            key=key,
            left=left,
            right=right,
        )

        pair_string_string.additional_properties = d
        return pair_string_string

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
