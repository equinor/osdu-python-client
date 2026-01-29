from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.delete_records_exception_cause import DeleteRecordsExceptionCause
    from ..models.delete_records_exception_stack_trace_item import (
        DeleteRecordsExceptionStackTraceItem,
    )
    from ..models.delete_records_exception_suppressed_item import (
        DeleteRecordsExceptionSuppressedItem,
    )
    from ..models.pair_string_string import PairStringString


T = TypeVar("T", bound="DeleteRecordsException")


@_attrs_define
class DeleteRecordsException:
    """
    Attributes:
        cause (DeleteRecordsExceptionCause | Unset):
        stack_trace (list[DeleteRecordsExceptionStackTraceItem] | Unset):
        not_deleted_records (list[PairStringString] | Unset):
        message (str | Unset):
        suppressed (list[DeleteRecordsExceptionSuppressedItem] | Unset):
        localized_message (str | Unset):
    """

    cause: DeleteRecordsExceptionCause | Unset = UNSET
    stack_trace: list[DeleteRecordsExceptionStackTraceItem] | Unset = UNSET
    not_deleted_records: list[PairStringString] | Unset = UNSET
    message: str | Unset = UNSET
    suppressed: list[DeleteRecordsExceptionSuppressedItem] | Unset = UNSET
    localized_message: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cause: dict[str, Any] | Unset = UNSET
        if not isinstance(self.cause, Unset):
            cause = self.cause.to_dict()

        stack_trace: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.stack_trace, Unset):
            stack_trace = []
            for stack_trace_item_data in self.stack_trace:
                stack_trace_item = stack_trace_item_data.to_dict()
                stack_trace.append(stack_trace_item)

        not_deleted_records: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.not_deleted_records, Unset):
            not_deleted_records = []
            for not_deleted_records_item_data in self.not_deleted_records:
                not_deleted_records_item = not_deleted_records_item_data.to_dict()
                not_deleted_records.append(not_deleted_records_item)

        message = self.message

        suppressed: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.suppressed, Unset):
            suppressed = []
            for suppressed_item_data in self.suppressed:
                suppressed_item = suppressed_item_data.to_dict()
                suppressed.append(suppressed_item)

        localized_message = self.localized_message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cause is not UNSET:
            field_dict["cause"] = cause
        if stack_trace is not UNSET:
            field_dict["stackTrace"] = stack_trace
        if not_deleted_records is not UNSET:
            field_dict["notDeletedRecords"] = not_deleted_records
        if message is not UNSET:
            field_dict["message"] = message
        if suppressed is not UNSET:
            field_dict["suppressed"] = suppressed
        if localized_message is not UNSET:
            field_dict["localizedMessage"] = localized_message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.delete_records_exception_cause import DeleteRecordsExceptionCause
        from ..models.delete_records_exception_stack_trace_item import (
            DeleteRecordsExceptionStackTraceItem,
        )
        from ..models.delete_records_exception_suppressed_item import (
            DeleteRecordsExceptionSuppressedItem,
        )
        from ..models.pair_string_string import PairStringString

        d = dict(src_dict)
        _cause = d.pop("cause", UNSET)
        cause: DeleteRecordsExceptionCause | Unset
        if isinstance(_cause, Unset):
            cause = UNSET
        else:
            cause = DeleteRecordsExceptionCause.from_dict(_cause)

        _stack_trace = d.pop("stackTrace", UNSET)
        stack_trace: list[DeleteRecordsExceptionStackTraceItem] | Unset = UNSET
        if _stack_trace is not UNSET:
            stack_trace = []
            for stack_trace_item_data in _stack_trace:
                stack_trace_item = DeleteRecordsExceptionStackTraceItem.from_dict(
                    stack_trace_item_data
                )

                stack_trace.append(stack_trace_item)

        _not_deleted_records = d.pop("notDeletedRecords", UNSET)
        not_deleted_records: list[PairStringString] | Unset = UNSET
        if _not_deleted_records is not UNSET:
            not_deleted_records = []
            for not_deleted_records_item_data in _not_deleted_records:
                not_deleted_records_item = PairStringString.from_dict(
                    not_deleted_records_item_data
                )

                not_deleted_records.append(not_deleted_records_item)

        message = d.pop("message", UNSET)

        _suppressed = d.pop("suppressed", UNSET)
        suppressed: list[DeleteRecordsExceptionSuppressedItem] | Unset = UNSET
        if _suppressed is not UNSET:
            suppressed = []
            for suppressed_item_data in _suppressed:
                suppressed_item = DeleteRecordsExceptionSuppressedItem.from_dict(
                    suppressed_item_data
                )

                suppressed.append(suppressed_item)

        localized_message = d.pop("localizedMessage", UNSET)

        delete_records_exception = cls(
            cause=cause,
            stack_trace=stack_trace,
            not_deleted_records=not_deleted_records,
            message=message,
            suppressed=suppressed,
            localized_message=localized_message,
        )

        delete_records_exception.additional_properties = d
        return delete_records_exception

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
