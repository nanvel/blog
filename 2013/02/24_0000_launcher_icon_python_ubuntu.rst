Launcher icon for python script on Ubuntu
=========================================

.. image:: https://raw.githubusercontent.com/nanvel/blog/master/2013/02/unitybaricon.png
    :width: 384px
    :alt: Python application icon on unity bar
    :align: left

Create ~/.local/share/applications/myapp.desktop:

.. code-block:: text

    [Desktop Entry]
    Type=Application
    Name=[Name of your app, for example My App. This can be free text.]
    Exec=[full path to your executable and executable name, for example /usr/local/bin/myapp.py]
    Icon=[full path to your executable's icon and icon name, for example /usr/local/share/icons/apps/myapp.png]
    Terminal=false
    StartupNotify=true

Links:
    - `http://askubuntu.com/questions/78730/how-do-i-add-a-custom-launcher <http://askubuntu.com/questions/78730/how-do-i-add-a-custom-launcher>`__

.. info::
    :tags: Python, Ubuntu
    :place: Starobilsk, Ukraine
