from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.property_ import Property


T = TypeVar("T", bound="Map")


@_attrs_define
class Map:
    """
    Attributes:
        field_ (Property | Unset):
    """

    field_: Property | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_, Unset):
            field_ = self.field_.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_ is not UNSET:
            field_dict["< * >"] = field_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.property_ import Property

        d = dict(src_dict)
        _field_ = d.pop("< * >", UNSET)
        field_: Property | Unset
        if isinstance(_field_, Unset):
            field_ = UNSET
        else:
            field_ = Property.from_dict(_field_)

        map_ = cls(
            field_=field_,
        )

        map_.additional_properties = d
        return map_

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
