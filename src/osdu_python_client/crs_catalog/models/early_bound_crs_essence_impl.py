from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.authority_code import AuthorityCode
    from ..models.compound_ct_essence_impl import CompoundCTEssenceImpl
    from ..models.late_bound_crs_essence import LateBoundCRSEssence
    from ..models.single_ct_essence_impl import SingleCTEssenceImpl


T = TypeVar("T", bound="EarlyBoundCRSEssenceImpl")


@_attrs_define
class EarlyBoundCRSEssenceImpl:
    """Early-bound coordinate reference system, i.e. a CRS with a transformation binding to WGS 84

    Attributes:
        auth_code (AuthorityCode | Unset):
        type_ (str | Unset):
        ver (str | Unset):
        name (str | Unset):
        late_bound_crs (LateBoundCRSEssence | Unset):
        single_ct (SingleCTEssenceImpl | Unset): Single cartographic transformation.
        compound_ct (CompoundCTEssenceImpl | Unset):
    """

    auth_code: AuthorityCode | Unset = UNSET
    type_: str | Unset = UNSET
    ver: str | Unset = UNSET
    name: str | Unset = UNSET
    late_bound_crs: LateBoundCRSEssence | Unset = UNSET
    single_ct: SingleCTEssenceImpl | Unset = UNSET
    compound_ct: CompoundCTEssenceImpl | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        auth_code: dict[str, Any] | Unset = UNSET
        if not isinstance(self.auth_code, Unset):
            auth_code = self.auth_code.to_dict()

        type_ = self.type_

        ver = self.ver

        name = self.name

        late_bound_crs: dict[str, Any] | Unset = UNSET
        if not isinstance(self.late_bound_crs, Unset):
            late_bound_crs = self.late_bound_crs.to_dict()

        single_ct: dict[str, Any] | Unset = UNSET
        if not isinstance(self.single_ct, Unset):
            single_ct = self.single_ct.to_dict()

        compound_ct: dict[str, Any] | Unset = UNSET
        if not isinstance(self.compound_ct, Unset):
            compound_ct = self.compound_ct.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if auth_code is not UNSET:
            field_dict["authCode"] = auth_code
        if type_ is not UNSET:
            field_dict["type"] = type_
        if ver is not UNSET:
            field_dict["ver"] = ver
        if name is not UNSET:
            field_dict["name"] = name
        if late_bound_crs is not UNSET:
            field_dict["lateBoundCRS"] = late_bound_crs
        if single_ct is not UNSET:
            field_dict["singleCT"] = single_ct
        if compound_ct is not UNSET:
            field_dict["compoundCT"] = compound_ct

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.authority_code import AuthorityCode
        from ..models.compound_ct_essence_impl import CompoundCTEssenceImpl
        from ..models.late_bound_crs_essence import LateBoundCRSEssence
        from ..models.single_ct_essence_impl import SingleCTEssenceImpl

        d = dict(src_dict)
        _auth_code = d.pop("authCode", UNSET)
        auth_code: AuthorityCode | Unset
        if isinstance(_auth_code, Unset):
            auth_code = UNSET
        else:
            auth_code = AuthorityCode.from_dict(_auth_code)

        type_ = d.pop("type", UNSET)

        ver = d.pop("ver", UNSET)

        name = d.pop("name", UNSET)

        _late_bound_crs = d.pop("lateBoundCRS", UNSET)
        late_bound_crs: LateBoundCRSEssence | Unset
        if isinstance(_late_bound_crs, Unset):
            late_bound_crs = UNSET
        else:
            late_bound_crs = LateBoundCRSEssence.from_dict(_late_bound_crs)

        _single_ct = d.pop("singleCT", UNSET)
        single_ct: SingleCTEssenceImpl | Unset
        if isinstance(_single_ct, Unset):
            single_ct = UNSET
        else:
            single_ct = SingleCTEssenceImpl.from_dict(_single_ct)

        _compound_ct = d.pop("compoundCT", UNSET)
        compound_ct: CompoundCTEssenceImpl | Unset
        if isinstance(_compound_ct, Unset):
            compound_ct = UNSET
        else:
            compound_ct = CompoundCTEssenceImpl.from_dict(_compound_ct)

        early_bound_crs_essence_impl = cls(
            auth_code=auth_code,
            type_=type_,
            ver=ver,
            name=name,
            late_bound_crs=late_bound_crs,
            single_ct=single_ct,
            compound_ct=compound_ct,
        )

        early_bound_crs_essence_impl.additional_properties = d
        return early_bound_crs_essence_impl

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
