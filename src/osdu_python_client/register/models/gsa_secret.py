from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.gsa_secret_value import GsaSecretValue


T = TypeVar("T", bound="GsaSecret")


@_attrs_define
class GsaSecret:
    """Represents a model for 'GSA' Secret type

    Attributes:
        secret_type (str):
        value (GsaSecretValue | Unset):
    """

    secret_type: str
    value: GsaSecretValue | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        secret_type = self.secret_type

        value: dict[str, Any] | Unset = UNSET
        if not isinstance(self.value, Unset):
            value = self.value.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "secretType": secret_type,
            }
        )
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.gsa_secret_value import GsaSecretValue

        d = dict(src_dict)
        secret_type = d.pop("secretType")

        _value = d.pop("value", UNSET)
        value: GsaSecretValue | Unset
        if isinstance(_value, Unset):
            value = UNSET
        else:
            value = GsaSecretValue.from_dict(_value)

        gsa_secret = cls(
            secret_type=secret_type,
            value=value,
        )

        gsa_secret.additional_properties = d
        return gsa_secret

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
