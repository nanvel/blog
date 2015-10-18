labels: Blog
        Tornado
created: 2014-11-22T11:21
place: Kyiv, Ukraine

# Ways to select tornado handler depends on request content

Looks like I can't easily select handler depends on request content in new tornado version.

```TypeError: issubclass() arg 1 must be a class -> AttributeError: '_RequestDispatcher' object has no attribute 'stream_request_body'```

```python
from tornado import web, options, ioloop


class Handler1(web.RequestHandler):

    def get(self):
        self.write('Hanler 1')


class Handler2(web.RequestHandler):

    def get(self):
        self.write('Hanler 2')


# --- tornado==3.2 ---
def index_handler(application, request, **kwargs):
    # useless example, replace by your own smart logic
    if request.query_arguments.get('v', '') == ['2.0']:
        return Handler2(application=application, request=request, **kwargs)
    return Handler1(application=application, request=request, **kwargs)


# --- tornado==4.0.2 ---
# Ways I found:
# - def get(self): if ... self.get_v20() else self.get_v10()
# - override web.RequestHandler._execute
# - override Application._get_host_handlers to allow to use HandlerFactory


class TheApplication(web.Application):

    def __init__(self, **kwargs):
        kwargs['handlers'] = [
            web.url(r'/', index_handler, name='index'),
        ]
        kwargs['debug'] = True
        super(TheApplication, self).__init__(**kwargs)


if __name__ == '__main__':
    """Result:
    http://localhost:5000/
    Hanler 1
    http://localhost:5000/?v=2.0
    Hanler 2
    """
    options.parse_command_line()
    application = TheApplication()
    application.listen(5000)
    ioloop.IOLoop.instance().start()
```
