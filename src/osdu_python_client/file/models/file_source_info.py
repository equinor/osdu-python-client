from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FileSourceInfo")


@_attrs_define
class FileSourceInfo:
    """File Source Info

    Attributes:
        file_source (str): Relative file path for the data in the file
        preload_file_path (str | Unset): File system path to the data file as it existed before loading to the data
            platform
        preload_file_create_user (str | Unset): Optional user name or reference, who created the file prior to up-
            loading to the platform.
        preload_file_create_date (str | Unset): Optional create date and time of the file prior to uploading to the
            platform.
        preload_file_modify_user (str | Unset): Optional user name or reference, who last modified the file prior to up-
            loading to the platform.
        preload_file_modify_date (str | Unset): Optional last modified date and time of the file prior to up-loading to
            the platform.
        name (str | Unset): user-friendly file name.
        file_size (str | Unset): Length of file in bytes. Implemented as string. The value must be convertible to a long
            integer (sizes can become very large).
        encoding_format_type_id (str | Unset): Encoding Format Type ID
        checksum (str | Unset): MD5 checksum of file bytes - a 32 byte hexadecimal number
        checksum_algorithm (str | Unset): The name of the checksum algorithm e.g. MD5, SHA-256.
    """

    file_source: str
    preload_file_path: str | Unset = UNSET
    preload_file_create_user: str | Unset = UNSET
    preload_file_create_date: str | Unset = UNSET
    preload_file_modify_user: str | Unset = UNSET
    preload_file_modify_date: str | Unset = UNSET
    name: str | Unset = UNSET
    file_size: str | Unset = UNSET
    encoding_format_type_id: str | Unset = UNSET
    checksum: str | Unset = UNSET
    checksum_algorithm: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        file_source = self.file_source

        preload_file_path = self.preload_file_path

        preload_file_create_user = self.preload_file_create_user

        preload_file_create_date = self.preload_file_create_date

        preload_file_modify_user = self.preload_file_modify_user

        preload_file_modify_date = self.preload_file_modify_date

        name = self.name

        file_size = self.file_size

        encoding_format_type_id = self.encoding_format_type_id

        checksum = self.checksum

        checksum_algorithm = self.checksum_algorithm

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "FileSource": file_source,
            }
        )
        if preload_file_path is not UNSET:
            field_dict["PreloadFilePath"] = preload_file_path
        if preload_file_create_user is not UNSET:
            field_dict["PreloadFileCreateUser"] = preload_file_create_user
        if preload_file_create_date is not UNSET:
            field_dict["PreloadFileCreateDate"] = preload_file_create_date
        if preload_file_modify_user is not UNSET:
            field_dict["PreloadFileModifyUser"] = preload_file_modify_user
        if preload_file_modify_date is not UNSET:
            field_dict["PreloadFileModifyDate"] = preload_file_modify_date
        if name is not UNSET:
            field_dict["Name"] = name
        if file_size is not UNSET:
            field_dict["FileSize"] = file_size
        if encoding_format_type_id is not UNSET:
            field_dict["EncodingFormatTypeID"] = encoding_format_type_id
        if checksum is not UNSET:
            field_dict["Checksum"] = checksum
        if checksum_algorithm is not UNSET:
            field_dict["ChecksumAlgorithm"] = checksum_algorithm

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        file_source = d.pop("FileSource")

        preload_file_path = d.pop("PreloadFilePath", UNSET)

        preload_file_create_user = d.pop("PreloadFileCreateUser", UNSET)

        preload_file_create_date = d.pop("PreloadFileCreateDate", UNSET)

        preload_file_modify_user = d.pop("PreloadFileModifyUser", UNSET)

        preload_file_modify_date = d.pop("PreloadFileModifyDate", UNSET)

        name = d.pop("Name", UNSET)

        file_size = d.pop("FileSize", UNSET)

        encoding_format_type_id = d.pop("EncodingFormatTypeID", UNSET)

        checksum = d.pop("Checksum", UNSET)

        checksum_algorithm = d.pop("ChecksumAlgorithm", UNSET)

        file_source_info = cls(
            file_source=file_source,
            preload_file_path=preload_file_path,
            preload_file_create_user=preload_file_create_user,
            preload_file_create_date=preload_file_create_date,
            preload_file_modify_user=preload_file_modify_user,
            preload_file_modify_date=preload_file_modify_date,
            name=name,
            file_size=file_size,
            encoding_format_type_id=encoding_format_type_id,
            checksum=checksum,
            checksum_algorithm=checksum_algorithm,
        )

        file_source_info.additional_properties = d
        return file_source_info

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
