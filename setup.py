from setuptools import setup, find_packages

version = __import__('mailchimp').__version__

setup(
    name = 'django-mailchimp',
    version = version,
    description = 'Mailchimp wrapper for Django',
    author = 'Jonas Obrist',
    url = 'http://github.com/ojii/django-mailchimp',
    packages = find_packages(),
    zip_safe=False,
    package_data={
        'mailchimp': [
            'templates/mailchimp/*.html',
        ],
    },
)