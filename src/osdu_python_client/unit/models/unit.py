from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.unit_deprecation_info import UnitDeprecationInfo
    from ..models.unit_essence import UnitEssence


T = TypeVar("T", bound="Unit")


@_attrs_define
class Unit:
    """
    Attributes:
        name (str | Unset):
        last_modified (str | Unset):
        source (str | Unset):
        essence_json (str | Unset):
        description (str | Unset):
        essence (UnitEssence | Unset):
        deprecation_info (UnitDeprecationInfo | Unset):
        display_symbol (str | Unset):
        namespace (str | Unset):
    """

    name: str | Unset = UNSET
    last_modified: str | Unset = UNSET
    source: str | Unset = UNSET
    essence_json: str | Unset = UNSET
    description: str | Unset = UNSET
    essence: UnitEssence | Unset = UNSET
    deprecation_info: UnitDeprecationInfo | Unset = UNSET
    display_symbol: str | Unset = UNSET
    namespace: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        last_modified = self.last_modified

        source = self.source

        essence_json = self.essence_json

        description = self.description

        essence: dict[str, Any] | Unset = UNSET
        if not isinstance(self.essence, Unset):
            essence = self.essence.to_dict()

        deprecation_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.deprecation_info, Unset):
            deprecation_info = self.deprecation_info.to_dict()

        display_symbol = self.display_symbol

        namespace = self.namespace

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if last_modified is not UNSET:
            field_dict["lastModified"] = last_modified
        if source is not UNSET:
            field_dict["source"] = source
        if essence_json is not UNSET:
            field_dict["essenceJson"] = essence_json
        if description is not UNSET:
            field_dict["description"] = description
        if essence is not UNSET:
            field_dict["essence"] = essence
        if deprecation_info is not UNSET:
            field_dict["deprecationInfo"] = deprecation_info
        if display_symbol is not UNSET:
            field_dict["displaySymbol"] = display_symbol
        if namespace is not UNSET:
            field_dict["namespace"] = namespace

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.unit_deprecation_info import UnitDeprecationInfo
        from ..models.unit_essence import UnitEssence

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        last_modified = d.pop("lastModified", UNSET)

        source = d.pop("source", UNSET)

        essence_json = d.pop("essenceJson", UNSET)

        description = d.pop("description", UNSET)

        _essence = d.pop("essence", UNSET)
        essence: UnitEssence | Unset
        if isinstance(_essence, Unset):
            essence = UNSET
        else:
            essence = UnitEssence.from_dict(_essence)

        _deprecation_info = d.pop("deprecationInfo", UNSET)
        deprecation_info: UnitDeprecationInfo | Unset
        if isinstance(_deprecation_info, Unset):
            deprecation_info = UNSET
        else:
            deprecation_info = UnitDeprecationInfo.from_dict(_deprecation_info)

        display_symbol = d.pop("displaySymbol", UNSET)

        namespace = d.pop("namespace", UNSET)

        unit = cls(
            name=name,
            last_modified=last_modified,
            source=source,
            essence_json=essence_json,
            description=description,
            essence=essence,
            deprecation_info=deprecation_info,
            display_symbol=display_symbol,
            namespace=namespace,
        )

        unit.additional_properties = d
        return unit

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
