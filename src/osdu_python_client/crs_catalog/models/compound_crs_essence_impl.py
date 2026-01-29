from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.authority_code import AuthorityCode
    from ..models.early_bound_crs_essence_impl import EarlyBoundCRSEssenceImpl
    from ..models.essence import Essence
    from ..models.late_bound_crs_essence_impl import LateBoundCRSEssenceImpl


T = TypeVar("T", bound="CompoundCRSEssenceImpl")


@_attrs_define
class CompoundCRSEssenceImpl:
    """Compound coordinate reference system aggregating a horizontal to a vertical CRS

    Attributes:
        horizontal_crs (Essence | Unset):
        vertical_crs (Essence | Unset):
        auth_code (AuthorityCode | Unset):
        type_ (str | Unset):
        ver (str | Unset):
        name (str | Unset):
        horz_late_bound_crs (LateBoundCRSEssenceImpl | Unset): Late-bound coordinate reference system, i.e. a CRS
            without a transformation binding to WGS 84
        vert_late_bound_crs (LateBoundCRSEssenceImpl | Unset): Late-bound coordinate reference system, i.e. a CRS
            without a transformation binding to WGS 84
        horz_early_bound_crs (EarlyBoundCRSEssenceImpl | Unset): Early-bound coordinate reference system, i.e. a CRS
            with a transformation binding to WGS 84
        vert_early_bound_crs (EarlyBoundCRSEssenceImpl | Unset): Early-bound coordinate reference system, i.e. a CRS
            with a transformation binding to WGS 84
    """

    horizontal_crs: Essence | Unset = UNSET
    vertical_crs: Essence | Unset = UNSET
    auth_code: AuthorityCode | Unset = UNSET
    type_: str | Unset = UNSET
    ver: str | Unset = UNSET
    name: str | Unset = UNSET
    horz_late_bound_crs: LateBoundCRSEssenceImpl | Unset = UNSET
    vert_late_bound_crs: LateBoundCRSEssenceImpl | Unset = UNSET
    horz_early_bound_crs: EarlyBoundCRSEssenceImpl | Unset = UNSET
    vert_early_bound_crs: EarlyBoundCRSEssenceImpl | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        horizontal_crs: dict[str, Any] | Unset = UNSET
        if not isinstance(self.horizontal_crs, Unset):
            horizontal_crs = self.horizontal_crs.to_dict()

        vertical_crs: dict[str, Any] | Unset = UNSET
        if not isinstance(self.vertical_crs, Unset):
            vertical_crs = self.vertical_crs.to_dict()

        auth_code: dict[str, Any] | Unset = UNSET
        if not isinstance(self.auth_code, Unset):
            auth_code = self.auth_code.to_dict()

        type_ = self.type_

        ver = self.ver

        name = self.name

        horz_late_bound_crs: dict[str, Any] | Unset = UNSET
        if not isinstance(self.horz_late_bound_crs, Unset):
            horz_late_bound_crs = self.horz_late_bound_crs.to_dict()

        vert_late_bound_crs: dict[str, Any] | Unset = UNSET
        if not isinstance(self.vert_late_bound_crs, Unset):
            vert_late_bound_crs = self.vert_late_bound_crs.to_dict()

        horz_early_bound_crs: dict[str, Any] | Unset = UNSET
        if not isinstance(self.horz_early_bound_crs, Unset):
            horz_early_bound_crs = self.horz_early_bound_crs.to_dict()

        vert_early_bound_crs: dict[str, Any] | Unset = UNSET
        if not isinstance(self.vert_early_bound_crs, Unset):
            vert_early_bound_crs = self.vert_early_bound_crs.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if horizontal_crs is not UNSET:
            field_dict["horizontalCRS"] = horizontal_crs
        if vertical_crs is not UNSET:
            field_dict["verticalCRS"] = vertical_crs
        if auth_code is not UNSET:
            field_dict["authCode"] = auth_code
        if type_ is not UNSET:
            field_dict["type"] = type_
        if ver is not UNSET:
            field_dict["ver"] = ver
        if name is not UNSET:
            field_dict["name"] = name
        if horz_late_bound_crs is not UNSET:
            field_dict["horzLateBoundCRS"] = horz_late_bound_crs
        if vert_late_bound_crs is not UNSET:
            field_dict["vertLateBoundCRS"] = vert_late_bound_crs
        if horz_early_bound_crs is not UNSET:
            field_dict["horzEarlyBoundCRS"] = horz_early_bound_crs
        if vert_early_bound_crs is not UNSET:
            field_dict["vertEarlyBoundCRS"] = vert_early_bound_crs

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.authority_code import AuthorityCode
        from ..models.early_bound_crs_essence_impl import EarlyBoundCRSEssenceImpl
        from ..models.essence import Essence
        from ..models.late_bound_crs_essence_impl import LateBoundCRSEssenceImpl

        d = dict(src_dict)
        _horizontal_crs = d.pop("horizontalCRS", UNSET)
        horizontal_crs: Essence | Unset
        if isinstance(_horizontal_crs, Unset):
            horizontal_crs = UNSET
        else:
            horizontal_crs = Essence.from_dict(_horizontal_crs)

        _vertical_crs = d.pop("verticalCRS", UNSET)
        vertical_crs: Essence | Unset
        if isinstance(_vertical_crs, Unset):
            vertical_crs = UNSET
        else:
            vertical_crs = Essence.from_dict(_vertical_crs)

        _auth_code = d.pop("authCode", UNSET)
        auth_code: AuthorityCode | Unset
        if isinstance(_auth_code, Unset):
            auth_code = UNSET
        else:
            auth_code = AuthorityCode.from_dict(_auth_code)

        type_ = d.pop("type", UNSET)

        ver = d.pop("ver", UNSET)

        name = d.pop("name", UNSET)

        _horz_late_bound_crs = d.pop("horzLateBoundCRS", UNSET)
        horz_late_bound_crs: LateBoundCRSEssenceImpl | Unset
        if isinstance(_horz_late_bound_crs, Unset):
            horz_late_bound_crs = UNSET
        else:
            horz_late_bound_crs = LateBoundCRSEssenceImpl.from_dict(
                _horz_late_bound_crs
            )

        _vert_late_bound_crs = d.pop("vertLateBoundCRS", UNSET)
        vert_late_bound_crs: LateBoundCRSEssenceImpl | Unset
        if isinstance(_vert_late_bound_crs, Unset):
            vert_late_bound_crs = UNSET
        else:
            vert_late_bound_crs = LateBoundCRSEssenceImpl.from_dict(
                _vert_late_bound_crs
            )

        _horz_early_bound_crs = d.pop("horzEarlyBoundCRS", UNSET)
        horz_early_bound_crs: EarlyBoundCRSEssenceImpl | Unset
        if isinstance(_horz_early_bound_crs, Unset):
            horz_early_bound_crs = UNSET
        else:
            horz_early_bound_crs = EarlyBoundCRSEssenceImpl.from_dict(
                _horz_early_bound_crs
            )

        _vert_early_bound_crs = d.pop("vertEarlyBoundCRS", UNSET)
        vert_early_bound_crs: EarlyBoundCRSEssenceImpl | Unset
        if isinstance(_vert_early_bound_crs, Unset):
            vert_early_bound_crs = UNSET
        else:
            vert_early_bound_crs = EarlyBoundCRSEssenceImpl.from_dict(
                _vert_early_bound_crs
            )

        compound_crs_essence_impl = cls(
            horizontal_crs=horizontal_crs,
            vertical_crs=vertical_crs,
            auth_code=auth_code,
            type_=type_,
            ver=ver,
            name=name,
            horz_late_bound_crs=horz_late_bound_crs,
            vert_late_bound_crs=vert_late_bound_crs,
            horz_early_bound_crs=horz_early_bound_crs,
            vert_early_bound_crs=vert_early_bound_crs,
        )

        compound_crs_essence_impl.additional_properties = d
        return compound_crs_essence_impl

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
