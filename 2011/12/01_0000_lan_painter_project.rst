Lan Painter project
===================

.. image:: https://raw.githubusercontent.com/nanvel/blog/master/2011/12/lp1.png
    :width: 500px
    :alt: Lan painter
    :align: left

Було розроблено для обчислювального центру Донбаського Державного Технічного Університету.

Можливості:

    - Малювання мережі (користувач додає вузли)
    - Експорт схеми у PDF
    - Збереження інформації про вузли
    - Пошук вузлів на схемі
    - Сканування елементів на схемі (ping вузлів) що дозволяє виявили обриви у мережі

Програма написана на C++/Qt у 2011 році.

Додавання/видалення/редагування вузлів
--------------------------------------

Вузлами я називаю комутатори. На схемі відображаються у вигляді прямокутників. Всередині прямокутників знаходиться список комп'ютерів що під'єднані до кумутатора.

Контекстне меню:

.. image:: https://raw.githubusercontent.com/nanvel/blog/master/2011/12/lp2.png
    :width: 374px
    :alt: Lan painter, context menu
    :align: left

Редагування вузла:

.. image:: https://raw.githubusercontent.com/nanvel/blog/master/2011/12/lp3.png
    :width: 421px
    :alt: Lan painter, node edit
    :align: left

Пошук на схемі
--------------

.. image:: https://raw.githubusercontent.com/nanvel/blog/master/2011/12/lp4.png
    :width: 725px
    :alt: Lan painter, search
    :align: left

І можна обрати вузол який буде вважатися коренем і вузли що знаходяться вище нього будуть сховані.

Збереження схеми у файл
-----------------------

.. image:: https://raw.githubusercontent.com/nanvel/blog/master/2011/12/lp5.png
    :width: 249px
    :alt: Lan painter, save scheme
    :align: left

Збереження схеми у форматі PDF:

.. image:: https://raw.githubusercontent.com/nanvel/blog/master/2011/12/lp6.png
    :width: 500px
    :alt: Lan painter, save as pdf
    :align: left

Сканування
----------

.. image:: https://raw.githubusercontent.com/nanvel/blog/master/2011/12/lp7.png
    :width: 195px
    :alt: Lan painter, scan nodes
    :align: left

Сканування виконується у фоновому режимі. Вікно програми можна згорнути у панель задач.

.. image:: https://raw.githubusercontent.com/nanvel/blog/master/2011/12/lp8.png
    :width: 134px
    :alt: Lan painter, system panel
    :align: left

Пошук вузлів за шаблоном
------------------------

.. image:: https://raw.githubusercontent.com/nanvel/blog/master/2011/12/lp9.png
    :width: 602px
    :alt: Lan painter, search nodes
    :align: left

Вбудована довідка
-----------------

.. image:: https://raw.githubusercontent.com/nanvel/blog/master/2011/12/lp10.png
    :width: 195px
    :alt: Lan painter, help page
    :align: left

Інтерфейс перекладено на англійську, українську та російську мови
-----------------------------------------------------------------

.. image:: https://raw.githubusercontent.com/nanvel/blog/master/2011/12/lp11.png
    :width: 240px
    :alt: Lan painter, select language
    :align: left

Links:
    - `Програма на Qt-apps.org <http://qt-apps.org/content/show.php/Lan+painter?content=142898>`__
    - `Source code <https://raw.githubusercontent.com/nanvel/blog/master/2011/12/lan_painter.zip>`__

.. info::
    :tags: Projects, Qt
    :place: Alchevs'k, Ukraine
