from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from mailchimp.exceptions import MailchimpWarning
import warnings

API_KEY = getattr(settings, 'MAILCHIMP_API_KEY', None)
if API_KEY is None:
    raise ImproperlyConfigured('django-mailchimp requires the MAILCHIMP_API_KEY setting')

SECURE = getattr(settings, 'MAILCHIMP_SECURE', True)

REAL_CACHE = bool(getattr(settings, 'MAILCHIMP_USE_REAL_CACHE', False))
CACHE_TIMEOUT = getattr(settings, 'MAILCHIMP_CACHE_TIMEOUT', 300)

WEBHOOK_KEY = getattr(settings, 'MAILCHIMP_WEBHOOK_KEY', '')
if not WEBHOOK_KEY:
    warnings.warn("you did not define a MAILCHIMP_WEBHOOK_KEY setting. "
        "django-mailchimp will create a random one by itself", MailchimpWarning)
    import string
    import random
    alphanum = string.ascii_letters + string.digits
    for x in range(50):
        WEBHOOK_KEY += random.choice(alphanum)

VIEWS_OVERVIEW = getattr(settings, 'MAILCHIMP_VIEWS_OVERVIEW', 'mailchimp.views.overview')
VIEWS_INFO = getattr(settings, 'MAILCHIMP_VIEWS_INFO', 'mailchimp.views.campaign_information')
VIEWS_SCHEDULE_OBJECT = getattr(settings, 'MAILCHIMP_VIEWS_SEND_OBJECT', 'mailchimp.views.schedule_campaign_for_object')