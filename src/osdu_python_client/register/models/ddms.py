from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.registered_interface import RegisteredInterface


T = TypeVar("T", bound="Ddms")


@_attrs_define
class Ddms:
    """Represents a model for Ddms

    Attributes:
        id (str):  Example: example-id-123.
        name (str):  Example: example-name.
        description (str | Unset):  Example: example-description.
        contact_email (str | Unset):  Example: abc@test.com.
        created_date_time_epoch (datetime.datetime | Unset):
        interfaces (list[RegisteredInterface] | Unset):
    """

    id: str
    name: str
    description: str | Unset = UNSET
    contact_email: str | Unset = UNSET
    created_date_time_epoch: datetime.datetime | Unset = UNSET
    interfaces: list[RegisteredInterface] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        description = self.description

        contact_email = self.contact_email

        created_date_time_epoch: str | Unset = UNSET
        if not isinstance(self.created_date_time_epoch, Unset):
            created_date_time_epoch = self.created_date_time_epoch.isoformat()

        interfaces: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.interfaces, Unset):
            interfaces = []
            for interfaces_item_data in self.interfaces:
                interfaces_item = interfaces_item_data.to_dict()
                interfaces.append(interfaces_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if contact_email is not UNSET:
            field_dict["contactEmail"] = contact_email
        if created_date_time_epoch is not UNSET:
            field_dict["createdDateTimeEpoch"] = created_date_time_epoch
        if interfaces is not UNSET:
            field_dict["interfaces"] = interfaces

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.registered_interface import RegisteredInterface

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        description = d.pop("description", UNSET)

        contact_email = d.pop("contactEmail", UNSET)

        _created_date_time_epoch = d.pop("createdDateTimeEpoch", UNSET)
        created_date_time_epoch: datetime.datetime | Unset
        if isinstance(_created_date_time_epoch, Unset):
            created_date_time_epoch = UNSET
        else:
            created_date_time_epoch = isoparse(_created_date_time_epoch)

        _interfaces = d.pop("interfaces", UNSET)
        interfaces: list[RegisteredInterface] | Unset = UNSET
        if _interfaces is not UNSET:
            interfaces = []
            for interfaces_item_data in _interfaces:
                interfaces_item = RegisteredInterface.from_dict(interfaces_item_data)

                interfaces.append(interfaces_item)

        ddms = cls(
            id=id,
            name=name,
            description=description,
            contact_email=contact_email,
            created_date_time_epoch=created_date_time_epoch,
            interfaces=interfaces,
        )

        ddms.additional_properties = d
        return ddms

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
