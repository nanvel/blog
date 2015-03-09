Project documentation with Sphinx
=================================

.. image:: https://raw.githubusercontent.com/nanvel/blog/master/2013/02/sphinx.png
    :width: 166px
    :alt: Sphinx - Python Documentation Generator
    :align: left

`Sphinx <http://en.wikipedia.org/wiki/Sphinx_%28documentation_generator%29>`__ - Python Documentation Generator.

Step 1: install Sphinx
----------------------

.. code-block:: bash

    $ pip install Sphinx

Step 2: create folder in which documentation will be stored
-----------------------------------------------------------

.. code-block:: bash

    $ mkdir docs
    $ cd docs

Step 3: initialize docs folder
------------------------------

.. code-block:: bash

    $ sphinx-quickstart
    # answer to several questions
    # enter 'y' for 'Separate source and build directories'

Add to .gitignore:

.. code-block:: bash

    docs/build

Step 4: modify Makefile, add target to run simple http server
-------------------------------------------------------------

Add to Makefile:

.. code-block:: makefile

    serve:
    	make html && cd build/html/ && python -m SimpleHTTPServer 8001

Check that all works fine:

.. code-block:: bash

    $ make serve
    # Open http://127.0.0.1:8001 in browser.

Step 5: edit source files
-------------------------

index.rst

.. code-block:: rst

    .. myproject documentation master file

    Welcome to myproject's documentation!
    =====================================

    Contents:

    .. toctree::
       :maxdepth: 2

        init.rst
        usage.rst

init.rst

.. code-block:: rst

    .. myproject init

    Init
    ====

    - ``virtualen .env --no-site-packages``
    - ``source .env/bin/activate``
    - ``pip install -r requirements.txt``
    - ``cp settings_local.py.default settings_local.py``
    - ``make syncdb``
    - ``make run``

usage.rst

.. code-block:: rst

    .. myproject usage

    Usage
    =====

    Some usage info.

    .. code-block:: bash

    make run

    `Simple link <http://sphinx-doc.org>`__

Try autodoc extension:

.. code-block:: rst

    .. automodule:: io
       :members:

If You use django, add next lines to conf.py:

.. code-block:: python

    sys.path.insert(0, os.path.relpath('../../../myapp'))
    os.environ['DJANGO_SETTINGS_MODULE'] = 'myapp.settings'

Links:
    - `http://sphinx-doc.org <http://sphinx-doc.org>`__

.. info::
    :tags: Documentation, Sphinx
    :place: Starobilsk, Ukraine
