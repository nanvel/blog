labels: Blog
        Tornado
created: 2014-07-26T00:00
place: Kyiv, Ukraine
comments: true

# [tornado] Async handlers, code refactor

Let's start with sync implementation:

```python
import json

from tornado import options
from tornado.ioloop import IOLoop
from tornado.web import RequestHandler, Application
from tornado.httpclient import HTTPClient, HTTPError


class FBHandler(RequestHandler):

    FB_GRAPH_ME_URL = 'https://graph.facebook.com/me?fields=id&access_token={fb_token}'

    def get(self):
        fb_id = self.get_argument('fb_id')
        fb_token = self.get_argument('fb_token')
        url = self.FB_GRAPH_ME_URL.format(fb_token=fb_token)
        http_client = HTTPClient()
        try:
            response = http_client.fetch(request=url, method='GET')
            if json.loads(response.body).get('id') == fb_id:
                self.write('Ok')
                return
        except HTTPError:
            pass
        self.write('Fail')


if __name__ == '__main__':
    options.parse_command_line()
    application = Application(
        handlers=[
            (r'/', FBHandler),
        ],
        debug=True,
    )
    application.listen(8000)
    IOLoop.instance().start()
```

Make it async:
```python
import json

from tornado import options
from tornado.ioloop import IOLoop
from tornado.web import RequestHandler, Application, asynchronous
from tornado.httpclient import AsyncHTTPClient, HTTPError


class FBHandler(RequestHandler):

    FB_GRAPH_ME_URL = 'https://graph.facebook.com/me?fields=id&access_token={fb_token}'

    @asynchronous
    def get(self):
        self.fb_id = self.get_argument('fb_id')
        fb_token = self.get_argument('fb_token')
        url = self.FB_GRAPH_ME_URL.format(fb_token=fb_token)
        http_client = AsyncHTTPClient()
        try:
            response = http_client.fetch(
                request=url, method='GET', callback=self.on_fetch)
        except HTTPError:
            self.write('Fail')

    def on_fetch(self, response):
        if json.loads(response.body).get('id') == self.fb_id:
            self.write('Ok')
        else:
            self.write('Fail')
        self.finish()


...
```

Add gen sugar:
```python
import json

from tornado import options, gen
from tornado.ioloop import IOLoop
from tornado.web import RequestHandler, Application
from tornado.httpclient import AsyncHTTPClient, HTTPError


class FBHandler(RequestHandler):

    FB_GRAPH_ME_URL = 'https://graph.facebook.com/me?fields=id&access_token={fb_token}'

    @gen.coroutine
    def get(self):
        fb_id = self.get_argument('fb_id')
        fb_token = self.get_argument('fb_token')
        url = self.FB_GRAPH_ME_URL.format(fb_token=fb_token)
        http_client = AsyncHTTPClient()
        try:
            response = yield http_client.fetch(request=url, method='GET')
            if json.loads(response.body).get('id') == fb_id:
                self.write('Ok')
                return
            self.write('Fail')
        except HTTPError:
            pass
        self.write('Fail')


...
```

Hold handlers as simple as possible:
```python
import json

from tornado import options, gen
from tornado.ioloop import IOLoop
from tornado.web import RequestHandler, Application
from tornado.httpclient import AsyncHTTPClient, HTTPError


class FBHandler(RequestHandler):

    @gen.coroutine
    def get(self):
        try:
            fb_id = self.get_argument('fb_id')
            fb_token = self.get_argument('fb_token')
            yield self.validate(fb_id=fb_id, fb_token=fb_token)
            self.write('Ok')
        except Exception:
            self.write('Fail')

    @gen.coroutine
    def validate(self, fb_id, fb_token):
        FB_GRAPH_ME_URL = 'https://graph.facebook.com/me?fields=id&access_token={fb_token}'

        url = FB_GRAPH_ME_URL.format(fb_token=fb_token)
        http_client = AsyncHTTPClient()
        response = yield http_client.fetch(request=url, method='GET')
        assert json.loads(response.body).get('id') == fb_id
        raise gen.Return(True)


...
```
