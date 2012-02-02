import re
import json
from neigefr.models import Snowflake, Zipcode
from neigefr.geo import get_geo

ZIPCODE = re.compile('(F-)?([0-9]{5})', re.IGNORECASE)
RANKING = re.compile('([0-9])/10')


class Flake(object):
    zipcode = None
    ranking = None


def process(data):
    "Process JSON data"
    flake = parse_body(data['text'])
    if not flake:
        return None
    if Zipcode.objects.filter(zipcode=flake.zipcode).exists():
        zipcode = Zipcode.objects.get(zipcode=flake.zipcode)
    else:
        longitude, latitude, city = get_geo(flake.zipcode)
        if city:
            zipcode = Zipcode.objects.create(
                zipcode=flake.zipcode,
                city=city,
                longitude=longitude,
                latitude=latitude
            )
    snowflake = Snowflake.objects.create(
        tweet_id=data['id'],
        tweet=json.dumps(data),
        latitude=zipcode.latitude,
        longitude=zipcode.longitude,
        rank=flake.ranking,
        zipcode=zipcode,
    )
    return snowflake


def parse_body(body):
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
