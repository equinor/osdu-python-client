from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.services import Services


T = TypeVar("T", bound="InfoOut")


@_attrs_define
class InfoOut:
    """
    Attributes:
        version (str):
        connected_outer_services (Services):
        artifact_id (None | str | Unset):
        name (None | str | Unset):  Default: 'policy'.
        group_id (None | str | Unset):
        build_time (None | str | Unset):
        branch (None | str | Unset):
        commit_id (None | str | Unset):
        commit_message (None | str | Unset):
    """

    version: str
    connected_outer_services: Services
    artifact_id: None | str | Unset = UNSET
    name: None | str | Unset = "policy"
    group_id: None | str | Unset = UNSET
    build_time: None | str | Unset = UNSET
    branch: None | str | Unset = UNSET
    commit_id: None | str | Unset = UNSET
    commit_message: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        version = self.version

        connected_outer_services = self.connected_outer_services.to_dict()

        artifact_id: None | str | Unset
        if isinstance(self.artifact_id, Unset):
            artifact_id = UNSET
        else:
            artifact_id = self.artifact_id

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        group_id: None | str | Unset
        if isinstance(self.group_id, Unset):
            group_id = UNSET
        else:
            group_id = self.group_id

        build_time: None | str | Unset
        if isinstance(self.build_time, Unset):
            build_time = UNSET
        else:
            build_time = self.build_time

        branch: None | str | Unset
        if isinstance(self.branch, Unset):
            branch = UNSET
        else:
            branch = self.branch

        commit_id: None | str | Unset
        if isinstance(self.commit_id, Unset):
            commit_id = UNSET
        else:
            commit_id = self.commit_id

        commit_message: None | str | Unset
        if isinstance(self.commit_message, Unset):
            commit_message = UNSET
        else:
            commit_message = self.commit_message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "version": version,
                "connectedOuterServices": connected_outer_services,
            }
        )
        if artifact_id is not UNSET:
            field_dict["artifactId"] = artifact_id
        if name is not UNSET:
            field_dict["name"] = name
        if group_id is not UNSET:
            field_dict["groupId"] = group_id
        if build_time is not UNSET:
            field_dict["buildTime"] = build_time
        if branch is not UNSET:
            field_dict["branch"] = branch
        if commit_id is not UNSET:
            field_dict["commitId"] = commit_id
        if commit_message is not UNSET:
            field_dict["commitMessage"] = commit_message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.services import Services

        d = dict(src_dict)
        version = d.pop("version")

        connected_outer_services = Services.from_dict(d.pop("connectedOuterServices"))

        def _parse_artifact_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        artifact_id = _parse_artifact_id(d.pop("artifactId", UNSET))

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_group_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        group_id = _parse_group_id(d.pop("groupId", UNSET))

        def _parse_build_time(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        build_time = _parse_build_time(d.pop("buildTime", UNSET))

        def _parse_branch(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        branch = _parse_branch(d.pop("branch", UNSET))

        def _parse_commit_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        commit_id = _parse_commit_id(d.pop("commitId", UNSET))

        def _parse_commit_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        commit_message = _parse_commit_message(d.pop("commitMessage", UNSET))

        info_out = cls(
            version=version,
            connected_outer_services=connected_outer_services,
            artifact_id=artifact_id,
            name=name,
            group_id=group_id,
            build_time=build_time,
            branch=branch,
            commit_id=commit_id,
            commit_message=commit_message,
        )

        info_out.additional_properties = d
        return info_out

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
