labels: Blog
        RST
        Projects
created: 2014-11-15T21:27
place: Kyiv, Ukraine
comments: true

# GBlog custom rst directives

[TOC]

## Code

```rst
.. code-block:: python

    import sys


    if __name__ == '__main__':
        pass
```

## Video

YouTube:
```rst
.. youtube:: oDB9KDF0QLU
    :align: left
    :width: 500
```

Vimeo:
```rst
.. vimeo:: 45370040
    :align: left
    :width: 500
```

## Image

```rst
.. image:: http://media-cache-ec0.pinimg.com/236x/a6/5a/34/a65a341e3fec7a52077708f118e01ce1.jpg
    :width: 200px
    :alt: Image example
    :align: center
```

![Image example](http://media-cache-ec0.pinimg.com/236x/a6/5a/34/a65a341e3fec7a52077708f118e01ce1.jpg)

## BlockQuote

```rst
.. blockquote::
    :content: When science and magic meet,<br>history is born.
    :author: A Certain Magical Index
    :author_url: https://en.wikipedia.org/wiki/A_Certain_Magical_Index
```

## Meta information

```rst
.. info::
    :tags: Tag1, Tag2
```

Links:

- [GBlog on GitHub](https://github.com/nanvel/gblog)
- [Restructured Text and Sphinx CheatSheet](http://thomas-cokelaer.info/tutorials/sphinx/rest_syntax.html)
