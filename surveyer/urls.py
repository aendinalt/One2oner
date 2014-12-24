from django.conf.urls import patterns, url
from surveyer.views import *


urlpatterns = patterns('',
    # Examples:
    url(r'^$', SurveysList.as_view(), name='surveys'),
    url(r'^(?P<pk>\d+)/$', SurveyDetail.as_view(), name='survey-details'),
    url(r'^edit/(?P<pk>\d+)/$', survey_edit, name='survey-edit'),
    url(r'^add/$', survey_add, name='survey-add'),

)
