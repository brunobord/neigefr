from django.conf.urls.defaults import patterns, url
from django.views.generic import TemplateView
from neigefr.views import IndexView

urlpatterns = patterns('',
    url(r'faq/', TemplateView.as_view(template_name="faq.html"), name='faq'),
    url(r'', IndexView.as_view(), name='index'),
)
