from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'one2oner.views.dashboard'),
    url(r'^surveys/', include('surveyer.urls')),
    url(r'^records/', include('records.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
