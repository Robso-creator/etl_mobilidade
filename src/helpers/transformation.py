import re

import unidecode
from geopy.geocoders import Nominatim
from pyproj import Proj
from pyproj import transform


def convert_utm_to_latlon(easting, northing, zone_number=23):
    proj_utm = Proj(proj='utm', zone=zone_number, datum='WGS84')
    proj_wgs84 = Proj(proj='latlong', datum='WGS84')

    lon, lat = transform(proj_utm, proj_wgs84, easting, northing)
    return lat, lon


geolocator = Nominatim(user_agent='geoapiExercises')


def reverse_geocode(lat, lon):
    try:
        location = geolocator.reverse((lat, lon), exactly_one=True)
        return location.address if location else None
    except Exception:
        return None


def extract_coordinates(geometry):
    match = re.match(r'POINT \(([^ ]+) ([^ ]+)\)', geometry)
    if match:
        lon, lat = match.groups()
        return float(lat), float(lon)
    return None, None


def remove_accents(input_str):
    return unidecode.unidecode(input_str)
