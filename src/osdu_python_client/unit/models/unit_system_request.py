from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.unit_system_essence_impl import UnitSystemEssenceImpl


T = TypeVar("T", bound="UnitSystemRequest")


@_attrs_define
class UnitSystemRequest:
    """Request to get all unit assignments for the given unit system

    Attributes:
        essence (UnitSystemEssenceImpl | Unset): A unit system essence
        persistable_reference (str | Unset): The unit system's persistable reference string
    """

    essence: UnitSystemEssenceImpl | Unset = UNSET
    persistable_reference: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        essence: dict[str, Any] | Unset = UNSET
        if not isinstance(self.essence, Unset):
            essence = self.essence.to_dict()

        persistable_reference = self.persistable_reference

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if essence is not UNSET:
            field_dict["essence"] = essence
        if persistable_reference is not UNSET:
            field_dict["persistableReference"] = persistable_reference

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.unit_system_essence_impl import UnitSystemEssenceImpl

        d = dict(src_dict)
        _essence = d.pop("essence", UNSET)
        essence: UnitSystemEssenceImpl | Unset
        if isinstance(_essence, Unset):
            essence = UNSET
        else:
            essence = UnitSystemEssenceImpl.from_dict(_essence)

        persistable_reference = d.pop("persistableReference", UNSET)

        unit_system_request = cls(
            essence=essence,
            persistable_reference=persistable_reference,
        )

        unit_system_request.additional_properties = d
        return unit_system_request

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
