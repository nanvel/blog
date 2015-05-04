CSS arrows
==========

.. raw:: html

    <style>
    body {
        background-color: #fff;
        margin: 0;
        padding: 0;
    }
    .color {
        color: #46a546;
    }
    .box {
        border: 1px solid #222;
        width: 200px;
        height: 50px;
        margin: 20px;
        position: relative;
    }
    .arrow-up:before {
        display: inline-block;
        content: '';
        width: 0;
        height: 0;
        border-bottom: 7px solid #fff;
        border-bottom-color: #222;
        border-right: 7px solid transparent;
        border-left: 7px solid transparent;
        position: absolute;
        top: -7px;
        left: 93px;
    }
    .arrow-up:after {
        display: inline-block;
        content: '';
        width: 0;
        height: 0;
        border-bottom: 6px solid #fff;
        border-right: 6px solid transparent;
        border-left: 6px solid transparent;
        position: absolute;
        top: -6px;
        left: 94px;
    }
    .arrow-right:before {
        display: inline-block;
        content: '';
        width: 0;
        height: 0;
        border-left: 7px solid #fff;
        border-left-color: #222;
        border-top: 7px solid transparent;
        border-bottom: 7px solid transparent;
        position: absolute;
        top: 18px;
        right: -7px;
    }
    .arrow-right:after {
        display: inline-block;
        content: '';
        width: 0;
        height: 0;
        border-left: 6px solid #fff;
        border-top: 6px solid transparent;
        border-bottom: 6px solid transparent;
        position: absolute;
        top: 19px;
        right: -6px;
    }
    .arrow-down:before {
        display: inline-block;
        content: '';
        width: 0;
        height: 0;
        border-top: 7px solid #fff;
        border-top-color: #222;
        border-right: 7px solid transparent;
        border-left: 7px solid transparent;
        position: absolute;
        bottom: -7px;
        left: 93px;
    }
    .arrow-down:after {
        display: inline-block;
        content: '';
        width: 0;
        height: 0;
        border-top: 6px solid #fff;
        border-right: 6px solid transparent;
        border-left: 6px solid transparent;
        position: absolute;
        bottom: -6px;
        left: 94px;
    }
    .arrow-left:before {
        display: inline-block;
        content: '';
        width: 0;
        height: 0;
        border-right: 7px solid #fff;
        border-right-color: #222;
        border-top: 7px solid transparent;
        border-bottom: 7px solid transparent;
        position: absolute;
        top: 18px;
        left: -7px;
    }
    .arrow-left:after {
        display: inline-block;
        content: '';
        width: 0;
        height: 0;
        border-right: 6px solid #fff;
        border-top: 6px solid transparent;
        border-bottom: 6px solid transparent;
        position: absolute;
        top: 19px;
        left: -6px;
    }
    </style>

.. code-block:: html

    <span class="color">/* common */</span>
    body {
        background-color: #fff;
        margin: 0;
        padding: 0;
    }
    .box {
        border: 1px solid #222;
        width: 200px;
        height: 50px;
        margin: 20px;
        position: relative;
    }

.. code-block:: html

    <span class="color">/* arrow up */</span>
    .arrow-up:before {
        display: inline-block;
        content: '';
        width: 0;
        height: 0;
        border-bottom: 7px solid #fff;
        border-bottom-color: #222;
        border-right: 7px solid transparent;
        border-left: 7px solid transparent;
        position: absolute;
        top: -7px;
        left: 93px;
    }
    .arrow-up:after {
        display: inline-block;
        content: '';
        width: 0;
        height: 0;
        border-bottom: 6px solid #fff;
        border-right: 6px solid transparent;
        border-left: 6px solid transparent;
        position: absolute;
        top: -6px;
        left: 94px;
    }

.. raw:: html

    <div class="box arrow-up"></div>

.. code-block:: html

    <span class="color">/* arrow right */</span>
    .arrow-right:before {
        display: inline-block;
        content: '';
        width: 0;
        height: 0;
        border-left: 7px solid #fff;
        border-left-color: #222;
        border-top: 7px solid transparent;
        border-bottom: 7px solid transparent;
        position: absolute;
        top: 18px;
        right: -7px;
    }
    .arrow-right:after {
        display: inline-block;
        content: '';
        width: 0;
        height: 0;
        border-left: 6px solid #fff;
        border-top: 6px solid transparent;
        border-bottom: 6px solid transparent;
        position: absolute;
        top: 19px;
        right: -6px;
    }

.. raw:: html

    <div class="box arrow-right"></div>

.. code-block:: html

    <span class="color">/* arrow down */</span>
    .arrow-down:before {
        display: inline-block;
        content: '';
        width: 0;
        height: 0;
        border-top: 7px solid #fff;
        border-top-color: #222;
        border-right: 7px solid transparent;
        border-left: 7px solid transparent;
        position: absolute;
        bottom: -7px;
        left: 93px;
    }
    .arrow-down:after {
        display: inline-block;
        content: '';
        width: 0;
        height: 0;
        border-top: 6px solid #fff;
        border-right: 6px solid transparent;
        border-left: 6px solid transparent;
        position: absolute;
        bottom: -6px;
        left: 94px;
    }

.. raw:: html

    <div class="box arrow-down"></div>

.. code-block:: html

    <span class="color">/* arrow left */</span>
    .arrow-left:before {
        display: inline-block;
        content: '';
        width: 0;
        height: 0;
        border-right: 7px solid #fff;
        border-right-color: #222;
        border-top: 7px solid transparent;
        border-bottom: 7px solid transparent;
        position: absolute;
        top: 18px;
        left: -7px;
    }
    .arrow-left:after {
        display: inline-block;
        content: '';
        width: 0;
        height: 0;
        border-right: 6px solid #fff;
        border-top: 6px solid transparent;
        border-bottom: 6px solid transparent;
        position: absolute;
        top: 19px;
        left: -6px;
    }

.. raw:: html

    <div class="box arrow-left"></div>

.. info::
    :tags: CSS
    :place: Starobilsk, Ukraine
