from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.workflow_metadata_registration_instructions_additional_property import (
        WorkflowMetadataRegistrationInstructionsAdditionalProperty,
    )


T = TypeVar("T", bound="WorkflowMetadataRegistrationInstructions")


@_attrs_define
class WorkflowMetadataRegistrationInstructions:
    """Workfow registration instructions which could contains:

    Name of already registered Airflow DAG
    Cotent of python DAG file
    etc By default this is Airflow DAG named workflowName

    """

    additional_properties: dict[
        str, WorkflowMetadataRegistrationInstructionsAdditionalProperty
    ] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.workflow_metadata_registration_instructions_additional_property import (
            WorkflowMetadataRegistrationInstructionsAdditionalProperty,
        )

        d = dict(src_dict)
        workflow_metadata_registration_instructions = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = (
                WorkflowMetadataRegistrationInstructionsAdditionalProperty.from_dict(
                    prop_dict
                )
            )

            additional_properties[prop_name] = additional_property

        workflow_metadata_registration_instructions.additional_properties = (
            additional_properties
        )
        return workflow_metadata_registration_instructions

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(
        self, key: str
    ) -> WorkflowMetadataRegistrationInstructionsAdditionalProperty:
        return self.additional_properties[key]

    def __setitem__(
        self,
        key: str,
        value: WorkflowMetadataRegistrationInstructionsAdditionalProperty,
    ) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
