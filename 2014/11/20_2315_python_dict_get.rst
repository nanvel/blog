Python dict.get()
=================

I am amazed how I done this mistake for 2 days in a row.

.. code-block:: python

    >>> isinstance(a, dict)
    True
    >>> a.get('a', '')[:100]
    '1'

I thought it always returns a string ...

.. code-block:: python

    >>> a.get('b', '')[:100]
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: 'NoneType' object has no attribute '__getitem__'

The dict is:

.. code-block::

    a = {'a': 1, 'b': None}

The proper way is:

.. code-block::

    >>> (a.get('b') or '')[:100]
    ''

.. info::
    :tags: Python
    :place: Kyiv, Ukraine
