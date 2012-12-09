import json
import logging
import requests

from django.core.management.base import NoArgsCommand

from ...models import Snowflake
from ...utils import process

logger = logging.getLogger('neigefr')


# https://twitter.com/#!/search/%40twitterapi
class Command(NoArgsCommand):
    help = "Is searching for tweets with #neigefr and store them in DB"

    def handle(self, **options):
        url = 'http://search.twitter.com/search.json?q=%23neigefr'
        last_snowflakes = Snowflake.objects.order_by('-tweet_id')
        if last_snowflakes:
            last = last_snowflakes[0]
            url = "%s&since_id=%d" % (url, last.tweet_id)
        data = requests.get(url)
        json_data = json.loads(data.text)
        for tweet in json_data['results']:
            process(tweet)
