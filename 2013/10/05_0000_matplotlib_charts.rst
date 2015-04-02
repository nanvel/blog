Displaying charts with Matplotlib
=================================

For beginning:

.. code-block:: python

    from matplotlib import pyplot as plt
    from numpy import sin, arange, pi


    if __name__ == '__main__':
        T = 5.
        t = arange(0, T, T / 1000)
        x = [sin(2 * pi / T * 5 * i) for i in t] # 5 sin periods
        plt.plot(t, x)
        plt.show()

.. image:: https://raw.githubusercontent.com/nanvel/blog/master/2013/10/gr_mpl_1.png
    :width: 667px
    :alt: Charts using matplotlib, example 1
    :align: left

Let's prettify charts:

.. code-block:: python

    if __name__ == '__main__':
        T = 5.
        t = arange(0, T, T / 1000)
        x = [sin(2 * pi / T * 5 * i) for i in t] # 5 sin periods
        fig = plt.figure(1)
        fig.canvas.set_window_title('sin chart example')
        plt.plot(t, x)
        plt.title('sin(t)')
        plt.xlabel('t')
        plt.ylabel('sin')
        plt.show()

.. image:: https://raw.githubusercontent.com/nanvel/blog/master/2013/10/gr_mpl_2.png
    :width: 664px
    :alt: Charts using matplotlib, example 2
    :align: left

More charts:

.. code-block:: python

    if __name__ == '__main__':
        T = 5.
        t = arange(0, T, T / 1000)
        x1 = [sin(2 * pi / T * 5 * i) for i in t] # 5 sin periods
        x2 = [sin(2 * pi / T * 1 * i) for i in t] # 1 sin periods
        fig = plt.figure(1)
        fig.canvas.set_window_title('sin chart example')
        plt.plot(t, x1, 'r-', t, x2, 'g-')
        plt.title('sin(t)')
        plt.xlabel('t')
        plt.ylabel('sin')
        plt.show()

.. image:: https://raw.githubusercontent.com/nanvel/blog/master/2013/10/gr_mpl_3.png
    :width: 668px
    :alt: Charts using matplotlib, example 3
    :align: left

.. code-block:: python

    if __name__ == '__main__':
        T = 5.
        t = arange(0, T, T / 1000)
        x1 = [sin(2 * pi / T * 5 * i) for i in t] # 5 sin periods
        x2 = [sin(2 * pi / T * 1 * i) for i in t] # 1 sin periods
        fig = plt.figure(1)
        fig.canvas.set_window_title('sin chart example')
        plt.subplot(121)
        plt.plot(t, x1, 'r-')
        plt.title('sin(t)')
        plt.xlabel('t')
        plt.ylabel('sin')
        plt.subplot(122)
        plt.plot(t, x2, 'g-')
        plt.show()

.. image:: https://raw.githubusercontent.com/nanvel/blog/master/2013/10/gr_mpl_4.png
    :width: 667px
    :alt: Charts using matplotlib, example 4
    :align: left

.. code-block:: python

    if __name__ == '__main__':
        T = 5.
        t = arange(0, T, T / 1000)
        x1 = [sin(2 * pi / T * 5 * i) for i in t] # 5 sin periods
        x2 = [sin(2 * pi / T * 1 * i) for i in t] # 1 sin periods
        fig1 = plt.figure(1)
        fig1.canvas.set_window_title('sin chart example 1')
        plt.plot(t, x1)
        plt.title('sin(t)')
        plt.xlabel('t')
        plt.ylabel('sin')
        fig2 = plt.figure(2)
        fig2.canvas.set_window_title('sin chart example 2')
        plt.plot(t, x2)
        plt.show()

.. image:: https://raw.githubusercontent.com/nanvel/blog/master/2013/10/gr_mpl_5.png
    :width: 800px
    :alt: Charts using matplotlib, example 5
    :align: left

Legend:

.. code-block:: python

    if __name__ == '__main__':
        T = 5.
        t = arange(0, T, T / 1000)
        x1 = [sin(2 * pi / T * 5 * i) for i in t] # 5 sin periods
        x2 = [sin(2 * pi / T * 1 * i) for i in t] # 1 sin periods
        fig = plt.figure(1)
        fig.canvas.set_window_title('sin chart example')
        p1, p2 = plt.plot(t, x1, 'r-', t, x2, 'g-')
        plt.title('sin(t)')
        plt.xlabel('t')
        plt.ylabel('sin')
        plt.legend([p1, p2], ['5 periods', '1 period'])
        plt.show()

.. image:: https://raw.githubusercontent.com/nanvel/blog/master/2013/10/gr_mpl_6.png
    :width: 664px
    :alt: Charts using matplotlib, example 6
    :align: left

Links:
    - http://matplotlib.org/users/pyplot_tutorial.html

.. info::
    :tags: Matplotlib
    :place: Starobilsk, Ukraine
