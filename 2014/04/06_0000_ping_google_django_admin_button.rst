Ping google django admin button
===============================

.. image:: https://raw.githubusercontent.com/nanvel/blog/master/2014/04/ping_google_button.png
    :width: 315px
    :alt: Ping google button
    :align: left

``ping_google()`` allows to notify google that your sitemaps were changed and need to reindex. This snippet shows how to add ping google button to item edit page on django admin site.

Edit ``admin/change_form.html``:

.. code-block:: bash

    cp .env/lib/python2.7/site-packages/django/contrib/admin/templates/admin/change_form.html myproject/templates/admin/

.. code-block:: diff

    --- a/myproject/templates/admin/change_form.html
    +++ b/myproject/templates/admin/change_form.html
    @@ -28,6 +28,9 @@
     {% block object-tools %}
     {% if change %}{% if not is_popup %}
       <ul class="object-tools">
    +    {% for button in buttons %}
    +      <li><a href="{{ button.0 }}/">{{ button.1 }}</a></li>
    +    {% endfor %}
         {% block object-tools-items %}

Edit ``admin.py`` file:

.. code-block::

    from django.contrib import admin, messages
    from django.contrib.sitemaps import ping_google

    from django.http import HttpResponseRedirect


    class ButtonableModelAdmin(admin.ModelAdmin):
        """
        A subclass of this admin will let you add buttons (like history) in the
        change view of an entry.
        More: https://djangosnippets.org/snippets/1016/
        admin/change_form.html template is modified.
        """

        buttons = []

        def change_view(self, request, object_id, extra_context={}):
            extra_context['buttons'] = self.buttons
            return super(ButtonableModelAdmin, self).change_view(
                    request=request, object_id=object_id, extra_context=extra_context)

        def button_view_dispatcher(self, request, object_id, command):
            obj = self.model._default_manager.get(pk=object_id)
            return getattr(self, command)(request, [obj]) \
                    or HttpResponseRedirect(request.META['HTTP_REFERER'])

        def get_urls(self):

            from django.conf.urls import patterns, url
            from django.utils.functional import update_wrapper

            def wrap(view):
                def wrapper(*args, **kwargs):
                    return self.admin_site.admin_view(view)(*args, **kwargs)
                return update_wrapper(wrapper, view)

            info = self.model._meta.app_label, self.model._meta.module_name

            return patterns('',
                *(url(r'^(\d+)/(%s)/$' % but[0], wrap(self.button_view_dispatcher)) for but in self.buttons)
            ) + super(ButtonableModelAdmin, self).get_urls()


    class MyModelAdmin(ButtonableModelAdmin):

        def _ping_google(self, request, queryset):
            try:
                ping_google()
                messages.success(
                    request,
                    'Sitemaps were submitted.')
            except Exception:
                messages.warning(
                    request,
                    'Sitemaps were not submitted.')

        _ping_google.short_description = 'Ping google'

        buttons = [(_ping_google.func_name, _ping_google.short_description)]

The ``ping_google()`` command only works if you have registered your site with `Google Webmaster Tools <http://www.google.com/webmasters/tools/>`__.

Links:
    - https://docs.djangoproject.com/en/dev/ref/contrib/sitemaps/#pinging-google
    - https://djangosnippets.org/snippets/1016/

.. info::
    :tags: Django, SEO
    :place: Starobilsk, Ukraine
