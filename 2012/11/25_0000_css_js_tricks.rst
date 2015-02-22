CSS and JS notes
================

Fullscreen mode
---------------

Switch to fullscreen:

.. code-block:: js

    var docElm = document.documentElement;
    if (docElm.requestFullscreen) {
        docElm.requestFullscreen();
    }
    else if (docElm.mozRequestFullScreen) {
        docElm.mozRequestFullScreen();
    }
    else if (docElm.webkitRequestFullScreen) {
        docElm.webkitRequestFullScreen();
    }

Cancel fullscreen:

.. code-block:: js

    if (document.exitFullscreen) {
        document.exitFullscreen();
    }
    else if (document.mozCancelFullScreen) {
        document.mozCancelFullScreen();
    }
    else if (document.webkitCancelFullScreen) {
        document.webkitCancelFullScreen();
    }

Unselectable text
-----------------

.. code-block:: css

    .uselectable {
        -webkit-user-select: none; /* Chrome/Safari */        
        -moz-user-select: none; /* Firefox */
        -ms-user-select: none; /* IE10+ */

        /* Rules below not implemented in browsers yet */
        -o-user-select: none;
        user-select: none;
    }

Remove outline
--------------

.. code-block:: css

    a {
        outline: none;
    }
    /* for buttons in firefox */
    button::-moz-focus-inner {
        border: 0;
    }

Remove outline for button
-------------------------

.. code-block:: js

    $('button').focus(function(){
        $(this).blur();
    })

Place one image over another
----------------------------

html:

.. code-block:: html

    <div class="container">
        <img src="http://host/img1.png" class="back">
        <img src="http://host/img2.png" class="front">
    </div>

css:

.. code-block:: css

    .container {
        position: relative;
        top: 0;
        left: 0;
    }
    .back {
        position: relative;
        top: 0;
        left: 0;
    }
    .front {
        position: absolute;
        top: 30px;
        left: 70px;
    }

Prevent putting IE into compatibility mode
------------------------------------------

.. code-block:: html

    <meta http-equiv="X-UA-Compatible" content="IE=8" /> 

Disable autocomplete
--------------------

.. code-block:: html

    <input type="text" autocomplete="off">

Open link in new tab
--------------------

.. code-block:: js

    window.open(url, '_blank');
    window.focus();

Check browser is Chrome
-----------------------

.. code-block:: js

    var is_chrome = /chrome/.test(navigator.userAgent.toLowerCase()

Submit form in new tab
----------------------

.. code-block:: html

    <form target="_blank">...</form>

.. info::
    :tags: CSS, JS
    :place: Alchevs'k, Ukraine
