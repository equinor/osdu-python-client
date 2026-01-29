from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.input_ import Input


T = TypeVar("T", bound="TranslateItem")


@_attrs_define
class TranslateItem:
    """
    Attributes:
        query (str):
        input_ (Input):
        unknowns (list[str]):
    """

    query: str
    input_: Input
    unknowns: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        query = self.query

        input_ = self.input_.to_dict()

        unknowns = self.unknowns

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "query": query,
                "input": input_,
                "unknowns": unknowns,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.input_ import Input

        d = dict(src_dict)
        query = d.pop("query")

        input_ = Input.from_dict(d.pop("input"))

        unknowns = cast(list[str], d.pop("unknowns"))

        translate_item = cls(
            query=query,
            input_=input_,
            unknowns=unknowns,
        )

        translate_item.additional_properties = d
        return translate_item

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
