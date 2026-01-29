from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.property_value import PropertyValue


T = TypeVar("T", bound="Property")


@_attrs_define
class Property:
    """
    Attributes:
        sensitive (bool | Unset):
        value (PropertyValue | Unset):
    """

    sensitive: bool | Unset = UNSET
    value: PropertyValue | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sensitive = self.sensitive

        value: dict[str, Any] | Unset = UNSET
        if not isinstance(self.value, Unset):
            value = self.value.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sensitive is not UNSET:
            field_dict["sensitive"] = sensitive
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.property_value import PropertyValue

        d = dict(src_dict)
        sensitive = d.pop("sensitive", UNSET)

        _value = d.pop("value", UNSET)
        value: PropertyValue | Unset
        if isinstance(_value, Unset):
            value = UNSET
        else:
            value = PropertyValue.from_dict(_value)

        property_ = cls(
            sensitive=sensitive,
            value=value,
        )

        property_.additional_properties = d
        return property_

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
