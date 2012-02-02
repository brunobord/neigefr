import logging
import requests
from django.core.management.base import NoArgsCommand
from neigefr.flake import process
from neigefr.models import Zipcode, Snowflake

logger = logging.getLogger(__name__)

# https://twitter.com/#!/search/%40twitterapi

class Command(NoArgsCommand):
    help = "Is searching for tweets with #neigefr and store them in DB"

    def handle(self, **options):
        url = 'http://search.twitter.com/search.json?q=%23neigefr'

        last_snowflakes = Snowflake.objects.order_by('-twitter_id')
        if last_snowflakes.count():
            last = last_snowflakes[0]
            url = "%s&since_id=%d" % (url, last.twitter_id)
        data = requests.get(url)
        print data.text
