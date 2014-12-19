from django.conf.urls import patterns, url
from surveyer.views import *


urlpatterns = patterns('',
    # Examples:
    url(r'^$', surveys_list, name='surveys'),
    url(r'^(?P<survey_id>\d+)/$', survey_details),
    url(r'^edit/(?P<survey_id>\d+)/$', survey_edit, name='survey-edit'),

)
