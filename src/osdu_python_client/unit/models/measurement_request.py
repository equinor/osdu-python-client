from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.measurement_essence_impl import MeasurementEssenceImpl


T = TypeVar("T", bound="MeasurementRequest")


@_attrs_define
class MeasurementRequest:
    """Request to get a specific measurement given a persistable reference string or measurement essence structure.

    Attributes:
        essence (MeasurementEssenceImpl | Unset): The essence of a measurement definition
        persistable_reference (str | Unset):
    """

    essence: MeasurementEssenceImpl | Unset = UNSET
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
        from ..models.measurement_essence_impl import MeasurementEssenceImpl

        d = dict(src_dict)
        _essence = d.pop("essence", UNSET)
        essence: MeasurementEssenceImpl | Unset
        if isinstance(_essence, Unset):
            essence = UNSET
        else:
            essence = MeasurementEssenceImpl.from_dict(_essence)

        persistable_reference = d.pop("persistableReference", UNSET)

        measurement_request = cls(
            essence=essence,
            persistable_reference=persistable_reference,
        )

        measurement_request.additional_properties = d
        return measurement_request

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
