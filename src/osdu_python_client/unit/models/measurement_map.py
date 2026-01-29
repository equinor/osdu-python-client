from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.measurement_map_item import MeasurementMapItem


T = TypeVar("T", bound="MeasurementMap")


@_attrs_define
class MeasurementMap:
    """
    Attributes:
        measurement_map_items (list[MeasurementMapItem] | Unset):
        from_namespace (str | Unset):
        to_namespace (str | Unset):
        measurement_map_item_count (int | Unset):
    """

    measurement_map_items: list[MeasurementMapItem] | Unset = UNSET
    from_namespace: str | Unset = UNSET
    to_namespace: str | Unset = UNSET
    measurement_map_item_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        measurement_map_items: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.measurement_map_items, Unset):
            measurement_map_items = []
            for measurement_map_items_item_data in self.measurement_map_items:
                measurement_map_items_item = measurement_map_items_item_data.to_dict()
                measurement_map_items.append(measurement_map_items_item)

        from_namespace = self.from_namespace

        to_namespace = self.to_namespace

        measurement_map_item_count = self.measurement_map_item_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if measurement_map_items is not UNSET:
            field_dict["measurementMapItems"] = measurement_map_items
        if from_namespace is not UNSET:
            field_dict["fromNamespace"] = from_namespace
        if to_namespace is not UNSET:
            field_dict["toNamespace"] = to_namespace
        if measurement_map_item_count is not UNSET:
            field_dict["measurementMapItemCount"] = measurement_map_item_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.measurement_map_item import MeasurementMapItem

        d = dict(src_dict)
        _measurement_map_items = d.pop("measurementMapItems", UNSET)
        measurement_map_items: list[MeasurementMapItem] | Unset = UNSET
        if _measurement_map_items is not UNSET:
            measurement_map_items = []
            for measurement_map_items_item_data in _measurement_map_items:
                measurement_map_items_item = MeasurementMapItem.from_dict(
                    measurement_map_items_item_data
                )

                measurement_map_items.append(measurement_map_items_item)

        from_namespace = d.pop("fromNamespace", UNSET)

        to_namespace = d.pop("toNamespace", UNSET)

        measurement_map_item_count = d.pop("measurementMapItemCount", UNSET)

        measurement_map = cls(
            measurement_map_items=measurement_map_items,
            from_namespace=from_namespace,
            to_namespace=to_namespace,
            measurement_map_item_count=measurement_map_item_count,
        )

        measurement_map.additional_properties = d
        return measurement_map

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
