labels: Blog
        Tornado
created: 2014-12-06T16:02

# Tornado time.sleep() replacement

Just decide to check is it works as I consider.

```python
import datetime
import logging
import time

from tornado import web, ioloop, gen, options


logger = logging.getLogger(__name__)


class MainHandler(web.RequestHandler):

    @gen.coroutine
    def sleep(self, seconds):
        yield gen.Task(
            ioloop.IOLoop.current().add_timeout,
            deadline=datetime.timedelta(seconds=seconds))

    @gen.coroutine
    def get(self):
        # self.finish()
        for i in xrange(5):
            logger.warning('Hello {i}'.format(i=i))
            # time.sleep(1)
            yield self.sleep(seconds=1)


application = web.Application([
    (r'/', MainHandler),
], debug=True)


if __name__ == "__main__":
    options.parse_command_line()
    application.listen(5000)
    ioloop.IOLoop.instance().start()
```

Output:
```
time.sleep()
[W 141206 15:53:34 tornado_sleep:17] Hello 0
[W 141206 15:53:35 tornado_sleep:17] Hello 1
[W 141206 15:53:36 tornado_sleep:17] Hello 2
[W 141206 15:53:37 tornado_sleep:17] Hello 3
[W 141206 15:53:38 tornado_sleep:17] Hello 4
[I 141206 15:53:39 web:1635] 200 GET / (::1) 5012.27ms
[W 141206 15:53:39 tornado_sleep:17] Hello 0
[W 141206 15:53:40 tornado_sleep:17] Hello 1
[W 141206 15:53:41 tornado_sleep:17] Hello 2
[W 141206 15:53:42 tornado_sleep:17] Hello 3
[W 141206 15:53:43 tornado_sleep:17] Hello 4
[I 141206 15:53:44 web:1635] 200 GET / (::1) 5014.00ms

self.sleep()
[W 141206 15:54:35 tornado_sleep:17] Hello 0
[W 141206 15:54:36 tornado_sleep:17] Hello 1
[W 141206 15:54:36 tornado_sleep:17] Hello 0
[W 141206 15:54:37 tornado_sleep:17] Hello 2
[W 141206 15:54:37 tornado_sleep:17] Hello 1
[W 141206 15:54:38 tornado_sleep:17] Hello 3
[W 141206 15:54:38 tornado_sleep:17] Hello 2
[W 141206 15:54:39 tornado_sleep:17] Hello 4
[W 141206 15:54:39 tornado_sleep:17] Hello 3
[I 141206 15:54:40 web:1635] 200 GET / (::1) 5038.38ms
[W 141206 15:54:40 tornado_sleep:17] Hello 4
[I 141206 15:54:41 web:1635] 200 GET / (::1) 5033.03ms
```

Place: Kyiv, Ukraine
