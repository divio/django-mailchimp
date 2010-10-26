================
Django Mailchimp
================

This is an integrated app for Django dealing with the Mailchimp mailing list system.

Getting started:
----------------

* Install django_mailchimp:

    pip install django_mailchimp
    
* Add an ``MAILCHIMP_API_KEY`` to your settings.py with your mailchimp API key as the value (obviously)
    
* Add ``mailchimp`` to your project's list of INSTALLED_APPS

* To start using the API, you should start by using utils.get_connection(). This will use the API_KEY you
just defined in settings.py


Subscribing a user to a list:
-----------------------------

* To get the list: 

	list = mailchimp.utils.get_connection().get_list_by_id(<list key id>)

* Now add a member to the mailing list: 

	list.subscribe('example@example.com',{})
