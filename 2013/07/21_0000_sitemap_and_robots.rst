sitemap.xml and robots.txt
==========================

Just sitemap.xml and robots.txt examples and urls configuration.

``urls.py``:

.. code-block:: python

    from django.views.generic.simple import direct_to_template


    urlpatterns += patterns('',
        (r'^robots\.txt$', direct_to_template,
            {'template': 'robots.txt', 'mimetype': 'text/plain'}),
        (r'^sitemap\.xml$', direct_to_template,
            {'template': 'sitemap.txt', 'mimetype': 'text/xml'}),
    )

Or use ``TemplateView`` for Django version above 1.4:

.. code-block:: python

    from django.views.generic import TemplateView


    urlpatterns += patterns('',
        (r'^robots\.txt$', TemplateView.as_view(
        template_name='robots.txt', content_type='text/plain')),
        (r'^sitemap\.xml$', TemplateView.as_view(
            template_name='sitemap.xml', content_type='text/xml')),
    )

``templates/sitemap.xml``:

.. code-block:: xml

    <?xml version='1.0' encoding='UTF-8'?>
    <urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://www.google.com/schemas/sitemap/0.84 http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd">
        <url>
            <loc>http://mysite.com/somepage/</loc>
            <lastmod>2013-01-01</lastmod>
            <changefreq>weekly</changefreq>
            <priority>1.00</priority>
        </url>
    </urlset>

``templates/robots.txt``:

.. code-block:: text

    User-agent: Yandex
    Disallow: /admin
    Disallow: /static
    Disallow: /media
    Host: mysite.com

    User-agent: Goolebot
    Disallow: /admin
    Disallow: /static
    Disallow: /media

    User-agent: *
    Crawl-delay: 30
    Disallow: /admin
    Disallow: /static
    Disallow: /media

Note, You should extend robots.txt by urls You don't wan't to be indexed by search crawlers.
Opposite to robots.txt, sitemap.xml should contains urls of pages You want search engines knows about.

Links:
    - http://fredericiana.com/2010/06/09/three-ways-to-add-a-robots-txt-to-your-django-project/
    - http://www.wordsinarow.com/xml-sitemaps.html

.. info::
    :tags: Django, Sitemap
    :place: Starobilsk, Ukraine
