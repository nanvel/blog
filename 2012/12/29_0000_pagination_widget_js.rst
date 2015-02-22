Pagination widget js
====================

.. image:: https://raw.githubusercontent.com/nanvel/blog/master/2015/12/pagination_js.png
    :width: 625px
    :alt: Video thumbnails
    :align: left

`pagination.js at Bitbucket <https://bitbucket.org/nanvel/paginationjs>`__.


Usage:
    - include pagination.js
    - add <div class="pagination" data-pages="10"></div> where you want to see paginator
    - specify pages count by data-pages attribute

.. code-block:: diff

    +    'js/pagination.js',

    -    <div class="pagination">
    -        <ul>
    -            {% if page.has_previous %}
    -                <li><a href="?page={{ page.previous_page_number }}{{ q|urlget:'q' }}">Prev</a></li>
    -            {% endif %}
    -            {% for p in page.paginator.page_range %}
    -                {% ifequal p page.number %}
    -                    <li class="disabled"><a href="?page={{ p }}{{ q|urlget:'q' }}">{{ p }}</a></li>
    -                {% else %}
    -                    <li><a href="?page={{ p }}{{ q|urlget:'q' }}">{{ p }}</a></li>
    -                {% endifequal %}
    -            {% endfor %}
    -            {% if page.has_next %}
    -                <li><a href="?page={{ page.next_page_number }}{{ q|urlget:'q' }}">Next</a></li>
    -            {% endif %}
    -        </ul>
    -    </div>
    +    <div class="pagination" data-pages="{{ page.paginator.num_pages }}"></div>

.. info::
    :tags: JS, Pagination
    :place: Alchevs'k, Ukraine
