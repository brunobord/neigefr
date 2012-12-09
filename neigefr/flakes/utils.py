import re
import json
import logging

from geocoders.geonames import geocode

from .models import Snowflake, Zipcode

SPECIAL_CASES = {'75000': 'Paris'}

ZIPCODE = re.compile('(F-)?([0-9]{5})', re.IGNORECASE)
RANKING = re.compile('([0-9]+)/10')

logger = logging.getLogger('neigefr')


class Flake(object):
    zipcode = None
    ranking = None


def find_zipcode(zipcode):
    """Find a Zipcode object. Or None"""
    if Zipcode.objects.filter(zipcode=zipcode).exists():
        return Zipcode.objects.get(zipcode=zipcode)


def parse_body(body):
    """Parse the tweet body. Return a Flake object"""
    flake = Flake()
    if '#neigefr' not in body:
        return None
    matcher = ZIPCODE.search(body)
    if matcher:
        flake.zipcode = matcher.group(2)
    matcher = RANKING.search(body)
    if matcher:
        flake.ranking = int(matcher.group(1))
    return flake


def process(data):
    """Process JSON data"""
    flake = parse_body(data['text'])
    if not flake:
        return None
    if not flake.zipcode:
        return None

    zipcode = find_zipcode(flake.zipcode)
    if not zipcode:
        longitude, latitude, city = get_geo(flake.zipcode)
        if city:
            zipcode = Zipcode.objects.create(
                zipcode=flake.zipcode,
                city=city,
                longitude=longitude,
                latitude=latitude
            )
        else:
            logger.error("Zipcode pas trouve {0}".format(flake.zipcode))
            return
    snowflake = Snowflake.objects.create(
        tweet_id=data['id'],
        tweet=json.dumps(data),
        latitude=zipcode.latitude,
        longitude=zipcode.longitude,
        rank=flake.ranking,
        zipcode=zipcode,
    )
    return snowflake


def get_geo(zipcode):
    searched_code = zipcode
    if zipcode in SPECIAL_CASES:
        searched_code = SPECIAL_CASES[zipcode]
    place, (latitude, longitude) = geocode('%s, France' % searched_code)
    return str(longitude), str(latitude), place
