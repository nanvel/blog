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

.. info::
    :tags: Tornado
    :place: Kyiv, Ukraine
