from django.conf.urls import patterns, url
from records.views import *


urlpatterns = patterns('',
    # Examples:
    url(r'^$', records_list, name='records'),
    url(r'^(?P<record_id>\d+)/$', record_details, name='record-details'),
    url(r'^edit/(?P<record_id>\d+)/$', record_edit, name='record-edit'),
    url(r'^add/$', record_edit, name='record-add'),
    url(r'^delete/(?P<pk>\d+)/$', record_delete, name='record-delete'),

)
