from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.abstract_feature import AbstractFeature


T = TypeVar("T", bound="AbstractAnyCrsFeatureCollection")


@_attrs_define
class AbstractAnyCrsFeatureCollection:
    """
    Attributes:
        persistable_reference_crs (str | Unset):
        coordinate_reference_system_id (str | Unset):
        type_ (str | Unset):
        features (list[AbstractFeature] | Unset):
    """

    persistable_reference_crs: str | Unset = UNSET
    coordinate_reference_system_id: str | Unset = UNSET
    type_: str | Unset = UNSET
    features: list[AbstractFeature] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        persistable_reference_crs = self.persistable_reference_crs

        coordinate_reference_system_id = self.coordinate_reference_system_id

        type_ = self.type_

        features: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.features, Unset):
            features = []
            for features_item_data in self.features:
                features_item = features_item_data.to_dict()
                features.append(features_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if persistable_reference_crs is not UNSET:
            field_dict["persistableReferenceCrs"] = persistable_reference_crs
        if coordinate_reference_system_id is not UNSET:
            field_dict["CoordinateReferenceSystemID"] = coordinate_reference_system_id
        if type_ is not UNSET:
            field_dict["type"] = type_
        if features is not UNSET:
            field_dict["features"] = features

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.abstract_feature import AbstractFeature

        d = dict(src_dict)
        persistable_reference_crs = d.pop("persistableReferenceCrs", UNSET)

        coordinate_reference_system_id = d.pop("CoordinateReferenceSystemID", UNSET)

        type_ = d.pop("type", UNSET)

        _features = d.pop("features", UNSET)
        features: list[AbstractFeature] | Unset = UNSET
        if _features is not UNSET:
            features = []
            for features_item_data in _features:
                features_item = AbstractFeature.from_dict(features_item_data)

                features.append(features_item)

        abstract_any_crs_feature_collection = cls(
            persistable_reference_crs=persistable_reference_crs,
            coordinate_reference_system_id=coordinate_reference_system_id,
            type_=type_,
            features=features,
        )

        abstract_any_crs_feature_collection.additional_properties = d
        return abstract_any_crs_feature_collection

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
