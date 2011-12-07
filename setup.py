from setuptools import setup, find_packages

version = __import__('mailchimp').__version__

setup(
    name = 'django-mailchimp',
    version = version,
    description = 'Mailchimp wrapper for Django',
    author = 'Jonas Obrist et al.',
    url = 'http://github.com/piquadrat/django-mailchimp',
    packages = find_packages(),
    zip_safe=False,
    package_data={
        'mailchimp': [
            'templates/mailchimp/*.html',
            'locale/en/LC_MESSAGES/django.po',
            'locale/en/LC_MESSAGES/django.mo',
            'locale/de/LC_MESSAGES/django.po',
            'locale/de/LC_MESSAGES/django.mo',
        ],
    },
)
