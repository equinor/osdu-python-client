from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.gsa_secret import GsaSecret
    from ..models.hmac_secret import HmacSecret


T = TypeVar("T", bound="Subscription")


@_attrs_define
class Subscription:
    """Represents a model for Subscription

    Attributes:
        name (str):  Example: test-subscription.
        topic (str):  Example: data-changed-v1.
        push_endpoint (str):  Example:  https://myListener.com.
        id (str | Unset): Subscription Id
        description (str | Unset):  Example: test-subscription.
        created_by (str | Unset):  Example: test@myapp.com.
        notification_id (str | Unset):  Example: de-6ee609b9-620e-477b-86f9-3b8907643a12.
        secret (GsaSecret | HmacSecret | Unset):
    """

    name: str
    topic: str
    push_endpoint: str
    id: str | Unset = UNSET
    description: str | Unset = UNSET
    created_by: str | Unset = UNSET
    notification_id: str | Unset = UNSET
    secret: GsaSecret | HmacSecret | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.gsa_secret import GsaSecret

        name = self.name

        topic = self.topic

        push_endpoint = self.push_endpoint

        id = self.id

        description = self.description

        created_by = self.created_by

        notification_id = self.notification_id

        secret: dict[str, Any] | Unset
        if isinstance(self.secret, Unset):
            secret = UNSET
        elif isinstance(self.secret, GsaSecret):
            secret = self.secret.to_dict()
        else:
            secret = self.secret.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "topic": topic,
                "pushEndpoint": push_endpoint,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if description is not UNSET:
            field_dict["description"] = description
        if created_by is not UNSET:
            field_dict["createdBy"] = created_by
        if notification_id is not UNSET:
            field_dict["notificationId"] = notification_id
        if secret is not UNSET:
            field_dict["secret"] = secret

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.gsa_secret import GsaSecret
        from ..models.hmac_secret import HmacSecret

        d = dict(src_dict)
        name = d.pop("name")

        topic = d.pop("topic")

        push_endpoint = d.pop("pushEndpoint")

        id = d.pop("id", UNSET)

        description = d.pop("description", UNSET)

        created_by = d.pop("createdBy", UNSET)

        notification_id = d.pop("notificationId", UNSET)

        def _parse_secret(data: object) -> GsaSecret | HmacSecret | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                secret_type_0 = GsaSecret.from_dict(data)

                return secret_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            secret_type_1 = HmacSecret.from_dict(data)

            return secret_type_1

        secret = _parse_secret(d.pop("secret", UNSET))

        subscription = cls(
            name=name,
            topic=topic,
            push_endpoint=push_endpoint,
            id=id,
            description=description,
            created_by=created_by,
            notification_id=notification_id,
            secret=secret,
        )

        subscription.additional_properties = d
        return subscription

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
