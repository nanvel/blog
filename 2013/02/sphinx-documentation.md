labels: Blog
        Documentation
created: 2013-02-23T00:00
place: Starobilsk, Ukraine

# Project documentation with Sphinx

![Sphinx - Python Documentation Generator](sphinx.png)

[Sphinx](http://en.wikipedia.org/wiki/Sphinx_%28documentation_generator%29) - Python Documentation Generator.

[TOC]

## Step 1: install Sphinx

```bash
$ pip install Sphinx
```

## Step 2: create folder in which documentation will be stored

```bash
$ mkdir docs
$ cd docs
```

## Step 3: initialize docs folder

```bash
$ sphinx-quickstart
# answer to several questions
# enter 'y' for 'Separate source and build directories'
```

Add to ```.gitignore```:
```bash
docs/build
```

## Step 4: modify ```Makefile```, add target to run simple http server

Add to ```Makefile```:
```makefile
serve:
	make html && cd build/html/ && python -m SimpleHTTPServer 8001
```

Check that all works fine:
```bash
$ make serve
# Open http://127.0.0.1:8001 in browser.
```

## Step 5: edit source files

```index.rst```:
```rst
.. myproject documentation master file

Welcome to myproject's documentation!
=====================================

Contents:

.. toctree::
    :maxdepth: 2

    init.rst
    usage.rst
```

```init.rst```:
```rst
.. myproject init

Init
====

- ``virtualen .env --no-site-packages``
- ``source .env/bin/activate``
- ``pip install -r requirements.txt``
- ``cp settings_local.py.default settings_local.py``
- ``make syncdb``
- ``make run``
```

```usage.rst```:
```rst
.. myproject usage

Usage
=====

Some usage info.

.. code-block:: bash

make run

`Simple link <http://sphinx-doc.org>`__
```

Try autodoc extension:
```rst
.. automodule:: io
   :members:
```

If You use django, add next lines to ```conf.py```:
```python
sys.path.insert(0, os.path.relpath('../../../myapp'))
os.environ['DJANGO_SETTINGS_MODULE'] = 'myapp.settings'
```

Links:

- [http://sphinx-doc.org](http://sphinx-doc.org)
