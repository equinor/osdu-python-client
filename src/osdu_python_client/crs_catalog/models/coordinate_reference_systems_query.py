from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.base_crs import BaseCRS
    from ..models.datum import Datum


T = TypeVar("T", bound="CoordinateReferenceSystemsQuery")


@_attrs_define
class CoordinateReferenceSystemsQuery:
    """Body for searching on CRSs

    Attributes:
        code_space (str | Unset): Corresponds to CodeSpace field on CRS records
        code (str | Unset): Corresponds to Code field on CRS records
        name (str | Unset): Corresponds to Code field on CRS records
        id (str | Unset): Corresponds to ID field on CRS records
        kind (str | Unset): Corresponds to Kind field on CRS records
        coordinate_reference_system_type (str | Unset): Type of CRS, e.g., BoundCRS, ProjectedCRS, GeodeticCRS,
            VerticalCRS
        return_bound_projected_and_projected_based_on_wgs_84 (bool | Unset): Whether or not to only return bound
            projected type or projected type based on wgs84. If true, it only returns CRS 1. with Kind as "BoundProjected"
            or 2. with Kind as "projected" and BaseCRS.AuthorityCode.Code as 4326
        return_bound_geographic_2d_and_wgs_84 (bool | Unset): Whether or not to only return bound geopraphic 2d type. If
            true, it only returns CRS 1. with Kind as "BoundGeographic2D" or 2. with Kind as "geographic 2D" and Code as
            4326 and CodeSpace as "EPSG"
        base_crs (BaseCRS | Unset): BaseCRS
        datum (Datum | Unset): Datum
        extent (str | Unset): Description of extent. Corresponds to PreferredUsage.Extent.Description in the record. All
            entities with PreferredUsage.Extent.Description containing the search string will be returned. Wildcard is not
            supported.
        persistable_reference_search (str | Unset):
        horizontal_axis_unit_id (str | Unset): Corresponds to CoordinateSystem.HorizontalAxisUnitID field on CRS
            records, e.g., "osdu:reference-data--UnitOfMeasure:dega:".
        vertical_axis_unit_id (str | Unset): CorrespondsCorresponds to CoordinateSystem.VerticalAxisUnitID field on CRS
            records
        latitude (float | Unset): Latitude point for searching on CRS bounding box
        longitude (float | Unset): Longitude point for searching on CRS bounding box
        include_deprecated (bool | Unset): Whether to return deprecated records marked with InactiveIndicator=true.
            Default is false
        offset (int | Unset): Corresponds to offset on search service
        limit (int | Unset): Corresponds to limit on search service. Default is to return all found entities.
        return_all_fields (bool | Unset): Whether to return all fields in the record. Default is false and only a subset
            is returned
        returned_fields (list[str] | Unset): Return all fields in the record
    """

    code_space: str | Unset = UNSET
    code: str | Unset = UNSET
    name: str | Unset = UNSET
    id: str | Unset = UNSET
    kind: str | Unset = UNSET
    coordinate_reference_system_type: str | Unset = UNSET
    return_bound_projected_and_projected_based_on_wgs_84: bool | Unset = UNSET
    return_bound_geographic_2d_and_wgs_84: bool | Unset = UNSET
    base_crs: BaseCRS | Unset = UNSET
    datum: Datum | Unset = UNSET
    extent: str | Unset = UNSET
    persistable_reference_search: str | Unset = UNSET
    horizontal_axis_unit_id: str | Unset = UNSET
    vertical_axis_unit_id: str | Unset = UNSET
    latitude: float | Unset = UNSET
    longitude: float | Unset = UNSET
    include_deprecated: bool | Unset = UNSET
    offset: int | Unset = UNSET
    limit: int | Unset = UNSET
    return_all_fields: bool | Unset = UNSET
    returned_fields: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code_space = self.code_space

        code = self.code

        name = self.name

        id = self.id

        kind = self.kind

        coordinate_reference_system_type = self.coordinate_reference_system_type

        return_bound_projected_and_projected_based_on_wgs_84 = (
            self.return_bound_projected_and_projected_based_on_wgs_84
        )

        return_bound_geographic_2d_and_wgs_84 = (
            self.return_bound_geographic_2d_and_wgs_84
        )

        base_crs: dict[str, Any] | Unset = UNSET
        if not isinstance(self.base_crs, Unset):
            base_crs = self.base_crs.to_dict()

        datum: dict[str, Any] | Unset = UNSET
        if not isinstance(self.datum, Unset):
            datum = self.datum.to_dict()

        extent = self.extent

        persistable_reference_search = self.persistable_reference_search

        horizontal_axis_unit_id = self.horizontal_axis_unit_id

        vertical_axis_unit_id = self.vertical_axis_unit_id

        latitude = self.latitude

        longitude = self.longitude

        include_deprecated = self.include_deprecated

        offset = self.offset

        limit = self.limit

        return_all_fields = self.return_all_fields

        returned_fields: list[str] | Unset = UNSET
        if not isinstance(self.returned_fields, Unset):
            returned_fields = self.returned_fields

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if code_space is not UNSET:
            field_dict["codeSpace"] = code_space
        if code is not UNSET:
            field_dict["code"] = code
        if name is not UNSET:
            field_dict["name"] = name
        if id is not UNSET:
            field_dict["id"] = id
        if kind is not UNSET:
            field_dict["kind"] = kind
        if coordinate_reference_system_type is not UNSET:
            field_dict["coordinateReferenceSystemType"] = (
                coordinate_reference_system_type
            )
        if return_bound_projected_and_projected_based_on_wgs_84 is not UNSET:
            field_dict["returnBoundProjectedAndProjectedBasedOnWgs84"] = (
                return_bound_projected_and_projected_based_on_wgs_84
            )
        if return_bound_geographic_2d_and_wgs_84 is not UNSET:
            field_dict["returnBoundGeographic2DAndWgs84"] = (
                return_bound_geographic_2d_and_wgs_84
            )
        if base_crs is not UNSET:
            field_dict["baseCRS"] = base_crs
        if datum is not UNSET:
            field_dict["datum"] = datum
        if extent is not UNSET:
            field_dict["extent"] = extent
        if persistable_reference_search is not UNSET:
            field_dict["persistableReferenceSearch"] = persistable_reference_search
        if horizontal_axis_unit_id is not UNSET:
            field_dict["horizontalAxisUnitId"] = horizontal_axis_unit_id
        if vertical_axis_unit_id is not UNSET:
            field_dict["verticalAxisUnitId"] = vertical_axis_unit_id
        if latitude is not UNSET:
            field_dict["latitude"] = latitude
        if longitude is not UNSET:
            field_dict["longitude"] = longitude
        if include_deprecated is not UNSET:
            field_dict["includeDeprecated"] = include_deprecated
        if offset is not UNSET:
            field_dict["offset"] = offset
        if limit is not UNSET:
            field_dict["limit"] = limit
        if return_all_fields is not UNSET:
            field_dict["returnAllFields"] = return_all_fields
        if returned_fields is not UNSET:
            field_dict["returnedFields"] = returned_fields

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.base_crs import BaseCRS
        from ..models.datum import Datum

        d = dict(src_dict)
        code_space = d.pop("codeSpace", UNSET)

        code = d.pop("code", UNSET)

        name = d.pop("name", UNSET)

        id = d.pop("id", UNSET)

        kind = d.pop("kind", UNSET)

        coordinate_reference_system_type = d.pop("coordinateReferenceSystemType", UNSET)

        return_bound_projected_and_projected_based_on_wgs_84 = d.pop(
            "returnBoundProjectedAndProjectedBasedOnWgs84", UNSET
        )

        return_bound_geographic_2d_and_wgs_84 = d.pop(
            "returnBoundGeographic2DAndWgs84", UNSET
        )

        _base_crs = d.pop("baseCRS", UNSET)
        base_crs: BaseCRS | Unset
        if isinstance(_base_crs, Unset):
            base_crs = UNSET
        else:
            base_crs = BaseCRS.from_dict(_base_crs)

        _datum = d.pop("datum", UNSET)
        datum: Datum | Unset
        if isinstance(_datum, Unset):
            datum = UNSET
        else:
            datum = Datum.from_dict(_datum)

        extent = d.pop("extent", UNSET)

        persistable_reference_search = d.pop("persistableReferenceSearch", UNSET)

        horizontal_axis_unit_id = d.pop("horizontalAxisUnitId", UNSET)

        vertical_axis_unit_id = d.pop("verticalAxisUnitId", UNSET)

        latitude = d.pop("latitude", UNSET)

        longitude = d.pop("longitude", UNSET)

        include_deprecated = d.pop("includeDeprecated", UNSET)

        offset = d.pop("offset", UNSET)

        limit = d.pop("limit", UNSET)

        return_all_fields = d.pop("returnAllFields", UNSET)

        returned_fields = cast(list[str], d.pop("returnedFields", UNSET))

        coordinate_reference_systems_query = cls(
            code_space=code_space,
            code=code,
            name=name,
            id=id,
            kind=kind,
            coordinate_reference_system_type=coordinate_reference_system_type,
            return_bound_projected_and_projected_based_on_wgs_84=return_bound_projected_and_projected_based_on_wgs_84,
            return_bound_geographic_2d_and_wgs_84=return_bound_geographic_2d_and_wgs_84,
            base_crs=base_crs,
            datum=datum,
            extent=extent,
            persistable_reference_search=persistable_reference_search,
            horizontal_axis_unit_id=horizontal_axis_unit_id,
            vertical_axis_unit_id=vertical_axis_unit_id,
            latitude=latitude,
            longitude=longitude,
            include_deprecated=include_deprecated,
            offset=offset,
            limit=limit,
            return_all_fields=return_all_fields,
            returned_fields=returned_fields,
        )

        coordinate_reference_systems_query.additional_properties = d
        return coordinate_reference_systems_query

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
