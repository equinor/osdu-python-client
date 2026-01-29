from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.workflow_metadata_registration_instructions import (
        WorkflowMetadataRegistrationInstructions,
    )


T = TypeVar("T", bound="WorkflowMetadata")


@_attrs_define
class WorkflowMetadata:
    r"""
    Attributes:
        workflow_id (str | Unset): System generated id, which uniquely recongnizes a workflow.
        workflow_name (str | Unset): Workfow name given as input from user while deploying the workflow.
        description (str | Unset): Description of workflow provided by user at time of creation of workflow.
        created_by (str | Unset): System captured user info who created workflow.
        creation_timestamp (int | Unset): System date of creation of workflow.Epoch tiemstamp.
        version (int | Unset): Sematic versions of workflow. These numbers are assigned in increasing order and
            correspond to edits\modifications to workflow definitions.
        is_deployed_through_workflow_service (bool | Unset):
        registration_instructions (WorkflowMetadataRegistrationInstructions | Unset): Workfow registration instructions
            which could contains:

            Name of already registered Airflow DAG
            Cotent of python DAG file
            etc By default this is Airflow DAG named workflowName
        is_system_workflow (bool | Unset):
    """

    workflow_id: str | Unset = UNSET
    workflow_name: str | Unset = UNSET
    description: str | Unset = UNSET
    created_by: str | Unset = UNSET
    creation_timestamp: int | Unset = UNSET
    version: int | Unset = UNSET
    is_deployed_through_workflow_service: bool | Unset = UNSET
    registration_instructions: WorkflowMetadataRegistrationInstructions | Unset = UNSET
    is_system_workflow: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        workflow_id = self.workflow_id

        workflow_name = self.workflow_name

        description = self.description

        created_by = self.created_by

        creation_timestamp = self.creation_timestamp

        version = self.version

        is_deployed_through_workflow_service = self.is_deployed_through_workflow_service

        registration_instructions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.registration_instructions, Unset):
            registration_instructions = self.registration_instructions.to_dict()

        is_system_workflow = self.is_system_workflow

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if workflow_id is not UNSET:
            field_dict["workflowId"] = workflow_id
        if workflow_name is not UNSET:
            field_dict["workflowName"] = workflow_name
        if description is not UNSET:
            field_dict["description"] = description
        if created_by is not UNSET:
            field_dict["createdBy"] = created_by
        if creation_timestamp is not UNSET:
            field_dict["creationTimestamp"] = creation_timestamp
        if version is not UNSET:
            field_dict["version"] = version
        if is_deployed_through_workflow_service is not UNSET:
            field_dict["isDeployedThroughWorkflowService"] = (
                is_deployed_through_workflow_service
            )
        if registration_instructions is not UNSET:
            field_dict["registrationInstructions"] = registration_instructions
        if is_system_workflow is not UNSET:
            field_dict["isSystemWorkflow"] = is_system_workflow

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.workflow_metadata_registration_instructions import (
            WorkflowMetadataRegistrationInstructions,
        )

        d = dict(src_dict)
        workflow_id = d.pop("workflowId", UNSET)

        workflow_name = d.pop("workflowName", UNSET)

        description = d.pop("description", UNSET)

        created_by = d.pop("createdBy", UNSET)

        creation_timestamp = d.pop("creationTimestamp", UNSET)

        version = d.pop("version", UNSET)

        is_deployed_through_workflow_service = d.pop(
            "isDeployedThroughWorkflowService", UNSET
        )

        _registration_instructions = d.pop("registrationInstructions", UNSET)
        registration_instructions: WorkflowMetadataRegistrationInstructions | Unset
        if isinstance(_registration_instructions, Unset):
            registration_instructions = UNSET
        else:
            registration_instructions = (
                WorkflowMetadataRegistrationInstructions.from_dict(
                    _registration_instructions
                )
            )

        is_system_workflow = d.pop("isSystemWorkflow", UNSET)

        workflow_metadata = cls(
            workflow_id=workflow_id,
            workflow_name=workflow_name,
            description=description,
            created_by=created_by,
            creation_timestamp=creation_timestamp,
            version=version,
            is_deployed_through_workflow_service=is_deployed_through_workflow_service,
            registration_instructions=registration_instructions,
            is_system_workflow=is_system_workflow,
        )

        workflow_metadata.additional_properties = d
        return workflow_metadata

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
