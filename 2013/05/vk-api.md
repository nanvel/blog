labels: Blog
        API
created: 2013-05-28T00:00
place: Starobilsk, Ukraine
comments: true

# Python script retrieves my vk news feed

```python
import cookielib
import urllib
import urllib2

from urlparse import urlparse
from HTMLParser import HTMLParser


class VKAuthFormContentHandler(HTMLParser):

    def __init__(self, *args, **kwargs):
        HTMLParser.__init__(self, *args, **kwargs)
        self._inside_form = False
        self.form_action = ''
        self.form_data = {}

    def handle_starttag(self, tag, attrs):
        if tag.lower() == 'form':
            attrs_dict = dict(attrs)
            if attrs_dict.get('method', '').lower() != 'post':
                return
            self.form_action = attrs_dict.get('action')
            self.form_method = attrs_dict.get('method')
            self._inside_form = True
        elif self._inside_form and tag.lower() == 'input':
            attrs_dict = dict(attrs)
            if ('name' not in attrs_dict) or (attrs_dict.get('type', '') not in ['hidden', 'text', 'password']):
                return
            self.form_data[attrs_dict['name']] = attrs_dict.get('value', '')

    def handle_endtag(self, tag):
        if tag.lower() == 'form':
            self._inside_form = False


class VKAuth(object):

    VK_AUTH_REDIRECT_URL = 'http://oauth.vk.com/blank.html'
    VK_AUTH_URL = "http://oauth.vk.com/oauth/authorize?redirect_uri={redirect_uri}&response_type=token&client_id={client_id}&scope={scope}&display=wap"

    _parser = VKAuthFormContentHandler()

    def login(self, app_id, user_email, user_secret, scope=['friends', 'offline', 'wall', 'photos']):
        opener = urllib2.build_opener(
            urllib2.HTTPCookieProcessor(cookielib.CookieJar()),
            urllib2.HTTPRedirectHandler())
        response = opener.open(self.VK_AUTH_URL.format(
            client_id=VK_APP_ID,
            scope=','.join(scope),
            redirect_uri=self.VK_AUTH_REDIRECT_URL)).read()
        self._parser.feed(response)
        data = self._parser.form_data
        action = self._parser.form_action
        data['email'] = VK_USER_EMAIL
        data['pass'] = VK_USER_SECRET
        response = opener.open(action, urllib.urlencode(data))
        if (
                urlparse(response.geturl()).path !=
                urlparse(self.VK_AUTH_REDIRECT_URL).path):
            # give access
            self._parser.data = {}
            self._parser.feed(response.read())
            response = opener.open(
                self._parser.form_action,
                urllib.urlencode(self._parser.form_data))
        user_id = None
        access_token = None
        for part in urlparse(response.geturl()).fragment.split('&'):
            parts = part.split('=')
            if len(parts) != 2:
                continue
            if parts[0] == 'user_id':
                user_id = parts[1]
            elif parts[0] == 'access_token':
                access_token = parts[1]
        return (user_id, access_token)


if __name__ == '__main__':
    VK_USER_EMAIL = '***'
    VK_USER_SECRET = '***'
    VK_APP_ID = '***'
    user_id, access_token = VKAuth().login(
        app_id=VK_APP_ID,
        user_email=VK_USER_EMAIL,
        user_secret=VK_USER_SECRET)
    url = 'https://api.vk.com/method/{method}?{args}'.format(
        method='newsfeed.get',
        args=urllib.urlencode({'access_token': access_token}))
    print urllib2.urlopen(url).read()
    # {"response":{"items":[{"type":"wall_photo","source_id" ...
```

Links:

- [http://habrahabr.ru/post/143972/](http://habrahabr.ru/post/143972/)
- [http://vk.com/page-1_2369282](http://vk.com/page-1_2369282)
