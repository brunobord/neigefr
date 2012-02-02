import logging
from django.core.management.base import BaseCommand
from neigefr.geo import get_geo
from neigefr.models import Zipcode
# , CommandError

logger = logging.getLogger(__name__)


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
