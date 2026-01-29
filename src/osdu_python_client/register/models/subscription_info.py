from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SubscriptionInfo")


@_attrs_define
class SubscriptionInfo:
    """Represents a model for SubscriptionInfo

    Attributes:
        id (str | Unset):  Example: dGVzdC1uYW1l.
        name (str | Unset):  Example: test-subscription.
        description (str | Unset):  Example: test description.
        topic (str | Unset):  Example: data-changed-v1.
        push_endpoint (str | Unset):  Example: https://myListener.com.
        created_by (str | Unset):  Example: test@myapp.com.
        notification_id (str | Unset):  Example: de-6ee609b9-620e-477b-86f9-3b8907643a12.
    """

    id: str | Unset = UNSET
    name: str | Unset = UNSET
    description: str | Unset = UNSET
    topic: str | Unset = UNSET
    push_endpoint: str | Unset = UNSET
    created_by: str | Unset = UNSET
    notification_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        description = self.description

        topic = self.topic

        push_endpoint = self.push_endpoint

        created_by = self.created_by

        notification_id = self.notification_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if topic is not UNSET:
            field_dict["topic"] = topic
        if push_endpoint is not UNSET:
            field_dict["pushEndpoint"] = push_endpoint
        if created_by is not UNSET:
            field_dict["createdBy"] = created_by
        if notification_id is not UNSET:
            field_dict["notificationId"] = notification_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        topic = d.pop("topic", UNSET)

        push_endpoint = d.pop("pushEndpoint", UNSET)

        created_by = d.pop("createdBy", UNSET)

        notification_id = d.pop("notificationId", UNSET)

        subscription_info = cls(
            id=id,
            name=name,
            description=description,
            topic=topic,
            push_endpoint=push_endpoint,
            created_by=created_by,
            notification_id=notification_id,
        )

        subscription_info.additional_properties = d
        return subscription_info

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
