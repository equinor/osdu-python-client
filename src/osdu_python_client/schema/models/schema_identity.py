from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SchemaIdentity")


@_attrs_define
class SchemaIdentity:
    """Schema authority source and type description

    Attributes:
        authority (str): Entity authority Example: osdu.
        source (str): Entity source Example: wks.
        entity_type (str): EntityType Code Example: wellbore.
        schema_version_major (int): Major Schema Version Number Example: 1.
        schema_version_minor (int): Minor Schema Version Number Example: 1.
        schema_version_patch (int): Patch Schema Version Number
        id (str | Unset): A read-only system defined id used for referencing of a schema. Example:
            osdu:wks:wellbore:1.0.0.
    """

    authority: str
    source: str
    entity_type: str
    schema_version_major: int
    schema_version_minor: int
    schema_version_patch: int
    id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        authority = self.authority

        source = self.source

        entity_type = self.entity_type

        schema_version_major = self.schema_version_major

        schema_version_minor = self.schema_version_minor

        schema_version_patch = self.schema_version_patch

        id = self.id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "authority": authority,
                "source": source,
                "entityType": entity_type,
                "schemaVersionMajor": schema_version_major,
                "schemaVersionMinor": schema_version_minor,
                "schemaVersionPatch": schema_version_patch,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        authority = d.pop("authority")

        source = d.pop("source")

        entity_type = d.pop("entityType")

        schema_version_major = d.pop("schemaVersionMajor")

        schema_version_minor = d.pop("schemaVersionMinor")

        schema_version_patch = d.pop("schemaVersionPatch")

        id = d.pop("id", UNSET)

        schema_identity = cls(
            authority=authority,
            source=source,
            entity_type=entity_type,
            schema_version_major=schema_version_major,
            schema_version_minor=schema_version_minor,
            schema_version_patch=schema_version_patch,
            id=id,
        )

        schema_identity.additional_properties = d
        return schema_identity

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
