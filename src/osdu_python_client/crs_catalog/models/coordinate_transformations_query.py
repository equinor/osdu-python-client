from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CoordinateTransformationsQuery")


@_attrs_define
class CoordinateTransformationsQuery:
    """Body for searching on CTs

    Attributes:
        code_space (str | Unset): Corresponds to CodeSpace field on CT records
        name (str | Unset): Corresponds to Name field on CT records. All entities with name containing the search string
            will be returned. Wildcard is not supported
        id (str | Unset): Corresponds to ID field on CT records
        code (str | Unset): Corresponds to Code field on CT records
        kind (str | Unset): Corresponds to the Kind field on CT records. Default is to not return CT records with Kind
            "VerticalTransformation". Viable options include "Transformation", "ConcatenatedOperation",
            "VerticalTransformation", "ExcludeVertical" (default) and "All". "All" is a special value which indicates
            returning records of all kinds.
        source_crs (str | Unset): Corresponds to SourceCRS.SourceCRSID (record id), e.g., "osdu:reference-data--
            CoordinateReferenceSystem:Geographic2D:EPSG::4198:". As SourceCRS and TargetCRS are interchangeable, it will
            also search TargetCRS.TargetCRSID
        target_crs (str | Unset): Corresponds to TargetCRS.TargetCRSID (record id), e.g., "osdu:reference-data--
            CoordinateReferenceSystem:Geographic2D:EPSG::4198:". As SourceCRS and TargetCRS are interchangeable, it will
            also search SourceCRS.SourceCRSID
        latitude (float | Unset): Returns all entities for which the (Latitude, Longitude) is inside the Extent bounding
            box. Must also provide longitude
        longitude (float | Unset): See latitude
        include_deprecated (bool | Unset): Whether to return deprecated records marked with InactiveIndicator=true.
            Default is false.
        offset (int | Unset): Corresponds to offset on search service
        limit (int | Unset): Corresponds to limit on search service. Default is to return all found entities.
        return_all_fields (bool | Unset): Whether to return all fields in the record. Default is false and only a subset
            is returned
        returned_fields (list[str] | Unset):
    """

    code_space: str | Unset = UNSET
    name: str | Unset = UNSET
    id: str | Unset = UNSET
    code: str | Unset = UNSET
    kind: str | Unset = UNSET
    source_crs: str | Unset = UNSET
    target_crs: str | Unset = UNSET
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

        name = self.name

        id = self.id

        code = self.code

        kind = self.kind

        source_crs = self.source_crs

        target_crs = self.target_crs

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
        if name is not UNSET:
            field_dict["name"] = name
        if id is not UNSET:
            field_dict["id"] = id
        if code is not UNSET:
            field_dict["code"] = code
        if kind is not UNSET:
            field_dict["kind"] = kind
        if source_crs is not UNSET:
            field_dict["sourceCRS"] = source_crs
        if target_crs is not UNSET:
            field_dict["targetCRS"] = target_crs
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
        d = dict(src_dict)
        code_space = d.pop("codeSpace", UNSET)

        name = d.pop("name", UNSET)

        id = d.pop("id", UNSET)

        code = d.pop("code", UNSET)

        kind = d.pop("kind", UNSET)

        source_crs = d.pop("sourceCRS", UNSET)

        target_crs = d.pop("targetCRS", UNSET)

        latitude = d.pop("latitude", UNSET)

        longitude = d.pop("longitude", UNSET)

        include_deprecated = d.pop("includeDeprecated", UNSET)

        offset = d.pop("offset", UNSET)

        limit = d.pop("limit", UNSET)

        return_all_fields = d.pop("returnAllFields", UNSET)

        returned_fields = cast(list[str], d.pop("returnedFields", UNSET))

        coordinate_transformations_query = cls(
            code_space=code_space,
            name=name,
            id=id,
            code=code,
            kind=kind,
            source_crs=source_crs,
            target_crs=target_crs,
            latitude=latitude,
            longitude=longitude,
            include_deprecated=include_deprecated,
            offset=offset,
            limit=limit,
            return_all_fields=return_all_fields,
            returned_fields=returned_fields,
        )

        coordinate_transformations_query.additional_properties = d
        return coordinate_transformations_query

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
