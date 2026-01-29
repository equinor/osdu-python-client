from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateGroupOperation")


@_attrs_define
class UpdateGroupOperation:
    """Represents a model for the Update Group Operation

    Attributes:
        path (str | Unset): Update Group Path
        value (list[str] | Unset): list of values to be updated
        op (str | Unset): Update Group Operation
    """

    path: str | Unset = UNSET
    value: list[str] | Unset = UNSET
    op: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        path = self.path

        value: list[str] | Unset = UNSET
        if not isinstance(self.value, Unset):
            value = self.value

        op = self.op

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if path is not UNSET:
            field_dict["path"] = path
        if value is not UNSET:
            field_dict["value"] = value
        if op is not UNSET:
            field_dict["op"] = op

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        path = d.pop("path", UNSET)

        value = cast(list[str], d.pop("value", UNSET))

        op = d.pop("op", UNSET)

        update_group_operation = cls(
            path=path,
            value=value,
            op=op,
        )

        update_group_operation.additional_properties = d
        return update_group_operation

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
