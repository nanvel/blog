
Django startproject template
============================

Django project template I use:

.. code-block:: text

    .
    ├── myproject
    │   ├── apps
    │   │   ├── core
    │   │   │   ├── __init__.py
    │   │   │   ├── models.py
    │   │   │   ├── tests.py
    │   │   │   └── views.py
    │   │   ├── myapp
    │   │   │   ├── __init__.py
    │   │   │   ├── models.py
    │   │   │   ├── tests.py
    │   │   │   └── views.py
    │   │   └── __init__.py
    │   ├── settings
    │   │   ├── __init__.py
    │   │   ├── admins.py
    │   │   ├── apps.py
    │   │   ├── db.py
    │   │   ├── default.py
    │   │   ├── local.py
    │   │   ├── logs.py
    │   │   └── media.py
    │   ├── static
    │   │   ├── css
    │   │   ├── img
    │   │   └── js
    │   ├── templates
    │   │   ├── base.html
    │   │   ├── core
    │   │   └── myapp
    │   ├── __init__.py
    │   ├── urls.py
    │   └── wsgi.py
    ├── .gitignore
    ├── Makefile
    ├── manage.py
    └── requirements.txt

It's tiring to change standard django project structure everytime when start new project, so I created my own project template:

https://github.com/nanvel/django-project-template

Apply it:

.. code-block:: bash

    django-admin.py startproject --template https://github.com/nanvel/django-project-template/archive/master.zip myproject

Differences from standard project template are:
    - splitted settings
    - apps directory
    - Makefile
    - default base.html, templates directory
    - default configurations for database and media paths
    - error pages
    - south included by default
    - requirements.txt

.. info::
    :tags: Django
    :place: Starobilsk, Ukraine
