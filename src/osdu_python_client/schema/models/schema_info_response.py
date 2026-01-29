from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.schema_info import SchemaInfo


T = TypeVar("T", bound="SchemaInfoResponse")


@_attrs_define
class SchemaInfoResponse:
    """The response for a GET schema request

    Attributes:
        schema_infos (list[SchemaInfo] | Unset):
        offset (int | Unset): The offset for the next query
        count (int | Unset): The number of schema versions in this response
        total_count (int | Unset): The total number of entity type codes in the repositories
    """

    schema_infos: list[SchemaInfo] | Unset = UNSET
    offset: int | Unset = UNSET
    count: int | Unset = UNSET
    total_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        schema_infos: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.schema_infos, Unset):
            schema_infos = []
            for schema_infos_item_data in self.schema_infos:
                schema_infos_item = schema_infos_item_data.to_dict()
                schema_infos.append(schema_infos_item)

        offset = self.offset

        count = self.count

        total_count = self.total_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if schema_infos is not UNSET:
            field_dict["schemaInfos"] = schema_infos
        if offset is not UNSET:
            field_dict["offset"] = offset
        if count is not UNSET:
            field_dict["count"] = count
        if total_count is not UNSET:
            field_dict["totalCount"] = total_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.schema_info import SchemaInfo

        d = dict(src_dict)
        _schema_infos = d.pop("schemaInfos", UNSET)
        schema_infos: list[SchemaInfo] | Unset = UNSET
        if _schema_infos is not UNSET:
            schema_infos = []
            for schema_infos_item_data in _schema_infos:
                schema_infos_item = SchemaInfo.from_dict(schema_infos_item_data)

                schema_infos.append(schema_infos_item)

        offset = d.pop("offset", UNSET)

        count = d.pop("count", UNSET)

        total_count = d.pop("totalCount", UNSET)

        schema_info_response = cls(
            schema_infos=schema_infos,
            offset=offset,
            count=count,
            total_count=total_count,
        )

        schema_info_response.additional_properties = d
        return schema_info_response

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
