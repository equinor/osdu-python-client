from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cursor_query_response_results_item import (
        CursorQueryResponseResultsItem,
    )


T = TypeVar("T", bound="CursorQueryResponse")


@_attrs_define
class CursorQueryResponse:
    """
    Attributes:
        cursor (str | Unset):
        results (list[CursorQueryResponseResultsItem] | Unset):
        total_count (int | Unset):
    """

    cursor: str | Unset = UNSET
    results: list[CursorQueryResponseResultsItem] | Unset = UNSET
    total_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cursor = self.cursor

        results: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.results, Unset):
            results = []
            for results_item_data in self.results:
                results_item = results_item_data.to_dict()
                results.append(results_item)

        total_count = self.total_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cursor is not UNSET:
            field_dict["cursor"] = cursor
        if results is not UNSET:
            field_dict["results"] = results
        if total_count is not UNSET:
            field_dict["totalCount"] = total_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cursor_query_response_results_item import (
            CursorQueryResponseResultsItem,
        )

        d = dict(src_dict)
        cursor = d.pop("cursor", UNSET)

        _results = d.pop("results", UNSET)
        results: list[CursorQueryResponseResultsItem] | Unset = UNSET
        if _results is not UNSET:
            results = []
            for results_item_data in _results:
                results_item = CursorQueryResponseResultsItem.from_dict(
                    results_item_data
                )

                results.append(results_item)

        total_count = d.pop("totalCount", UNSET)

        cursor_query_response = cls(
            cursor=cursor,
            results=results,
            total_count=total_count,
        )

        cursor_query_response.additional_properties = d
        return cursor_query_response

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
