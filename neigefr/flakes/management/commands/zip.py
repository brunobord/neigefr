import logging

from django.core.management.base import BaseCommand

from ...models import Zipcode
from ...utils import get_geo


logger = logging.getLogger('neigefr')


class Command(BaseCommand):
    args = "<zipcode>"
    help = "Insert a location in the database according to its zipcode"

    def handle(self, zipcode, *args, **kwargs):
        if not Zipcode.objects.filter(zipcode=zipcode).exists():
            longitude, latitude, city = get_geo(zipcode)
            logger.info("Creating: %s (%s)" % (city, zipcode))
            if city:
                Zipcode.objects.create(
                    zipcode=zipcode,
                    city=city,
                    longitude=longitude,
                    latitude=latitude
                )
