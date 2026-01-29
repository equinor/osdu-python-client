from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.unit_assignment import UnitAssignment


T = TypeVar("T", bound="UnitSystem")


@_attrs_define
class UnitSystem:
    """
    Attributes:
        name (str | Unset):
        offset (int | Unset):
        last_modified (str | Unset):
        source (str | Unset):
        description (str | Unset):
        ancestry (str | Unset):
        persistable_reference (str | Unset):
        unit_assignment_count (int | Unset):
        reference_unit_system (str | Unset):
        unit_assignments (list[UnitAssignment] | Unset):
        unit_assignment_count_in_response (int | Unset):
        unit_assignment_count_total (int | Unset):
    """

    name: str | Unset = UNSET
    offset: int | Unset = UNSET
    last_modified: str | Unset = UNSET
    source: str | Unset = UNSET
    description: str | Unset = UNSET
    ancestry: str | Unset = UNSET
    persistable_reference: str | Unset = UNSET
    unit_assignment_count: int | Unset = UNSET
    reference_unit_system: str | Unset = UNSET
    unit_assignments: list[UnitAssignment] | Unset = UNSET
    unit_assignment_count_in_response: int | Unset = UNSET
    unit_assignment_count_total: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        offset = self.offset

        last_modified = self.last_modified

        source = self.source

        description = self.description

        ancestry = self.ancestry

        persistable_reference = self.persistable_reference

        unit_assignment_count = self.unit_assignment_count

        reference_unit_system = self.reference_unit_system

        unit_assignments: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.unit_assignments, Unset):
            unit_assignments = []
            for unit_assignments_item_data in self.unit_assignments:
                unit_assignments_item = unit_assignments_item_data.to_dict()
                unit_assignments.append(unit_assignments_item)

        unit_assignment_count_in_response = self.unit_assignment_count_in_response

        unit_assignment_count_total = self.unit_assignment_count_total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if offset is not UNSET:
            field_dict["offset"] = offset
        if last_modified is not UNSET:
            field_dict["lastModified"] = last_modified
        if source is not UNSET:
            field_dict["source"] = source
        if description is not UNSET:
            field_dict["description"] = description
        if ancestry is not UNSET:
            field_dict["ancestry"] = ancestry
        if persistable_reference is not UNSET:
            field_dict["persistableReference"] = persistable_reference
        if unit_assignment_count is not UNSET:
            field_dict["unitAssignmentCount"] = unit_assignment_count
        if reference_unit_system is not UNSET:
            field_dict["referenceUnitSystem"] = reference_unit_system
        if unit_assignments is not UNSET:
            field_dict["unitAssignments"] = unit_assignments
        if unit_assignment_count_in_response is not UNSET:
            field_dict["unitAssignmentCountInResponse"] = (
                unit_assignment_count_in_response
            )
        if unit_assignment_count_total is not UNSET:
            field_dict["unitAssignmentCountTotal"] = unit_assignment_count_total

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.unit_assignment import UnitAssignment

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        offset = d.pop("offset", UNSET)

        last_modified = d.pop("lastModified", UNSET)

        source = d.pop("source", UNSET)

        description = d.pop("description", UNSET)

        ancestry = d.pop("ancestry", UNSET)

        persistable_reference = d.pop("persistableReference", UNSET)

        unit_assignment_count = d.pop("unitAssignmentCount", UNSET)

        reference_unit_system = d.pop("referenceUnitSystem", UNSET)

        _unit_assignments = d.pop("unitAssignments", UNSET)
        unit_assignments: list[UnitAssignment] | Unset = UNSET
        if _unit_assignments is not UNSET:
            unit_assignments = []
            for unit_assignments_item_data in _unit_assignments:
                unit_assignments_item = UnitAssignment.from_dict(
                    unit_assignments_item_data
                )

                unit_assignments.append(unit_assignments_item)

        unit_assignment_count_in_response = d.pop(
            "unitAssignmentCountInResponse", UNSET
        )

        unit_assignment_count_total = d.pop("unitAssignmentCountTotal", UNSET)

        unit_system = cls(
            name=name,
            offset=offset,
            last_modified=last_modified,
            source=source,
            description=description,
            ancestry=ancestry,
            persistable_reference=persistable_reference,
            unit_assignment_count=unit_assignment_count,
            reference_unit_system=reference_unit_system,
            unit_assignments=unit_assignments,
            unit_assignment_count_in_response=unit_assignment_count_in_response,
            unit_assignment_count_total=unit_assignment_count_total,
        )

        unit_system.additional_properties = d
        return unit_system

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
