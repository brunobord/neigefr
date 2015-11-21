import datetime

from django.conf import settings
from django.views.generic import ListView
from django.utils import timezone

from .models import Snowflake


class FlakeMixin(object):
    def get_queryset(self):
        datetime_limit = timezone.now() - datetime.timedelta(hours=4)
        queryset = Snowflake.objects.exclude(
            date_created__lt=datetime_limit)[:100]
        return queryset


class IndexView(FlakeMixin, ListView):
    "Home page"
    template_name = 'flakes/index.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(IndexView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['GOOGLE_MAPS_KEY'] = settings.GOOGLE_MAPS_KEY
        return context
index = IndexView.as_view()
