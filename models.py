import datetime
from django.db import models
from django.utils import simplejson as json


class Zipcode(models.Model):
    "France-based Zipcode"
    zipcode = models.CharField("zipcode", max_length=10, db_index=True)
    city = models.CharField('city', max_length=255, blank=True)
    latitude = models.CharField('latitude', max_length=100)
    longitude = models.CharField('longitude', max_length=100)

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
    date_created = models.DateTimeField('date created', default=datetime.datetime.now, db_index=True)

    class Meta:
        verbose_name = 'flake'
        verbose_name_plural = 'flakes'

    @property
    def tweet_object(self):
        "Load the tweet full object, for eventual further analysis"
        return json.loads(self.tweet)

    @property
    def flakesize(self):
        "Return the snowflake size in pixels."
        rank = self.rank
        if self.rank > 10:
            rank = 10
        sizes = {
            0: 0, 1: 6, 2: 8, 3: 8, 4: 12, 5: 16, 6: 16, 7: 24, 8: 24, 9: 32,
            10: 32
        }
        return sizes.get(rank, 8)
