from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.invalid_tag_with_reason import InvalidTagWithReason


T = TypeVar("T", bound="InvalidTagsWithReason")


@_attrs_define
class InvalidTagsWithReason:
    """Represents a collection of invalid LegalTags.

    Attributes:
        invalid_legal_tags (list[InvalidTagWithReason] | Unset): A collection of invalid LegalTags
    """

    invalid_legal_tags: list[InvalidTagWithReason] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        invalid_legal_tags: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.invalid_legal_tags, Unset):
            invalid_legal_tags = []
            for invalid_legal_tags_item_data in self.invalid_legal_tags:
                invalid_legal_tags_item = invalid_legal_tags_item_data.to_dict()
                invalid_legal_tags.append(invalid_legal_tags_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if invalid_legal_tags is not UNSET:
            field_dict["invalidLegalTags"] = invalid_legal_tags

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.invalid_tag_with_reason import InvalidTagWithReason

        d = dict(src_dict)
        _invalid_legal_tags = d.pop("invalidLegalTags", UNSET)
        invalid_legal_tags: list[InvalidTagWithReason] | Unset = UNSET
        if _invalid_legal_tags is not UNSET:
            invalid_legal_tags = []
            for invalid_legal_tags_item_data in _invalid_legal_tags:
                invalid_legal_tags_item = InvalidTagWithReason.from_dict(
                    invalid_legal_tags_item_data
                )

                invalid_legal_tags.append(invalid_legal_tags_item)

        invalid_tags_with_reason = cls(
            invalid_legal_tags=invalid_legal_tags,
        )

        invalid_tags_with_reason.additional_properties = d
        return invalid_tags_with_reason

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
