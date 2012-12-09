from django.contrib import admin
from neigefr.models import Zipcode, Snowflake


class ZipcodeAdmin(admin.ModelAdmin):
    list_display = ('city', 'longitude', 'latitude')


class SnowflakeAdmin(admin.ModelAdmin):
    list_display = ('pk', 'tweet_id', 'zipcode', 'rank')

admin.site.register(Zipcode, ZipcodeAdmin)
admin.site.register(Snowflake, SnowflakeAdmin)
