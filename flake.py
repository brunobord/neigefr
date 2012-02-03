import json
from neigefr.helpers import find_zipcode, parse_body
from neigefr.models import Snowflake, Zipcode
from neigefr.geo import get_geo


def process(data):
    "Process JSON data"
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
            print "Zipcode pas trouve", flake.zipcode
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
