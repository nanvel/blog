[Django] Where to store host specific variables
===============================================

1. ``settings/local.py``
------------------------

.. code-block:: text

    myproject/
        - settings/
            - __init__.py
            - default.py
            - local.py

``__init__.py``:

.. code-block:: python

    from .default import *


    try:
        from .local import *
    except ImportError:
        import logging
        logger = logging.get_logger(__name__)
        logger.error('settings/local.py was not found!')

``local.py`` shouldn't be under git index.

Useful practice to add few patterns of local.py for different hosts:
    - ``settings/local.py.development``
    - ``settings/local.py.staging``
    - ``settings/local.py.production``

Keep in mind, don't store sensitive information in files under git index.

2. ``~/.bashrc``
----------------

Unix shell, when starting, reads .bashrc file and executes commands it contains.
First, reads file ``/etc/.bashrc`` and next - ``~/.bashrc``.

My .bashrc on dev laptop looks like:

.. code-block:: bash

    export VIRTUALENV_DISTRIBUTE=true
    export PIP_REQUIRE_VIRTUALENV=true
    export PIP_DOWNLOAD_CACHE=$HOME/.pip/cache
    export SOME_VAR=someval

To make ``SOME_VAR`` available in ``django.conf.settings``:

.. code-block:: python

    # settings.py
    from sys import environ

    ...

    SOME_VAR = getattr(environ, 'SOME_VAR', <default value>)

.. info::
    :tags: Django
    :place: Kyiv, Ukraine
