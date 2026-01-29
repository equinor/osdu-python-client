from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.schema_info import SchemaInfo
    from ..models.schema_request_schema import SchemaRequestSchema


T = TypeVar("T", bound="SchemaRequest")


@_attrs_define
class SchemaRequest:
    """Represents a model to Schema Request

    Attributes:
        schema_info (SchemaInfo): Represents a model to Schema Info including status, creation and schemaIdentity
        schema (SchemaRequestSchema):
    """

    schema_info: SchemaInfo
    schema: SchemaRequestSchema
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        schema_info = self.schema_info.to_dict()

        schema = self.schema.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "schemaInfo": schema_info,
                "schema": schema,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.schema_info import SchemaInfo
        from ..models.schema_request_schema import SchemaRequestSchema

        d = dict(src_dict)
        schema_info = SchemaInfo.from_dict(d.pop("schemaInfo"))

        schema = SchemaRequestSchema.from_dict(d.pop("schema"))

        schema_request = cls(
            schema_info=schema_info,
            schema=schema,
        )

        schema_request.additional_properties = d
        return schema_request

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
