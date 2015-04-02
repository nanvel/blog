[Django] Database transactions
==============================

Today I found that Django database transactions feature may be very useful in some applications:
    - change/add many records in one place of code
    - skip changes on exception
    - add all records or nothing - atomic behavior

Example:

.. code-block:: python

    # this code produces 100 requests to database
    from .models import MyModel

    def my_view(request):
        for i in range(100):
            m = MyModel(number=i)
            m.save()

.. code-block:: python

    # this code produces only 1 request to database
    from django.db import transaction

    from .models import MyModel

    @transaction.commit_on_success
    def my_view(request):
        for i in range(100):
            m = MyModel(number=i)
            m.save()

.. code-block:: python

    # this will add only one record to database
    from .models import MyModel

    def my_view(request):
        for i in range(100):
            m = MyModel(number=i)
            m.save()
            raise Exception('Some error')

.. code-block:: python

    # this will add no records to database
    from django.db import transaction

    from .models import MyModel

    @transaction.commit_on_success
    def my_view(request):
        for i in range(100):
            m = MyModel(number=i)
            m.save()
            raise Exception('Some error')

See more examples in `documentation <https://docs.djangoproject.com/en/1.5/topics/db/transactions/>`__.

My fail: It appears that MySQL MyISAM does not support transcations (or, maybe this feature should be enable somehow, anyway, seems like InnoDB is a better choice).

If You use MySQL, enable InnoDB:

.. code-block:: python

    DATABASES = {
        'default': {
        'ENGINE': 'django.db.backends.mysql',
            ...
            'OPTIONS': {
                'init_command': 'SET storage_engine=INNODB',
            },
        }
    }

Links:
    - https://docs.djangoproject.com/en/1.5/topics/db/transactions/

.. info::
    :tags: Django, Database
    :place: Starobilsk, Ukraine
