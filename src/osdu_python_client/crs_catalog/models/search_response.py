from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cursor_query_response import CursorQueryResponse
    from ..models.query_response import QueryResponse


T = TypeVar("T", bound="SearchResponse")


@_attrs_define
class SearchResponse:
    """Results for most V3 endpoints

    Attributes:
        search_results (QueryResponse | Unset): Results from Search service
        cursor_search_results (CursorQueryResponse | Unset):
        query (str | Unset): Query string used against Search service
    """

    search_results: QueryResponse | Unset = UNSET
    cursor_search_results: CursorQueryResponse | Unset = UNSET
    query: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        search_results: dict[str, Any] | Unset = UNSET
        if not isinstance(self.search_results, Unset):
            search_results = self.search_results.to_dict()

        cursor_search_results: dict[str, Any] | Unset = UNSET
        if not isinstance(self.cursor_search_results, Unset):
            cursor_search_results = self.cursor_search_results.to_dict()

        query = self.query

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if search_results is not UNSET:
            field_dict["searchResults"] = search_results
        if cursor_search_results is not UNSET:
            field_dict["cursorSearchResults"] = cursor_search_results
        if query is not UNSET:
            field_dict["query"] = query

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cursor_query_response import CursorQueryResponse
        from ..models.query_response import QueryResponse

        d = dict(src_dict)
        _search_results = d.pop("searchResults", UNSET)
        search_results: QueryResponse | Unset
        if isinstance(_search_results, Unset):
            search_results = UNSET
        else:
            search_results = QueryResponse.from_dict(_search_results)

        _cursor_search_results = d.pop("cursorSearchResults", UNSET)
        cursor_search_results: CursorQueryResponse | Unset
        if isinstance(_cursor_search_results, Unset):
            cursor_search_results = UNSET
        else:
            cursor_search_results = CursorQueryResponse.from_dict(
                _cursor_search_results
            )

        query = d.pop("query", UNSET)

        search_response = cls(
            search_results=search_results,
            cursor_search_results=cursor_search_results,
            query=query,
        )

        search_response.additional_properties = d
        return search_response

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
