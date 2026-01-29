from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.schema_info_schema_scope import SchemaInfoSchemaScope
from ..models.schema_info_schema_status import SchemaInfoSchemaStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.schema_identity import SchemaIdentity


T = TypeVar("T", bound="SchemaInfo")


@_attrs_define
class SchemaInfo:
    """Represents a model to Schema Info including status, creation and schemaIdentity

    Attributes:
        schema_identity (SchemaIdentity): Schema authority source and type description
        status (SchemaInfoSchemaStatus): Schema lifecycle status Example: PUBLISHED.
        created_by (str | Unset): The user who created the schema. This value is taken from API caller token. Example:
            user@opendes.com.
        date_created (datetime.datetime | Unset): The UTC date time of the entity creation Example:
            2019-05-23T11:16:03Z.
        scope (SchemaInfoSchemaScope | Unset):  Schema Scope - is it internal or shared. This is a system defined
            attribute based on partition-id passed. Example: INTERNAL.
        superseded_by (SchemaIdentity | Unset): Schema authority source and type description
    """

    schema_identity: SchemaIdentity
    status: SchemaInfoSchemaStatus
    created_by: str | Unset = UNSET
    date_created: datetime.datetime | Unset = UNSET
    scope: SchemaInfoSchemaScope | Unset = UNSET
    superseded_by: SchemaIdentity | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        schema_identity = self.schema_identity.to_dict()

        status = self.status.value

        created_by = self.created_by

        date_created: str | Unset = UNSET
        if not isinstance(self.date_created, Unset):
            date_created = self.date_created.isoformat()

        scope: str | Unset = UNSET
        if not isinstance(self.scope, Unset):
            scope = self.scope.value

        superseded_by: dict[str, Any] | Unset = UNSET
        if not isinstance(self.superseded_by, Unset):
            superseded_by = self.superseded_by.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "schemaIdentity": schema_identity,
                "status": status,
            }
        )
        if created_by is not UNSET:
            field_dict["createdBy"] = created_by
        if date_created is not UNSET:
            field_dict["dateCreated"] = date_created
        if scope is not UNSET:
            field_dict["scope"] = scope
        if superseded_by is not UNSET:
            field_dict["supersededBy"] = superseded_by

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.schema_identity import SchemaIdentity

        d = dict(src_dict)
        schema_identity = SchemaIdentity.from_dict(d.pop("schemaIdentity"))

        status = SchemaInfoSchemaStatus(d.pop("status"))

        created_by = d.pop("createdBy", UNSET)

        _date_created = d.pop("dateCreated", UNSET)
        date_created: datetime.datetime | Unset
        if isinstance(_date_created, Unset):
            date_created = UNSET
        else:
            date_created = isoparse(_date_created)

        _scope = d.pop("scope", UNSET)
        scope: SchemaInfoSchemaScope | Unset
        if isinstance(_scope, Unset):
            scope = UNSET
        else:
            scope = SchemaInfoSchemaScope(_scope)

        _superseded_by = d.pop("supersededBy", UNSET)
        superseded_by: SchemaIdentity | Unset
        if isinstance(_superseded_by, Unset):
            superseded_by = UNSET
        else:
            superseded_by = SchemaIdentity.from_dict(_superseded_by)

        schema_info = cls(
            schema_identity=schema_identity,
            status=status,
            created_by=created_by,
            date_created=date_created,
            scope=scope,
            superseded_by=superseded_by,
        )

        schema_info.additional_properties = d
        return schema_info

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
