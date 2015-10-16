labels: Blog
        Django
        Testing
created: 2013-04-27T00:00
place: Starobilsk, Ukraine

# [Django] Session. Control and testing

Before use ```request.session.session_key``` in view, check that it exists first:
```python
if request.session.session_key is None:
    request.session.save()
```

Session saves by middleware, if ```session.modified == True```, before response will be sent. If ```settings.SESSION_SAVE_EVERY_REQUEST == True```, session will be saved to the database on every request, and ```session.modified``` doesn't matter.

If we need to control session manually, we can do like this:
```python
def my_view(request):
    # do something, change session 1
    request.session.save()
    # do something, change session 2
    request.session.modified = False
    return response
    # the first changes will be saved and the second - no
```

As for testing, ```TestCase.client``` doesn't has session, but we can add it:
```python
from django.conf import settings
from django.test import TestCase
from django.utils.importlib import import_module


class WithSessionTestCase(TestCase):

    def create_session(self):
        # initialize session
        settings.SESSION_ENGINE = 'django.contrib.sessions.backends.file'
        engine = import_module(settings.SESSION_ENGINE)
        store = engine.SessionStore()
        store.save()
        self.session = store
        self.client.cookies[settings.SESSION_COOKIE_NAME] = store.session_key

    def test_something(self):
        self.create_session()
        # now self.client.session is available
```

Links:

- [https://docs.djangoproject.com/en/dev/topics/http/sessions/](https://docs.djangoproject.com/en/dev/topics/http/sessions/)
