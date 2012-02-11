import re
from neigefr.models import Zipcode


ZIPCODE = re.compile('(F-)?([0-9]{5})', re.IGNORECASE)
RANKING = re.compile('([0-9]+)/10')


class Flake(object):
    zipcode = None
    ranking = None


def find_zipcode(zipcode):
    "Find a Zipcode object. Or None"
    if Zipcode.objects.filter(zipcode=zipcode).exists():
        return Zipcode.objects.get(zipcode=zipcode)


def parse_body(body):
    "Parse the tweet body. Return a Flake object"
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
