NicEdit widget for Django
=========================

.. image:: https://raw.githubusercontent.com/nanvel/blog/master/2013/08/django_nicedit.png
    :width: 665px
    :alt: django-nicedit widget on admin page
    :align: left

NicEdit widget for django with image upload feature.

NicEdit home: `http://nicedit.com/ <http://nicedit.com/>`__

django-nicedit on PyPI: `https://pypi.python.org/pypi/django-nicedit/ <https://pypi.python.org/pypi/django-nicedit/>`__

django-nicedit on GitHub: `https://github.com/nanvel/django-nicedit <https://github.com/nanvel/django-nicedit>`__

Installation
------------

To get the latest stable release from PyPi:

.. code-block:: bash

    pip install django-nicedit

To get the latest commit from GitHub:

.. code-block:: bash

    pip install -e git+git://github.com/nanvel/django-nicedit.git#egg=nicedit

Add nicedit to INSTALLED_APPS

.. code-block:: python

    INSTALLED_APPS = (
        ...,
        'south',
        'nicedit',
    )

Add nicedit URLs to urls.py:

.. code-block:: python

    urlpatterns = patterns('',
        ...
        url(r'^nicedit/', include('nicedit.urls')),
    )

Migrate database:

.. code-block:: bash

    python manage.py migrate nicedit

MEDIA_ROOT should be specified, example:

.. code-block:: python

    MEDIA_ROOT = os.path.join(os.path.dirname('__file__'), '../media')
    MEDIA_URL = '/media/'

Add to urls configuration:

.. code-block:: python

    from django.conf.urls.static import static
    from django.conf import settings

    if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

Usage
-----

forms.py:

.. code-block:: python

    from django import forms

    from nicedit.widgets import NicEditWidget


    class MessageForm(forms.Form):
        message = forms.CharField(
            widget=NicEditWidget(attrs={'style': 'width: 800px;'}))

views.py:

.. code-block:: python

    from django.shortcuts import render

    from .forms import MessageForm


    def home(request):
        form = MessageForm()
        return render(request, 'home.html', {'form': form})

template:

.. code-block:: django

    <!DOCTYPE html>
    <html lang="en">
        <head>
            <meta charset="utf-8">
            <title>NicEdit widget</title>
            {{ form.media }}
        </head>
        <body>
            <form action='.' method='post'>
                {% csrf_token %}
                {{ form.message }}
                <button type="submit">Submit</button>
            </form>
        </body>
    </html>

Usage in admin:

.. code-block:: python

    # -*- coding: utf-8 -*-
    from django import forms
    from django.contrib import admin

    from nicedit.widgets import NicEditAdminWidget

    from .models import Item

    class ItemAdminForm(forms.ModelForm):

        class Meta:
            model = Item
            widgets = {
                'text': NicEditAdminWidget(
                    attrs={'style': 'width: 610px;'},
                    js_options={"buttonList": [
                        'save', 'bold', 'italic', 'underline', 'left', 'center',
                        'right', 'justify', 'ol', 'ul', 'fontSize',  # 'fontFamily',
                        'fontFormat', 'indent', 'outdent', 'image', 'upload', 'link',
                        'unlink', 'forecolor', 'bgcolor', 'xhtml']}
                ),
            }


    class ItemAdmin(admin.ModelAdmin):

        form = ItemAdminForm

See `testproject <https://github.com/nanvel/django-nicedit/tree/master/testproject>`__ for example.

.. info::
    :tags: Django, NicEdit
    :place: Phuket, Thailand
