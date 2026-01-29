from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.file_source_info import FileSourceInfo


T = TypeVar("T", bound="DatasetProperties")


@_attrs_define
class DatasetProperties:
    """Dataset Properties

    Attributes:
        file_source_info (FileSourceInfo): File Source Info
    """

    file_source_info: FileSourceInfo
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        file_source_info = self.file_source_info.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "FileSourceInfo": file_source_info,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.file_source_info import FileSourceInfo

        d = dict(src_dict)
        file_source_info = FileSourceInfo.from_dict(d.pop("FileSourceInfo"))

        dataset_properties = cls(
            file_source_info=file_source_info,
        )

        dataset_properties.additional_properties = d
        return dataset_properties

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
