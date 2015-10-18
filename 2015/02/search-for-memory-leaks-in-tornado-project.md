labels: Blog
        Python
        Tornado
created: 2015-02-15T13:01
place: Phuket, Thailand

# Search for memory leaks in tornado project

Guppy doesn't work with Python 3 (for February 2015).

requirements.txt:
```text
guppy
```

Use MemoryHandler to inspect memory usage:
```python
from guppy import hpy
from tornado import web, ioloop, gen, options


class LeakObject(object):

    def __init__(self):
        self.a = {}
        for i in xrange(1000):
            self.a[i] = 'leak' * 1000

    def __del__(self):
        pass


class LeakHandler(web.RequestHandler):

    def get(self):
        # create memory leak
        obj1 = LeakObject()
        obj2 = LeakObject()
        obj1.leak = obj2
        obj2.leak = obj1
        self.write('Leak')


class MemoryHandler(web.RequestHandler):

    def get(self):
        h = hpy()
        r = h.heap()
        self.write('<pre>')
        self.write(unicode(r))
        r = r.more
        self.write(unicode(r))
        r = r.more
        self.write(unicode(r))
        self.write('</pre>')


application = web.Application([
    (r'/leak', LeakHandler),
    (r'/memory', MemoryHandler),
], debug=True)


if __name__ == "__main__":
    options.parse_command_line()
    application.listen(5000)
    ioloop.IOLoop.instance().start()
```

```bash
nanvel-air:leaks nanvel$ curl http://localhost:5000/leak
Leak
...
nanvel-air:leaks nanvel$ curl http://localhost:5000/memory
<pre>
Partition of a set of 153822 objects. Total size = 206002744 bytes.
 Index  Count   %     Size   % Cumulative  % Kind (class / dict of class)
     0  83492  54 197180696  96 197180696  96 str
     1    341   0  2958200   1 200138896  97 dict (no owner)
     2  15243  10  1287768   1 201426664  98 tuple
     3  37662  24   903888   0 202330552  98 int
     4    202   0   652528   0 202983080  99 dict of module
     5   4172   3   534016   0 203517096  99 types.CodeType
     6   3994   3   479280   0 203996376  99 function
     7    493   0   457528   0 204453904  99 dict of type
     8    493   0   442384   0 204896288  99 type
     9    201   0   199128   0 205095416 100 dict of class
<188 more rows. Type e.g. '_.more' to view.> Index  Count   %     Size   % Cumulative  % Kind (class / dict of class)
    10    426   0   100816   0 205196232 100 list
    11   1187   1    94960   0 205291192 100 __builtin__.wrapper_descriptor
    12    844   1    74272   0 205365464 100 __builtin__.weakref
    13    885   1    63720   0 205429184 100 types.BuiltinFunctionType
    14    698   0    50256   0 205479440 100 __builtin__.method_descriptor
    15    178   0    41296   0 205520736 100 __builtin__.set
    16     19   0    40648   0 205561384 100 dict of email.LazyImporter
    17    585   0    34808   0 205596192 100 unicode
    18     26   0    31856   0 205628048 100 dict of abc.ABCMeta
    19     68   0    30024   0 205658072 100 _sre.SRE_Pattern
<178 more rows. Type e.g. '_.more' to view.> Index  Count   %     Size   % Cumulative  % Kind (class / dict of class)
    20     96   0    26880   0 205684952 100 dict of function
    21    355   0    25560   0 205710512 100 types.GetSetDescriptorType
    22     26   0    23504   0 205734016 100 abc.ABCMeta
    23     78   0    21840   0 205755856 100 dict of _weakrefset.WeakSet
    24    201   0    20904   0 205776760 100 class
    25    255   0    18360   0 205795120 100 types.MemberDescriptorType
>   26     48   0    13440   0 205808560 100 dict of __main__.LeakObject
    27    138   0    12144   0 205820704 100 __builtin__.property
    28     22   0    11536   0 205832240 100 dict of guppy.etc.Glue.Interface
    29    202   0    11312   0 205843552 100 module
<168 more rows. Type e.g. '_.more' to view.></pre>
```
