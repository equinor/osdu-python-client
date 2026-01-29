from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.authority_code import AuthorityCode
    from ..models.crs_essence import CRSEssence


T = TypeVar("T", bound="CompoundCRSEssence")


@_attrs_define
class CompoundCRSEssence:
    """
    Attributes:
        horizontal_crs_authority_code (AuthorityCode | Unset):
        vertical_crs_authority_code (AuthorityCode | Unset):
        horizontal_crs_essence (CRSEssence | Unset):
        vertical_crs_essence (CRSEssence | Unset):
        name (str | Unset):
        type_ (str | Unset):
        engine_version (str | Unset):
        authority_code (AuthorityCode | Unset):
    """

    horizontal_crs_authority_code: AuthorityCode | Unset = UNSET
    vertical_crs_authority_code: AuthorityCode | Unset = UNSET
    horizontal_crs_essence: CRSEssence | Unset = UNSET
    vertical_crs_essence: CRSEssence | Unset = UNSET
    name: str | Unset = UNSET
    type_: str | Unset = UNSET
    engine_version: str | Unset = UNSET
    authority_code: AuthorityCode | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        horizontal_crs_authority_code: dict[str, Any] | Unset = UNSET
        if not isinstance(self.horizontal_crs_authority_code, Unset):
            horizontal_crs_authority_code = self.horizontal_crs_authority_code.to_dict()

        vertical_crs_authority_code: dict[str, Any] | Unset = UNSET
        if not isinstance(self.vertical_crs_authority_code, Unset):
            vertical_crs_authority_code = self.vertical_crs_authority_code.to_dict()

        horizontal_crs_essence: dict[str, Any] | Unset = UNSET
        if not isinstance(self.horizontal_crs_essence, Unset):
            horizontal_crs_essence = self.horizontal_crs_essence.to_dict()

        vertical_crs_essence: dict[str, Any] | Unset = UNSET
        if not isinstance(self.vertical_crs_essence, Unset):
            vertical_crs_essence = self.vertical_crs_essence.to_dict()

        name = self.name

        type_ = self.type_

        engine_version = self.engine_version

        authority_code: dict[str, Any] | Unset = UNSET
        if not isinstance(self.authority_code, Unset):
            authority_code = self.authority_code.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if horizontal_crs_authority_code is not UNSET:
            field_dict["horizontalCRSAuthorityCode"] = horizontal_crs_authority_code
        if vertical_crs_authority_code is not UNSET:
            field_dict["verticalCRSAuthorityCode"] = vertical_crs_authority_code
        if horizontal_crs_essence is not UNSET:
            field_dict["horizontalCRSEssence"] = horizontal_crs_essence
        if vertical_crs_essence is not UNSET:
            field_dict["verticalCRSEssence"] = vertical_crs_essence
        if name is not UNSET:
            field_dict["name"] = name
        if type_ is not UNSET:
            field_dict["type"] = type_
        if engine_version is not UNSET:
            field_dict["engineVersion"] = engine_version
        if authority_code is not UNSET:
            field_dict["authorityCode"] = authority_code

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.authority_code import AuthorityCode
        from ..models.crs_essence import CRSEssence

        d = dict(src_dict)
        _horizontal_crs_authority_code = d.pop("horizontalCRSAuthorityCode", UNSET)
        horizontal_crs_authority_code: AuthorityCode | Unset
        if isinstance(_horizontal_crs_authority_code, Unset):
            horizontal_crs_authority_code = UNSET
        else:
            horizontal_crs_authority_code = AuthorityCode.from_dict(
                _horizontal_crs_authority_code
            )

        _vertical_crs_authority_code = d.pop("verticalCRSAuthorityCode", UNSET)
        vertical_crs_authority_code: AuthorityCode | Unset
        if isinstance(_vertical_crs_authority_code, Unset):
            vertical_crs_authority_code = UNSET
        else:
            vertical_crs_authority_code = AuthorityCode.from_dict(
                _vertical_crs_authority_code
            )

        _horizontal_crs_essence = d.pop("horizontalCRSEssence", UNSET)
        horizontal_crs_essence: CRSEssence | Unset
        if isinstance(_horizontal_crs_essence, Unset):
            horizontal_crs_essence = UNSET
        else:
            horizontal_crs_essence = CRSEssence.from_dict(_horizontal_crs_essence)

        _vertical_crs_essence = d.pop("verticalCRSEssence", UNSET)
        vertical_crs_essence: CRSEssence | Unset
        if isinstance(_vertical_crs_essence, Unset):
            vertical_crs_essence = UNSET
        else:
            vertical_crs_essence = CRSEssence.from_dict(_vertical_crs_essence)

        name = d.pop("name", UNSET)

        type_ = d.pop("type", UNSET)

        engine_version = d.pop("engineVersion", UNSET)

        _authority_code = d.pop("authorityCode", UNSET)
        authority_code: AuthorityCode | Unset
        if isinstance(_authority_code, Unset):
            authority_code = UNSET
        else:
            authority_code = AuthorityCode.from_dict(_authority_code)

        compound_crs_essence = cls(
            horizontal_crs_authority_code=horizontal_crs_authority_code,
            vertical_crs_authority_code=vertical_crs_authority_code,
            horizontal_crs_essence=horizontal_crs_essence,
            vertical_crs_essence=vertical_crs_essence,
            name=name,
            type_=type_,
            engine_version=engine_version,
            authority_code=authority_code,
        )

        compound_crs_essence.additional_properties = d
        return compound_crs_essence

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
