from django.conf.urls import patterns, include, url
from django.contrib import admin
from views import *

urlpatterns = patterns('',
    # Examples:
    url(r'^$', DashboardView.as_view()),
    url(r'^surveys/', include('surveyer.urls')),
    url(r'^records/', include('records.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
