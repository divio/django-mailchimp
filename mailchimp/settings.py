from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

API_KEY = getattr(settings, 'MAILCHIMP_API_KEY', None)
if API_KEY is None:
    raise ImproperlyConfigured('django-mailchimp requires the MAILCHIMP_API_KEY setting')

SECURE = getattr(settings, 'MAILCHIMP_SECURE', True)

WEBHOOK_KEY = getattr(settings, 'MAILCHIMP_WEBHOOK_KEY', None)
if WEBHOOK_KEY is None:
    raise ImproperlyConfigured('django-mailchimp requires the WEBHOOK_KEY setting')

VIEWS_OVERVIEW = getattr(settings, 'MAILCHIMP_VIEWS_OVERVIEW', 'mailchimp.views.overview')
VIEWS_SEND = getattr(settings, 'MAILCHIMP_VIEWS_SEND', 'mailchimp.views.send_campaign')
VIEWS_INFO = getattr(settings, 'MAILCHIMP_VIEWS_INFO', 'mailchimp.views.campaign_information')
VIEWS_SCHEDULE_OBJECT = getattr(settings, 'MAILCHIMP_VIEWS_SEND_OBJECT', 'mailchimp.views.schedule_campaign_for_object')