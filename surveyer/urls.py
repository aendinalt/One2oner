from django.conf.urls import patterns, url
from surveyer.views import *


urlpatterns = patterns('',
    # Examples:
    url(r'^$', surveys_list),
    url(r'^(?P<survey_id>\d+)/$', survey_details),

)
