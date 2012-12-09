# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, url, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import TemplateView

urlpatterns = patterns('',
    url(r'^faq/?$', TemplateView.as_view(template_name='faq.html'), name='faq'),
    url(r'^', include('neigefr.flakes.urls')),
)

urlpatterns += staticfiles_urlpatterns()
