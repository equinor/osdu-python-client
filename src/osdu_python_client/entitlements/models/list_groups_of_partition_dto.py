from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.parent_reference import ParentReference


T = TypeVar("T", bound="ListGroupsOfPartitionDto")


@_attrs_define
class ListGroupsOfPartitionDto:
    """Represents a List Group of Partition model.

    Attributes:
        groups (list[ParentReference] | Unset): Represents a List of Groups
        cursor (str | Unset): cursor
        total_count (int | Unset): Total Count
    """

    groups: list[ParentReference] | Unset = UNSET
    cursor: str | Unset = UNSET
    total_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        groups: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.groups, Unset):
            groups = []
            for groups_item_data in self.groups:
                groups_item = groups_item_data.to_dict()
                groups.append(groups_item)

        cursor = self.cursor

        total_count = self.total_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if groups is not UNSET:
            field_dict["groups"] = groups
        if cursor is not UNSET:
            field_dict["cursor"] = cursor
        if total_count is not UNSET:
            field_dict["totalCount"] = total_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.parent_reference import ParentReference

        d = dict(src_dict)
        _groups = d.pop("groups", UNSET)
        groups: list[ParentReference] | Unset = UNSET
        if _groups is not UNSET:
            groups = []
            for groups_item_data in _groups:
                groups_item = ParentReference.from_dict(groups_item_data)

                groups.append(groups_item)

        cursor = d.pop("cursor", UNSET)

        total_count = d.pop("totalCount", UNSET)

        list_groups_of_partition_dto = cls(
            groups=groups,
            cursor=cursor,
            total_count=total_count,
        )

        list_groups_of_partition_dto.additional_properties = d
        return list_groups_of_partition_dto

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
