from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.acl import Acl
    from ..models.legal import Legal
    from ..models.record_ancestry import RecordAncestry
    from ..models.record_data import RecordData
    from ..models.record_meta_item import RecordMetaItem
    from ..models.record_tags import RecordTags


T = TypeVar("T", bound="Record")


@_attrs_define
class Record:
    """
    Attributes:
        acl (Acl):
        id (str | Unset):
        version (int | Unset):
        kind (str | Unset):
        legal (Legal | Unset):
        data (RecordData | Unset):
        ancestry (RecordAncestry | Unset):
        meta (list[RecordMetaItem] | Unset):
        tags (RecordTags | Unset):
        create_user (str | Unset):
        create_time (str | Unset):
        modify_user (str | Unset):
        modify_time (str | Unset):
    """

    acl: Acl
    id: str | Unset = UNSET
    version: int | Unset = UNSET
    kind: str | Unset = UNSET
    legal: Legal | Unset = UNSET
    data: RecordData | Unset = UNSET
    ancestry: RecordAncestry | Unset = UNSET
    meta: list[RecordMetaItem] | Unset = UNSET
    tags: RecordTags | Unset = UNSET
    create_user: str | Unset = UNSET
    create_time: str | Unset = UNSET
    modify_user: str | Unset = UNSET
    modify_time: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        acl = self.acl.to_dict()

        id = self.id

        version = self.version

        kind = self.kind

        legal: dict[str, Any] | Unset = UNSET
        if not isinstance(self.legal, Unset):
            legal = self.legal.to_dict()

        data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        ancestry: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ancestry, Unset):
            ancestry = self.ancestry.to_dict()

        meta: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.meta, Unset):
            meta = []
            for meta_item_data in self.meta:
                meta_item = meta_item_data.to_dict()
                meta.append(meta_item)

        tags: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags.to_dict()

        create_user = self.create_user

        create_time = self.create_time

        modify_user = self.modify_user

        modify_time = self.modify_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "acl": acl,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if version is not UNSET:
            field_dict["version"] = version
        if kind is not UNSET:
            field_dict["kind"] = kind
        if legal is not UNSET:
            field_dict["legal"] = legal
        if data is not UNSET:
            field_dict["data"] = data
        if ancestry is not UNSET:
            field_dict["ancestry"] = ancestry
        if meta is not UNSET:
            field_dict["meta"] = meta
        if tags is not UNSET:
            field_dict["tags"] = tags
        if create_user is not UNSET:
            field_dict["createUser"] = create_user
        if create_time is not UNSET:
            field_dict["createTime"] = create_time
        if modify_user is not UNSET:
            field_dict["modifyUser"] = modify_user
        if modify_time is not UNSET:
            field_dict["modifyTime"] = modify_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.acl import Acl
        from ..models.legal import Legal
        from ..models.record_ancestry import RecordAncestry
        from ..models.record_data import RecordData
        from ..models.record_meta_item import RecordMetaItem
        from ..models.record_tags import RecordTags

        d = dict(src_dict)
        acl = Acl.from_dict(d.pop("acl"))

        id = d.pop("id", UNSET)

        version = d.pop("version", UNSET)

        kind = d.pop("kind", UNSET)

        _legal = d.pop("legal", UNSET)
        legal: Legal | Unset
        if isinstance(_legal, Unset):
            legal = UNSET
        else:
            legal = Legal.from_dict(_legal)

        _data = d.pop("data", UNSET)
        data: RecordData | Unset
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = RecordData.from_dict(_data)

        _ancestry = d.pop("ancestry", UNSET)
        ancestry: RecordAncestry | Unset
        if isinstance(_ancestry, Unset):
            ancestry = UNSET
        else:
            ancestry = RecordAncestry.from_dict(_ancestry)

        _meta = d.pop("meta", UNSET)
        meta: list[RecordMetaItem] | Unset = UNSET
        if _meta is not UNSET:
            meta = []
            for meta_item_data in _meta:
                meta_item = RecordMetaItem.from_dict(meta_item_data)

                meta.append(meta_item)

        _tags = d.pop("tags", UNSET)
        tags: RecordTags | Unset
        if isinstance(_tags, Unset):
            tags = UNSET
        else:
            tags = RecordTags.from_dict(_tags)

        create_user = d.pop("createUser", UNSET)

        create_time = d.pop("createTime", UNSET)

        modify_user = d.pop("modifyUser", UNSET)

        modify_time = d.pop("modifyTime", UNSET)

        record = cls(
            acl=acl,
            id=id,
            version=version,
            kind=kind,
            legal=legal,
            data=data,
            ancestry=ancestry,
            meta=meta,
            tags=tags,
            create_user=create_user,
            create_time=create_time,
            modify_user=modify_user,
            modify_time=modify_time,
        )

        record.additional_properties = d
        return record

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
