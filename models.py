import datetime
from django.db import models


class Zipcode(models.Model):
    zipcode = models.CharField("zipcode", max_length=10, db_index=True)
    city = models.CharField('city', max_length=255, blank=True)
    latitude = models.CharField('latitude', max_length=100)
    longitude = models.CharField('longitude', max_length=100)

    def __unicode__(self):
        return self.city or self.zipcode


class Snowflake(models.Model):
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
