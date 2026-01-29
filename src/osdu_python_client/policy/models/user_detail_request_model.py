from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user_details_model import UserDetailsModel


T = TypeVar("T", bound="UserDetailRequestModel")


@_attrs_define
class UserDetailRequestModel:
    """
    Attributes:
        user_detail (UserDetailsModel):
        ttl (int | None | Unset):
    """

    user_detail: UserDetailsModel
    ttl: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        user_detail = self.user_detail.to_dict()

        ttl: int | None | Unset
        if isinstance(self.ttl, Unset):
            ttl = UNSET
        else:
            ttl = self.ttl

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "user_detail": user_detail,
            }
        )
        if ttl is not UNSET:
            field_dict["ttl"] = ttl

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user_details_model import UserDetailsModel

        d = dict(src_dict)
        user_detail = UserDetailsModel.from_dict(d.pop("user_detail"))

        def _parse_ttl(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        ttl = _parse_ttl(d.pop("ttl", UNSET))

        user_detail_request_model = cls(
            user_detail=user_detail,
            ttl=ttl,
        )

        user_detail_request_model.additional_properties = d
        return user_detail_request_model

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
