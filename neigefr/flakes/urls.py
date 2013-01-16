# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, url

from . import views

urlpatterns = patterns('',
    url(r'^text/?$', views.flake_list, name='flake_list'),
    url(r'', views.index, name='index'),
)
