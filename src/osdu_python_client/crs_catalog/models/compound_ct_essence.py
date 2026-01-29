from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.authority_code import AuthorityCode
    from ..models.ct_essence import CTEssence


T = TypeVar("T", bound="CompoundCTEssence")


@_attrs_define
class CompoundCTEssence:
    """
    Attributes:
        ctauthority_codes (list[AuthorityCode] | Unset):
        ctessences (list[CTEssence] | Unset):
        policy (str | Unset):
        name (str | Unset):
        type_ (str | Unset):
        engine_version (str | Unset):
        authority_code (AuthorityCode | Unset):
    """

    ctauthority_codes: list[AuthorityCode] | Unset = UNSET
    ctessences: list[CTEssence] | Unset = UNSET
    policy: str | Unset = UNSET
    name: str | Unset = UNSET
    type_: str | Unset = UNSET
    engine_version: str | Unset = UNSET
    authority_code: AuthorityCode | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ctauthority_codes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.ctauthority_codes, Unset):
            ctauthority_codes = []
            for ctauthority_codes_item_data in self.ctauthority_codes:
                ctauthority_codes_item = ctauthority_codes_item_data.to_dict()
                ctauthority_codes.append(ctauthority_codes_item)

        ctessences: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.ctessences, Unset):
            ctessences = []
            for ctessences_item_data in self.ctessences:
                ctessences_item = ctessences_item_data.to_dict()
                ctessences.append(ctessences_item)

        policy = self.policy

        name = self.name

        type_ = self.type_

        engine_version = self.engine_version

        authority_code: dict[str, Any] | Unset = UNSET
        if not isinstance(self.authority_code, Unset):
            authority_code = self.authority_code.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ctauthority_codes is not UNSET:
            field_dict["ctauthorityCodes"] = ctauthority_codes
        if ctessences is not UNSET:
            field_dict["ctessences"] = ctessences
        if policy is not UNSET:
            field_dict["policy"] = policy
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
        from ..models.ct_essence import CTEssence

        d = dict(src_dict)
        _ctauthority_codes = d.pop("ctauthorityCodes", UNSET)
        ctauthority_codes: list[AuthorityCode] | Unset = UNSET
        if _ctauthority_codes is not UNSET:
            ctauthority_codes = []
            for ctauthority_codes_item_data in _ctauthority_codes:
                ctauthority_codes_item = AuthorityCode.from_dict(
                    ctauthority_codes_item_data
                )

                ctauthority_codes.append(ctauthority_codes_item)

        _ctessences = d.pop("ctessences", UNSET)
        ctessences: list[CTEssence] | Unset = UNSET
        if _ctessences is not UNSET:
            ctessences = []
            for ctessences_item_data in _ctessences:
                ctessences_item = CTEssence.from_dict(ctessences_item_data)

                ctessences.append(ctessences_item)

        policy = d.pop("policy", UNSET)

        name = d.pop("name", UNSET)

        type_ = d.pop("type", UNSET)

        engine_version = d.pop("engineVersion", UNSET)

        _authority_code = d.pop("authorityCode", UNSET)
        authority_code: AuthorityCode | Unset
        if isinstance(_authority_code, Unset):
            authority_code = UNSET
        else:
            authority_code = AuthorityCode.from_dict(_authority_code)

        compound_ct_essence = cls(
            ctauthority_codes=ctauthority_codes,
            ctessences=ctessences,
            policy=policy,
            name=name,
            type_=type_,
            engine_version=engine_version,
            authority_code=authority_code,
        )

        compound_ct_essence.additional_properties = d
        return compound_ct_essence

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
