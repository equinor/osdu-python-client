from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.connected_outer_service import ConnectedOuterService


T = TypeVar("T", bound="VersionInfo")


@_attrs_define
class VersionInfo:
    """
    Attributes:
        group_id (str | Unset):
        artifact_id (str | Unset):
        version (str | Unset):
        build_time (str | Unset):
        branch (str | Unset):
        commit_id (str | Unset):
        commit_message (str | Unset):
        connected_outer_services (list[ConnectedOuterService] | Unset):
    """

    group_id: str | Unset = UNSET
    artifact_id: str | Unset = UNSET
    version: str | Unset = UNSET
    build_time: str | Unset = UNSET
    branch: str | Unset = UNSET
    commit_id: str | Unset = UNSET
    commit_message: str | Unset = UNSET
    connected_outer_services: list[ConnectedOuterService] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        group_id = self.group_id

        artifact_id = self.artifact_id

        version = self.version

        build_time = self.build_time

        branch = self.branch

        commit_id = self.commit_id

        commit_message = self.commit_message

        connected_outer_services: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.connected_outer_services, Unset):
            connected_outer_services = []
            for connected_outer_services_item_data in self.connected_outer_services:
                connected_outer_services_item = (
                    connected_outer_services_item_data.to_dict()
                )
                connected_outer_services.append(connected_outer_services_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if group_id is not UNSET:
            field_dict["groupId"] = group_id
        if artifact_id is not UNSET:
            field_dict["artifactId"] = artifact_id
        if version is not UNSET:
            field_dict["version"] = version
        if build_time is not UNSET:
            field_dict["buildTime"] = build_time
        if branch is not UNSET:
            field_dict["branch"] = branch
        if commit_id is not UNSET:
            field_dict["commitId"] = commit_id
        if commit_message is not UNSET:
            field_dict["commitMessage"] = commit_message
        if connected_outer_services is not UNSET:
            field_dict["connectedOuterServices"] = connected_outer_services

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.connected_outer_service import ConnectedOuterService

        d = dict(src_dict)
        group_id = d.pop("groupId", UNSET)

        artifact_id = d.pop("artifactId", UNSET)

        version = d.pop("version", UNSET)

        build_time = d.pop("buildTime", UNSET)

        branch = d.pop("branch", UNSET)

        commit_id = d.pop("commitId", UNSET)

        commit_message = d.pop("commitMessage", UNSET)

        _connected_outer_services = d.pop("connectedOuterServices", UNSET)
        connected_outer_services: list[ConnectedOuterService] | Unset = UNSET
        if _connected_outer_services is not UNSET:
            connected_outer_services = []
            for connected_outer_services_item_data in _connected_outer_services:
                connected_outer_services_item = ConnectedOuterService.from_dict(
                    connected_outer_services_item_data
                )

                connected_outer_services.append(connected_outer_services_item)

        version_info = cls(
            group_id=group_id,
            artifact_id=artifact_id,
            version=version,
            build_time=build_time,
            branch=branch,
            commit_id=commit_id,
            commit_message=commit_message,
            connected_outer_services=connected_outer_services,
        )

        version_info.additional_properties = d
        return version_info

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
