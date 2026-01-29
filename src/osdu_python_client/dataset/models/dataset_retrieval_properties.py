from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dataset_retrieval_properties_retrieval_properties import (
        DatasetRetrievalPropertiesRetrievalProperties,
    )


T = TypeVar("T", bound="DatasetRetrievalProperties")


@_attrs_define
class DatasetRetrievalProperties:
    """
    Attributes:
        dataset_registry_id (str | Unset):
        retrieval_properties (DatasetRetrievalPropertiesRetrievalProperties | Unset):
        provider_key (str | Unset):
    """

    dataset_registry_id: str | Unset = UNSET
    retrieval_properties: DatasetRetrievalPropertiesRetrievalProperties | Unset = UNSET
    provider_key: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dataset_registry_id = self.dataset_registry_id

        retrieval_properties: dict[str, Any] | Unset = UNSET
        if not isinstance(self.retrieval_properties, Unset):
            retrieval_properties = self.retrieval_properties.to_dict()

        provider_key = self.provider_key

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if dataset_registry_id is not UNSET:
            field_dict["datasetRegistryId"] = dataset_registry_id
        if retrieval_properties is not UNSET:
            field_dict["retrievalProperties"] = retrieval_properties
        if provider_key is not UNSET:
            field_dict["providerKey"] = provider_key

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dataset_retrieval_properties_retrieval_properties import (
            DatasetRetrievalPropertiesRetrievalProperties,
        )

        d = dict(src_dict)
        dataset_registry_id = d.pop("datasetRegistryId", UNSET)

        _retrieval_properties = d.pop("retrievalProperties", UNSET)
        retrieval_properties: DatasetRetrievalPropertiesRetrievalProperties | Unset
        if isinstance(_retrieval_properties, Unset):
            retrieval_properties = UNSET
        else:
            retrieval_properties = (
                DatasetRetrievalPropertiesRetrievalProperties.from_dict(
                    _retrieval_properties
                )
            )

        provider_key = d.pop("providerKey", UNSET)

        dataset_retrieval_properties = cls(
            dataset_registry_id=dataset_registry_id,
            retrieval_properties=retrieval_properties,
            provider_key=provider_key,
        )

        dataset_retrieval_properties.additional_properties = d
        return dataset_retrieval_properties

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
