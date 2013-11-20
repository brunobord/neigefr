import logging

from django.conf import settings
from django.core.management.base import NoArgsCommand

from ...models import Snowflake
from ...utils import process
from ....settings import api

logger = logging.getLogger('neigefr')


# https://twitter.com/#!/search/%40twitterapi
class Command(NoArgsCommand):
    help = "Is searching for tweets with #neigefr and store them in DB"

    def handle(self, **options):
        for country in settings.COUNTRY_CODES:
            kwargs = {
                'term': '%23neige{0}'.format(country.lower())
            }

            last_snowflakes = Snowflake.objects.filter(
                zipcode__country=country.upper()
            ).order_by('-tweet_id')

            if last_snowflakes:
                last = last_snowflakes[0]
                kwargs['since_id'] = last.tweet_id

            response = api.GetSearch(**kwargs)
            for tweet in response:
                process(tweet)
