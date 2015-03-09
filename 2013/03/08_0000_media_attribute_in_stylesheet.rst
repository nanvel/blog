media attribute in link[rel=stylesheet]
=======================================

.. code-block:: html

    <!DOCTYPE html>
    <html>
        <head>
            <meta charset="utf-8">
            <title>media attribute for link[rel=stylesheet]</title>
            <link rel="stylesheet" type="text/css" media="screen" href="normal.css" />
            <link rel="stylesheet" type="text/css" media="screen and (max-device-width: 800px)" href="small.css" />
        </head>
        <body>
            <div class="cube"></div>
        </body>
    </html>

.. code-block:: css

    /* normal.css */
    .cube {
        width: 100px;
        height: 100px;
        background-color: #a00;
    }
    small.css:
    .cube {
        background-color: #0a0;
    }

Result:

.. image:: https://raw.githubusercontent.com/nanvel/blog/master/2013/03/stylesheet_media.JPG
    :width: 598px
    :alt: Stylesheet media attribute
    :align: left

Links:
    - http://alistapart.com/article/responsive-web-design

.. info::
    :tags: HTML
    :place: Starobilsk, Ukraine
