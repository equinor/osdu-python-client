from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.trigger_workflow_request_execution_context_additional_property import (
        TriggerWorkflowRequestExecutionContextAdditionalProperty,
    )


T = TypeVar("T", bound="TriggerWorkflowRequestExecutionContext")


@_attrs_define
class TriggerWorkflowRequestExecutionContext:
    """Map to configure workflow speciffic key value pairs"""

    additional_properties: dict[
        str, TriggerWorkflowRequestExecutionContextAdditionalProperty
    ] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.trigger_workflow_request_execution_context_additional_property import (
            TriggerWorkflowRequestExecutionContextAdditionalProperty,
        )

        d = dict(src_dict)
        trigger_workflow_request_execution_context = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = (
                TriggerWorkflowRequestExecutionContextAdditionalProperty.from_dict(
                    prop_dict
                )
            )

            additional_properties[prop_name] = additional_property

        trigger_workflow_request_execution_context.additional_properties = (
            additional_properties
        )
        return trigger_workflow_request_execution_context

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(
        self, key: str
    ) -> TriggerWorkflowRequestExecutionContextAdditionalProperty:
        return self.additional_properties[key]

    def __setitem__(
        self, key: str, value: TriggerWorkflowRequestExecutionContextAdditionalProperty
    ) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
