from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.authority_code import AuthorityCode
    from ..models.spherical_bounding_box import SphericalBoundingBox


T = TypeVar("T", bound="AreaOfUseEssenceImpl")


@_attrs_define
class AreaOfUseEssenceImpl:
    """the area of use essence

    Attributes:
        name (str | Unset):
        auth_code (AuthorityCode | Unset):
        type_ (str | Unset):
        bound_box (SphericalBoundingBox | Unset):
    """

    name: str | Unset = UNSET
    auth_code: AuthorityCode | Unset = UNSET
    type_: str | Unset = UNSET
    bound_box: SphericalBoundingBox | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        auth_code: dict[str, Any] | Unset = UNSET
        if not isinstance(self.auth_code, Unset):
            auth_code = self.auth_code.to_dict()

        type_ = self.type_

        bound_box: dict[str, Any] | Unset = UNSET
        if not isinstance(self.bound_box, Unset):
            bound_box = self.bound_box.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if auth_code is not UNSET:
            field_dict["authCode"] = auth_code
        if type_ is not UNSET:
            field_dict["type"] = type_
        if bound_box is not UNSET:
            field_dict["boundBox"] = bound_box

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.authority_code import AuthorityCode
        from ..models.spherical_bounding_box import SphericalBoundingBox

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        _auth_code = d.pop("authCode", UNSET)
        auth_code: AuthorityCode | Unset
        if isinstance(_auth_code, Unset):
            auth_code = UNSET
        else:
            auth_code = AuthorityCode.from_dict(_auth_code)

        type_ = d.pop("type", UNSET)

        _bound_box = d.pop("boundBox", UNSET)
        bound_box: SphericalBoundingBox | Unset
        if isinstance(_bound_box, Unset):
            bound_box = UNSET
        else:
            bound_box = SphericalBoundingBox.from_dict(_bound_box)

        area_of_use_essence_impl = cls(
            name=name,
            auth_code=auth_code,
            type_=type_,
            bound_box=bound_box,
        )

        area_of_use_essence_impl.additional_properties = d
        return area_of_use_essence_impl

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
