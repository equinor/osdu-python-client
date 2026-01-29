from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.sort_query_order_item import SortQueryOrderItem
from ..types import UNSET, Unset

T = TypeVar("T", bound="SortQuery")


@_attrs_define
class SortQuery:
    """
    Attributes:
        field (list[str] | Unset):
        order (list[SortQueryOrderItem] | Unset):
        filter_ (list[str] | Unset):
    """

    field: list[str] | Unset = UNSET
    order: list[SortQueryOrderItem] | Unset = UNSET
    filter_: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field: list[str] | Unset = UNSET
        if not isinstance(self.field, Unset):
            field = self.field

        order: list[str] | Unset = UNSET
        if not isinstance(self.order, Unset):
            order = []
            for order_item_data in self.order:
                order_item = order_item_data.value
                order.append(order_item)

        filter_: list[str] | Unset = UNSET
        if not isinstance(self.filter_, Unset):
            filter_ = self.filter_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field is not UNSET:
            field_dict["field"] = field
        if order is not UNSET:
            field_dict["order"] = order
        if filter_ is not UNSET:
            field_dict["filter"] = filter_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        field = cast(list[str], d.pop("field", UNSET))

        _order = d.pop("order", UNSET)
        order: list[SortQueryOrderItem] | Unset = UNSET
        if _order is not UNSET:
            order = []
            for order_item_data in _order:
                order_item = SortQueryOrderItem(order_item_data)

                order.append(order_item)

        filter_ = cast(list[str], d.pop("filter", UNSET))

        sort_query = cls(
            field=field,
            order=order,
            filter_=filter_,
        )

        sort_query.additional_properties = d
        return sort_query

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
