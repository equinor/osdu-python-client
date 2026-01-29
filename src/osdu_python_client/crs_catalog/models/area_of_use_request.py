from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.area_of_use_essence_impl import AreaOfUseEssenceImpl


T = TypeVar("T", bound="AreaOfUseRequest")


@_attrs_define
class AreaOfUseRequest:
    """Request to get area of use

    Attributes:
        essence (AreaOfUseEssenceImpl | Unset): the area of use essence
        persistable_reference (str | Unset): persistable reference string as passed through the request
    """

    essence: AreaOfUseEssenceImpl | Unset = UNSET
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
        from ..models.area_of_use_essence_impl import AreaOfUseEssenceImpl

        d = dict(src_dict)
        _essence = d.pop("essence", UNSET)
        essence: AreaOfUseEssenceImpl | Unset
        if isinstance(_essence, Unset):
            essence = UNSET
        else:
            essence = AreaOfUseEssenceImpl.from_dict(_essence)

        persistable_reference = d.pop("persistableReference", UNSET)

        area_of_use_request = cls(
            essence=essence,
            persistable_reference=persistable_reference,
        )

        area_of_use_request.additional_properties = d
        return area_of_use_request

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
