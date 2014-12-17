from django.conf.urls import patterns, url
from records.views import *


urlpatterns = patterns('',
    # Examples:
    url(r'^$', records_list, name='records'),
    url(r'^(?P<record_id>\d+)/$', record_details),

)
