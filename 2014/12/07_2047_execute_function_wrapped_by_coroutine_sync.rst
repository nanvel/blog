Execute function wrapped by tornado.gen.coroutine synchronously
===============================================================

It turned out a simple task, just use IOLoop.run_sync:

.. code-block:: python

    import datetime
    import logging

    from tornado import ioloop, gen, options


    logger = logging.getLogger(__name__)


    @gen.coroutine
    def sleep(seconds=2):
        logger.warning('start')
        yield gen.Task(
            ioloop.IOLoop.current().add_timeout,
            deadline=datetime.timedelta(seconds=seconds))
        logger.warning('stop')


    if __name__ == "__main__":
        options.parse_command_line()
        ioloop.IOLoop.instance().run_sync(sleep, timeout=1000)


*UPD 2014.12.27*

It turned out, that run_sync doesn't work in celery tasks if Kqueue used(didn't tested it with epoll), simple workaround - just use Select instead:

.. code-block:: python

    from tornado.platform.select import SelectIOLoop


    @celery.task()
    def my_task():
        ioloop_inst = SelectIOLoop.instance()
        ioloop_inst.initialize()
        ioloop_inst.run_sync(sleep, timeout=1000)


.. info::
    :tags: Tornado
    :place: Kyiv, Ukraine
