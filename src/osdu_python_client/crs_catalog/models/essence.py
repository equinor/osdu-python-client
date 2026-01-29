from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.authority_code import AuthorityCode


T = TypeVar("T", bound="Essence")


@_attrs_define
class Essence:
    """
    Attributes:
        type_ (str | Unset):
        authority_code (AuthorityCode | Unset):
    """

    type_: str | Unset = UNSET
    authority_code: AuthorityCode | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        authority_code: dict[str, Any] | Unset = UNSET
        if not isinstance(self.authority_code, Unset):
            authority_code = self.authority_code.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if authority_code is not UNSET:
            field_dict["authorityCode"] = authority_code

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.authority_code import AuthorityCode

        d = dict(src_dict)
        type_ = d.pop("type", UNSET)

        _authority_code = d.pop("authorityCode", UNSET)
        authority_code: AuthorityCode | Unset
        if isinstance(_authority_code, Unset):
            authority_code = UNSET
        else:
            authority_code = AuthorityCode.from_dict(_authority_code)

        essence = cls(
            type_=type_,
            authority_code=authority_code,
        )

        essence.additional_properties = d
        return essence

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
