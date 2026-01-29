from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.crs_essence_impl import CRSEssenceImpl


T = TypeVar("T", bound="CRSRequest")


@_attrs_define
class CRSRequest:
    """Request to get one CRS (any sub-type) given its 'persistableReference' (serialized essence) or 'essence' structure.
    Only one, persistableReference or essence must be provided. If both are provided, essence takes precedence. If both
    are provided, essence takes precedence

        Attributes:
            crsessence_json (CRSEssenceImpl | Unset): Any coordinate reference system essence carrying all possible
                properties for LateBoundCRSEssence, EarlyBoundCRSEssence and CompoundCRSEssence
            essence (CRSEssenceImpl | Unset): Any coordinate reference system essence carrying all possible properties for
                LateBoundCRSEssence, EarlyBoundCRSEssence and CompoundCRSEssence
            persistable_reference (str | Unset): persistable reference string
    """

    crsessence_json: CRSEssenceImpl | Unset = UNSET
    essence: CRSEssenceImpl | Unset = UNSET
    persistable_reference: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        crsessence_json: dict[str, Any] | Unset = UNSET
        if not isinstance(self.crsessence_json, Unset):
            crsessence_json = self.crsessence_json.to_dict()

        essence: dict[str, Any] | Unset = UNSET
        if not isinstance(self.essence, Unset):
            essence = self.essence.to_dict()

        persistable_reference = self.persistable_reference

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if crsessence_json is not UNSET:
            field_dict["crsessenceJson"] = crsessence_json
        if essence is not UNSET:
            field_dict["essence"] = essence
        if persistable_reference is not UNSET:
            field_dict["persistableReference"] = persistable_reference

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.crs_essence_impl import CRSEssenceImpl

        d = dict(src_dict)
        _crsessence_json = d.pop("crsessenceJson", UNSET)
        crsessence_json: CRSEssenceImpl | Unset
        if isinstance(_crsessence_json, Unset):
            crsessence_json = UNSET
        else:
            crsessence_json = CRSEssenceImpl.from_dict(_crsessence_json)

        _essence = d.pop("essence", UNSET)
        essence: CRSEssenceImpl | Unset
        if isinstance(_essence, Unset):
            essence = UNSET
        else:
            essence = CRSEssenceImpl.from_dict(_essence)

        persistable_reference = d.pop("persistableReference", UNSET)

        crs_request = cls(
            crsessence_json=crsessence_json,
            essence=essence,
            persistable_reference=persistable_reference,
        )

        crs_request.additional_properties = d
        return crs_request

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
