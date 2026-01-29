from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.readable_property_values_countries_of_origin import (
        ReadablePropertyValuesCountriesOfOrigin,
    )
    from ..models.readable_property_values_other_relevant_data_countries import (
        ReadablePropertyValuesOtherRelevantDataCountries,
    )


T = TypeVar("T", bound="ReadablePropertyValues")


@_attrs_define
class ReadablePropertyValues:
    """Shows the allowed values of the fields of a LegalTag.

    Attributes:
        countries_of_origin (ReadablePropertyValuesCountriesOfOrigin | Unset): The values of all the allowed Countries
            of Origin with the ISO Alpha 2 code and country name.
        other_relevant_data_countries (ReadablePropertyValuesOtherRelevantDataCountries | Unset): The values of all the
            allowed Other Relevant Data Countries with the ISO Alpha 2 code and country name.
        security_classifications (list[str] | Unset): The values of all the allowed Security Classifications.
        export_classification_control_numbers (list[str] | Unset): The name of all the allowed Export Classifications.
        personal_data_types (list[str] | Unset): The name of all the allowed Personal Data Type values.
        data_types (list[str] | Unset): The name of all the allowed Data Type values.
    """

    countries_of_origin: ReadablePropertyValuesCountriesOfOrigin | Unset = UNSET
    other_relevant_data_countries: (
        ReadablePropertyValuesOtherRelevantDataCountries | Unset
    ) = UNSET
    security_classifications: list[str] | Unset = UNSET
    export_classification_control_numbers: list[str] | Unset = UNSET
    personal_data_types: list[str] | Unset = UNSET
    data_types: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        countries_of_origin: dict[str, Any] | Unset = UNSET
        if not isinstance(self.countries_of_origin, Unset):
            countries_of_origin = self.countries_of_origin.to_dict()

        other_relevant_data_countries: dict[str, Any] | Unset = UNSET
        if not isinstance(self.other_relevant_data_countries, Unset):
            other_relevant_data_countries = self.other_relevant_data_countries.to_dict()

        security_classifications: list[str] | Unset = UNSET
        if not isinstance(self.security_classifications, Unset):
            security_classifications = self.security_classifications

        export_classification_control_numbers: list[str] | Unset = UNSET
        if not isinstance(self.export_classification_control_numbers, Unset):
            export_classification_control_numbers = (
                self.export_classification_control_numbers
            )

        personal_data_types: list[str] | Unset = UNSET
        if not isinstance(self.personal_data_types, Unset):
            personal_data_types = self.personal_data_types

        data_types: list[str] | Unset = UNSET
        if not isinstance(self.data_types, Unset):
            data_types = self.data_types

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if countries_of_origin is not UNSET:
            field_dict["countriesOfOrigin"] = countries_of_origin
        if other_relevant_data_countries is not UNSET:
            field_dict["otherRelevantDataCountries"] = other_relevant_data_countries
        if security_classifications is not UNSET:
            field_dict["securityClassifications"] = security_classifications
        if export_classification_control_numbers is not UNSET:
            field_dict["exportClassificationControlNumbers"] = (
                export_classification_control_numbers
            )
        if personal_data_types is not UNSET:
            field_dict["personalDataTypes"] = personal_data_types
        if data_types is not UNSET:
            field_dict["dataTypes"] = data_types

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.readable_property_values_countries_of_origin import (
            ReadablePropertyValuesCountriesOfOrigin,
        )
        from ..models.readable_property_values_other_relevant_data_countries import (
            ReadablePropertyValuesOtherRelevantDataCountries,
        )

        d = dict(src_dict)
        _countries_of_origin = d.pop("countriesOfOrigin", UNSET)
        countries_of_origin: ReadablePropertyValuesCountriesOfOrigin | Unset
        if isinstance(_countries_of_origin, Unset):
            countries_of_origin = UNSET
        else:
            countries_of_origin = ReadablePropertyValuesCountriesOfOrigin.from_dict(
                _countries_of_origin
            )

        _other_relevant_data_countries = d.pop("otherRelevantDataCountries", UNSET)
        other_relevant_data_countries: (
            ReadablePropertyValuesOtherRelevantDataCountries | Unset
        )
        if isinstance(_other_relevant_data_countries, Unset):
            other_relevant_data_countries = UNSET
        else:
            other_relevant_data_countries = (
                ReadablePropertyValuesOtherRelevantDataCountries.from_dict(
                    _other_relevant_data_countries
                )
            )

        security_classifications = cast(
            list[str], d.pop("securityClassifications", UNSET)
        )

        export_classification_control_numbers = cast(
            list[str], d.pop("exportClassificationControlNumbers", UNSET)
        )

        personal_data_types = cast(list[str], d.pop("personalDataTypes", UNSET))

        data_types = cast(list[str], d.pop("dataTypes", UNSET))

        readable_property_values = cls(
            countries_of_origin=countries_of_origin,
            other_relevant_data_countries=other_relevant_data_countries,
            security_classifications=security_classifications,
            export_classification_control_numbers=export_classification_control_numbers,
            personal_data_types=personal_data_types,
            data_types=data_types,
        )

        readable_property_values.additional_properties = d
        return readable_property_values

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
