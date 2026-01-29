from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_action_dto import CreateActionDto
    from ..models.json_node import JsonNode


T = TypeVar("T", bound="TestActionRequest")


@_attrs_define
class TestActionRequest:
    """Represents a model for TestActionRequest

    Attributes:
        test_payload (JsonNode): testPayload Example: {'id': 'common:regularheightfield:123456', 'kind':
            'common:petrel:regularheightfield:1.0.0', 'data': {'uri': 'https://myproj.com/abc123'}}.
        action (CreateActionDto | Unset): Represents a model to create Action
    """

    test_payload: JsonNode
    action: CreateActionDto | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        test_payload = self.test_payload.to_dict()

        action: dict[str, Any] | Unset = UNSET
        if not isinstance(self.action, Unset):
            action = self.action.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "testPayload": test_payload,
            }
        )
        if action is not UNSET:
            field_dict["action"] = action

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_action_dto import CreateActionDto
        from ..models.json_node import JsonNode

        d = dict(src_dict)
        test_payload = JsonNode.from_dict(d.pop("testPayload"))

        _action = d.pop("action", UNSET)
        action: CreateActionDto | Unset
        if isinstance(_action, Unset):
            action = UNSET
        else:
            action = CreateActionDto.from_dict(_action)

        test_action_request = cls(
            test_payload=test_payload,
            action=action,
        )

        test_action_request.additional_properties = d
        return test_action_request

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
