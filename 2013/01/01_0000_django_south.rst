Schema- and data-migration in Django with South
===============================================

.. image:: https://raw.githubusercontent.com/nanvel/blog/master/2013/01/south_logo.png
    :width: 210px
    :alt: South
    :align: left

Documentation and tutorials available at `http://south.aeracode.org/ <http://south.aeracode.org/>`__.

Task: User profile application.

project/requirements.txt:

.. code-block:: text

    django==1.4.3
    south==0.7.6

Create project, add users application, add `users` and `south` to INSTALLED_APPS, configure  DATABASES.

.. code-block:: bash

    python manage.py syncdb

**Create initial migrations (once):**

.. code-block:: bash

    python manage.py schemamigration users --initial
    Creating migrations directory at '.../project/users/migrations'...
    Creating __init__.py in '../project/users/migrations'...
    Created 0001_initial.py. You can now apply this migration with: ./manage.py migrate users

Create initial migrations for every app You created.

Create new model:

.. code-block:: python

    from django.db import models


    class UserProfile(models.Model):
        name = models.CharField(max_length=200)
        email = models.EmailField()
        address = models.CharField(max_length=200)

We need to create new table for this model, schema-migration:

.. code-block:: bash

    python manage.py schemamigration users --auto
     + Added model users.UserProfile
    Created 0002_auto__add_userprofile.py. You can now apply this migration with: ./manage.py migrate users

Don't forget to add 0002_auto__add_userprofile.py to git index, execute migrations:

.. code-block:: bash

    python manage.py migrate users
    Running migrations for users:
     - Migrating forwards to 0002_auto__add_userprofile.
     > users:0001_initial
     > users:0002_auto__add_userprofile
     - Loading initial data for users.
    Installed 0 object(s) from 0 fixture(s)

What if requirements were updated and we need to store phone number additionally?

**Add `phone` field to the model:**

.. code-block:: python

    class UserProfile(models.Model):
        name = models.CharField(max_length=200)
        email = models.EmailField()
        address = models.CharField(max_length=200)
        phone = models.CharField(max_length=20, blank=True, null=True)

Create schema-migration and execute it:

.. code-block:: bash

    python manage.py schemamigration users --auto
     + Added field phone on users.UserProfile
    Created 0003_auto__add_field_userprofile_phone.py. You can now apply this migration with: ./manage.py migrate users

    python manage.py migrate users
    Running migrations for users:
     - Migrating forwards to 0003_auto__add_field_userprofile_phone.
     > users:0003_auto__add_field_userprofile_phone
     - Loading initial data for users.
    Installed 0 object(s) from 0 fixture(s)

**Add one more model?**

.. code-block:: python

    class Country(models.Model):
        name = models.CharField(max_length=100)


    class UserProfile(models.Model):
        name = models.CharField(max_length=200)
        email = models.EmailField()
        country = models.ForeignKey(Country, related_name='country_users', null=True)
        address = models.CharField(max_length=200)
        phone = models.CharField(max_length=20, blank=True, null=True)

As simple as before, just schemamigration -> migrate:

.. code-block:: bash

    python manage.py schemamigration users --auto
     + Added model users.Country
     + Added field country on users.UserProfile
    Created 0004_auto__add_country__add_field_userprofile_country.py. You can now apply this migration with: ./manage.py migrate users

    python manage.py migrate users
    Running migrations for users:
     - Migrating forwards to 0004_auto__add_country__add_field_userprofile_country.
     > users:0004_auto__add_country__add_field_userprofile_country
     - Loading initial data for users.
    Installed 0 object(s) from 0 fixture(s)

**Increase complexity:**

instead `name`, we need to use fname and lname, and we already have some data in the table.

We can accomplish this with two schema- and one data-migration. In data-migration we need to copy data from `name` field to `fname` and `lname` fields, for example:

.. code-block:: text

    (name == 'Mikuru Asahina') -> (fname == 'Mikuru', lname == 'Asahina')

Roadmap:
    - add `fname` and `lname` fields
    - copy data from `name` field to `fname` and `lname`
    - remove `name` field

.. code-block:: python

    class UserProfile(models.Model):
        name = models.CharField(max_length=200)
        fname = models.CharField(max_length=100, blank=True, null=True)
        lname = models.CharField(max_length=100, blnak=True, null=True)
        email = models.EmailField()
        country = models.ForeignKey(Country, related_name='country_users', null=True)
        address = models.CharField(max_length=200)
        phone = models.CharField(max_length=20, blank=True, null=True)

.. code-block:: bash

    python manage.py schemamigration users --auto
     + Added field fname on users.UserProfile
     + Added field lname on users.UserProfile
    Created 0005_auto__add_field_userprofile_fname__add_field_userprofile_lname.py. You can now apply this migration with: ./manage.py migrate users

    python manage.py migrate users
    Running migrations for users:
     - Migrating forwards to 0005_auto__add_field_userprofile_fname__add_field_userprofile_lname.
     > users:0005_auto__add_field_userprofile_fname__add_field_userprofile_lname
     - Loading initial data for users.
    Installed 0 object(s) from 0 fixture(s)

Create data-migration:

.. code-block:: bash

    python manage.py datamigration users split_name
    Created 0006_split_name.py.

Edit automatically created project/users/migrations/0006_split_name.py file.

.. code-block:: python

    class Migration(DataMigration):

        def forwards(self, orm):
            for up in orm.UserProfile.objects.all():
                if not up.name:
                    continue
                names = up.name.split()
                if len(names) == 1:
                    up.fname = names[0]
                else:
                    up.fname = names.pop(0)
                    up.lname = ' '.join(names)
                up.save()

        def backwards(self, orm):
            for up in orm.UserProfile.objects.all():
                up.name = ' '.join((up.fname or '', up.lname or ''))
                up.save()

Migration execution looks the same as for schema-migration:

.. code-block:: bash

    python manage.py migrate users
    Running migrations for users:
     - Migrating forwards to 0006_split_name.
     > users:0006_split_name
     - Migration 'users:0006_split_name' is marked for no-dry-run.
     - Loading initial data for users.
    Installed 0 object(s) from 0 fixture(s)

Finally remove `name` field:

.. code-block:: python

    class UserProfile(models.Model):
        fname = models.CharField(max_length=100, blank=True, null=True)
        lname = models.CharField(max_length=100, blank=True, null=True)
        email = models.EmailField()
        country = models.ForeignKey(Country, related_name='country_users', null=True)
        address = models.CharField(max_length=200)
        phone = models.CharField(max_length=20, blank=True, null=True)

.. code-block:: bash

    python manage.py schemamigration users --auto
     ? The field 'UserProfile.name' does not have a default specified, yet is NOT NULL.
     ? Since you are removing this field, you MUST specify a default
     ? value to use for existing rows. Would you like to:
     ?  1. Quit now, and add a default to the field in models.py
     ?  2. Specify a one-off value to use for existing columns now
     ?  3. Disable the backwards migration by raising an exception.
     ? Please select a choice: 2
     ? Please enter Python code for your one-off default value.
     ? The datetime module is available, so you can do e.g. datetime.date.today()
     >>> 'noname'
     - Deleted field name on users.UserProfile
    Created 0007_auto__del_field_userprofile_name.py. You can now apply this migration with: ./manage.py migrate users

    python manage.py migrate users
    Running migrations for users:
     - Migrating forwards to 0007_auto__del_field_userprofile_name.
     > users:0007_auto__del_field_userprofile_name
     - Loading initial data for users.
    Installed 0 object(s) from 0 fixture(s)

If you want to use South in project that already has tables in database: `read about converting an app <http://south.readthedocs.org/en/latest/convertinganapp.html#converting-an-app>`__.

Links:
    - `Common Pitfalls with Django and South <http://andrewingram.net/2012/dec/common-pitfalls-django-south/>`__

.. info::
    :tags: Django, South
    :place: Alchevs'k, Ukraine
