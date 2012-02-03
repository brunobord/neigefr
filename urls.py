from django.conf.urls.defaults import patterns, url
from neigefr.views import IndexView

urlpatterns = patterns('',
    url(r'', IndexView.as_view()),
)
