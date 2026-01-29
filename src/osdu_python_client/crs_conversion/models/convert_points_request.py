from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.point import Point


T = TypeVar("T", bound="ConvertPointsRequest")


@_attrs_define
class ConvertPointsRequest:
    r"""Request to convert a set of points from a source CRS to a target CRS

    Attributes:
        from_crs (str): Source CRS as persistable reference string Example: "{"lateBoundCRS":{"wkt":"GEOGCS[\"GCS_Provis
            ional_S_American_1956\",DATUM[\"D_Provisional_S_American_1956\",SPHEROID[\"International_1924\",6378388.0,297.0]
            ],PRIMEM[\"Greenwich\",0.0],UNIT[\"Degree\",0.0174532925199433],AUTHORITY[\"EPSG\",4248]]","ver":"PE_10_3_1","na
            me":"GCS_Provisional_S_American_1956","authCode":{"auth":"EPSG","code":"4248"},"type":"LBC"},"singleCT":{"wkt":"
            GEOGTRAN[\"PSAD_1956_To_WGS_1984_9\",GEOGCS[\"GCS_Provisional_S_American_1956\",DATUM[\"D_Provisional_S_American
            _1956\",SPHEROID[\"International_1924\",6378388.0,297.0]],PRIMEM[\"Greenwich\",0.0],UNIT[\"Degree\",0.0174532925
            199433]],GEOGCS[\"GCS_WGS_1984\",DATUM[\"D_WGS_1984\",SPHEROID[\"WGS_1984\",6378137.0,298.257223563]],PRIMEM[\"G
            reenwich\",0.0],UNIT[\"Degree\",0.0174532925199433]],METHOD[\"Geocentric_Translation\"],PARAMETER[\"X_Axis_Trans
            lation\",-295.0],PARAMETER[\"Y_Axis_Translation\",173.0],PARAMETER[\"Z_Axis_Translation\",-
            371.0],AUTHORITY[\"EPSG\",1209]]","ver":"PE_10_3_1","name":"PSAD_1956_To_WGS_1984_9","authCode":{"auth":"EPSG","
            code":"1209"},"type":"ST"},"ver":"PE_10_3_1","name":"PSAD56 * DMA-Ven
            [4248,1209]","authCode":{"auth":"SLB","code":"4248009"},"type":"EBC"}".
        to_crs (str): Target CRS as persistable reference string Example: "{"lateBoundCRS":{"wkt":"PROJCS[\"Trinidad_190
            3_Trinidad_Grid\",GEOGCS[\"GCS_Trinidad_1903\",DATUM[\"D_Trinidad_1903\",SPHEROID[\"Clarke_1858\",6378293.645208
            76,294.260676369]],PRIMEM[\"Greenwich\",0.0],UNIT[\"Degree\",0.0174532925199433]],PROJECTION[\"Cassini\"],PARAME
            TER[\"False_Easting\",430000.0],PARAMETER[\"False_Northing\",325000.0],PARAMETER[\"Central_Meridian\",-
            61.3333333333333],PARAMETER[\"Scale_Factor\",1.0],PARAMETER[\"Latitude_Of_Origin\",10.4416666666667],UNIT[\"Link
            _Clarke\",0.201166195164],AUTHORITY[\"EPSG\",30200]]","ver":"PE_10_3_1","name":"Trinidad_1903_Trinidad_Grid","au
            thCode":{"auth":"EPSG","code":"30200"},"type":"LBC"},"singleCT":{"wkt":"GEOGTRAN[\"Trinidad_1903_To_WGS_1984_2\"
            ,GEOGCS[\"GCS_Trinidad_1903\",DATUM[\"D_Trinidad_1903\",SPHEROID[\"Clarke_1858\",6378293.64520876,294.260676369]
            ],PRIMEM[\"Greenwich\",0.0],UNIT[\"Degree\",0.0174532925199433]],GEOGCS[\"GCS_WGS_1984\",DATUM[\"D_WGS_1984\",SP
            HEROID[\"WGS_1984\",6378137.0,298.257223563]],PRIMEM[\"Greenwich\",0.0],UNIT[\"Degree\",0.0174532925199433]],MET
            HOD[\"Geocentric_Translation\"],PARAMETER[\"X_Axis_Translation\",-
            61.0],PARAMETER[\"Y_Axis_Translation\",285.2],PARAMETER[\"Z_Axis_Translation\",471.6],AUTHORITY[\"EPSG\",10085]]
            ","ver":"PE_10_3_1","name":"Trinidad_1903_To_WGS_1984_2","authCode":{"auth":"EPSG","code":"10085"},"type":"ST"},
            "ver":"PE_10_3_1","name":"Trinidad 1903 * EOG-Tto Trin / Trinidad Grid
            [30200,10085]","authCode":{"auth":"SLB","code":"30200002"},"type":"EBC"}".
        points (list[Point]): List of points to be converted Example: [{'x': -61.04340628871454, 'y':
            10.673103179456877, 'z': 0}].
    """

    from_crs: str
    to_crs: str
    points: list[Point]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from_crs = self.from_crs

        to_crs = self.to_crs

        points = []
        for points_item_data in self.points:
            points_item = points_item_data.to_dict()
            points.append(points_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "fromCRS": from_crs,
                "toCRS": to_crs,
                "points": points,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.point import Point

        d = dict(src_dict)
        from_crs = d.pop("fromCRS")

        to_crs = d.pop("toCRS")

        points = []
        _points = d.pop("points")
        for points_item_data in _points:
            points_item = Point.from_dict(points_item_data)

            points.append(points_item)

        convert_points_request = cls(
            from_crs=from_crs,
            to_crs=to_crs,
            points=points,
        )

        convert_points_request.additional_properties = d
        return convert_points_request

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
