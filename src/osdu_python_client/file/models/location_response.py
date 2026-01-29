from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.location_response_location import LocationResponseLocation


T = TypeVar("T", bound="LocationResponse")


@_attrs_define
class LocationResponse:
    """
    Attributes:
        file_id (str | Unset):
        location (LocationResponseLocation | Unset):
    """

    file_id: str | Unset = UNSET
    location: LocationResponseLocation | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        file_id = self.file_id

        location: dict[str, Any] | Unset = UNSET
        if not isinstance(self.location, Unset):
            location = self.location.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if file_id is not UNSET:
            field_dict["FileID"] = file_id
        if location is not UNSET:
            field_dict["Location"] = location

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.location_response_location import LocationResponseLocation

        d = dict(src_dict)
        file_id = d.pop("FileID", UNSET)

        _location = d.pop("Location", UNSET)
        location: LocationResponseLocation | Unset
        if isinstance(_location, Unset):
            location = UNSET
        else:
            location = LocationResponseLocation.from_dict(_location)

        location_response = cls(
            file_id=file_id,
            location=location,
        )

        location_response.additional_properties = d
        return location_response

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
