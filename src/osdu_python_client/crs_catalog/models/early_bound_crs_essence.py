from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.authority_code import AuthorityCode
    from ..models.ct_essence import CTEssence
    from ..models.late_bound_crs_essence import LateBoundCRSEssence


T = TypeVar("T", bound="EarlyBoundCRSEssence")


@_attrs_define
class EarlyBoundCRSEssence:
    """
    Attributes:
        ctauthority_code (AuthorityCode | Unset):
        late_bound_crs_authority_code (AuthorityCode | Unset):
        ctessence (CTEssence | Unset):
        late_bound_crs_essence (LateBoundCRSEssence | Unset):
        name (str | Unset):
        type_ (str | Unset):
        engine_version (str | Unset):
        authority_code (AuthorityCode | Unset):
    """

    ctauthority_code: AuthorityCode | Unset = UNSET
    late_bound_crs_authority_code: AuthorityCode | Unset = UNSET
    ctessence: CTEssence | Unset = UNSET
    late_bound_crs_essence: LateBoundCRSEssence | Unset = UNSET
    name: str | Unset = UNSET
    type_: str | Unset = UNSET
    engine_version: str | Unset = UNSET
    authority_code: AuthorityCode | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ctauthority_code: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ctauthority_code, Unset):
            ctauthority_code = self.ctauthority_code.to_dict()

        late_bound_crs_authority_code: dict[str, Any] | Unset = UNSET
        if not isinstance(self.late_bound_crs_authority_code, Unset):
            late_bound_crs_authority_code = self.late_bound_crs_authority_code.to_dict()

        ctessence: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ctessence, Unset):
            ctessence = self.ctessence.to_dict()

        late_bound_crs_essence: dict[str, Any] | Unset = UNSET
        if not isinstance(self.late_bound_crs_essence, Unset):
            late_bound_crs_essence = self.late_bound_crs_essence.to_dict()

        name = self.name

        type_ = self.type_

        engine_version = self.engine_version

        authority_code: dict[str, Any] | Unset = UNSET
        if not isinstance(self.authority_code, Unset):
            authority_code = self.authority_code.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ctauthority_code is not UNSET:
            field_dict["ctauthorityCode"] = ctauthority_code
        if late_bound_crs_authority_code is not UNSET:
            field_dict["lateBoundCRSAuthorityCode"] = late_bound_crs_authority_code
        if ctessence is not UNSET:
            field_dict["ctessence"] = ctessence
        if late_bound_crs_essence is not UNSET:
            field_dict["lateBoundCRSEssence"] = late_bound_crs_essence
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
        from ..models.late_bound_crs_essence import LateBoundCRSEssence

        d = dict(src_dict)
        _ctauthority_code = d.pop("ctauthorityCode", UNSET)
        ctauthority_code: AuthorityCode | Unset
        if isinstance(_ctauthority_code, Unset):
            ctauthority_code = UNSET
        else:
            ctauthority_code = AuthorityCode.from_dict(_ctauthority_code)

        _late_bound_crs_authority_code = d.pop("lateBoundCRSAuthorityCode", UNSET)
        late_bound_crs_authority_code: AuthorityCode | Unset
        if isinstance(_late_bound_crs_authority_code, Unset):
            late_bound_crs_authority_code = UNSET
        else:
            late_bound_crs_authority_code = AuthorityCode.from_dict(
                _late_bound_crs_authority_code
            )

        _ctessence = d.pop("ctessence", UNSET)
        ctessence: CTEssence | Unset
        if isinstance(_ctessence, Unset):
            ctessence = UNSET
        else:
            ctessence = CTEssence.from_dict(_ctessence)

        _late_bound_crs_essence = d.pop("lateBoundCRSEssence", UNSET)
        late_bound_crs_essence: LateBoundCRSEssence | Unset
        if isinstance(_late_bound_crs_essence, Unset):
            late_bound_crs_essence = UNSET
        else:
            late_bound_crs_essence = LateBoundCRSEssence.from_dict(
                _late_bound_crs_essence
            )

        name = d.pop("name", UNSET)

        type_ = d.pop("type", UNSET)

        engine_version = d.pop("engineVersion", UNSET)

        _authority_code = d.pop("authorityCode", UNSET)
        authority_code: AuthorityCode | Unset
        if isinstance(_authority_code, Unset):
            authority_code = UNSET
        else:
            authority_code = AuthorityCode.from_dict(_authority_code)

        early_bound_crs_essence = cls(
            ctauthority_code=ctauthority_code,
            late_bound_crs_authority_code=late_bound_crs_authority_code,
            ctessence=ctessence,
            late_bound_crs_essence=late_bound_crs_essence,
            name=name,
            type_=type_,
            engine_version=engine_version,
            authority_code=authority_code,
        )

        early_bound_crs_essence.additional_properties = d
        return early_bound_crs_essence

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
