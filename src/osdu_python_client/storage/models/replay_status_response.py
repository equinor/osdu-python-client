from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.replay_filter import ReplayFilter
    from ..models.replay_status import ReplayStatus


T = TypeVar("T", bound="ReplayStatusResponse")


@_attrs_define
class ReplayStatusResponse:
    """
    Attributes:
        replay_id (str | Unset):
        operation (str | Unset):
        total_records (int | Unset):
        started_at (datetime.datetime | Unset):
        elapsed_time (str | Unset):
        processed_records (int | Unset):
        overall_state (str | Unset):
        filter_ (ReplayFilter | Unset):
        status (list[ReplayStatus] | Unset):
    """

    replay_id: str | Unset = UNSET
    operation: str | Unset = UNSET
    total_records: int | Unset = UNSET
    started_at: datetime.datetime | Unset = UNSET
    elapsed_time: str | Unset = UNSET
    processed_records: int | Unset = UNSET
    overall_state: str | Unset = UNSET
    filter_: ReplayFilter | Unset = UNSET
    status: list[ReplayStatus] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        replay_id = self.replay_id

        operation = self.operation

        total_records = self.total_records

        started_at: str | Unset = UNSET
        if not isinstance(self.started_at, Unset):
            started_at = self.started_at.isoformat()

        elapsed_time = self.elapsed_time

        processed_records = self.processed_records

        overall_state = self.overall_state

        filter_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.filter_, Unset):
            filter_ = self.filter_.to_dict()

        status: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = []
            for status_item_data in self.status:
                status_item = status_item_data.to_dict()
                status.append(status_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if replay_id is not UNSET:
            field_dict["replayId"] = replay_id
        if operation is not UNSET:
            field_dict["operation"] = operation
        if total_records is not UNSET:
            field_dict["totalRecords"] = total_records
        if started_at is not UNSET:
            field_dict["startedAt"] = started_at
        if elapsed_time is not UNSET:
            field_dict["elapsedTime"] = elapsed_time
        if processed_records is not UNSET:
            field_dict["processedRecords"] = processed_records
        if overall_state is not UNSET:
            field_dict["overallState"] = overall_state
        if filter_ is not UNSET:
            field_dict["filter"] = filter_
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.replay_filter import ReplayFilter
        from ..models.replay_status import ReplayStatus

        d = dict(src_dict)
        replay_id = d.pop("replayId", UNSET)

        operation = d.pop("operation", UNSET)

        total_records = d.pop("totalRecords", UNSET)

        _started_at = d.pop("startedAt", UNSET)
        started_at: datetime.datetime | Unset
        if isinstance(_started_at, Unset):
            started_at = UNSET
        else:
            started_at = isoparse(_started_at)

        elapsed_time = d.pop("elapsedTime", UNSET)

        processed_records = d.pop("processedRecords", UNSET)

        overall_state = d.pop("overallState", UNSET)

        _filter_ = d.pop("filter", UNSET)
        filter_: ReplayFilter | Unset
        if isinstance(_filter_, Unset):
            filter_ = UNSET
        else:
            filter_ = ReplayFilter.from_dict(_filter_)

        _status = d.pop("status", UNSET)
        status: list[ReplayStatus] | Unset = UNSET
        if _status is not UNSET:
            status = []
            for status_item_data in _status:
                status_item = ReplayStatus.from_dict(status_item_data)

                status.append(status_item)

        replay_status_response = cls(
            replay_id=replay_id,
            operation=operation,
            total_records=total_records,
            started_at=started_at,
            elapsed_time=elapsed_time,
            processed_records=processed_records,
            overall_state=overall_state,
            filter_=filter_,
            status=status,
        )

        replay_status_response.additional_properties = d
        return replay_status_response

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
