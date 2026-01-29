from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.properties_extension_properties import PropertiesExtensionProperties


T = TypeVar("T", bound="Properties")


@_attrs_define
class Properties:
    """
    Attributes:
        country_of_origin (list[str] | Unset):
        contract_id (str | Unset):
        expiration_date (datetime.datetime | Unset):
        originator (str | Unset):
        data_type (str | Unset):
        security_classification (str | Unset):
        personal_data (str | Unset):
        export_classification (str | Unset):
        extension_properties (PropertiesExtensionProperties | Unset):
    """

    country_of_origin: list[str] | Unset = UNSET
    contract_id: str | Unset = UNSET
    expiration_date: datetime.datetime | Unset = UNSET
    originator: str | Unset = UNSET
    data_type: str | Unset = UNSET
    security_classification: str | Unset = UNSET
    personal_data: str | Unset = UNSET
    export_classification: str | Unset = UNSET
    extension_properties: PropertiesExtensionProperties | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        country_of_origin: list[str] | Unset = UNSET
        if not isinstance(self.country_of_origin, Unset):
            country_of_origin = self.country_of_origin

        contract_id = self.contract_id

        expiration_date: str | Unset = UNSET
        if not isinstance(self.expiration_date, Unset):
            expiration_date = self.expiration_date.isoformat()

        originator = self.originator

        data_type = self.data_type

        security_classification = self.security_classification

        personal_data = self.personal_data

        export_classification = self.export_classification

        extension_properties: dict[str, Any] | Unset = UNSET
        if not isinstance(self.extension_properties, Unset):
            extension_properties = self.extension_properties.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if country_of_origin is not UNSET:
            field_dict["countryOfOrigin"] = country_of_origin
        if contract_id is not UNSET:
            field_dict["contractId"] = contract_id
        if expiration_date is not UNSET:
            field_dict["expirationDate"] = expiration_date
        if originator is not UNSET:
            field_dict["originator"] = originator
        if data_type is not UNSET:
            field_dict["dataType"] = data_type
        if security_classification is not UNSET:
            field_dict["securityClassification"] = security_classification
        if personal_data is not UNSET:
            field_dict["personalData"] = personal_data
        if export_classification is not UNSET:
            field_dict["exportClassification"] = export_classification
        if extension_properties is not UNSET:
            field_dict["extensionProperties"] = extension_properties

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.properties_extension_properties import (
            PropertiesExtensionProperties,
        )

        d = dict(src_dict)
        country_of_origin = cast(list[str], d.pop("countryOfOrigin", UNSET))

        contract_id = d.pop("contractId", UNSET)

        _expiration_date = d.pop("expirationDate", UNSET)
        expiration_date: datetime.datetime | Unset
        if isinstance(_expiration_date, Unset):
            expiration_date = UNSET
        else:
            expiration_date = isoparse(_expiration_date)

        originator = d.pop("originator", UNSET)

        data_type = d.pop("dataType", UNSET)

        security_classification = d.pop("securityClassification", UNSET)

        personal_data = d.pop("personalData", UNSET)

        export_classification = d.pop("exportClassification", UNSET)

        _extension_properties = d.pop("extensionProperties", UNSET)
        extension_properties: PropertiesExtensionProperties | Unset
        if isinstance(_extension_properties, Unset):
            extension_properties = UNSET
        else:
            extension_properties = PropertiesExtensionProperties.from_dict(
                _extension_properties
            )

        properties = cls(
            country_of_origin=country_of_origin,
            contract_id=contract_id,
            expiration_date=expiration_date,
            originator=originator,
            data_type=data_type,
            security_classification=security_classification,
            personal_data=personal_data,
            export_classification=export_classification,
            extension_properties=extension_properties,
        )

        properties.additional_properties = d
        return properties

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
