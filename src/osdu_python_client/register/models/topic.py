from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.topic_example import TopicExample


T = TypeVar("T", bound="Topic")


@_attrs_define
class Topic:
    """
    Attributes:
        name (str | Unset):
        description (str | Unset):
        state (str | Unset):
        example (TopicExample | Unset):
    """

    name: str | Unset = UNSET
    description: str | Unset = UNSET
    state: str | Unset = UNSET
    example: TopicExample | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description = self.description

        state = self.state

        example: dict[str, Any] | Unset = UNSET
        if not isinstance(self.example, Unset):
            example = self.example.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if state is not UNSET:
            field_dict["state"] = state
        if example is not UNSET:
            field_dict["example"] = example

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.topic_example import TopicExample

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        state = d.pop("state", UNSET)

        _example = d.pop("example", UNSET)
        example: TopicExample | Unset
        if isinstance(_example, Unset):
            example = UNSET
        else:
            example = TopicExample.from_dict(_example)

        topic = cls(
            name=name,
            description=description,
            state=state,
            example=example,
        )

        topic.additional_properties = d
        return topic

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
