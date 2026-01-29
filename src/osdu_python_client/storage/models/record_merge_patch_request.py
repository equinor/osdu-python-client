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
    from ..models.record_merge_patch_request_data import RecordMergePatchRequestData
    from ..models.record_merge_patch_request_tags import RecordMergePatchRequestTags


T = TypeVar("T", bound="RecordMergePatchRequest")


@_attrs_define
class RecordMergePatchRequest:
    """Data to be patched

    Example:
        {'acl': {'viewers': ['data.viewer@tenant.com'], 'owners': ['data.owner@tenant.com']}, 'legal': {'legaltags':
            ['tenant-public-usa-dataset-1'], 'otherRelevantDataCountries': ['US']}, 'data': {'wellName': 'Updated Well
            Name', 'status': 'active'}, 'tags': {'environment': 'production'}}

    Attributes:
        kind (str | Unset): Record kind
        acl (Acl | Unset):
        legal (Legal | Unset):
        data (RecordMergePatchRequestData | Unset): Record data
        tags (RecordMergePatchRequestTags | Unset): Record tags as key-value pairs
        ancestry (RecordAncestry | Unset):
        deleted (bool | Unset): Soft delete flag - set to false to undelete
        deleted_at (str | Unset): Deletion timestamp - set to null to undelete
    """

    kind: str | Unset = UNSET
    acl: Acl | Unset = UNSET
    legal: Legal | Unset = UNSET
    data: RecordMergePatchRequestData | Unset = UNSET
    tags: RecordMergePatchRequestTags | Unset = UNSET
    ancestry: RecordAncestry | Unset = UNSET
    deleted: bool | Unset = UNSET
    deleted_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        kind = self.kind

        acl: dict[str, Any] | Unset = UNSET
        if not isinstance(self.acl, Unset):
            acl = self.acl.to_dict()

        legal: dict[str, Any] | Unset = UNSET
        if not isinstance(self.legal, Unset):
            legal = self.legal.to_dict()

        data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        tags: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags.to_dict()

        ancestry: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ancestry, Unset):
            ancestry = self.ancestry.to_dict()

        deleted = self.deleted

        deleted_at = self.deleted_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if kind is not UNSET:
            field_dict["kind"] = kind
        if acl is not UNSET:
            field_dict["acl"] = acl
        if legal is not UNSET:
            field_dict["legal"] = legal
        if data is not UNSET:
            field_dict["data"] = data
        if tags is not UNSET:
            field_dict["tags"] = tags
        if ancestry is not UNSET:
            field_dict["ancestry"] = ancestry
        if deleted is not UNSET:
            field_dict["deleted"] = deleted
        if deleted_at is not UNSET:
            field_dict["deletedAt"] = deleted_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.acl import Acl
        from ..models.legal import Legal
        from ..models.record_ancestry import RecordAncestry
        from ..models.record_merge_patch_request_data import RecordMergePatchRequestData
        from ..models.record_merge_patch_request_tags import RecordMergePatchRequestTags

        d = dict(src_dict)
        kind = d.pop("kind", UNSET)

        _acl = d.pop("acl", UNSET)
        acl: Acl | Unset
        if isinstance(_acl, Unset):
            acl = UNSET
        else:
            acl = Acl.from_dict(_acl)

        _legal = d.pop("legal", UNSET)
        legal: Legal | Unset
        if isinstance(_legal, Unset):
            legal = UNSET
        else:
            legal = Legal.from_dict(_legal)

        _data = d.pop("data", UNSET)
        data: RecordMergePatchRequestData | Unset
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = RecordMergePatchRequestData.from_dict(_data)

        _tags = d.pop("tags", UNSET)
        tags: RecordMergePatchRequestTags | Unset
        if isinstance(_tags, Unset):
            tags = UNSET
        else:
            tags = RecordMergePatchRequestTags.from_dict(_tags)

        _ancestry = d.pop("ancestry", UNSET)
        ancestry: RecordAncestry | Unset
        if isinstance(_ancestry, Unset):
            ancestry = UNSET
        else:
            ancestry = RecordAncestry.from_dict(_ancestry)

        deleted = d.pop("deleted", UNSET)

        deleted_at = d.pop("deletedAt", UNSET)

        record_merge_patch_request = cls(
            kind=kind,
            acl=acl,
            legal=legal,
            data=data,
            tags=tags,
            ancestry=ancestry,
            deleted=deleted,
            deleted_at=deleted_at,
        )

        record_merge_patch_request.additional_properties = d
        return record_merge_patch_request

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
