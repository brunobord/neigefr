from geocoders.geonames import geocode

SPECIAL_CASES = {'75000': 'Paris'}


def get_geo(zipcode):
    searched_code = zipcode
    if zipcode in SPECIAL_CASES:
        searched_code = SPECIAL_CASES[zipcode]
    place, (longitude, latitude) = geocode('%s, France' % searched_code)
    return str(longitude), str(latitude), place
