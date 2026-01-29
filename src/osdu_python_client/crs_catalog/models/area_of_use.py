from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.area_of_use_deprecation_info import AreaOfUseDeprecationInfo
    from ..models.area_of_use_essence import AreaOfUseEssence
    from ..models.deprecation_info import DeprecationInfo
    from ..models.essence import Essence
    from ..models.named_reference import NamedReference


T = TypeVar("T", bound="AreaOfUse")


@_attrs_define
class AreaOfUse:
    """
    Attributes:
        name (str | Unset):
        area_of_use_deprecation_info (AreaOfUseDeprecationInfo | Unset):
        area_of_use_essence (AreaOfUseEssence | Unset):
        last_modified (str | Unset):
        named_reference (NamedReference | Unset): Name and Persistable Reference (the essence converted to a JSON
            string).
        alias_names (list[str] | Unset):
        essence (Essence | Unset):
        deprecation_info (DeprecationInfo | Unset):
        description (str | Unset):
    """

    name: str | Unset = UNSET
    area_of_use_deprecation_info: AreaOfUseDeprecationInfo | Unset = UNSET
    area_of_use_essence: AreaOfUseEssence | Unset = UNSET
    last_modified: str | Unset = UNSET
    named_reference: NamedReference | Unset = UNSET
    alias_names: list[str] | Unset = UNSET
    essence: Essence | Unset = UNSET
    deprecation_info: DeprecationInfo | Unset = UNSET
    description: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        area_of_use_deprecation_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.area_of_use_deprecation_info, Unset):
            area_of_use_deprecation_info = self.area_of_use_deprecation_info.to_dict()

        area_of_use_essence: dict[str, Any] | Unset = UNSET
        if not isinstance(self.area_of_use_essence, Unset):
            area_of_use_essence = self.area_of_use_essence.to_dict()

        last_modified = self.last_modified

        named_reference: dict[str, Any] | Unset = UNSET
        if not isinstance(self.named_reference, Unset):
            named_reference = self.named_reference.to_dict()

        alias_names: list[str] | Unset = UNSET
        if not isinstance(self.alias_names, Unset):
            alias_names = self.alias_names

        essence: dict[str, Any] | Unset = UNSET
        if not isinstance(self.essence, Unset):
            essence = self.essence.to_dict()

        deprecation_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.deprecation_info, Unset):
            deprecation_info = self.deprecation_info.to_dict()

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if area_of_use_deprecation_info is not UNSET:
            field_dict["areaOfUseDeprecationInfo"] = area_of_use_deprecation_info
        if area_of_use_essence is not UNSET:
            field_dict["areaOfUseEssence"] = area_of_use_essence
        if last_modified is not UNSET:
            field_dict["lastModified"] = last_modified
        if named_reference is not UNSET:
            field_dict["namedReference"] = named_reference
        if alias_names is not UNSET:
            field_dict["aliasNames"] = alias_names
        if essence is not UNSET:
            field_dict["essence"] = essence
        if deprecation_info is not UNSET:
            field_dict["deprecationInfo"] = deprecation_info
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.area_of_use_deprecation_info import AreaOfUseDeprecationInfo
        from ..models.area_of_use_essence import AreaOfUseEssence
        from ..models.deprecation_info import DeprecationInfo
        from ..models.essence import Essence
        from ..models.named_reference import NamedReference

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        _area_of_use_deprecation_info = d.pop("areaOfUseDeprecationInfo", UNSET)
        area_of_use_deprecation_info: AreaOfUseDeprecationInfo | Unset
        if isinstance(_area_of_use_deprecation_info, Unset):
            area_of_use_deprecation_info = UNSET
        else:
            area_of_use_deprecation_info = AreaOfUseDeprecationInfo.from_dict(
                _area_of_use_deprecation_info
            )

        _area_of_use_essence = d.pop("areaOfUseEssence", UNSET)
        area_of_use_essence: AreaOfUseEssence | Unset
        if isinstance(_area_of_use_essence, Unset):
            area_of_use_essence = UNSET
        else:
            area_of_use_essence = AreaOfUseEssence.from_dict(_area_of_use_essence)

        last_modified = d.pop("lastModified", UNSET)

        _named_reference = d.pop("namedReference", UNSET)
        named_reference: NamedReference | Unset
        if isinstance(_named_reference, Unset):
            named_reference = UNSET
        else:
            named_reference = NamedReference.from_dict(_named_reference)

        alias_names = cast(list[str], d.pop("aliasNames", UNSET))

        _essence = d.pop("essence", UNSET)
        essence: Essence | Unset
        if isinstance(_essence, Unset):
            essence = UNSET
        else:
            essence = Essence.from_dict(_essence)

        _deprecation_info = d.pop("deprecationInfo", UNSET)
        deprecation_info: DeprecationInfo | Unset
        if isinstance(_deprecation_info, Unset):
            deprecation_info = UNSET
        else:
            deprecation_info = DeprecationInfo.from_dict(_deprecation_info)

        description = d.pop("description", UNSET)

        area_of_use = cls(
            name=name,
            area_of_use_deprecation_info=area_of_use_deprecation_info,
            area_of_use_essence=area_of_use_essence,
            last_modified=last_modified,
            named_reference=named_reference,
            alias_names=alias_names,
            essence=essence,
            deprecation_info=deprecation_info,
            description=description,
        )

        area_of_use.additional_properties = d
        return area_of_use

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
