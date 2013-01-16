# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, url, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import TemplateView
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

    url(r'^faq/?$', TemplateView.as_view(template_name='faq.html'), name='faq'),
    url(r'^', include('neigefr.flakes.urls')),
)

urlpatterns += staticfiles_urlpatterns()
