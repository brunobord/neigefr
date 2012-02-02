from django.conf import settings
import json
import requests


def get_geo(zipcode):
    url = "http://maps.google.com/maps/geo?q="+zipcode+",France&output=json&sensor=false&key="+settings.GOOGLE_MAPS_KEY
    location = get_from_geo(url)
    status = location["Status"]["code"]
    if status != 200:
        return None, None
    place = location["Placemark"][0]
    country_code = place["AddressDetails"]["Country"]["CountryNameCode"]
    if country_code != "FR":
        return None, None, None
    longitude, latitude, height = place["Point"]["coordinates"]
    locality_name = place['AddressDetails']['Country']['AdministrativeArea']['SubAdministrativeArea']['Locality']['LocalityName']
    return str(longitude), str(latitude), locality_name


def get_from_geo(url):
    result = requests.get(url)
    data = json.loads(result.text)
    return data
