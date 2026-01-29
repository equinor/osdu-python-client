from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.unit_system_info import UnitSystemInfo


T = TypeVar("T", bound="UnitSystemInfoResponse")


@_attrs_define
class UnitSystemInfoResponse:
    """The unit system info structures

    Attributes:
        unit_system_info_list (list[UnitSystemInfo] | Unset): The array of unit system names
        total_count (int | Unset): The total number of elements in the list defined in the catalog
        offset (int | Unset): The offset into the list as requested
        count (int | Unset):
    """

    unit_system_info_list: list[UnitSystemInfo] | Unset = UNSET
    total_count: int | Unset = UNSET
    offset: int | Unset = UNSET
    count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        unit_system_info_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.unit_system_info_list, Unset):
            unit_system_info_list = []
            for unit_system_info_list_item_data in self.unit_system_info_list:
                unit_system_info_list_item = unit_system_info_list_item_data.to_dict()
                unit_system_info_list.append(unit_system_info_list_item)

        total_count = self.total_count

        offset = self.offset

        count = self.count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if unit_system_info_list is not UNSET:
            field_dict["unitSystemInfoList"] = unit_system_info_list
        if total_count is not UNSET:
            field_dict["totalCount"] = total_count
        if offset is not UNSET:
            field_dict["offset"] = offset
        if count is not UNSET:
            field_dict["count"] = count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.unit_system_info import UnitSystemInfo

        d = dict(src_dict)
        _unit_system_info_list = d.pop("unitSystemInfoList", UNSET)
        unit_system_info_list: list[UnitSystemInfo] | Unset = UNSET
        if _unit_system_info_list is not UNSET:
            unit_system_info_list = []
            for unit_system_info_list_item_data in _unit_system_info_list:
                unit_system_info_list_item = UnitSystemInfo.from_dict(
                    unit_system_info_list_item_data
                )

                unit_system_info_list.append(unit_system_info_list_item)

        total_count = d.pop("totalCount", UNSET)

        offset = d.pop("offset", UNSET)

        count = d.pop("count", UNSET)

        unit_system_info_response = cls(
            unit_system_info_list=unit_system_info_list,
            total_count=total_count,
            offset=offset,
            count=count,
        )

        unit_system_info_response.additional_properties = d
        return unit_system_info_response

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
