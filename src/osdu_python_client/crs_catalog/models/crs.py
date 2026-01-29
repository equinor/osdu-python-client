from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.area_of_use import AreaOfUse
    from ..models.authority_code import AuthorityCode
    from ..models.crs_deprecation_info import CRSDeprecationInfo
    from ..models.deprecation_info import DeprecationInfo
    from ..models.essence import Essence
    from ..models.named_reference import NamedReference


T = TypeVar("T", bound="CRS")


@_attrs_define
class CRS:
    """
    Attributes:
        transformation_ready (bool | Unset):
        crsdeprecation_info (CRSDeprecationInfo | Unset):
        base_crs_authority_code (AuthorityCode | Unset):
        number_of_axes (int | Unset):
        axis_units (list[str] | Unset):
        crstype (str | Unset):
        source (str | Unset):
        area_of_use (AreaOfUse | Unset):
        last_modified (str | Unset):
        named_reference (NamedReference | Unset): Name and Persistable Reference (the essence converted to a JSON
            string).
        alias_names (list[str] | Unset):
        essence (Essence | Unset):
        deprecation_info (DeprecationInfo | Unset):
        description (str | Unset):
    """

    transformation_ready: bool | Unset = UNSET
    crsdeprecation_info: CRSDeprecationInfo | Unset = UNSET
    base_crs_authority_code: AuthorityCode | Unset = UNSET
    number_of_axes: int | Unset = UNSET
    axis_units: list[str] | Unset = UNSET
    crstype: str | Unset = UNSET
    source: str | Unset = UNSET
    area_of_use: AreaOfUse | Unset = UNSET
    last_modified: str | Unset = UNSET
    named_reference: NamedReference | Unset = UNSET
    alias_names: list[str] | Unset = UNSET
    essence: Essence | Unset = UNSET
    deprecation_info: DeprecationInfo | Unset = UNSET
    description: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        transformation_ready = self.transformation_ready

        crsdeprecation_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.crsdeprecation_info, Unset):
            crsdeprecation_info = self.crsdeprecation_info.to_dict()

        base_crs_authority_code: dict[str, Any] | Unset = UNSET
        if not isinstance(self.base_crs_authority_code, Unset):
            base_crs_authority_code = self.base_crs_authority_code.to_dict()

        number_of_axes = self.number_of_axes

        axis_units: list[str] | Unset = UNSET
        if not isinstance(self.axis_units, Unset):
            axis_units = self.axis_units

        crstype = self.crstype

        source = self.source

        area_of_use: dict[str, Any] | Unset = UNSET
        if not isinstance(self.area_of_use, Unset):
            area_of_use = self.area_of_use.to_dict()

        last_modified = self.last_modified

        named_reference: dict[str, Any] | Unset = UNSET
        if not isinstance(self.named_reference, Unset):
            named_reference = self.named_reference.to_dict()

        alias_names: list[str] | Unset = UNSET
        if not isinstance(self.alias_names, Unset):
            alias_names = self.alias_names

        essence: dict[str, Any] | Unset = UNSET
        if not isinstance(self.essence, Unset):
            essence = self.essence.to_dict()

        deprecation_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.deprecation_info, Unset):
            deprecation_info = self.deprecation_info.to_dict()

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if transformation_ready is not UNSET:
            field_dict["transformationReady"] = transformation_ready
        if crsdeprecation_info is not UNSET:
            field_dict["crsdeprecationInfo"] = crsdeprecation_info
        if base_crs_authority_code is not UNSET:
            field_dict["baseCRSAuthorityCode"] = base_crs_authority_code
        if number_of_axes is not UNSET:
            field_dict["numberOfAxes"] = number_of_axes
        if axis_units is not UNSET:
            field_dict["axisUnits"] = axis_units
        if crstype is not UNSET:
            field_dict["crstype"] = crstype
        if source is not UNSET:
            field_dict["source"] = source
        if area_of_use is not UNSET:
            field_dict["areaOfUse"] = area_of_use
        if last_modified is not UNSET:
            field_dict["lastModified"] = last_modified
        if named_reference is not UNSET:
            field_dict["namedReference"] = named_reference
        if alias_names is not UNSET:
            field_dict["aliasNames"] = alias_names
        if essence is not UNSET:
            field_dict["essence"] = essence
        if deprecation_info is not UNSET:
            field_dict["deprecationInfo"] = deprecation_info
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.area_of_use import AreaOfUse
        from ..models.authority_code import AuthorityCode
        from ..models.crs_deprecation_info import CRSDeprecationInfo
        from ..models.deprecation_info import DeprecationInfo
        from ..models.essence import Essence
        from ..models.named_reference import NamedReference

        d = dict(src_dict)
        transformation_ready = d.pop("transformationReady", UNSET)

        _crsdeprecation_info = d.pop("crsdeprecationInfo", UNSET)
        crsdeprecation_info: CRSDeprecationInfo | Unset
        if isinstance(_crsdeprecation_info, Unset):
            crsdeprecation_info = UNSET
        else:
            crsdeprecation_info = CRSDeprecationInfo.from_dict(_crsdeprecation_info)

        _base_crs_authority_code = d.pop("baseCRSAuthorityCode", UNSET)
        base_crs_authority_code: AuthorityCode | Unset
        if isinstance(_base_crs_authority_code, Unset):
            base_crs_authority_code = UNSET
        else:
            base_crs_authority_code = AuthorityCode.from_dict(_base_crs_authority_code)

        number_of_axes = d.pop("numberOfAxes", UNSET)

        axis_units = cast(list[str], d.pop("axisUnits", UNSET))

        crstype = d.pop("crstype", UNSET)

        source = d.pop("source", UNSET)

        _area_of_use = d.pop("areaOfUse", UNSET)
        area_of_use: AreaOfUse | Unset
        if isinstance(_area_of_use, Unset):
            area_of_use = UNSET
        else:
            area_of_use = AreaOfUse.from_dict(_area_of_use)

        last_modified = d.pop("lastModified", UNSET)

        _named_reference = d.pop("namedReference", UNSET)
        named_reference: NamedReference | Unset
        if isinstance(_named_reference, Unset):
            named_reference = UNSET
        else:
            named_reference = NamedReference.from_dict(_named_reference)

        alias_names = cast(list[str], d.pop("aliasNames", UNSET))

        _essence = d.pop("essence", UNSET)
        essence: Essence | Unset
        if isinstance(_essence, Unset):
            essence = UNSET
        else:
            essence = Essence.from_dict(_essence)

        _deprecation_info = d.pop("deprecationInfo", UNSET)
        deprecation_info: DeprecationInfo | Unset
        if isinstance(_deprecation_info, Unset):
            deprecation_info = UNSET
        else:
            deprecation_info = DeprecationInfo.from_dict(_deprecation_info)

        description = d.pop("description", UNSET)

        crs = cls(
            transformation_ready=transformation_ready,
            crsdeprecation_info=crsdeprecation_info,
            base_crs_authority_code=base_crs_authority_code,
            number_of_axes=number_of_axes,
            axis_units=axis_units,
            crstype=crstype,
            source=source,
            area_of_use=area_of_use,
            last_modified=last_modified,
            named_reference=named_reference,
            alias_names=alias_names,
            essence=essence,
            deprecation_info=deprecation_info,
            description=description,
        )

        crs.additional_properties = d
        return crs

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
