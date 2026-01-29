from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.member_dto_member_type import MemberDtoMemberType
from ..models.member_dto_role import MemberDtoRole
from ..types import UNSET, Unset

T = TypeVar("T", bound="MemberDto")


@_attrs_define
class MemberDto:
    """Represents a model for the Member

    Attributes:
        email (str | Unset): Email Id of the member
        role (MemberDtoRole | Unset): Role of the member
        member_type (MemberDtoMemberType | Unset): Type of the member
        data_partition_id (str | Unset): dataPartitionId
    """

    email: str | Unset = UNSET
    role: MemberDtoRole | Unset = UNSET
    member_type: MemberDtoMemberType | Unset = UNSET
    data_partition_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        email = self.email

        role: str | Unset = UNSET
        if not isinstance(self.role, Unset):
            role = self.role.value

        member_type: str | Unset = UNSET
        if not isinstance(self.member_type, Unset):
            member_type = self.member_type.value

        data_partition_id = self.data_partition_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if email is not UNSET:
            field_dict["email"] = email
        if role is not UNSET:
            field_dict["role"] = role
        if member_type is not UNSET:
            field_dict["memberType"] = member_type
        if data_partition_id is not UNSET:
            field_dict["dataPartitionId"] = data_partition_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        email = d.pop("email", UNSET)

        _role = d.pop("role", UNSET)
        role: MemberDtoRole | Unset
        if isinstance(_role, Unset):
            role = UNSET
        else:
            role = MemberDtoRole(_role)

        _member_type = d.pop("memberType", UNSET)
        member_type: MemberDtoMemberType | Unset
        if isinstance(_member_type, Unset):
            member_type = UNSET
        else:
            member_type = MemberDtoMemberType(_member_type)

        data_partition_id = d.pop("dataPartitionId", UNSET)

        member_dto = cls(
            email=email,
            role=role,
            member_type=member_type,
            data_partition_id=data_partition_id,
        )

        member_dto.additional_properties = d
        return member_dto

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
