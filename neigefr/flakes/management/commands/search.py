import logging
import requests

from django.conf import settings
from django.core.management.base import NoArgsCommand

from ...models import Snowflake
from ...utils import process

logger = logging.getLogger('neigefr')


# https://twitter.com/#!/search/%40twitterapi
class Command(NoArgsCommand):
    help = "Is searching for tweets with #neigefr and store them in DB"

    def handle(self, **options):
        for country in settings.COUNTRY_CODES:
            url = 'http://search.twitter.com/search.json'
            payload = {
               'q': '%23neige{0}'.format(country.lower()),
            }

            last_snowflakes = Snowflake.objects.filter(
                zipcode__country=country.upper()
            ).order_by('-tweet_id')
            if last_snowflakes:
                last = last_snowflakes[0]
                payload['since_id'] = last.tweet_id

            response = requests.get(url, params=payload)
            for tweet in response.json['results']:
                process(tweet)
