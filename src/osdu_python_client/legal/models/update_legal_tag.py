from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_legal_tag_extension_properties import (
        UpdateLegalTagExtensionProperties,
    )


T = TypeVar("T", bound="UpdateLegalTag")


@_attrs_define
class UpdateLegalTag:
    """The model to update an existing LegalTag

    Attributes:
        name (str | Unset): The name of the LegalTag Example: OSDU-Private-EHCData.
        contract_id (str | Unset): The Id of the physical contract associated with the data being ingested. Example: No
            Contract Related.
        description (str | Unset): The optional description if the LegalTag to allow for easier discoverability of
            Legaltags overtime.
        expiration_date (datetime.datetime | Unset): The optional expiration date of the contract in the format YYYY-MM-
            DD Example: 2025-12-25.
        extension_properties (UpdateLegalTagExtensionProperties | Unset): The optional object field to attach any
            company specific attributes.
    """

    name: str | Unset = UNSET
    contract_id: str | Unset = UNSET
    description: str | Unset = UNSET
    expiration_date: datetime.datetime | Unset = UNSET
    extension_properties: UpdateLegalTagExtensionProperties | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        contract_id = self.contract_id

        description = self.description

        expiration_date: str | Unset = UNSET
        if not isinstance(self.expiration_date, Unset):
            expiration_date = self.expiration_date.isoformat()

        extension_properties: dict[str, Any] | Unset = UNSET
        if not isinstance(self.extension_properties, Unset):
            extension_properties = self.extension_properties.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if contract_id is not UNSET:
            field_dict["contractId"] = contract_id
        if description is not UNSET:
            field_dict["description"] = description
        if expiration_date is not UNSET:
            field_dict["expirationDate"] = expiration_date
        if extension_properties is not UNSET:
            field_dict["extensionProperties"] = extension_properties

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_legal_tag_extension_properties import (
            UpdateLegalTagExtensionProperties,
        )

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        contract_id = d.pop("contractId", UNSET)

        description = d.pop("description", UNSET)

        _expiration_date = d.pop("expirationDate", UNSET)
        expiration_date: datetime.datetime | Unset
        if isinstance(_expiration_date, Unset):
            expiration_date = UNSET
        else:
            expiration_date = isoparse(_expiration_date)

        _extension_properties = d.pop("extensionProperties", UNSET)
        extension_properties: UpdateLegalTagExtensionProperties | Unset
        if isinstance(_extension_properties, Unset):
            extension_properties = UNSET
        else:
            extension_properties = UpdateLegalTagExtensionProperties.from_dict(
                _extension_properties
            )

        update_legal_tag = cls(
            name=name,
            contract_id=contract_id,
            description=description,
            expiration_date=expiration_date,
            extension_properties=extension_properties,
        )

        update_legal_tag.additional_properties = d
        return update_legal_tag

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
