from django.conf.urls.defaults import *
from mailchimp.settings import VIEWS_SEND, VIEWS_INFO, VIEWS_OVERVIEW, VIEWS_SCHEDULE_OBJECT
from mailchimp.views import webhook

urlpatterns = patterns('',
    url(r'^$', VIEWS_OVERVIEW, name='mailchimp_overview', kwargs={'page':'1'}),
    url(r'^(?P<page>\d+)/$', VIEWS_OVERVIEW, name='mailchimp_overview'),
    url(r'^send/$', VIEWS_SEND, name='mailchimp_send_campaign'),
    url(r'^send/(?P<content_type>\d+)/(?P<pk>\d+)/$', VIEWS_SCHEDULE_OBJECT, name='mailchimp_schedule_for_object'),
    url(r'^info/(?P<campaign_id>\w+)/$', VIEWS_INFO, name='mailchimp_campaign_info'),
    url(r'^webhook/(?P<key>\w+)/', webhook, name='mailchimp_webhook'),
)
