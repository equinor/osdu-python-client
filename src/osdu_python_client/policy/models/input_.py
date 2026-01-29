from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.input_operation import InputOperation
from ..types import UNSET, Unset

T = TypeVar("T", bound="Input")


@_attrs_define
class Input:
    """
    Attributes:
        operation (InputOperation):
        groups (list[str] | None | Unset):
        xuserid (None | str | Unset):  Default: ''.
        token (None | str | Unset):  Default: ''.
        datapartitionid (None | str | Unset):  Default: ''.
    """

    operation: InputOperation
    groups: list[str] | None | Unset = UNSET
    xuserid: None | str | Unset = ""
    token: None | str | Unset = ""
    datapartitionid: None | str | Unset = ""
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        operation = self.operation.value

        groups: list[str] | None | Unset
        if isinstance(self.groups, Unset):
            groups = UNSET
        elif isinstance(self.groups, list):
            groups = self.groups

        else:
            groups = self.groups

        xuserid: None | str | Unset
        if isinstance(self.xuserid, Unset):
            xuserid = UNSET
        else:
            xuserid = self.xuserid

        token: None | str | Unset
        if isinstance(self.token, Unset):
            token = UNSET
        else:
            token = self.token

        datapartitionid: None | str | Unset
        if isinstance(self.datapartitionid, Unset):
            datapartitionid = UNSET
        else:
            datapartitionid = self.datapartitionid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "operation": operation,
            }
        )
        if groups is not UNSET:
            field_dict["groups"] = groups
        if xuserid is not UNSET:
            field_dict["xuserid"] = xuserid
        if token is not UNSET:
            field_dict["token"] = token
        if datapartitionid is not UNSET:
            field_dict["datapartitionid"] = datapartitionid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        operation = InputOperation(d.pop("operation"))

        def _parse_groups(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                groups_type_0 = cast(list[str], data)

                return groups_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        groups = _parse_groups(d.pop("groups", UNSET))

        def _parse_xuserid(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        xuserid = _parse_xuserid(d.pop("xuserid", UNSET))

        def _parse_token(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        token = _parse_token(d.pop("token", UNSET))

        def _parse_datapartitionid(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        datapartitionid = _parse_datapartitionid(d.pop("datapartitionid", UNSET))

        input_ = cls(
            operation=operation,
            groups=groups,
            xuserid=xuserid,
            token=token,
            datapartitionid=datapartitionid,
        )

        input_.additional_properties = d
        return input_

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
