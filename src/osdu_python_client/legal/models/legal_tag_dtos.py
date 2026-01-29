from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.legal_tag_dto import LegalTagDto


T = TypeVar("T", bound="LegalTagDtos")


@_attrs_define
class LegalTagDtos:
    """Represents a collection of LegalTags.

    Attributes:
        legal_tags (list[LegalTagDto] | Unset): A collection of complete LegalTags
    """

    legal_tags: list[LegalTagDto] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        legal_tags: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.legal_tags, Unset):
            legal_tags = []
            for legal_tags_item_data in self.legal_tags:
                legal_tags_item = legal_tags_item_data.to_dict()
                legal_tags.append(legal_tags_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if legal_tags is not UNSET:
            field_dict["legalTags"] = legal_tags

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.legal_tag_dto import LegalTagDto

        d = dict(src_dict)
        _legal_tags = d.pop("legalTags", UNSET)
        legal_tags: list[LegalTagDto] | Unset = UNSET
        if _legal_tags is not UNSET:
            legal_tags = []
            for legal_tags_item_data in _legal_tags:
                legal_tags_item = LegalTagDto.from_dict(legal_tags_item_data)

                legal_tags.append(legal_tags_item)

        legal_tag_dtos = cls(
            legal_tags=legal_tags,
        )

        legal_tag_dtos.additional_properties = d
        return legal_tag_dtos

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
