labels: Blog
        Django
created: 2013-09-17T00:00
place: Starobilsk, Ukraine

# [Django] Compress response generator output

Without compressing:
```python
from django.http import HttpResponse


def mygenerator(n):
    for i in range(n):
        yield 'abc' * (i + 1)


def myview(request):
    response = HttpResponse(
        mygenerator(10),
        content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename=mygenerator.txt'
return response
```

Add magic:
```python
from django.http import HttpResponse
from gzip import GzipFile
from StringIO import StringIO


class Gzipper(object):
    """ Text stream compressor. """

    def __init__(self, filename=None):
        self.io = StringIO()
        self.zipfile = GzipFile(filename, mode='wb', fileobj=self.io)

    def read(self):
        self.zipfile.flush()
        self.io.seek(0)
        line = self.io.read()
        self.io.seek(0)
        self.io.truncate()
        return line

    def write(self, l):
        self.zipfile.write(l)

    def close(self):
        self.zipfile.close()
        self.io.seek(0)
        return self.io.read()

def mygenerator(n):
    zipper = Gzipper(filename='mygenerator.txt')
    for i in range(n):
        zipper.write('abc' * (i + 1))
        yield zipper.read()
    yield zipper.close()


def myview(request):
    response = HttpResponse(
        mygenerator(10),
        content_type='application/x-gzip')
    response['Content-Disposition'] = 'attachment; filename=mygenerator.gz'
return response
```
