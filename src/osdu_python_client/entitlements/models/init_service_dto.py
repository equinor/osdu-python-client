from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.alias_entity import AliasEntity


T = TypeVar("T", bound="InitServiceDto")


@_attrs_define
class InitServiceDto:
    """
    Attributes:
        alias_mappings (list[AliasEntity] | Unset):
    """

    alias_mappings: list[AliasEntity] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        alias_mappings: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.alias_mappings, Unset):
            alias_mappings = []
            for alias_mappings_item_data in self.alias_mappings:
                alias_mappings_item = alias_mappings_item_data.to_dict()
                alias_mappings.append(alias_mappings_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if alias_mappings is not UNSET:
            field_dict["aliasMappings"] = alias_mappings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.alias_entity import AliasEntity

        d = dict(src_dict)
        _alias_mappings = d.pop("aliasMappings", UNSET)
        alias_mappings: list[AliasEntity] | Unset = UNSET
        if _alias_mappings is not UNSET:
            alias_mappings = []
            for alias_mappings_item_data in _alias_mappings:
                alias_mappings_item = AliasEntity.from_dict(alias_mappings_item_data)

                alias_mappings.append(alias_mappings_item)

        init_service_dto = cls(
            alias_mappings=alias_mappings,
        )

        init_service_dto.additional_properties = d
        return init_service_dto

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
