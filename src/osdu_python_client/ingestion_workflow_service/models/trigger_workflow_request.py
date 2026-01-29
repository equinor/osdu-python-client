from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.trigger_workflow_request_execution_context import (
        TriggerWorkflowRequestExecutionContext,
    )


T = TypeVar("T", bound="TriggerWorkflowRequest")


@_attrs_define
class TriggerWorkflowRequest:
    """
    Attributes:
        run_id (str | Unset): Optional. Explicit setting up workflow run id.
        execution_context (TriggerWorkflowRequestExecutionContext | Unset): Map to configure workflow speciffic key
            value pairs
    """

    run_id: str | Unset = UNSET
    execution_context: TriggerWorkflowRequestExecutionContext | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        run_id = self.run_id

        execution_context: dict[str, Any] | Unset = UNSET
        if not isinstance(self.execution_context, Unset):
            execution_context = self.execution_context.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if run_id is not UNSET:
            field_dict["runId"] = run_id
        if execution_context is not UNSET:
            field_dict["executionContext"] = execution_context

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.trigger_workflow_request_execution_context import (
            TriggerWorkflowRequestExecutionContext,
        )

        d = dict(src_dict)
        run_id = d.pop("runId", UNSET)

        _execution_context = d.pop("executionContext", UNSET)
        execution_context: TriggerWorkflowRequestExecutionContext | Unset
        if isinstance(_execution_context, Unset):
            execution_context = UNSET
        else:
            execution_context = TriggerWorkflowRequestExecutionContext.from_dict(
                _execution_context
            )

        trigger_workflow_request = cls(
            run_id=run_id,
            execution_context=execution_context,
        )

        trigger_workflow_request.additional_properties = d
        return trigger_workflow_request

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
