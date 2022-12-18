labels: Draft
        Python
created: 2022-10-22T16:45
modified: 2022-12-18T12:54
place: Bangkok, Thailand
comments: true

# Python 3 standard library notes

loc: 818

## Syntax

`...` is equal to `pass` for an empty class.

## Modules

`collections`:

- `Deque` - double-ended queue
- `defaultdict`
- `OrderedDict`
- [`array`](https://docs.python.org/3/library/array.html) - limited to a single type
- [heapq](https://docs.python.org/3/library/heapq.html) - maintains list sorted
- [bisect](https://docs.python.org/3/library/bisect.html) - maintains list sorted
- [ChainMap](https://docs.python.org/3/library/collections.html#collections.ChainMap) - combines dicts
- [Counter](https://docs.python.org/3/library/collections.html#collections.Counter) - counting hashable objects

## Regexp

```python
# finditer() returns an iterator that produces Match instances instead of strings returned by findall()
r = re.compile(r'(\d+)')

list(r.finditer('1, 100'))
# [<re.Match object; span=(0, 1), match='1'>,
#  <re.Match object; span=(3, 6), match='100'>]
```

Regular expression flags:

- `ASCII`: ASCII-only matching
- `IGNORECASE`: ignore case
- `MULTILINE`: multi-line
- `DOTALL`: dot matches all
- `VERBOSE`: verbose
- `LOCALE`: locale dependent
- `DEBUG`: display debug information

## `functools.singledispatch`

```python
from functools import singledispatch


@singledispatch
def myfunc(arg):
    print("Default")


@myfunc.register(int)
def myfunc_int(arg):
    print("Int")


@myfunc.register(list)
def myfunc_list(arg):
    print("List")


myfunc('s')
myfunc(1)
myfunc([1])
```

## `itertools.chain`

```python
from itertools import chain


for i in chain([1, 2, 3], [4, 5, 6]):
    print(i)
```

## `itertools.islice`

```python
islice(range(100), 5)  # first 5
islice(range(100), 5, 10)  # 5 to 10
islice(range(100), 0, 100, 10)  # 0, 10, 20, ...
```

## `itertools.dropwhile`, `itertools.takewhile`

dropwhile: after the condition is False for the first time - all remaining are returned.

```python
from itertools import dropwhile


dropwhile(lambda x: x < 10, [-1, 1, 10, 100])
```

## `itertools.compress`

```python
from itertools import cycle, compress


every_third = cycle([False, False, True])
data = range(10)

compress(data, every_third)  # [2, 5, 8]
```

## `itertools.groupby`

```python
import operator
from itertools import groupby


for k, g in groupby(data, operator.attgetter('x')):
    print(k, g)
```

## `itertools.accumulate`

```python
from itertools import accumulate


accumulate(range(5))  # 0, 1, 3, 6, 10
```

## `itertools.product`

```python
list(product(['a', 'b'], ['0', '1']))
# [('a', '0'), ('a', '1'), ('b', '0'), ('b', '1')]
```

## `itertools.permutations`, `itertools.combinations`

Items from the given input, combined in possible permutations of the given length.

```python
from itertools import permutations, combinations


list(permutations([1, 2, 3], 2))
# [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]

list(combinations([1, 2, 3], 2))
# [(1, 2), (1, 3), (2, 3)]
```

`combinations` - unique combinations.

## `operator`

```python
lt(a, b)
le(a, b)
ne(a, b)
...

neg(a)
truediv(a, b)
...

and_(a, b)
invert(c)
...

attrgetter('arg')
itemgetter(0)
```

## `time`

```python
time()  # system "wall clock"
monotonic()  # have to be used for elapsed time (never moves backward)
perf_counter()  # clock with highest resolution
clock()  # cpu time
process_time()  # cpu time


time.get_clock_info('monotonic')
# namespace(implementation='mach_absolute_time()', monotonic=True, adjustable=False, resolution=4.166666666666667e-08)
```

## `statistics`

```python
from statistics import mean


# average
mean([10, 5, 4, 2, 7, 9])
# 6.166666666666667

# most common
mode([10, 5, 4, 2, 7, 9, 2])
# 2

median([10, 5, 4, 2, 7, 9])
# 6.0
median_low([10, 5, 4, 2, 7, 9])
# 5
median_high([10, 5, 4, 2, 7, 9])
# 7

# standard deviation
variance([10, 5, 4, 2, 7, 9])
# 9.366666666666667
stdev([10, 5, 4, 2, 7, 9])
# 3.0605010483034745
```

## `linecache`

Randomly access files by line number.

## `shutil`

High level file operations such as file and directory copy, creating and extracting archives.

## `filecmp`

Compare files and directories.

Compare directories:
```python
import filecmp


dc = filecmp.dircmp('example/dir1', 'example/dir2')
dc.report()
```

## `os.path`

```python
os.path.commonprefix(['/one/two/three', '/one/two'])
# '/one/two'

os.sep
# '/'

os.path.normpath('/one/two/.././abc.txt')
# '/one/abc.txt'

os.path.getatime(path)  # access time
os.path.getmtime(path)  # modification time
os.path.getctime(path)  # creation time
os.path.getsize(path)  # size in bytes
```

## `pathlib`

System path as objects.

```python
import pathlib


f = pathlib.Path('example.txt')

# if f.exists(): ...

f.write_bytes("Example content".encode('utf-8'))

with f.open('r', encoding='utf-8') as handle:
    handle.read()
```

Deleting files: for files, symbolic links, and most other path types, use `unlink()`.

## `glob`

Filename pattern matching.

```python
import glob


for name in sorted(glob.glob('dir/*')):
    print(name)
```

`fnmatch` - unix-style glob pattern matching.

## `linecache`

Read text files efficiently.

## `tempfile`

Creating temporary files with unique names securely, so they cannot be guessed by someone wanting to break the application or steal the data.

Spooled files: hold files in memory.

```python
import tempfile


with tempfile.SpooledTemporaryFile(max_size=100, mode='w+t', encoding='utf-8') as temp:
    # temp._rolled, temp._file  # rollover to disk?
    ...
```

## `mmap`

Memory-map files.


## `codecs`

`codecs` provide classes that manage the data encoding and decoding, so applications do not have to do that work.

```python
with codecs.open(filename, mode='w', encoding=encoding) as f:
    ...
```

Error handling modes:

- strict
- replace
- ignore
- xmlcharrefreplace
- backslashreplace

Python includes codecs for working with base64, bzip2, ROT-13, ZIP, and other data formats.

```python
import codecs
import io


buffer = io.StringIO()
stream = codecs.getwriter('rot-13')(buffer)

text = 'example text'

stream.write(text)
stream.flush()
print(buffer.getvalue())
```

`IncrementalEncoder`, `IncrementalDecoder`: for large data sets, encodings operate better incrementally, working on one small chunk of data at a time.

## `pickle`

Objects that have non-pickable attributes can define `__getstate__()` and `__setstate__()` to return a subset of the state of the instance to be pickled.

## `shelve`

Persistent storage of objects.

```python
import shelve


with shelve.open('test_shelf.db') as s:
    s['key1'] = {
        'int': 10,
        's': 'string',
    }
```

## Tools

venv:
```console
python3 -m venv .venv                             
source .venv/bin/activate
```

## Links

[Python 3 Standard Library by Example](https://www.amazon.com/Python-Standard-Library-Example-Developers-ebook/dp/B072QZZDV7/) by Doug Hellmann
