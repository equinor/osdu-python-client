from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Filter")


@_attrs_define
class Filter:
    """Represents a model for Filter

    Attributes:
        entity_type (list[str] | Unset):  Example: ['regularheightfield'].
        source (list[str] | Unset):  Example: ['petrel'].
        version (list[str] | Unset):  Example: ['*'].
    """

    entity_type: list[str] | Unset = UNSET
    source: list[str] | Unset = UNSET
    version: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        entity_type: list[str] | Unset = UNSET
        if not isinstance(self.entity_type, Unset):
            entity_type = self.entity_type

        source: list[str] | Unset = UNSET
        if not isinstance(self.source, Unset):
            source = self.source

        version: list[str] | Unset = UNSET
        if not isinstance(self.version, Unset):
            version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if entity_type is not UNSET:
            field_dict["entityType"] = entity_type
        if source is not UNSET:
            field_dict["source"] = source
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        entity_type = cast(list[str], d.pop("entityType", UNSET))

        source = cast(list[str], d.pop("source", UNSET))

        version = cast(list[str], d.pop("version", UNSET))

        filter_ = cls(
            entity_type=entity_type,
            source=source,
            version=version,
        )

        filter_.additional_properties = d
        return filter_

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
