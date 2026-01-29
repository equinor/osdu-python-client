from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.record import Record


T = TypeVar("T", bound="CreateDatasetRegistryRequest")


@_attrs_define
class CreateDatasetRegistryRequest:
    """Dataset registry ids

    Attributes:
        dataset_registries (list[Record]):
    """

    dataset_registries: list[Record]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dataset_registries = []
        for dataset_registries_item_data in self.dataset_registries:
            dataset_registries_item = dataset_registries_item_data.to_dict()
            dataset_registries.append(dataset_registries_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "datasetRegistries": dataset_registries,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.record import Record

        d = dict(src_dict)
        dataset_registries = []
        _dataset_registries = d.pop("datasetRegistries")
        for dataset_registries_item_data in _dataset_registries:
            dataset_registries_item = Record.from_dict(dataset_registries_item_data)

            dataset_registries.append(dataset_registries_item)

        create_dataset_registry_request = cls(
            dataset_registries=dataset_registries,
        )

        create_dataset_registry_request.additional_properties = d
        return create_dataset_registry_request

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
