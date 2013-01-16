import re
import json
import logging
import requests

from django.conf import settings

from .models import Snowflake, Zipcode

HASHTAG = re.compile('#neige({0})'.format('|'.join(settings.COUNTRY_CODES)))
ZIPCODE = re.compile('(F-|CH-|B-)?([0-9]{4,5})', re.IGNORECASE)
RANKING = re.compile('([0-9]+)/10')

logger = logging.getLogger('neigefr')


class Flake(object):
    zipcode = None
    country = None
    ranking = None


def get_object_or_None(klass, *args, **kwargs):
    try:
        return klass._default_manager.get(*args, **kwargs)
    except klass.DoesNotExist:
        return None


def parse_body(body):
    """Parse the tweet body. Returns a Flake object"""
    flake = Flake()
    matcher = HASHTAG.search(body)
    if matcher is None:
        return
    flake.country = matcher.group(1).upper()
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
    if not flake.country:
        return None

    zipcode = get_object_or_None(Zipcode,
                                 zipcode=flake.zipcode,
                                 country=flake.country)
    if zipcode is None:
        city, (latitude, longitude) = geocode(flake.zipcode, flake.country)
        if city:
            zipcode = Zipcode.objects.create(
                zipcode=flake.zipcode,
                city=city,
                country=flake.country,
                longitude=str(longitude),
                latitude=str(latitude)
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


def geocode(zipcode, country):
    if country is None:
        country = 'FR'

    url = 'http://ws.geonames.org/postalCodeSearchJSON'
    payload = {
        'postalcode': zipcode,
        'country': country,
    }
    response = requests.get(url, params=payload)
    json_data = response.json
    if not json_data['postalCodes']:
        return None, (None, None)

    place = json_data['postalCodes'][0]
    name = place['placeName']
    if place['adminName1'] and name != place['adminName1']:
        name += ', ' + place['adminName1']
    return name, (place['lat'], place['lng'])
