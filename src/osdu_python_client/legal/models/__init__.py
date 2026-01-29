"""Contains all the data models used in inputs/outputs"""

from .app_error import AppError
from .connected_outer_service import ConnectedOuterService
from .feature_flag_state import FeatureFlagState
from .invalid_tag_with_reason import InvalidTagWithReason
from .invalid_tags_with_reason import InvalidTagsWithReason
from .legal_tag_dto import LegalTagDto
from .legal_tag_dtos import LegalTagDtos
from .properties import Properties
from .properties_extension_properties import PropertiesExtensionProperties
from .properties_extension_properties_additional_property import (
    PropertiesExtensionPropertiesAdditionalProperty,
)
from .query_legal_tag import QueryLegalTag
from .readable_property_values import ReadablePropertyValues
from .readable_property_values_countries_of_origin import (
    ReadablePropertyValuesCountriesOfOrigin,
)
from .readable_property_values_other_relevant_data_countries import (
    ReadablePropertyValuesOtherRelevantDataCountries,
)
from .request_legal_tags import RequestLegalTags
from .update_legal_tag import UpdateLegalTag
from .update_legal_tag_extension_properties import UpdateLegalTagExtensionProperties
from .update_legal_tag_extension_properties_additional_property import (
    UpdateLegalTagExtensionPropertiesAdditionalProperty,
)
from .version_info import VersionInfo

__all__ = (
    "AppError",
    "ConnectedOuterService",
    "FeatureFlagState",
    "InvalidTagsWithReason",
    "InvalidTagWithReason",
    "LegalTagDto",
    "LegalTagDtos",
    "Properties",
    "PropertiesExtensionProperties",
    "PropertiesExtensionPropertiesAdditionalProperty",
    "QueryLegalTag",
    "ReadablePropertyValues",
    "ReadablePropertyValuesCountriesOfOrigin",
    "ReadablePropertyValuesOtherRelevantDataCountries",
    "RequestLegalTags",
    "UpdateLegalTag",
    "UpdateLegalTagExtensionProperties",
    "UpdateLegalTagExtensionPropertiesAdditionalProperty",
    "VersionInfo",
)
