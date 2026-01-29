from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DeleteRecordsExceptionCauseStackTraceItem")


@_attrs_define
class DeleteRecordsExceptionCauseStackTraceItem:
    """
    Attributes:
        class_loader_name (str | Unset):
        module_name (str | Unset):
        module_version (str | Unset):
        method_name (str | Unset):
        file_name (str | Unset):
        line_number (int | Unset):
        native_method (bool | Unset):
        class_name (str | Unset):
    """

    class_loader_name: str | Unset = UNSET
    module_name: str | Unset = UNSET
    module_version: str | Unset = UNSET
    method_name: str | Unset = UNSET
    file_name: str | Unset = UNSET
    line_number: int | Unset = UNSET
    native_method: bool | Unset = UNSET
    class_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        class_loader_name = self.class_loader_name

        module_name = self.module_name

        module_version = self.module_version

        method_name = self.method_name

        file_name = self.file_name

        line_number = self.line_number

        native_method = self.native_method

        class_name = self.class_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if class_loader_name is not UNSET:
            field_dict["classLoaderName"] = class_loader_name
        if module_name is not UNSET:
            field_dict["moduleName"] = module_name
        if module_version is not UNSET:
            field_dict["moduleVersion"] = module_version
        if method_name is not UNSET:
            field_dict["methodName"] = method_name
        if file_name is not UNSET:
            field_dict["fileName"] = file_name
        if line_number is not UNSET:
            field_dict["lineNumber"] = line_number
        if native_method is not UNSET:
            field_dict["nativeMethod"] = native_method
        if class_name is not UNSET:
            field_dict["className"] = class_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        class_loader_name = d.pop("classLoaderName", UNSET)

        module_name = d.pop("moduleName", UNSET)

        module_version = d.pop("moduleVersion", UNSET)

        method_name = d.pop("methodName", UNSET)

        file_name = d.pop("fileName", UNSET)

        line_number = d.pop("lineNumber", UNSET)

        native_method = d.pop("nativeMethod", UNSET)

        class_name = d.pop("className", UNSET)

        delete_records_exception_cause_stack_trace_item = cls(
            class_loader_name=class_loader_name,
            module_name=module_name,
            module_version=module_version,
            method_name=method_name,
            file_name=file_name,
            line_number=line_number,
            native_method=native_method,
            class_name=class_name,
        )

        delete_records_exception_cause_stack_trace_item.additional_properties = d
        return delete_records_exception_cause_stack_trace_item

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
