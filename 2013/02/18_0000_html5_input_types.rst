HTML5 input types
=================

HTML5 defines over a dozen new input types!

But not all of them works even in modern browsers.
In Firefox they all look like they have type == "text".

In chromium I got following result:

.. image:: https://raw.githubusercontent.com/nanvel/blog/master/2013/02/html5inputs.png
    :width: 278px
    :alt: HTML5 inputs
    :align: left

.. code-block:: html

    <!DOCTYPE html>
    <html>
        <head>
            <title>Inputs</title>
        </head>
        <body>
            <script>
                var types = ['search', 'number', 'range', 'color', 'tel', 'url', 'email', 'date', 'month', 'week', 'time', 'datetime', 'datetime-local']
                var body = document.getElementsByTagName('body')[0]
                for(var input, i=0; i<types.length; i++) {
                    input = document.createElement('INPUT');
                    input.setAttribute('type', types[i]);
                    body.appendChild(document.createTextNode(types[i] + ':'))
                    body.appendChild(input);
                    body.appendChild(document.createElement('BR'))
                }
            </script>
        </body>
    </html>

Links:
    - `HTML5: Up and Running by Mark Pilgrim <http://shop.oreilly.com/product/9780596806033.do>`__

.. info::
    :tags: HTML5, JavaScript
    :place: Starobilsk, Ukraine
