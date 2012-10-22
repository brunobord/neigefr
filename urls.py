from django.conf.urls.defaults import patterns, url
from django.views.generic import TemplateView
from neigefr.views import IndexView, TextView

urlpatterns = patterns('',
    url(r'^faq/?$', TemplateView.as_view(template_name="faq.html"), name='faq'),
    url(r'^text/?$', TextView.as_view(), name='textfile'),
    url(r'', IndexView.as_view(), name='index'),
)
