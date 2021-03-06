labels: Blog
        Tornado
created: 2014-12-06T23:14
place: Kyiv, Ukraine
comments: true

# Handle errors in a tornado application, the right way

> Exceptions... allow error handling to be organized cleanly in a central or high-level place within the program structure.
>
> Doug Hellmann, Python Exception Handling Techniques

After a few false steps, seems like, I found the right way to handle errors in a tornado application.

Main points:

- use ApplicationException(inherited from tornado.web.HTTPError) exception to return the application custom errors (like "user was not found" or "specified age is invalid")
- override tornado.web.RequestHandler.write_error, make it return errors in json format

See [my question on stackoverflow](http://stackoverflow.com/questions/26371051/better-way-to-handle-errors-in-tornado-request-handler/26392743).

```python
import json
import traceback

from tornado import web, options, ioloop


class MyAppException(web.HTTPError):

    pass


class MyAppBaseHandler(web.RequestHandler):

    def write_error(self, status_code, **kwargs):

        self.set_header('Content-Type', 'application/json')
        if self.settings.get("serve_traceback") and "exc_info" in kwargs:
            # in debug mode, try to send a traceback
            lines = []
            for line in traceback.format_exception(*kwargs["exc_info"]):
                lines.append(line)
            self.finish(json.dumps({
                'error': {
                    'code': status_code,
                    'message': self._reason,
                    'traceback': lines,
                }
            }))
        else:
            self.finish(json.dumps({
                'error': {
                    'code': status_code,
                    'message': self._reason,
                }
            }))


class AgeHandler(MyAppBaseHandler):

    def get(self):
        age = self.get_argument('age')
        age = int(age)
        if age < 1 or age > 200:
            raise MyAppException(reason='Wrong age value.', status_code=400)
        self.write('Your age is {age}'.format(age=age))


class MyApplication(web.Application):

    def __init__(self, **kwargs):
        kwargs['handlers'] = [
            web.url(r'/', AgeHandler, name='age'),
        ]
        kwargs['debug'] = True
        super(MyApplication, self).__init__(**kwargs)


if __name__ == '__main__':
    options.parse_command_line()
    application = MyApplication()
    application.listen(5000)
    ioloop.IOLoop.instance().start()
```

debug == False:
```json
{
   "error":{
      "code":400,
      "message":"Wrong age value."
   }
}
```

debug == True:
```json
{
   "error":{
      "traceback":[
         "Traceback (most recent call last):\n",
         "  File \".env/lib/python3.3/site-packages/tornado/web.py\", line 1332, in _execute\n    result = method(*self.path_args, **self.path_kwargs)\n",
         "  File \"app.py\", line 46, in get\n    raise MyAppException(reason='Wrong age value.', status_code=400)\n",
         "MyAppException: HTTP 400: Wrong age value.\n"
      ],
      "message":"Wrong age value.",
      "code":400
   }
}
```
