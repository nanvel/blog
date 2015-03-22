django-ga-mail reusable app
===========================

.. image:: https://raw.githubusercontent.com/nanvel/blog/master/2013/08/ga_letter.png
    :width: 302px
    :alt: Analytics letter
    :align: left

Today I published django-ga-mail app on pypi. This app just sends analytics to my email box few times a week, so I don't need to open Google Analytics site to view analytics.

GitHub: https://github.com/nanvel/django-ga-mail

PyPI: https://pypi.python.org/pypi/django-ga-mail/0.2.1

Installation is quite simple.

.. code-block:: bash

    $ pip install django-ga-mail

Add ga_mail to your INSTALLED_APPS:

.. code-block:: python

    INSTALLED_APPS = (
        ...,
        'ga_mail',
    )

Set next variables in settings:

.. code-block:: python

    GA_PROFILE_ID = 12345678
    GA_USERNAME = 'some.user@gmail.com'
    # don't use your working account here,
    # create another one for analytics and give it access to ga profile
    GA_PASSWORD = 'somepass'
    GA_SOURCE_APP_NAME = 'some.site',
    ANALYTICS_BLOCKS = (
        'new_visitors_30days_today',
        'new_visitors_7days_today_vs_14days_7days',
        'pageviews_7days_today')

Check that ``MANAGERS`` variable contains necessary emails.

Available blocks:
    - ``returning_visitors_7days_today``
    - ``new_visitors_7days_today``
    - ``new_visitors_30days_today``
    - ``new_visitors_7days_today_vs_14days_7days``
    - ``new_visitors_7days_today_vs_returning_visitors_7days_today``
    - ``pageviews_7days_today``
    - ``countries_30days_today``

Call ``python manage.py ga_mail`` to send analytics report.

I added next line to /etc/crontab to send analytics one time a week:

.. code-block:: text

    22 5    * * 2   deploy  cd /home/deploy/envs/mysite/ && .env/bin/python manage.py ga_mail

*UPD 2013.08.27*

Updated letter templates. Added ``countries_30days_today`` block.

.. info::
    :tags: Google analytics, Django
    :place: Starobilsk, Ukraine
