from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.file_data_endian import FileDataEndian
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dataset_properties import DatasetProperties
    from ..models.file_data_extension_properties import FileDataExtensionProperties


T = TypeVar("T", bound="FileData")


@_attrs_define
class FileData:
    r"""The file data container containing all necessary details of the file record

    Attributes:
        dataset_properties (DatasetProperties): Dataset Properties
        name (str | Unset): An optional name of the dataset, e.g. a user friendly file or file collection name.
        description (str | Unset): An optional, textual description of the dataset.
        total_size (str | Unset): Total size of the dataset in bytes; for files it is the same as declared in
            FileSourceInfo.FileSize or the sum of all individual files. Implemented as string. The value must be convertible
            to a long integer (sizes can become very large).
        encoding_format_type_id (str | Unset): Encoding Format Type ID
        schema_format_type_id (str | Unset): Schema Format Type ID
        resource_home_region_id (str | Unset): Resource Home Region ID
        resource_host_region_i_ds (list[str] | Unset): Resource Host Region IDs
        resource_curation_status (str | Unset): Resource Curation Status
        resource_lifecycle_status (str | Unset): Resource Lifecycle Status
        resource_security_classification (str | Unset): Resource Security Classification
        source (str | Unset): Source
        existence_kind (str | Unset): Existence Kind
        endian (FileDataEndian | Unset): Endianness of binary value. Enumeration- \BIG\ \LITTLE\.  If absent
            applications will need to interpret from context indicators.
        checksum (str | Unset): MD5 checksum of file bytes - a 32 byte hexadecimal number
        extension_properties (FileDataExtensionProperties | Unset): File DMS Extension Properties
    """

    dataset_properties: DatasetProperties
    name: str | Unset = UNSET
    description: str | Unset = UNSET
    total_size: str | Unset = UNSET
    encoding_format_type_id: str | Unset = UNSET
    schema_format_type_id: str | Unset = UNSET
    resource_home_region_id: str | Unset = UNSET
    resource_host_region_i_ds: list[str] | Unset = UNSET
    resource_curation_status: str | Unset = UNSET
    resource_lifecycle_status: str | Unset = UNSET
    resource_security_classification: str | Unset = UNSET
    source: str | Unset = UNSET
    existence_kind: str | Unset = UNSET
    endian: FileDataEndian | Unset = UNSET
    checksum: str | Unset = UNSET
    extension_properties: FileDataExtensionProperties | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dataset_properties = self.dataset_properties.to_dict()

        name = self.name

        description = self.description

        total_size = self.total_size

        encoding_format_type_id = self.encoding_format_type_id

        schema_format_type_id = self.schema_format_type_id

        resource_home_region_id = self.resource_home_region_id

        resource_host_region_i_ds: list[str] | Unset = UNSET
        if not isinstance(self.resource_host_region_i_ds, Unset):
            resource_host_region_i_ds = self.resource_host_region_i_ds

        resource_curation_status = self.resource_curation_status

        resource_lifecycle_status = self.resource_lifecycle_status

        resource_security_classification = self.resource_security_classification

        source = self.source

        existence_kind = self.existence_kind

        endian: str | Unset = UNSET
        if not isinstance(self.endian, Unset):
            endian = self.endian.value

        checksum = self.checksum

        extension_properties: dict[str, Any] | Unset = UNSET
        if not isinstance(self.extension_properties, Unset):
            extension_properties = self.extension_properties.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "DatasetProperties": dataset_properties,
            }
        )
        if name is not UNSET:
            field_dict["Name"] = name
        if description is not UNSET:
            field_dict["Description"] = description
        if total_size is not UNSET:
            field_dict["TotalSize"] = total_size
        if encoding_format_type_id is not UNSET:
            field_dict["EncodingFormatTypeID"] = encoding_format_type_id
        if schema_format_type_id is not UNSET:
            field_dict["SchemaFormatTypeID"] = schema_format_type_id
        if resource_home_region_id is not UNSET:
            field_dict["ResourceHomeRegionID"] = resource_home_region_id
        if resource_host_region_i_ds is not UNSET:
            field_dict["ResourceHostRegionIDs"] = resource_host_region_i_ds
        if resource_curation_status is not UNSET:
            field_dict["ResourceCurationStatus"] = resource_curation_status
        if resource_lifecycle_status is not UNSET:
            field_dict["ResourceLifecycleStatus"] = resource_lifecycle_status
        if resource_security_classification is not UNSET:
            field_dict["ResourceSecurityClassification"] = (
                resource_security_classification
            )
        if source is not UNSET:
            field_dict["Source"] = source
        if existence_kind is not UNSET:
            field_dict["ExistenceKind"] = existence_kind
        if endian is not UNSET:
            field_dict["Endian"] = endian
        if checksum is not UNSET:
            field_dict["Checksum"] = checksum
        if extension_properties is not UNSET:
            field_dict["ExtensionProperties"] = extension_properties

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dataset_properties import DatasetProperties
        from ..models.file_data_extension_properties import FileDataExtensionProperties

        d = dict(src_dict)
        dataset_properties = DatasetProperties.from_dict(d.pop("DatasetProperties"))

        name = d.pop("Name", UNSET)

        description = d.pop("Description", UNSET)

        total_size = d.pop("TotalSize", UNSET)

        encoding_format_type_id = d.pop("EncodingFormatTypeID", UNSET)

        schema_format_type_id = d.pop("SchemaFormatTypeID", UNSET)

        resource_home_region_id = d.pop("ResourceHomeRegionID", UNSET)

        resource_host_region_i_ds = cast(
            list[str], d.pop("ResourceHostRegionIDs", UNSET)
        )

        resource_curation_status = d.pop("ResourceCurationStatus", UNSET)

        resource_lifecycle_status = d.pop("ResourceLifecycleStatus", UNSET)

        resource_security_classification = d.pop(
            "ResourceSecurityClassification", UNSET
        )

        source = d.pop("Source", UNSET)

        existence_kind = d.pop("ExistenceKind", UNSET)

        _endian = d.pop("Endian", UNSET)
        endian: FileDataEndian | Unset
        if isinstance(_endian, Unset):
            endian = UNSET
        else:
            endian = FileDataEndian(_endian)

        checksum = d.pop("Checksum", UNSET)

        _extension_properties = d.pop("ExtensionProperties", UNSET)
        extension_properties: FileDataExtensionProperties | Unset
        if isinstance(_extension_properties, Unset):
            extension_properties = UNSET
        else:
            extension_properties = FileDataExtensionProperties.from_dict(
                _extension_properties
            )

        file_data = cls(
            dataset_properties=dataset_properties,
            name=name,
            description=description,
            total_size=total_size,
            encoding_format_type_id=encoding_format_type_id,
            schema_format_type_id=schema_format_type_id,
            resource_home_region_id=resource_home_region_id,
            resource_host_region_i_ds=resource_host_region_i_ds,
            resource_curation_status=resource_curation_status,
            resource_lifecycle_status=resource_lifecycle_status,
            resource_security_classification=resource_security_classification,
            source=source,
            existence_kind=existence_kind,
            endian=endian,
            checksum=checksum,
            extension_properties=extension_properties,
        )

        file_data.additional_properties = d
        return file_data

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
