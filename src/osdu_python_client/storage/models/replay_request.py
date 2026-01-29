from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.replay_filter import ReplayFilter


T = TypeVar("T", bound="ReplayRequest")


@_attrs_define
class ReplayRequest:
    """
    Attributes:
        replay_id (str | Unset):
        operation (str | Unset):
        filter_ (ReplayFilter | Unset):
    """

    replay_id: str | Unset = UNSET
    operation: str | Unset = UNSET
    filter_: ReplayFilter | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        replay_id = self.replay_id

        operation = self.operation

        filter_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.filter_, Unset):
            filter_ = self.filter_.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if replay_id is not UNSET:
            field_dict["replayId"] = replay_id
        if operation is not UNSET:
            field_dict["operation"] = operation
        if filter_ is not UNSET:
            field_dict["filter"] = filter_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.replay_filter import ReplayFilter

        d = dict(src_dict)
        replay_id = d.pop("replayId", UNSET)

        operation = d.pop("operation", UNSET)

        _filter_ = d.pop("filter", UNSET)
        filter_: ReplayFilter | Unset
        if isinstance(_filter_, Unset):
            filter_ = UNSET
        else:
            filter_ = ReplayFilter.from_dict(_filter_)

        replay_request = cls(
            replay_id=replay_id,
            operation=operation,
            filter_=filter_,
        )

        replay_request.additional_properties = d
        return replay_request

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
