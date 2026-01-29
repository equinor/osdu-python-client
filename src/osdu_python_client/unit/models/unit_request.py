from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.unit_essence_impl import UnitEssenceImpl


T = TypeVar("T", bound="UnitRequest")


@_attrs_define
class UnitRequest:
    """Request to get a single unit instance given an essence.

    Attributes:
        persistable_reference (str | Unset): The persistable reference string for the unit; optional, only one
            'persistableReference' or 'essence' must be defined
        essence (UnitEssenceImpl | Unset): The essence of a unit parameterization
    """

    persistable_reference: str | Unset = UNSET
    essence: UnitEssenceImpl | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        persistable_reference = self.persistable_reference

        essence: dict[str, Any] | Unset = UNSET
        if not isinstance(self.essence, Unset):
            essence = self.essence.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if persistable_reference is not UNSET:
            field_dict["persistableReference"] = persistable_reference
        if essence is not UNSET:
            field_dict["essence"] = essence

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.unit_essence_impl import UnitEssenceImpl

        d = dict(src_dict)
        persistable_reference = d.pop("persistableReference", UNSET)

        _essence = d.pop("essence", UNSET)
        essence: UnitEssenceImpl | Unset
        if isinstance(_essence, Unset):
            essence = UNSET
        else:
            essence = UnitEssenceImpl.from_dict(_essence)

        unit_request = cls(
            persistable_reference=persistable_reference,
            essence=essence,
        )

        unit_request.additional_properties = d
        return unit_request

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
