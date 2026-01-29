from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.parent_reference import ParentReference


T = TypeVar("T", bound="ListGroupResponseDto")


@_attrs_define
class ListGroupResponseDto:
    """Represents a model for List Group Response.

    Attributes:
        des_id (str | Unset): desId
        member_email (str | Unset): member email
        groups (list[ParentReference] | Unset): Represents a List of Groups
    """

    des_id: str | Unset = UNSET
    member_email: str | Unset = UNSET
    groups: list[ParentReference] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        des_id = self.des_id

        member_email = self.member_email

        groups: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.groups, Unset):
            groups = []
            for groups_item_data in self.groups:
                groups_item = groups_item_data.to_dict()
                groups.append(groups_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if des_id is not UNSET:
            field_dict["desId"] = des_id
        if member_email is not UNSET:
            field_dict["memberEmail"] = member_email
        if groups is not UNSET:
            field_dict["groups"] = groups

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.parent_reference import ParentReference

        d = dict(src_dict)
        des_id = d.pop("desId", UNSET)

        member_email = d.pop("memberEmail", UNSET)

        _groups = d.pop("groups", UNSET)
        groups: list[ParentReference] | Unset = UNSET
        if _groups is not UNSET:
            groups = []
            for groups_item_data in _groups:
                groups_item = ParentReference.from_dict(groups_item_data)

                groups.append(groups_item)

        list_group_response_dto = cls(
            des_id=des_id,
            member_email=member_email,
            groups=groups,
        )

        list_group_response_dto.additional_properties = d
        return list_group_response_dto

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
