from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.area_of_use import AreaOfUse


T = TypeVar("T", bound="AreaOfUseResults")


@_attrs_define
class AreaOfUseResults:
    """Object to hold the list of `AreaOfUse` objects from a search

    Attributes:
        offset (int | Unset): The offset of the first item in the list of all AreaOfUse. It is optional and is 0 by
            default.
        count (int | Unset): The maximum number of the AreaOfUse returned. It is optional and is 100 by default.
        total_count (int | Unset): The mode of return: 'persistable_reference' (default) string or 'essence' structure
            or both 'persistable_reference_essence'.
        areas_of_use (list[AreaOfUse] | Unset):
    """

    offset: int | Unset = UNSET
    count: int | Unset = UNSET
    total_count: int | Unset = UNSET
    areas_of_use: list[AreaOfUse] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        offset = self.offset

        count = self.count

        total_count = self.total_count

        areas_of_use: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.areas_of_use, Unset):
            areas_of_use = []
            for areas_of_use_item_data in self.areas_of_use:
                areas_of_use_item = areas_of_use_item_data.to_dict()
                areas_of_use.append(areas_of_use_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if offset is not UNSET:
            field_dict["offset"] = offset
        if count is not UNSET:
            field_dict["count"] = count
        if total_count is not UNSET:
            field_dict["totalCount"] = total_count
        if areas_of_use is not UNSET:
            field_dict["areasOfUse"] = areas_of_use

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.area_of_use import AreaOfUse

        d = dict(src_dict)
        offset = d.pop("offset", UNSET)

        count = d.pop("count", UNSET)

        total_count = d.pop("totalCount", UNSET)

        _areas_of_use = d.pop("areasOfUse", UNSET)
        areas_of_use: list[AreaOfUse] | Unset = UNSET
        if _areas_of_use is not UNSET:
            areas_of_use = []
            for areas_of_use_item_data in _areas_of_use:
                areas_of_use_item = AreaOfUse.from_dict(areas_of_use_item_data)

                areas_of_use.append(areas_of_use_item)

        area_of_use_results = cls(
            offset=offset,
            count=count,
            total_count=total_count,
            areas_of_use=areas_of_use,
        )

        area_of_use_results.additional_properties = d
        return area_of_use_results

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
