from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="QueryLegalTag")


@_attrs_define
class QueryLegalTag:
    """Represents the Search Query objects for Legaltags.

    Attributes:
        query_list (list[str]): Filter condition query
        operator_list (list[str] | Unset): If there are multiple conditions need to be joined in by logical operators
        sort_by (str | Unset):
        sort_order (str | Unset):
        limit (int | Unset):
    """

    query_list: list[str]
    operator_list: list[str] | Unset = UNSET
    sort_by: str | Unset = UNSET
    sort_order: str | Unset = UNSET
    limit: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        query_list = self.query_list

        operator_list: list[str] | Unset = UNSET
        if not isinstance(self.operator_list, Unset):
            operator_list = self.operator_list

        sort_by = self.sort_by

        sort_order = self.sort_order

        limit = self.limit

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "queryList": query_list,
            }
        )
        if operator_list is not UNSET:
            field_dict["operatorList"] = operator_list
        if sort_by is not UNSET:
            field_dict["sortBy"] = sort_by
        if sort_order is not UNSET:
            field_dict["sortOrder"] = sort_order
        if limit is not UNSET:
            field_dict["limit"] = limit

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        query_list = cast(list[str], d.pop("queryList"))

        operator_list = cast(list[str], d.pop("operatorList", UNSET))

        sort_by = d.pop("sortBy", UNSET)

        sort_order = d.pop("sortOrder", UNSET)

        limit = d.pop("limit", UNSET)

        query_legal_tag = cls(
            query_list=query_list,
            operator_list=operator_list,
            sort_by=sort_by,
            sort_order=sort_order,
            limit=limit,
        )

        query_legal_tag.additional_properties = d
        return query_legal_tag

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
