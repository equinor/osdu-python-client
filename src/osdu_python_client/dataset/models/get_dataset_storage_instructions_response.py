from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_dataset_storage_instructions_response_storage_location import (
        GetDatasetStorageInstructionsResponseStorageLocation,
    )


T = TypeVar("T", bound="GetDatasetStorageInstructionsResponse")


@_attrs_define
class GetDatasetStorageInstructionsResponse:
    """
    Attributes:
        storage_location (GetDatasetStorageInstructionsResponseStorageLocation | Unset):
        provider_key (str | Unset):
    """

    storage_location: GetDatasetStorageInstructionsResponseStorageLocation | Unset = (
        UNSET
    )
    provider_key: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        storage_location: dict[str, Any] | Unset = UNSET
        if not isinstance(self.storage_location, Unset):
            storage_location = self.storage_location.to_dict()

        provider_key = self.provider_key

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if storage_location is not UNSET:
            field_dict["storageLocation"] = storage_location
        if provider_key is not UNSET:
            field_dict["providerKey"] = provider_key

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_dataset_storage_instructions_response_storage_location import (
            GetDatasetStorageInstructionsResponseStorageLocation,
        )

        d = dict(src_dict)
        _storage_location = d.pop("storageLocation", UNSET)
        storage_location: GetDatasetStorageInstructionsResponseStorageLocation | Unset
        if isinstance(_storage_location, Unset):
            storage_location = UNSET
        else:
            storage_location = (
                GetDatasetStorageInstructionsResponseStorageLocation.from_dict(
                    _storage_location
                )
            )

        provider_key = d.pop("providerKey", UNSET)

        get_dataset_storage_instructions_response = cls(
            storage_location=storage_location,
            provider_key=provider_key,
        )

        get_dataset_storage_instructions_response.additional_properties = d
        return get_dataset_storage_instructions_response

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
