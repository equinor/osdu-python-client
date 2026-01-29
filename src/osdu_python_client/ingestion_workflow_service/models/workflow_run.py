from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.workflow_run_status import WorkflowRunStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="WorkflowRun")


@_attrs_define
class WorkflowRun:
    """Reperesent one workflow run.

    Attributes:
        workflow_id (str | Unset): Workflow id for the workflow
        workflow_name (str | Unset): Workflow id for the workflow
        run_id (str | Unset): Run id for the workflow
        start_time_stamp (int | Unset): Start timestamp of the workflow run.Epoch time stamp
        end_time_stamp (int | Unset): End timestamp of the workflow run.Epoch timestamp
        status (WorkflowRunStatus | Unset): Task execution status
        submitted_by (str | Unset): System captured user details which triggered the run.
        workflow_engine_execution_date (str | Unset):
    """

    workflow_id: str | Unset = UNSET
    workflow_name: str | Unset = UNSET
    run_id: str | Unset = UNSET
    start_time_stamp: int | Unset = UNSET
    end_time_stamp: int | Unset = UNSET
    status: WorkflowRunStatus | Unset = UNSET
    submitted_by: str | Unset = UNSET
    workflow_engine_execution_date: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        workflow_id = self.workflow_id

        workflow_name = self.workflow_name

        run_id = self.run_id

        start_time_stamp = self.start_time_stamp

        end_time_stamp = self.end_time_stamp

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        submitted_by = self.submitted_by

        workflow_engine_execution_date = self.workflow_engine_execution_date

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if workflow_id is not UNSET:
            field_dict["workflowId"] = workflow_id
        if workflow_name is not UNSET:
            field_dict["workflowName"] = workflow_name
        if run_id is not UNSET:
            field_dict["runId"] = run_id
        if start_time_stamp is not UNSET:
            field_dict["startTimeStamp"] = start_time_stamp
        if end_time_stamp is not UNSET:
            field_dict["endTimeStamp"] = end_time_stamp
        if status is not UNSET:
            field_dict["status"] = status
        if submitted_by is not UNSET:
            field_dict["submittedBy"] = submitted_by
        if workflow_engine_execution_date is not UNSET:
            field_dict["workflowEngineExecutionDate"] = workflow_engine_execution_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        workflow_id = d.pop("workflowId", UNSET)

        workflow_name = d.pop("workflowName", UNSET)

        run_id = d.pop("runId", UNSET)

        start_time_stamp = d.pop("startTimeStamp", UNSET)

        end_time_stamp = d.pop("endTimeStamp", UNSET)

        _status = d.pop("status", UNSET)
        status: WorkflowRunStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = WorkflowRunStatus(_status)

        submitted_by = d.pop("submittedBy", UNSET)

        workflow_engine_execution_date = d.pop("workflowEngineExecutionDate", UNSET)

        workflow_run = cls(
            workflow_id=workflow_id,
            workflow_name=workflow_name,
            run_id=run_id,
            start_time_stamp=start_time_stamp,
            end_time_stamp=end_time_stamp,
            status=status,
            submitted_by=submitted_by,
            workflow_engine_execution_date=workflow_engine_execution_date,
        )

        workflow_run.additional_properties = d
        return workflow_run

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
