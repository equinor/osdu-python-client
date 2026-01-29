from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.registered_interface_schema import RegisteredInterfaceSchema


T = TypeVar("T", bound="RegisteredInterface")


@_attrs_define
class RegisteredInterface:
    """Represents a model for RegisteredInterface

    Attributes:
        entity_type (str):  Example: wellbore.
        schema (RegisteredInterfaceSchema):
    """

    entity_type: str
    schema: RegisteredInterfaceSchema
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        entity_type = self.entity_type

        schema = self.schema.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "entityType": entity_type,
                "schema": schema,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.registered_interface_schema import RegisteredInterfaceSchema

        d = dict(src_dict)
        entity_type = d.pop("entityType")

        schema = RegisteredInterfaceSchema.from_dict(d.pop("schema"))

        registered_interface = cls(
            entity_type=entity_type,
            schema=schema,
        )

        registered_interface.additional_properties = d
        return registered_interface

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
