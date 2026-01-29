from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.crs import CRS


T = TypeVar("T", bound="CRSResults")


@_attrs_define
class CRSResults:
    """A response containing a list of CRSes.

    Attributes:
        offset (int | Unset): The offset of the first item in the list of all AreaOfUse. It is optional and is 0 by
            default.
        count (int | Unset): The maximum number of the AreaOfUse returned. It is optional and is 100 by default.
        total_count (int | Unset): The mode of return: 'persistable_reference' (default) string or 'essence' structure
            or both 'persistable_reference_essence'.
        crses (list[CRS] | Unset): A response containing a list of CRSes.
    """

    offset: int | Unset = UNSET
    count: int | Unset = UNSET
    total_count: int | Unset = UNSET
    crses: list[CRS] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        offset = self.offset

        count = self.count

        total_count = self.total_count

        crses: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.crses, Unset):
            crses = []
            for crses_item_data in self.crses:
                crses_item = crses_item_data.to_dict()
                crses.append(crses_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if offset is not UNSET:
            field_dict["offset"] = offset
        if count is not UNSET:
            field_dict["count"] = count
        if total_count is not UNSET:
            field_dict["totalCount"] = total_count
        if crses is not UNSET:
            field_dict["crses"] = crses

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.crs import CRS

        d = dict(src_dict)
        offset = d.pop("offset", UNSET)

        count = d.pop("count", UNSET)

        total_count = d.pop("totalCount", UNSET)

        _crses = d.pop("crses", UNSET)
        crses: list[CRS] | Unset = UNSET
        if _crses is not UNSET:
            crses = []
            for crses_item_data in _crses:
                crses_item = CRS.from_dict(crses_item_data)

                crses.append(crses_item)

        crs_results = cls(
            offset=offset,
            count=count,
            total_count=total_count,
            crses=crses,
        )

        crs_results.additional_properties = d
        return crs_results

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
