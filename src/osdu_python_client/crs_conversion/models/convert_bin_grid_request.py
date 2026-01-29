from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.abstract_bin_grid import AbstractBinGrid


T = TypeVar("T", bound="ConvertBinGridRequest")


@_attrs_define
class ConvertBinGridRequest:
    """
    Attributes:
        to_crs (str | Unset):
        in_bin_grid (AbstractBinGrid | Unset):
    """

    to_crs: str | Unset = UNSET
    in_bin_grid: AbstractBinGrid | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        to_crs = self.to_crs

        in_bin_grid: dict[str, Any] | Unset = UNSET
        if not isinstance(self.in_bin_grid, Unset):
            in_bin_grid = self.in_bin_grid.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if to_crs is not UNSET:
            field_dict["toCRS"] = to_crs
        if in_bin_grid is not UNSET:
            field_dict["inBinGrid"] = in_bin_grid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.abstract_bin_grid import AbstractBinGrid

        d = dict(src_dict)
        to_crs = d.pop("toCRS", UNSET)

        _in_bin_grid = d.pop("inBinGrid", UNSET)
        in_bin_grid: AbstractBinGrid | Unset
        if isinstance(_in_bin_grid, Unset):
            in_bin_grid = UNSET
        else:
            in_bin_grid = AbstractBinGrid.from_dict(_in_bin_grid)

        convert_bin_grid_request = cls(
            to_crs=to_crs,
            in_bin_grid=in_bin_grid,
        )

        convert_bin_grid_request.additional_properties = d
        return convert_bin_grid_request

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
