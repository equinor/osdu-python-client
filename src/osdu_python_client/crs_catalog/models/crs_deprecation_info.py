from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.crs import CRS


T = TypeVar("T", bound="CRSDeprecationInfo")


@_attrs_define
class CRSDeprecationInfo:
    """
    Attributes:
        superseded_by_crs (CRS | Unset):
        deprecation_state (str | Unset):
        remarks (str | Unset):
    """

    superseded_by_crs: CRS | Unset = UNSET
    deprecation_state: str | Unset = UNSET
    remarks: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        superseded_by_crs: dict[str, Any] | Unset = UNSET
        if not isinstance(self.superseded_by_crs, Unset):
            superseded_by_crs = self.superseded_by_crs.to_dict()

        deprecation_state = self.deprecation_state

        remarks = self.remarks

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if superseded_by_crs is not UNSET:
            field_dict["supersededByCRS"] = superseded_by_crs
        if deprecation_state is not UNSET:
            field_dict["deprecationState"] = deprecation_state
        if remarks is not UNSET:
            field_dict["remarks"] = remarks

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.crs import CRS

        d = dict(src_dict)
        _superseded_by_crs = d.pop("supersededByCRS", UNSET)
        superseded_by_crs: CRS | Unset
        if isinstance(_superseded_by_crs, Unset):
            superseded_by_crs = UNSET
        else:
            superseded_by_crs = CRS.from_dict(_superseded_by_crs)

        deprecation_state = d.pop("deprecationState", UNSET)

        remarks = d.pop("remarks", UNSET)

        crs_deprecation_info = cls(
            superseded_by_crs=superseded_by_crs,
            deprecation_state=deprecation_state,
            remarks=remarks,
        )

        crs_deprecation_info.additional_properties = d
        return crs_deprecation_info

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
