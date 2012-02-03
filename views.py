# from django.views.generic import TemplateView
from django.views.generic import ListView
from neigefr.models import Snowflake
from django.conf import settings


class IndexView(ListView):
    template_name = "index.html"
    queryset = Snowflake.objects.exclude(rank=0)[:100]

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(IndexView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['GOOGLE_MAPS_KEY'] = settings.GOOGLE_MAPS_KEY
        return context
