import datetime
from django.views.generic import ListView
from django.conf import settings
from neigefr.models import Snowflake


class IndexView(ListView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(IndexView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['GOOGLE_MAPS_KEY'] = settings.GOOGLE_MAPS_KEY
        return context

    def get_queryset(self):
        datetime_limit = datetime.datetime.now() - datetime.timedelta(hours=1)
        queryset = Snowflake.objects.exclude(date_created__lt=datetime_limit).exclude(rank=0)[:100]
        return queryset
