from django.contrib import admin
from neigefr.models import Zipcode, Snowflake


class ZipcodeAdmin(admin.ModelAdmin):
    pass


class SnowflakeAdmin(admin.ModelAdmin):
    pass

admin.site.register(Zipcode, ZipcodeAdmin)
admin.site.register(Snowflake, SnowflakeAdmin)
