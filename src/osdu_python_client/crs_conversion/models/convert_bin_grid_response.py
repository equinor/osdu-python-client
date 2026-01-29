from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.abstract_bin_grid import AbstractBinGrid
    from ..models.max_mis_location import MaxMisLocation


T = TypeVar("T", bound="ConvertBinGridResponse")


@_attrs_define
class ConvertBinGridResponse:
    """
    Attributes:
        max_mis_location (MaxMisLocation | Unset):
        out_bin_grid (AbstractBinGrid | Unset):
        applied_operations (list[str] | Unset):
    """

    max_mis_location: MaxMisLocation | Unset = UNSET
    out_bin_grid: AbstractBinGrid | Unset = UNSET
    applied_operations: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        max_mis_location: dict[str, Any] | Unset = UNSET
        if not isinstance(self.max_mis_location, Unset):
            max_mis_location = self.max_mis_location.to_dict()

        out_bin_grid: dict[str, Any] | Unset = UNSET
        if not isinstance(self.out_bin_grid, Unset):
            out_bin_grid = self.out_bin_grid.to_dict()

        applied_operations: list[str] | Unset = UNSET
        if not isinstance(self.applied_operations, Unset):
            applied_operations = self.applied_operations

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if max_mis_location is not UNSET:
            field_dict["maxMisLocation"] = max_mis_location
        if out_bin_grid is not UNSET:
            field_dict["outBinGrid"] = out_bin_grid
        if applied_operations is not UNSET:
            field_dict["AppliedOperations"] = applied_operations

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.abstract_bin_grid import AbstractBinGrid
        from ..models.max_mis_location import MaxMisLocation

        d = dict(src_dict)
        _max_mis_location = d.pop("maxMisLocation", UNSET)
        max_mis_location: MaxMisLocation | Unset
        if isinstance(_max_mis_location, Unset):
            max_mis_location = UNSET
        else:
            max_mis_location = MaxMisLocation.from_dict(_max_mis_location)

        _out_bin_grid = d.pop("outBinGrid", UNSET)
        out_bin_grid: AbstractBinGrid | Unset
        if isinstance(_out_bin_grid, Unset):
            out_bin_grid = UNSET
        else:
            out_bin_grid = AbstractBinGrid.from_dict(_out_bin_grid)

        applied_operations = cast(list[str], d.pop("AppliedOperations", UNSET))

        convert_bin_grid_response = cls(
            max_mis_location=max_mis_location,
            out_bin_grid=out_bin_grid,
            applied_operations=applied_operations,
        )

        convert_bin_grid_response.additional_properties = d
        return convert_bin_grid_response

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
