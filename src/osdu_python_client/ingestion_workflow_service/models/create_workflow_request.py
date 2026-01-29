from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_workflow_request_registration_instructions import (
        CreateWorkflowRequestRegistrationInstructions,
    )


T = TypeVar("T", bound="CreateWorkflowRequest")


@_attrs_define
class CreateWorkflowRequest:
    """
    Attributes:
        registration_instructions (CreateWorkflowRequestRegistrationInstructions): Workfow registration instructions
            which could contains:

            Name of already registered Airflow DAG
            Content of python DAG file
            etc By default this is Airflow DAG named workflowName
        workflow_name (str | Unset): Workfow name given as input from user while deploying the workflow
        description (str | Unset): Description of workflow provided by user at time of creation of workflow
    """

    registration_instructions: CreateWorkflowRequestRegistrationInstructions
    workflow_name: str | Unset = UNSET
    description: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        registration_instructions = self.registration_instructions.to_dict()

        workflow_name = self.workflow_name

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "registrationInstructions": registration_instructions,
            }
        )
        if workflow_name is not UNSET:
            field_dict["workflowName"] = workflow_name
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_workflow_request_registration_instructions import (
            CreateWorkflowRequestRegistrationInstructions,
        )

        d = dict(src_dict)
        registration_instructions = (
            CreateWorkflowRequestRegistrationInstructions.from_dict(
                d.pop("registrationInstructions")
            )
        )

        workflow_name = d.pop("workflowName", UNSET)

        description = d.pop("description", UNSET)

        create_workflow_request = cls(
            registration_instructions=registration_instructions,
            workflow_name=workflow_name,
            description=description,
        )

        create_workflow_request.additional_properties = d
        return create_workflow_request

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
