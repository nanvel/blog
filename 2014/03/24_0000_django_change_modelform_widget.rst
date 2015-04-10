Three ways to change widget in Django ModelForm
===============================================

The problem: replace TextInput with Textarea.

``models.py``:

.. code-block:: python

    from django.db import models


    class MyModel(models.model):
        title = models.CharField(max_length=1000)
        description = models.CharField(
            max_length=5000, help_text='Your amazing description')

``forms.py``:

.. code-block:: python

    from django import forms

    from .models import MyModel


    class MyForm(forms.ModelForm):

        description = forms.CharField(widget=forms.Textarea)

        class Meta:
            model = MyModel

This is the worst one. Why? Help text specified in the model field will be not visible in form.

Better way:

.. code-block:: python

    from django import forms

    from .models import MyModel


    class MyForm(forms.ModelForm):

        class Meta:
            model = MyModel

        def __init__(self, *args, **kwargs):
            super(MyForm, self).__init__(*args, **kwargs)
            self.fields['description'].widget = forms.Textarea

And the best:

.. code-block:: python

    from django import forms

    from .models import MyModel


    class MyForm(forms.ModelForm):

        class Meta:
            model = MyModel
            widgets = {
                'description': forms.Textarea,
            }

.. info::
    :tags: Django
    :place: Starobilsk, Ukraine
