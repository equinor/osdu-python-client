from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.measurement_deprecation_info import MeasurementDeprecationInfo
    from ..models.measurement_essence import MeasurementEssence


T = TypeVar("T", bound="Measurement")


@_attrs_define
class Measurement:
    """
    Attributes:
        name (str | Unset):
        last_modified (str | Unset):
        code (str | Unset):
        unit_quantity_code (str | Unset):
        essence_json (str | Unset):
        child_measurement_essence_jsons (list[str] | Unset):
        unit_essence_jsons (list[str] | Unset):
        preferred_unit_essence_jsons (list[str] | Unset):
        parent_essence_json (str | Unset):
        dimension_analysis (str | Unset):
        description (str | Unset):
        dimension_code (str | Unset):
        essence (MeasurementEssence | Unset):
        base_measurement (bool | Unset):
        base_measurement_essence_json (str | Unset):
        deprecation_info (MeasurementDeprecationInfo | Unset):
        namespace (str | Unset):
    """

    name: str | Unset = UNSET
    last_modified: str | Unset = UNSET
    code: str | Unset = UNSET
    unit_quantity_code: str | Unset = UNSET
    essence_json: str | Unset = UNSET
    child_measurement_essence_jsons: list[str] | Unset = UNSET
    unit_essence_jsons: list[str] | Unset = UNSET
    preferred_unit_essence_jsons: list[str] | Unset = UNSET
    parent_essence_json: str | Unset = UNSET
    dimension_analysis: str | Unset = UNSET
    description: str | Unset = UNSET
    dimension_code: str | Unset = UNSET
    essence: MeasurementEssence | Unset = UNSET
    base_measurement: bool | Unset = UNSET
    base_measurement_essence_json: str | Unset = UNSET
    deprecation_info: MeasurementDeprecationInfo | Unset = UNSET
    namespace: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        last_modified = self.last_modified

        code = self.code

        unit_quantity_code = self.unit_quantity_code

        essence_json = self.essence_json

        child_measurement_essence_jsons: list[str] | Unset = UNSET
        if not isinstance(self.child_measurement_essence_jsons, Unset):
            child_measurement_essence_jsons = self.child_measurement_essence_jsons

        unit_essence_jsons: list[str] | Unset = UNSET
        if not isinstance(self.unit_essence_jsons, Unset):
            unit_essence_jsons = self.unit_essence_jsons

        preferred_unit_essence_jsons: list[str] | Unset = UNSET
        if not isinstance(self.preferred_unit_essence_jsons, Unset):
            preferred_unit_essence_jsons = self.preferred_unit_essence_jsons

        parent_essence_json = self.parent_essence_json

        dimension_analysis = self.dimension_analysis

        description = self.description

        dimension_code = self.dimension_code

        essence: dict[str, Any] | Unset = UNSET
        if not isinstance(self.essence, Unset):
            essence = self.essence.to_dict()

        base_measurement = self.base_measurement

        base_measurement_essence_json = self.base_measurement_essence_json

        deprecation_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.deprecation_info, Unset):
            deprecation_info = self.deprecation_info.to_dict()

        namespace = self.namespace

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if last_modified is not UNSET:
            field_dict["lastModified"] = last_modified
        if code is not UNSET:
            field_dict["code"] = code
        if unit_quantity_code is not UNSET:
            field_dict["unitQuantityCode"] = unit_quantity_code
        if essence_json is not UNSET:
            field_dict["essenceJson"] = essence_json
        if child_measurement_essence_jsons is not UNSET:
            field_dict["childMeasurementEssenceJsons"] = child_measurement_essence_jsons
        if unit_essence_jsons is not UNSET:
            field_dict["unitEssenceJsons"] = unit_essence_jsons
        if preferred_unit_essence_jsons is not UNSET:
            field_dict["preferredUnitEssenceJsons"] = preferred_unit_essence_jsons
        if parent_essence_json is not UNSET:
            field_dict["parentEssenceJson"] = parent_essence_json
        if dimension_analysis is not UNSET:
            field_dict["dimensionAnalysis"] = dimension_analysis
        if description is not UNSET:
            field_dict["description"] = description
        if dimension_code is not UNSET:
            field_dict["dimensionCode"] = dimension_code
        if essence is not UNSET:
            field_dict["essence"] = essence
        if base_measurement is not UNSET:
            field_dict["baseMeasurement"] = base_measurement
        if base_measurement_essence_json is not UNSET:
            field_dict["baseMeasurementEssenceJson"] = base_measurement_essence_json
        if deprecation_info is not UNSET:
            field_dict["deprecationInfo"] = deprecation_info
        if namespace is not UNSET:
            field_dict["namespace"] = namespace

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.measurement_deprecation_info import MeasurementDeprecationInfo
        from ..models.measurement_essence import MeasurementEssence

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        last_modified = d.pop("lastModified", UNSET)

        code = d.pop("code", UNSET)

        unit_quantity_code = d.pop("unitQuantityCode", UNSET)

        essence_json = d.pop("essenceJson", UNSET)

        child_measurement_essence_jsons = cast(
            list[str], d.pop("childMeasurementEssenceJsons", UNSET)
        )

        unit_essence_jsons = cast(list[str], d.pop("unitEssenceJsons", UNSET))

        preferred_unit_essence_jsons = cast(
            list[str], d.pop("preferredUnitEssenceJsons", UNSET)
        )

        parent_essence_json = d.pop("parentEssenceJson", UNSET)

        dimension_analysis = d.pop("dimensionAnalysis", UNSET)

        description = d.pop("description", UNSET)

        dimension_code = d.pop("dimensionCode", UNSET)

        _essence = d.pop("essence", UNSET)
        essence: MeasurementEssence | Unset
        if isinstance(_essence, Unset):
            essence = UNSET
        else:
            essence = MeasurementEssence.from_dict(_essence)

        base_measurement = d.pop("baseMeasurement", UNSET)

        base_measurement_essence_json = d.pop("baseMeasurementEssenceJson", UNSET)

        _deprecation_info = d.pop("deprecationInfo", UNSET)
        deprecation_info: MeasurementDeprecationInfo | Unset
        if isinstance(_deprecation_info, Unset):
            deprecation_info = UNSET
        else:
            deprecation_info = MeasurementDeprecationInfo.from_dict(_deprecation_info)

        namespace = d.pop("namespace", UNSET)

        measurement = cls(
            name=name,
            last_modified=last_modified,
            code=code,
            unit_quantity_code=unit_quantity_code,
            essence_json=essence_json,
            child_measurement_essence_jsons=child_measurement_essence_jsons,
            unit_essence_jsons=unit_essence_jsons,
            preferred_unit_essence_jsons=preferred_unit_essence_jsons,
            parent_essence_json=parent_essence_json,
            dimension_analysis=dimension_analysis,
            description=description,
            dimension_code=dimension_code,
            essence=essence,
            base_measurement=base_measurement,
            base_measurement_essence_json=base_measurement_essence_json,
            deprecation_info=deprecation_info,
            namespace=namespace,
        )

        measurement.additional_properties = d
        return measurement

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
