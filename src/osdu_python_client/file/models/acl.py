from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Acl")


@_attrs_define
class Acl:
    """
    Attributes:
        viewers (list[str] | Unset):
        owners (list[str] | Unset):
    """

    viewers: list[str] | Unset = UNSET
    owners: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        viewers: list[str] | Unset = UNSET
        if not isinstance(self.viewers, Unset):
            viewers = self.viewers

        owners: list[str] | Unset = UNSET
        if not isinstance(self.owners, Unset):
            owners = self.owners

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if viewers is not UNSET:
            field_dict["viewers"] = viewers
        if owners is not UNSET:
            field_dict["owners"] = owners

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        viewers = cast(list[str], d.pop("viewers", UNSET))

        owners = cast(list[str], d.pop("owners", UNSET))

        acl = cls(
            viewers=viewers,
            owners=owners,
        )

        acl.additional_properties = d
        return acl

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
