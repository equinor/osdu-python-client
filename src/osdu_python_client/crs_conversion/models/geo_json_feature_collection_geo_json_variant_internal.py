from enum import Enum


class GeoJsonFeatureCollectionGeoJsonVariantInternal(str, Enum):
    ANY_CRS_GEO_JSON = "ANY_CRS_GEO_JSON"
    GEO_JSON = "GEO_JSON"

    def __str__(self) -> str:
        return str(self.value)
