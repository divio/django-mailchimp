from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from mailchimp.exceptions import MailchimpWarning
import warnings

API_KEY = getattr(settings, 'MAILCHIMP_API_KEY', None)
if API_KEY is None:
    raise ImproperlyConfigured('django-mailchimp requires the MAILCHIMP_API_KEY setting')

SECURE = getattr(settings, 'MAILCHIMP_SECURE', True)

# THIS DOES NOT WORK:
#REAL_CACHE = bool(getattr(settings, 'MAILCHIMP_USE_REAL_CACHE', False))
"""
In [1]: from mailchimp.utils import get_connection

In [2]: c = get_connection ()

In [3]: c.campaigns
key lists <type 'str'>
value {'f48ceea763': <List object: Affichage List>, 'a41f00cba2': <List object: API Test List>} <type 'dict'>
key lists <type 'str'>
value {'f48ceea763': <List object: Affichage List>, 'a41f00cba2': <List object: API Test List>} <type 'dict'>
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/jonas/workspace/affichage/<ipython console> in <module>()

/home/jonas/workspace/django-mailchimp/mailchimp/chimp.pyc in campaigns(self)
    354     @property
    355     def campaigns(self):
--> 356         return self.get_campaigns()
    357 
    358     def get_campaigns(self):

/home/jonas/workspace/django-mailchimp/mailchimp/chimp.pyc in get_campaigns(self)
    357 
    358     def get_campaigns(self):
--> 359         return self.cache.get('campaigns', self._get_categories)
    360 
    361     @property

/home/jonas/workspace/django-mailchimp/mailchimp/utils.py in get(self, key, obj, *args, **kwargs)
     37         value = self._get(key)
     38         if value is None:
---> 39             value = obj(*args, **kwargs) if callable(obj) else obj
     40             self._set(key, value)
     41         return value

/home/jonas/workspace/django-mailchimp/mailchimp/chimp.pyc in _get_categories(self)
    374 
    375     def _get_categories(self):
--> 376         return build_dict(self, Campaign, self.con.campaigns())
    377 
    378     def _get_lists(self):

/home/jonas/workspace/django-mailchimp/mailchimp/utils.py in build_dict(master, klass, data, key)
     87 
     88 def build_dict(master, klass, data, key='id'):
---> 89     return  dict([(info[key], klass(master, info)) for info in data])
     90 
     91 def _convert(name):

/home/jonas/workspace/django-mailchimp/mailchimp/chimp.pyc in __init__(self, master, info)
     92     def __init__(self, master, info):
     93         super(Campaign, self).__init__(master, info)
---> 94         self.list = self.master.get_list_by_id(self.list_id)
     95         self._content = None
     96         self.frozen_info = info

/home/jonas/workspace/django-mailchimp/mailchimp/chimp.pyc in get_list_by_id(self, id)
    383 
    384     def get_list_by_id(self, id):
--> 385         return self._get_by_id('lists', id)
    386 
    387     def get_campaign_by_id(self, id):

/home/jonas/workspace/django-mailchimp/mailchimp/chimp.pyc in _get_by_id(self, thing, id)
    396     def _get_by_id(self, thing, id):
    397         try:
--> 398             return getattr(self, thing)[id]
    399         except KeyError:
    400             self.cache.flush(thing)

/home/jonas/workspace/django-mailchimp/mailchimp/chimp.pyc in lists(self)
    361     @property
    362     def lists(self):
--> 363         return self.get_lists()
    364 
    365     def get_lists(self):

/home/jonas/workspace/django-mailchimp/mailchimp/chimp.pyc in get_lists(self)
    364 
    365     def get_lists(self):
--> 366         return self.cache.get('lists', self._get_lists)
    367 
    368     @property

/home/jonas/workspace/django-mailchimp/mailchimp/utils.py in get(self, key, obj, *args, **kwargs)
     38         if value is None:
     39             value = obj(*args, **kwargs) if callable(obj) else obj
---> 40             self._set(key, value)
     41         return value
     42 

/home/jonas/workspace/django-mailchimp/mailchimp/utils.py in _real_set(self, key, value)
     44         print 'key', key, type(key)
     45         print 'value', value, type(value)
---> 46         cache.set(key, value, CACHE_TIMEOUT)
     47 
     48     def _real_get(self, key):

/home/jonas/workspace/affichage/parts/django/django/core/cache/backends/locmem.pyc in set(self, key, value, timeout)
     81         try:
     82             try:
---> 83                 self._set(key, pickle.dumps(value), timeout)
     84             except pickle.PickleError:
     85                 pass

/usr/lib/python2.6/copy_reg.pyc in _reduce_ex(self, proto)
     68     else:
     69         if base is self.__class__:
---> 70             raise TypeError, "can't pickle %s objects" % base.__name__
     71         state = base(self)
     72     args = (self.__class__, base, state)

TypeError: can't pickle instancemethod objects

"""
REAL_CACHE = False
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
VIEWS_TEST_OBJECT = getattr(settings, 'MAILCHIMP_VIEWS_TEST_OBJECT', 'mailchimp.views.test_campaign_for_object')