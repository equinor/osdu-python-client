from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.authority_code import AuthorityCode


T = TypeVar("T", bound="SingleCTEssenceImpl")


@_attrs_define
class SingleCTEssenceImpl:
    """Single cartographic transformation.

    Attributes:
        auth_code (AuthorityCode | Unset):
        type_ (str | Unset):
        ver (str | Unset):
        name (str | Unset):
        wkt (str | Unset):
    """

    auth_code: AuthorityCode | Unset = UNSET
    type_: str | Unset = UNSET
    ver: str | Unset = UNSET
    name: str | Unset = UNSET
    wkt: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        auth_code: dict[str, Any] | Unset = UNSET
        if not isinstance(self.auth_code, Unset):
            auth_code = self.auth_code.to_dict()

        type_ = self.type_

        ver = self.ver

        name = self.name

        wkt = self.wkt

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if auth_code is not UNSET:
            field_dict["authCode"] = auth_code
        if type_ is not UNSET:
            field_dict["type"] = type_
        if ver is not UNSET:
            field_dict["ver"] = ver
        if name is not UNSET:
            field_dict["name"] = name
        if wkt is not UNSET:
            field_dict["wkt"] = wkt

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.authority_code import AuthorityCode

        d = dict(src_dict)
        _auth_code = d.pop("authCode", UNSET)
        auth_code: AuthorityCode | Unset
        if isinstance(_auth_code, Unset):
            auth_code = UNSET
        else:
            auth_code = AuthorityCode.from_dict(_auth_code)

        type_ = d.pop("type", UNSET)

        ver = d.pop("ver", UNSET)

        name = d.pop("name", UNSET)

        wkt = d.pop("wkt", UNSET)

        single_ct_essence_impl = cls(
            auth_code=auth_code,
            type_=type_,
            ver=ver,
            name=name,
            wkt=wkt,
        )

        single_ct_essence_impl.additional_properties = d
        return single_ct_essence_impl

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
