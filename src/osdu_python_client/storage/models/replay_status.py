from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ReplayStatus")


@_attrs_define
class ReplayStatus:
    """
    Attributes:
        kind (str | Unset):
        total_records (int | Unset):
        processed_records (int | Unset):
        state (str | Unset):
        started_at (datetime.datetime | Unset):
        elapsed_time (str | Unset):
    """

    kind: str | Unset = UNSET
    total_records: int | Unset = UNSET
    processed_records: int | Unset = UNSET
    state: str | Unset = UNSET
    started_at: datetime.datetime | Unset = UNSET
    elapsed_time: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        kind = self.kind

        total_records = self.total_records

        processed_records = self.processed_records

        state = self.state

        started_at: str | Unset = UNSET
        if not isinstance(self.started_at, Unset):
            started_at = self.started_at.isoformat()

        elapsed_time = self.elapsed_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if kind is not UNSET:
            field_dict["kind"] = kind
        if total_records is not UNSET:
            field_dict["totalRecords"] = total_records
        if processed_records is not UNSET:
            field_dict["processedRecords"] = processed_records
        if state is not UNSET:
            field_dict["state"] = state
        if started_at is not UNSET:
            field_dict["startedAt"] = started_at
        if elapsed_time is not UNSET:
            field_dict["elapsedTime"] = elapsed_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        kind = d.pop("kind", UNSET)

        total_records = d.pop("totalRecords", UNSET)

        processed_records = d.pop("processedRecords", UNSET)

        state = d.pop("state", UNSET)

        _started_at = d.pop("startedAt", UNSET)
        started_at: datetime.datetime | Unset
        if isinstance(_started_at, Unset):
            started_at = UNSET
        else:
            started_at = isoparse(_started_at)

        elapsed_time = d.pop("elapsedTime", UNSET)

        replay_status = cls(
            kind=kind,
            total_records=total_records,
            processed_records=processed_records,
            state=state,
            started_at=started_at,
            elapsed_time=elapsed_time,
        )

        replay_status.additional_properties = d
        return replay_status

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
