from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UnitSystemInfo")


@_attrs_define
class UnitSystemInfo:
    """A container for UnitSystem properties

    Attributes:
        name (str | Unset): The unit system name
        description (str | Unset): The unit system description
        ancestry (str | Unset): The unit system ancestry, i.e. names separated by '.'
        persistable_reference (str | Unset): The unit system's persistable reference string.
    """

    name: str | Unset = UNSET
    description: str | Unset = UNSET
    ancestry: str | Unset = UNSET
    persistable_reference: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description = self.description

        ancestry = self.ancestry

        persistable_reference = self.persistable_reference

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if ancestry is not UNSET:
            field_dict["ancestry"] = ancestry
        if persistable_reference is not UNSET:
            field_dict["persistableReference"] = persistable_reference

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        ancestry = d.pop("ancestry", UNSET)

        persistable_reference = d.pop("persistableReference", UNSET)

        unit_system_info = cls(
            name=name,
            description=description,
            ancestry=ancestry,
            persistable_reference=persistable_reference,
        )

        unit_system_info.additional_properties = d
        return unit_system_info

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
