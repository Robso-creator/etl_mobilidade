import re

import unidecode
from pyproj import Transformer


def convert_utm_to_latlon(easting, northing, zone_number=23):
    utm_crs = f"EPSG:327{zone_number}"
    wgs84_crs = 'EPSG:4326'

    transformer = Transformer.from_crs(utm_crs, wgs84_crs)
    lat, lon = transformer.transform(easting, northing)

    return lat, lon


def extract_coordinates_point(geometry):
    match = re.match(r'POINT \(([^ ]+) ([^ ]+)\)', geometry)
    if match:
        easting, northing = match.groups()
        return float(easting), float(northing)
    return None, None


def extract_coordinates_linestring(linestring):
    match = re.match(r'LINESTRING \(([^,]+)', linestring)
    if match:
        coord_str = match.group(1)
        easting, northing = map(float, coord_str.split())
        return float(easting), float(northing)
    return None, None


def remove_accents(input_str):
    return unidecode.unidecode(input_str)
