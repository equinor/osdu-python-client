from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.area_of_use import AreaOfUse
    from ..models.authority_code import AuthorityCode
    from ..models.ct_deprecation_info import CTDeprecationInfo
    from ..models.deprecation_info import DeprecationInfo
    from ..models.essence import Essence
    from ..models.named_reference import NamedReference


T = TypeVar("T", bound="CT")


@_attrs_define
class CT:
    """
    Attributes:
        from_crs_authority_code (AuthorityCode | Unset):
        to_crs_authority_code (AuthorityCode | Unset):
        ctdeprecation_info (CTDeprecationInfo | Unset):
        source (str | Unset):
        area_of_use (AreaOfUse | Unset):
        last_modified (str | Unset):
        named_reference (NamedReference | Unset): Name and Persistable Reference (the essence converted to a JSON
            string).
        alias_names (list[str] | Unset):
        essence (Essence | Unset):
        deprecation_info (DeprecationInfo | Unset):
        description (str | Unset):
    """

    from_crs_authority_code: AuthorityCode | Unset = UNSET
    to_crs_authority_code: AuthorityCode | Unset = UNSET
    ctdeprecation_info: CTDeprecationInfo | Unset = UNSET
    source: str | Unset = UNSET
    area_of_use: AreaOfUse | Unset = UNSET
    last_modified: str | Unset = UNSET
    named_reference: NamedReference | Unset = UNSET
    alias_names: list[str] | Unset = UNSET
    essence: Essence | Unset = UNSET
    deprecation_info: DeprecationInfo | Unset = UNSET
    description: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from_crs_authority_code: dict[str, Any] | Unset = UNSET
        if not isinstance(self.from_crs_authority_code, Unset):
            from_crs_authority_code = self.from_crs_authority_code.to_dict()

        to_crs_authority_code: dict[str, Any] | Unset = UNSET
        if not isinstance(self.to_crs_authority_code, Unset):
            to_crs_authority_code = self.to_crs_authority_code.to_dict()

        ctdeprecation_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ctdeprecation_info, Unset):
            ctdeprecation_info = self.ctdeprecation_info.to_dict()

        source = self.source

        area_of_use: dict[str, Any] | Unset = UNSET
        if not isinstance(self.area_of_use, Unset):
            area_of_use = self.area_of_use.to_dict()

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
        if from_crs_authority_code is not UNSET:
            field_dict["fromCRSAuthorityCode"] = from_crs_authority_code
        if to_crs_authority_code is not UNSET:
            field_dict["toCRSAuthorityCode"] = to_crs_authority_code
        if ctdeprecation_info is not UNSET:
            field_dict["ctdeprecationInfo"] = ctdeprecation_info
        if source is not UNSET:
            field_dict["source"] = source
        if area_of_use is not UNSET:
            field_dict["areaOfUse"] = area_of_use
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
        from ..models.area_of_use import AreaOfUse
        from ..models.authority_code import AuthorityCode
        from ..models.ct_deprecation_info import CTDeprecationInfo
        from ..models.deprecation_info import DeprecationInfo
        from ..models.essence import Essence
        from ..models.named_reference import NamedReference

        d = dict(src_dict)
        _from_crs_authority_code = d.pop("fromCRSAuthorityCode", UNSET)
        from_crs_authority_code: AuthorityCode | Unset
        if isinstance(_from_crs_authority_code, Unset):
            from_crs_authority_code = UNSET
        else:
            from_crs_authority_code = AuthorityCode.from_dict(_from_crs_authority_code)

        _to_crs_authority_code = d.pop("toCRSAuthorityCode", UNSET)
        to_crs_authority_code: AuthorityCode | Unset
        if isinstance(_to_crs_authority_code, Unset):
            to_crs_authority_code = UNSET
        else:
            to_crs_authority_code = AuthorityCode.from_dict(_to_crs_authority_code)

        _ctdeprecation_info = d.pop("ctdeprecationInfo", UNSET)
        ctdeprecation_info: CTDeprecationInfo | Unset
        if isinstance(_ctdeprecation_info, Unset):
            ctdeprecation_info = UNSET
        else:
            ctdeprecation_info = CTDeprecationInfo.from_dict(_ctdeprecation_info)

        source = d.pop("source", UNSET)

        _area_of_use = d.pop("areaOfUse", UNSET)
        area_of_use: AreaOfUse | Unset
        if isinstance(_area_of_use, Unset):
            area_of_use = UNSET
        else:
            area_of_use = AreaOfUse.from_dict(_area_of_use)

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

        ct = cls(
            from_crs_authority_code=from_crs_authority_code,
            to_crs_authority_code=to_crs_authority_code,
            ctdeprecation_info=ctdeprecation_info,
            source=source,
            area_of_use=area_of_use,
            last_modified=last_modified,
            named_reference=named_reference,
            alias_names=alias_names,
            essence=essence,
            deprecation_info=deprecation_info,
            description=description,
        )

        ct.additional_properties = d
        return ct

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
