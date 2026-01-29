from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cursor_query_request_kind import CursorQueryRequestKind
    from ..models.sort_query import SortQuery
    from ..models.spatial_filter import SpatialFilter


T = TypeVar("T", bound="CursorQueryRequest")


@_attrs_define
class CursorQueryRequest:
    """
    Attributes:
        kind (CursorQueryRequestKind):
        limit (int | Unset):
        query (str | Unset):
        suggest_phrase (str | Unset):
        highlighted_fields (list[str] | Unset):
        returned_fields (list[str] | Unset):
        sort (SortQuery | Unset):
        query_as_owner (bool | Unset):
        track_total_count (bool | Unset):
        spatial_filter (SpatialFilter | Unset):
        cursor (str | Unset):
    """

    kind: CursorQueryRequestKind
    limit: int | Unset = UNSET
    query: str | Unset = UNSET
    suggest_phrase: str | Unset = UNSET
    highlighted_fields: list[str] | Unset = UNSET
    returned_fields: list[str] | Unset = UNSET
    sort: SortQuery | Unset = UNSET
    query_as_owner: bool | Unset = UNSET
    track_total_count: bool | Unset = UNSET
    spatial_filter: SpatialFilter | Unset = UNSET
    cursor: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        kind = self.kind.to_dict()

        limit = self.limit

        query = self.query

        suggest_phrase = self.suggest_phrase

        highlighted_fields: list[str] | Unset = UNSET
        if not isinstance(self.highlighted_fields, Unset):
            highlighted_fields = self.highlighted_fields

        returned_fields: list[str] | Unset = UNSET
        if not isinstance(self.returned_fields, Unset):
            returned_fields = self.returned_fields

        sort: dict[str, Any] | Unset = UNSET
        if not isinstance(self.sort, Unset):
            sort = self.sort.to_dict()

        query_as_owner = self.query_as_owner

        track_total_count = self.track_total_count

        spatial_filter: dict[str, Any] | Unset = UNSET
        if not isinstance(self.spatial_filter, Unset):
            spatial_filter = self.spatial_filter.to_dict()

        cursor = self.cursor

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "kind": kind,
            }
        )
        if limit is not UNSET:
            field_dict["limit"] = limit
        if query is not UNSET:
            field_dict["query"] = query
        if suggest_phrase is not UNSET:
            field_dict["suggestPhrase"] = suggest_phrase
        if highlighted_fields is not UNSET:
            field_dict["highlightedFields"] = highlighted_fields
        if returned_fields is not UNSET:
            field_dict["returnedFields"] = returned_fields
        if sort is not UNSET:
            field_dict["sort"] = sort
        if query_as_owner is not UNSET:
            field_dict["queryAsOwner"] = query_as_owner
        if track_total_count is not UNSET:
            field_dict["trackTotalCount"] = track_total_count
        if spatial_filter is not UNSET:
            field_dict["spatialFilter"] = spatial_filter
        if cursor is not UNSET:
            field_dict["cursor"] = cursor

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cursor_query_request_kind import CursorQueryRequestKind
        from ..models.sort_query import SortQuery
        from ..models.spatial_filter import SpatialFilter

        d = dict(src_dict)
        kind = CursorQueryRequestKind.from_dict(d.pop("kind"))

        limit = d.pop("limit", UNSET)

        query = d.pop("query", UNSET)

        suggest_phrase = d.pop("suggestPhrase", UNSET)

        highlighted_fields = cast(list[str], d.pop("highlightedFields", UNSET))

        returned_fields = cast(list[str], d.pop("returnedFields", UNSET))

        _sort = d.pop("sort", UNSET)
        sort: SortQuery | Unset
        if isinstance(_sort, Unset):
            sort = UNSET
        else:
            sort = SortQuery.from_dict(_sort)

        query_as_owner = d.pop("queryAsOwner", UNSET)

        track_total_count = d.pop("trackTotalCount", UNSET)

        _spatial_filter = d.pop("spatialFilter", UNSET)
        spatial_filter: SpatialFilter | Unset
        if isinstance(_spatial_filter, Unset):
            spatial_filter = UNSET
        else:
            spatial_filter = SpatialFilter.from_dict(_spatial_filter)

        cursor = d.pop("cursor", UNSET)

        cursor_query_request = cls(
            kind=kind,
            limit=limit,
            query=query,
            suggest_phrase=suggest_phrase,
            highlighted_fields=highlighted_fields,
            returned_fields=returned_fields,
            sort=sort,
            query_as_owner=query_as_owner,
            track_total_count=track_total_count,
            spatial_filter=spatial_filter,
            cursor=cursor,
        )

        cursor_query_request.additional_properties = d
        return cursor_query_request

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
