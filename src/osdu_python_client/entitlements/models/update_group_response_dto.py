from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateGroupResponseDto")


@_attrs_define
class UpdateGroupResponseDto:
    """Represents a model for the Update Group Response

    Attributes:
        name (str | Unset): Name of the Updated Group
        email (str | Unset): Email of the Updated Group
        app_ids (list[str] | Unset): List of AppId of the Updated Group
    """

    name: str | Unset = UNSET
    email: str | Unset = UNSET
    app_ids: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        email = self.email

        app_ids: list[str] | Unset = UNSET
        if not isinstance(self.app_ids, Unset):
            app_ids = self.app_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if email is not UNSET:
            field_dict["email"] = email
        if app_ids is not UNSET:
            field_dict["appIds"] = app_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        email = d.pop("email", UNSET)

        app_ids = cast(list[str], d.pop("appIds", UNSET))

        update_group_response_dto = cls(
            name=name,
            email=email,
            app_ids=app_ids,
        )

        update_group_response_dto.additional_properties = d
        return update_group_response_dto

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
