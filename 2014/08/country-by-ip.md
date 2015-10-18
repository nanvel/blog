labels: Blog
        Tornado
        Geo
created: 2014-08-23T00:00
place: Kyiv, Ukraine

# Get country code/name by IP address

Using tornado and [maxmind geoip2](http://dev.maxmind.com/geoip/geoip2/downloadable/) database:
```bash
pip install tornado
pip install geoip2
```

Use ```self.country``` to get client country code:
```python
import os.path

from geoip2.database import Reader as GeoIP2Reader
from tornado import options
from tornado.ioloop import IOLoop
from tornado.web import RequestHandler, Application


class BaseHandler(RequestHandler):

    # download it from maxmind site: http://dev.maxmind.com/geoip/geoip2/geolite2/
    GEOIP_BINARY = 'bin/GeoLite2-Country.mmdb'

    @property
    def country(self):
        try:
            ip = self.request.remote_ip
            geoip = getattr(self.application, '_geoip', None)
            if not geoip:
                geoip_file = os.path.join(
                    os.path.dirname(os.path.realpath(__file__)),
                    self.GEOIP_BINARY)
                geoip = GeoIP2Reader(geoip_file)
                self.application._geoip = geoip
            return geoip.country(ip).country.iso_code
        except Exception as e:
            return None


class CountryHandler(BaseHandler):

    def get(self):
        self.write(str(self.country))


if __name__ == '__main__':
    options.parse_command_line()
    application = Application(
        handlers=[
            (r'/', CountryHandler),
        ],
        debug=True,
    )
    application.listen(8000)
    IOLoop.instance().start()
```
