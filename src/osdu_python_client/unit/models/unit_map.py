from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.unit_map_item import UnitMapItem


T = TypeVar("T", bound="UnitMap")


@_attrs_define
class UnitMap:
    """
    Attributes:
        unit_map_items (list[UnitMapItem] | Unset):
        from_namespace (str | Unset):
        to_namespace (str | Unset):
        unit_map_item_count (int | Unset):
    """

    unit_map_items: list[UnitMapItem] | Unset = UNSET
    from_namespace: str | Unset = UNSET
    to_namespace: str | Unset = UNSET
    unit_map_item_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        unit_map_items: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.unit_map_items, Unset):
            unit_map_items = []
            for unit_map_items_item_data in self.unit_map_items:
                unit_map_items_item = unit_map_items_item_data.to_dict()
                unit_map_items.append(unit_map_items_item)

        from_namespace = self.from_namespace

        to_namespace = self.to_namespace

        unit_map_item_count = self.unit_map_item_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if unit_map_items is not UNSET:
            field_dict["unitMapItems"] = unit_map_items
        if from_namespace is not UNSET:
            field_dict["fromNamespace"] = from_namespace
        if to_namespace is not UNSET:
            field_dict["toNamespace"] = to_namespace
        if unit_map_item_count is not UNSET:
            field_dict["unitMapItemCount"] = unit_map_item_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.unit_map_item import UnitMapItem

        d = dict(src_dict)
        _unit_map_items = d.pop("unitMapItems", UNSET)
        unit_map_items: list[UnitMapItem] | Unset = UNSET
        if _unit_map_items is not UNSET:
            unit_map_items = []
            for unit_map_items_item_data in _unit_map_items:
                unit_map_items_item = UnitMapItem.from_dict(unit_map_items_item_data)

                unit_map_items.append(unit_map_items_item)

        from_namespace = d.pop("fromNamespace", UNSET)

        to_namespace = d.pop("toNamespace", UNSET)

        unit_map_item_count = d.pop("unitMapItemCount", UNSET)

        unit_map = cls(
            unit_map_items=unit_map_items,
            from_namespace=from_namespace,
            to_namespace=to_namespace,
            unit_map_item_count=unit_map_item_count,
        )

        unit_map.additional_properties = d
        return unit_map

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
