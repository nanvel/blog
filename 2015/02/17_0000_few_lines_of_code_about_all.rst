Few lines of code about `__all__`
=================================

::

    dates/
        - __init__.py
        - tomorrow.py
        - tomorrow_all.py

tomorrow.py:

.. code-block:: python

    import datetime


    def tomorrow():
        return (datetime.datetime.now() + datetime.timedelta(days=1)).date()

tomorrow_all.py:

.. code-block:: python

    import datetime


    __all__ = ['tomorrow']


    def tomorrow():
        return (datetime.datetime.now() + datetime.timedelta(days=1)).date()

1. Without `__all__`

`__init__.py`:

.. code-block:: python

    from .tomorrow import *

::

    >>> from dates import tomorrow
    >>> tomorrow()
    datetime.date(2015, 2, 18)
    >>> from dates import datetime
    >>> datetime
    <module 'datetime' from '/Users/nanvel/myprojects/tests/all_test/.env/lib/python2.7/lib-dynload/datetime.so'>

2. With `__all__`

`__init__.py`:

.. code-block:: python

    from .tomorrow_all import *

::

    >>> from dates import tomorrow
    >>> tomorrow()
    datetime.date(2015, 2, 18)
    >>> from dates import datetime
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    ImportError: cannot import name datetime

3. `__all__` is not required

`__init__.py`:

.. code-block:: python

    from .tomorrow import tomorrow

::

    >>> from dates import tomorrow
    >>> tomorrow()
    datetime.date(2015, 2, 18)
    >>> from dates import datetime
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    ImportError: cannot import name datetime

.. info::
    :tags: Python
    :place: Phuket, Thailand
