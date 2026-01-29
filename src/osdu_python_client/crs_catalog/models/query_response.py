from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.aggregation_response import AggregationResponse
    from ..models.query_response_results_item import QueryResponseResultsItem


T = TypeVar("T", bound="QueryResponse")


@_attrs_define
class QueryResponse:
    """Results from Search service

    Attributes:
        results (list[QueryResponseResultsItem] | Unset):
        aggregations (list[AggregationResponse] | Unset):
        phrase_suggestions (list[str] | Unset):
        total_count (int | Unset):
    """

    results: list[QueryResponseResultsItem] | Unset = UNSET
    aggregations: list[AggregationResponse] | Unset = UNSET
    phrase_suggestions: list[str] | Unset = UNSET
    total_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        results: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.results, Unset):
            results = []
            for results_item_data in self.results:
                results_item = results_item_data.to_dict()
                results.append(results_item)

        aggregations: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.aggregations, Unset):
            aggregations = []
            for aggregations_item_data in self.aggregations:
                aggregations_item = aggregations_item_data.to_dict()
                aggregations.append(aggregations_item)

        phrase_suggestions: list[str] | Unset = UNSET
        if not isinstance(self.phrase_suggestions, Unset):
            phrase_suggestions = self.phrase_suggestions

        total_count = self.total_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if results is not UNSET:
            field_dict["results"] = results
        if aggregations is not UNSET:
            field_dict["aggregations"] = aggregations
        if phrase_suggestions is not UNSET:
            field_dict["phraseSuggestions"] = phrase_suggestions
        if total_count is not UNSET:
            field_dict["totalCount"] = total_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.aggregation_response import AggregationResponse
        from ..models.query_response_results_item import QueryResponseResultsItem

        d = dict(src_dict)
        _results = d.pop("results", UNSET)
        results: list[QueryResponseResultsItem] | Unset = UNSET
        if _results is not UNSET:
            results = []
            for results_item_data in _results:
                results_item = QueryResponseResultsItem.from_dict(results_item_data)

                results.append(results_item)

        _aggregations = d.pop("aggregations", UNSET)
        aggregations: list[AggregationResponse] | Unset = UNSET
        if _aggregations is not UNSET:
            aggregations = []
            for aggregations_item_data in _aggregations:
                aggregations_item = AggregationResponse.from_dict(
                    aggregations_item_data
                )

                aggregations.append(aggregations_item)

        phrase_suggestions = cast(list[str], d.pop("phraseSuggestions", UNSET))

        total_count = d.pop("totalCount", UNSET)

        query_response = cls(
            results=results,
            aggregations=aggregations,
            phrase_suggestions=phrase_suggestions,
            total_count=total_count,
        )

        query_response.additional_properties = d
        return query_response

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
