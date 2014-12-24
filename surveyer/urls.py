from django.conf.urls import patterns, url
from surveyer.views import *


urlpatterns = patterns('',
    # Examples:
    url(r'^$', SurveysList.as_view(), name='surveys'),
    url(r'^(?P<pk>\d+)/$', SurveyDetail.as_view(), name='survey-details'),
    url(r'^edit/(?P<pk>\d+)/$', SurveyUpdate.as_view(), name='survey-edit'),
    url(r'^add/$', SurveyAdd.as_view(), name='survey-add'),
    url(r'^delete/(?P<pk>\d+)/$', SurveyDelete.as_view(), name='survey-delete'),

)
