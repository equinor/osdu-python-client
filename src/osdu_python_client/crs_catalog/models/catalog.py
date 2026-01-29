from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.area_of_use import AreaOfUse
    from ..models.catalog_attributes import CatalogAttributes
    from ..models.compound_crs import CompoundCRS
    from ..models.compound_ct import CompoundCT
    from ..models.crs import CRS
    from ..models.ct import CT
    from ..models.early_bound_crs import EarlyBoundCRS
    from ..models.late_bound_crs import LateBoundCRS
    from ..models.single_ct import SingleCT


T = TypeVar("T", bound="Catalog")


@_attrs_define
class Catalog:
    """
    Attributes:
        attributes (CatalogAttributes | Unset):
        single_c_ts_count (int | Unset):
        area_of_use_count (int | Unset):
        catalog_response (Catalog | Unset):
        areas_of_use (list[AreaOfUse] | Unset):
        all_cr_ses (list[CRS] | Unset):
        late_bound_cr_ses (list[LateBoundCRS] | Unset):
        early_bound_cr_ses (list[EarlyBoundCRS] | Unset):
        compound_cr_ses (list[CompoundCRS] | Unset):
        all_c_ts (list[CT] | Unset):
        single_c_ts (list[SingleCT] | Unset):
        compound_c_ts (list[CompoundCT] | Unset):
        compound_c_ts_count (int | Unset):
        late_bound_cr_ses_count (int | Unset):
        early_bound_cr_ses_count (int | Unset):
        compound_cr_ses_count (int | Unset):
    """

    attributes: CatalogAttributes | Unset = UNSET
    single_c_ts_count: int | Unset = UNSET
    area_of_use_count: int | Unset = UNSET
    catalog_response: Catalog | Unset = UNSET
    areas_of_use: list[AreaOfUse] | Unset = UNSET
    all_cr_ses: list[CRS] | Unset = UNSET
    late_bound_cr_ses: list[LateBoundCRS] | Unset = UNSET
    early_bound_cr_ses: list[EarlyBoundCRS] | Unset = UNSET
    compound_cr_ses: list[CompoundCRS] | Unset = UNSET
    all_c_ts: list[CT] | Unset = UNSET
    single_c_ts: list[SingleCT] | Unset = UNSET
    compound_c_ts: list[CompoundCT] | Unset = UNSET
    compound_c_ts_count: int | Unset = UNSET
    late_bound_cr_ses_count: int | Unset = UNSET
    early_bound_cr_ses_count: int | Unset = UNSET
    compound_cr_ses_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        attributes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.attributes, Unset):
            attributes = self.attributes.to_dict()

        single_c_ts_count = self.single_c_ts_count

        area_of_use_count = self.area_of_use_count

        catalog_response: dict[str, Any] | Unset = UNSET
        if not isinstance(self.catalog_response, Unset):
            catalog_response = self.catalog_response.to_dict()

        areas_of_use: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.areas_of_use, Unset):
            areas_of_use = []
            for areas_of_use_item_data in self.areas_of_use:
                areas_of_use_item = areas_of_use_item_data.to_dict()
                areas_of_use.append(areas_of_use_item)

        all_cr_ses: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.all_cr_ses, Unset):
            all_cr_ses = []
            for all_cr_ses_item_data in self.all_cr_ses:
                all_cr_ses_item = all_cr_ses_item_data.to_dict()
                all_cr_ses.append(all_cr_ses_item)

        late_bound_cr_ses: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.late_bound_cr_ses, Unset):
            late_bound_cr_ses = []
            for late_bound_cr_ses_item_data in self.late_bound_cr_ses:
                late_bound_cr_ses_item = late_bound_cr_ses_item_data.to_dict()
                late_bound_cr_ses.append(late_bound_cr_ses_item)

        early_bound_cr_ses: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.early_bound_cr_ses, Unset):
            early_bound_cr_ses = []
            for early_bound_cr_ses_item_data in self.early_bound_cr_ses:
                early_bound_cr_ses_item = early_bound_cr_ses_item_data.to_dict()
                early_bound_cr_ses.append(early_bound_cr_ses_item)

        compound_cr_ses: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.compound_cr_ses, Unset):
            compound_cr_ses = []
            for compound_cr_ses_item_data in self.compound_cr_ses:
                compound_cr_ses_item = compound_cr_ses_item_data.to_dict()
                compound_cr_ses.append(compound_cr_ses_item)

        all_c_ts: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.all_c_ts, Unset):
            all_c_ts = []
            for all_c_ts_item_data in self.all_c_ts:
                all_c_ts_item = all_c_ts_item_data.to_dict()
                all_c_ts.append(all_c_ts_item)

        single_c_ts: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.single_c_ts, Unset):
            single_c_ts = []
            for single_c_ts_item_data in self.single_c_ts:
                single_c_ts_item = single_c_ts_item_data.to_dict()
                single_c_ts.append(single_c_ts_item)

        compound_c_ts: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.compound_c_ts, Unset):
            compound_c_ts = []
            for compound_c_ts_item_data in self.compound_c_ts:
                compound_c_ts_item = compound_c_ts_item_data.to_dict()
                compound_c_ts.append(compound_c_ts_item)

        compound_c_ts_count = self.compound_c_ts_count

        late_bound_cr_ses_count = self.late_bound_cr_ses_count

        early_bound_cr_ses_count = self.early_bound_cr_ses_count

        compound_cr_ses_count = self.compound_cr_ses_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if attributes is not UNSET:
            field_dict["attributes"] = attributes
        if single_c_ts_count is not UNSET:
            field_dict["singleCTsCount"] = single_c_ts_count
        if area_of_use_count is not UNSET:
            field_dict["areaOfUseCount"] = area_of_use_count
        if catalog_response is not UNSET:
            field_dict["catalogResponse"] = catalog_response
        if areas_of_use is not UNSET:
            field_dict["areasOfUse"] = areas_of_use
        if all_cr_ses is not UNSET:
            field_dict["allCRSes"] = all_cr_ses
        if late_bound_cr_ses is not UNSET:
            field_dict["lateBoundCRSes"] = late_bound_cr_ses
        if early_bound_cr_ses is not UNSET:
            field_dict["earlyBoundCRSes"] = early_bound_cr_ses
        if compound_cr_ses is not UNSET:
            field_dict["compoundCRSes"] = compound_cr_ses
        if all_c_ts is not UNSET:
            field_dict["allCTs"] = all_c_ts
        if single_c_ts is not UNSET:
            field_dict["singleCTs"] = single_c_ts
        if compound_c_ts is not UNSET:
            field_dict["compoundCTs"] = compound_c_ts
        if compound_c_ts_count is not UNSET:
            field_dict["compoundCTsCount"] = compound_c_ts_count
        if late_bound_cr_ses_count is not UNSET:
            field_dict["lateBoundCRSesCount"] = late_bound_cr_ses_count
        if early_bound_cr_ses_count is not UNSET:
            field_dict["earlyBoundCRSesCount"] = early_bound_cr_ses_count
        if compound_cr_ses_count is not UNSET:
            field_dict["compoundCRSesCount"] = compound_cr_ses_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.area_of_use import AreaOfUse
        from ..models.catalog_attributes import CatalogAttributes
        from ..models.compound_crs import CompoundCRS
        from ..models.compound_ct import CompoundCT
        from ..models.crs import CRS
        from ..models.ct import CT
        from ..models.early_bound_crs import EarlyBoundCRS
        from ..models.late_bound_crs import LateBoundCRS
        from ..models.single_ct import SingleCT

        d = dict(src_dict)
        _attributes = d.pop("attributes", UNSET)
        attributes: CatalogAttributes | Unset
        if isinstance(_attributes, Unset):
            attributes = UNSET
        else:
            attributes = CatalogAttributes.from_dict(_attributes)

        single_c_ts_count = d.pop("singleCTsCount", UNSET)

        area_of_use_count = d.pop("areaOfUseCount", UNSET)

        _catalog_response = d.pop("catalogResponse", UNSET)
        catalog_response: Catalog | Unset
        if isinstance(_catalog_response, Unset):
            catalog_response = UNSET
        else:
            catalog_response = Catalog.from_dict(_catalog_response)

        _areas_of_use = d.pop("areasOfUse", UNSET)
        areas_of_use: list[AreaOfUse] | Unset = UNSET
        if _areas_of_use is not UNSET:
            areas_of_use = []
            for areas_of_use_item_data in _areas_of_use:
                areas_of_use_item = AreaOfUse.from_dict(areas_of_use_item_data)

                areas_of_use.append(areas_of_use_item)

        _all_cr_ses = d.pop("allCRSes", UNSET)
        all_cr_ses: list[CRS] | Unset = UNSET
        if _all_cr_ses is not UNSET:
            all_cr_ses = []
            for all_cr_ses_item_data in _all_cr_ses:
                all_cr_ses_item = CRS.from_dict(all_cr_ses_item_data)

                all_cr_ses.append(all_cr_ses_item)

        _late_bound_cr_ses = d.pop("lateBoundCRSes", UNSET)
        late_bound_cr_ses: list[LateBoundCRS] | Unset = UNSET
        if _late_bound_cr_ses is not UNSET:
            late_bound_cr_ses = []
            for late_bound_cr_ses_item_data in _late_bound_cr_ses:
                late_bound_cr_ses_item = LateBoundCRS.from_dict(
                    late_bound_cr_ses_item_data
                )

                late_bound_cr_ses.append(late_bound_cr_ses_item)

        _early_bound_cr_ses = d.pop("earlyBoundCRSes", UNSET)
        early_bound_cr_ses: list[EarlyBoundCRS] | Unset = UNSET
        if _early_bound_cr_ses is not UNSET:
            early_bound_cr_ses = []
            for early_bound_cr_ses_item_data in _early_bound_cr_ses:
                early_bound_cr_ses_item = EarlyBoundCRS.from_dict(
                    early_bound_cr_ses_item_data
                )

                early_bound_cr_ses.append(early_bound_cr_ses_item)

        _compound_cr_ses = d.pop("compoundCRSes", UNSET)
        compound_cr_ses: list[CompoundCRS] | Unset = UNSET
        if _compound_cr_ses is not UNSET:
            compound_cr_ses = []
            for compound_cr_ses_item_data in _compound_cr_ses:
                compound_cr_ses_item = CompoundCRS.from_dict(compound_cr_ses_item_data)

                compound_cr_ses.append(compound_cr_ses_item)

        _all_c_ts = d.pop("allCTs", UNSET)
        all_c_ts: list[CT] | Unset = UNSET
        if _all_c_ts is not UNSET:
            all_c_ts = []
            for all_c_ts_item_data in _all_c_ts:
                all_c_ts_item = CT.from_dict(all_c_ts_item_data)

                all_c_ts.append(all_c_ts_item)

        _single_c_ts = d.pop("singleCTs", UNSET)
        single_c_ts: list[SingleCT] | Unset = UNSET
        if _single_c_ts is not UNSET:
            single_c_ts = []
            for single_c_ts_item_data in _single_c_ts:
                single_c_ts_item = SingleCT.from_dict(single_c_ts_item_data)

                single_c_ts.append(single_c_ts_item)

        _compound_c_ts = d.pop("compoundCTs", UNSET)
        compound_c_ts: list[CompoundCT] | Unset = UNSET
        if _compound_c_ts is not UNSET:
            compound_c_ts = []
            for compound_c_ts_item_data in _compound_c_ts:
                compound_c_ts_item = CompoundCT.from_dict(compound_c_ts_item_data)

                compound_c_ts.append(compound_c_ts_item)

        compound_c_ts_count = d.pop("compoundCTsCount", UNSET)

        late_bound_cr_ses_count = d.pop("lateBoundCRSesCount", UNSET)

        early_bound_cr_ses_count = d.pop("earlyBoundCRSesCount", UNSET)

        compound_cr_ses_count = d.pop("compoundCRSesCount", UNSET)

        catalog = cls(
            attributes=attributes,
            single_c_ts_count=single_c_ts_count,
            area_of_use_count=area_of_use_count,
            catalog_response=catalog_response,
            areas_of_use=areas_of_use,
            all_cr_ses=all_cr_ses,
            late_bound_cr_ses=late_bound_cr_ses,
            early_bound_cr_ses=early_bound_cr_ses,
            compound_cr_ses=compound_cr_ses,
            all_c_ts=all_c_ts,
            single_c_ts=single_c_ts,
            compound_c_ts=compound_c_ts,
            compound_c_ts_count=compound_c_ts_count,
            late_bound_cr_ses_count=late_bound_cr_ses_count,
            early_bound_cr_ses_count=early_bound_cr_ses_count,
            compound_cr_ses_count=compound_cr_ses_count,
        )

        catalog.additional_properties = d
        return catalog

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
