import time
from datetime import datetime
from django.db import models
from django.utils import simplejson as json
from django.utils import timezone

from django_countries import CountryField


class Zipcode(models.Model):
    "France-based Zipcode"
    zipcode = models.CharField("zipcode", max_length=10, db_index=True)
    city = models.CharField('city', max_length=255, blank=True)
    country = CountryField(default='FR')
    latitude = models.CharField('latitude', max_length=100)
    longitude = models.CharField('longitude', max_length=100)

    class Meta:
        app_label = 'neigefr'
        db_table = 'neigefr_zipcode'

    def __unicode__(self):
        return self.city or self.zipcode


class Snowflake(models.Model):
    "A tweet equals a snowflake."
    tweet_id = models.BigIntegerField('tweet ID', unique=True, db_index=True)
    tweet = models.TextField("raw tweet")
    latitude = models.CharField('latitude', max_length=100)
    longitude = models.CharField('longitude', max_length=100)
    rank = models.IntegerField('rank', blank=True, null=True)
    zipcode = models.ForeignKey(Zipcode, blank=True)
    date_created = models.DateTimeField('date created', default=timezone.now, db_index=True)

    class Meta:
        app_label = 'neigefr'
        db_table = 'neigefr_snowflake'
        verbose_name = 'flake'
        verbose_name_plural = 'flakes'

    @property
    def tweet_object(self):
        "Load the tweet full object, for eventual further analysis"
        return json.loads(self.tweet)

    @property
    def tweet_time(self):
        "Return the time property of the tweet"
        try:
            time_struct = time.strptime(self.tweet_object['created_at'],
                                        "%a, %d %b %Y %H:%M:%S +0000")
            date_datetime = datetime.fromtimestamp(time.mktime(time_struct))
            return date_datetime.strftime("%H:%M")
        except:
            time_struct = time.strptime(self.tweet_object['created_at'],
                                        "%a %b %d %H:%M:%S +0000 %Y")
            date_datetime = datetime.fromtimestamp(time.mktime(time_struct))
            return date_datetime.strftime("%H:%M")

    @property
    def flakesize(self):
        "Return the snowflake size in pixels."
        rank = self.rank
        if self.rank > 10:
            rank = 10
        sizes = {
            0: 16, 1: 16, 2: 20, 3: 20, 4: 24, 5: 24, 6: 28, 7: 28, 8: 32, 9: 32,
            10: 32
        }
        return sizes.get(rank, 16)
