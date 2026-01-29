from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.filter_ import Filter


T = TypeVar("T", bound="CreateActionDto")


@_attrs_define
class CreateActionDto:
    """Represents a model to create Action

    Attributes:
        name (str):  Example: Petrel Project.
        id (str | Unset):  Example: petrel-launch-project.
        description (str | Unset):  Example: This action launches the Petrel projects landing page that holds the
            selected data..
        img (str | Unset):  Example: https://mycdn.com/img.png.
        url (str | Unset):  Example: https://myapp.osdu.com/action/{type}/{id}.
        contact_email (str | Unset):  Example: abc@test.com.
        filter_ (Filter | Unset): Represents a model for Filter
    """

    name: str
    id: str | Unset = UNSET
    description: str | Unset = UNSET
    img: str | Unset = UNSET
    url: str | Unset = UNSET
    contact_email: str | Unset = UNSET
    filter_: Filter | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        id = self.id

        description = self.description

        img = self.img

        url = self.url

        contact_email = self.contact_email

        filter_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.filter_, Unset):
            filter_ = self.filter_.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if description is not UNSET:
            field_dict["description"] = description
        if img is not UNSET:
            field_dict["img"] = img
        if url is not UNSET:
            field_dict["url"] = url
        if contact_email is not UNSET:
            field_dict["contactEmail"] = contact_email
        if filter_ is not UNSET:
            field_dict["filter"] = filter_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.filter_ import Filter

        d = dict(src_dict)
        name = d.pop("name")

        id = d.pop("id", UNSET)

        description = d.pop("description", UNSET)

        img = d.pop("img", UNSET)

        url = d.pop("url", UNSET)

        contact_email = d.pop("contactEmail", UNSET)

        _filter_ = d.pop("filter", UNSET)
        filter_: Filter | Unset
        if isinstance(_filter_, Unset):
            filter_ = UNSET
        else:
            filter_ = Filter.from_dict(_filter_)

        create_action_dto = cls(
            name=name,
            id=id,
            description=description,
            img=img,
            url=url,
            contact_email=contact_email,
            filter_=filter_,
        )

        create_action_dto.additional_properties = d
        return create_action_dto

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
