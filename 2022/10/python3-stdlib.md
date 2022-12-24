labels: Python
created: 2022-10-22T16:45
modified: 2022-12-24T12:52
place: Bangkok, Thailand
comments: true

# Python 3 standard library notes

[TOC]

## Syntax

`...` is equal to `pass` for an empty body.

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

## enum

Defines enumeration type.

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

## functools.singledispatch

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

## itertools.chain

```python
from itertools import chain


for i in chain([1, 2, 3], [4, 5, 6]):
    print(i)
```

## itertools.islice

```python
islice(range(100), 5)  # first 5
islice(range(100), 5, 10)  # 5 to 10
islice(range(100), 0, 100, 10)  # 0, 10, 20, ...
```

## itertools.dropwhile, itertools.takewhile

dropwhile: after the condition is False for the first time - all remaining are returned.

```python
from itertools import dropwhile


dropwhile(lambda x: x < 10, [-1, 1, 10, 100])
```

## itertools.compress

```python
from itertools import cycle, compress


every_third = cycle([False, False, True])
data = range(10)

compress(data, every_third)  # [2, 5, 8]
```

## itertools.groupby

```python
import operator
from itertools import groupby


for k, g in groupby(data, operator.attgetter('x')):
    print(k, g)
```

## itertools.accumulate

```python
from itertools import accumulate


accumulate(range(5))  # 0, 1, 3, 6, 10
```

## itertools.product

```python
list(product(['a', 'b'], ['0', '1']))
# [('a', '0'), ('a', '1'), ('b', '0'), ('b', '1')]
```

## itertools.permutations, itertools.combinations

Items from the given input, combined in possible permutations of the given length.

```python
from itertools import permutations, combinations


list(permutations([1, 2, 3], 2))
# [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]

list(combinations([1, 2, 3], 2))
# [(1, 2), (1, 3), (2, 3)]
```

`combinations` - unique combinations.

## operator

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

## time

```python
time()  # system "wall clock"
monotonic()  # have to be used for elapsed time (never moves backward)
perf_counter()  # clock with highest resolution
clock()  # cpu time
process_time()  # cpu time


time.get_clock_info('monotonic')
# namespace(implementation='mach_absolute_time()', monotonic=True, adjustable=False, resolution=4.166666666666667e-08)
```

## statistics

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

## linecache

Randomly access files by line number.

## shutil

High-level file operations, such as file and directory copy, creating and extracting archives.

## filecmp

Compare files and directories.

Compare directories:
```python
import filecmp


dc = filecmp.dircmp('example/dir1', 'example/dir2')
dc.report()
```

## os.path

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

## pathlib

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

## glob

Filename pattern matching.

```python
import glob


for name in sorted(glob.glob('dir/*')):
    print(name)
```

`fnmatch` - unix-style glob pattern matching.

## linecache

Read text files efficiently.

## tempfile

Creating temporary files with unique names securely, so they cannot be guessed by someone wanting to break the application or steal the data.

Spooled files: hold files in memory.

```python
import tempfile


with tempfile.SpooledTemporaryFile(max_size=100, mode='w+t', encoding='utf-8') as temp:
    # temp._rolled, temp._file  # rollover to disk?
    ...
```

## mmap

Memory-map files.


## codecs

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

## pickle

Objects that have non-pickable attributes can define `__getstate__()` and `__setstate__()` to return a subset of the state of the instance to be pickled.

## shelve

Persistent storage of objects.

```python
import shelve


with shelve.open('test_shelf.db') as s:
    s['key1'] = {
        'int': 10,
        's': 'string',
    }
```

## dbm

Unix key-value databases.

## sqlite3

Embedded relational database. Implements a Python DB-API 2.0.

SQLite is designed to be embedded in applications, instead of using a separate database server program.

```python
import sqlite3
import sys


db_filename = 'todo.db'
project_name = sys.argv[1]


with sqlite3.connect(db_filename) as conn:
    cursor = conn.cursor()

    query = """
        SELECT id, priority, details, status, deadline
        FROM task
        WHERE project = ?  # WHERE project = :project_name
    """

    cursor.execute(query, (project_name,))
    # cursor.execute(query, {'project_name': project_name})

    for row in cursor.fetchall():
        pass
```

Locking modes (isolation levels):

- Deferred (default) - locks once when change is begun
- Immediate - locks as soon as a change starts and prevents other cursors from making changes until the transaction is committed
- Exclusive - Locks the database to all readers
- None - auto-commit mode

In-memory:
```python
with sqlite3.connect(':memory:') as conn:
    ...
```

Python functions in SQL:
```python
def decrypt(s):
    return codecs.encode('s', 'rot-13')


with qlite3.connect(db_filename) as conn:
    conn.create_function('decrypt', 1, decrypt)
    cursor = conn.cursor()
    query = "SELECT id, decrypt(details) FROM task;"
```

Regexp:
```python
query = "SELECT * FROM table WHERE column REGEXP'.*pattern.*';"
```

## csv

Comma-separated value files.

Quote:

- QUOTE_ALL (quote all regardless of type)
- QUOTE_MINIMAL (quote fields with special characters)

Dialects: `csv.list_dialects()`: `excel`, `excel-tabs`, `unix`, can register new.

DictReader and DictWriter.

## zlib

GNU zlib compression.

```python
compressed = zlib.compress(data, level)  # levels 0-9 
```

Checksums:
```python
checksum = zlib.adler32(data)  # adler32, crc32
```

## tarfile

Tar archive access.

## zipfile

ZIP archive access.

## hashlib

Generating signatures of message content using standard algorithms such as MD5 and SHA.

`hmac` - for verifying that a message has not been altered.

## signal

Asynchronous system events.
Exposes the Unix signal mechanism for sending events to other processes.

## concurrent.futures

Manage pools of concurrent tasks.
Implementation of thread and process-based executors for managing resource pools for running concurrent tasks.

Executors are used for managing pools of workers, and futures are used for managing results computed by the workers.

```python
with futures.ThreadPoolExecutor(max_workers=2) as ex:
    f = ex.submit(task, 5)
    result = f.result()
```

## subprocess

`run()` function was added in Python 3.5.

```python
import subprocess


completed = subproces.run(['ls', '-l'])
print(completed.returncode)
```

Pass PIPE for the stdout and stderr arguments to capture the output.

```python
cat = subprocess.Popen(
    ['cat', 'index.rst'],
    stdout=subprocess.PIPE
)

print(cat.stdout)
```

Exit codes:

- `== 0`: no error
- `> 0`: the process had an error and exited
- `< 0`: the process was killed with a signal

## threading

To wait for a daemon thread has completed its work, use the `join()` method.

`enumerate()` returns a list of active Thread instances:
```python
main_thread = threading.main_thread()
for t in main_thread.enumerate():
    if t is main_thread:
        continue
    ...
```

Event objects are a simple way to communicate between threads safely.

Lock object - guard against simultaneous access to an object.

Barriers - another thread synchronization mechanism.


## asyncio

Asynchronous I/O, Event Loop, and Concurrency Tools.

Single-thread, single-process approach in which parts of an application cooperate to switch tasks explicitly at optimal times.

[A Brief History of Python Async](https://nanvel.name/2022/11/talk-async)

## selectors

Provides a high-level interface for watching multiple sockets simultaneously.

## socket

Network communication.

UDP - user datagram protocol. Provides unreliable delivery of individual messages. Is commonly used where the order is less important and multicasting.

TCP - transmission control protocol. Provides byte stream between the client and the server, ensuring message delivery of failure notification through timeout management, retransmission, and other features.

## socketserver

Creating network servers.

## urllib

`parse` - manipulates URL strings.

`request` - API for retrieving content remotely.

`http.server` - create a web server.

`http.cookies` - parse cookies.

`urllib.parse.urldefrag` - parse, break url into components.

## base64

Encode binary data with ASCII.

## uuid

Universal Unique Identifiers as described in RFC-4122.

Does not require a central registar and can guarantee uniqueness across space and time.

`uuid1()` - uses host MAC.

`uuid3()` and `uuid5()` - name based values.

`uuid4()` - random values.

## json

Compact:
```python
json.dumps(data, separators=(',', ':'))
```

`json.tool` - command-line program for reformatting JSON data to be easier to read:
```bash
python3 -m json.tool example.json
```

## smtplib

Comunicates with an email server to deliver a message.

`smtpd` - create a custom mail server.

`imaplib` - uses IMAP protocol to manipulate messages.

`mailbox` - store and modify local messages archive.

## Command-line application

`argparse` - Interface for parsing and validating command-line arguments.

`getopt` - low-level arguments processing.

`getpass` - securely prompt the user for a password or other secret value.

`cmd` - a framework for interactive, command-driven shell-style programs.

`shlex` - a parser for shell-style syntax.

`configparser` - manage application configuration files.

`fileinput` - read from files, command-line filter framework.

`atexit` - schedule function to call on program shutting down.

`sched` - scheduler for triggering events and specific times in the future.

## readline

Interface for the GNU readline library (useful for command line completion).

## Internationalization and localization

`gettext` - create message catalogs.

`locale` - cultural localization API. Changes the way numbers, currency, dates, and times are formatted.

Environment:
```bash
LANG_en_US LC_CTYPE=en_US LC_ALL=en_US python3 ...
```

## Developer tools

`trace` - monitors the way Python executes a program.

`profile`, `timeit` - measure the speed of a program.

`tabnanny` - scanner that reports ambiguous use of indentation.

## unittest

Based on XUnit framework design by Kent Beck and Erich Gamma.

Test classes and methods can be decorated with `skip()` to always skip the tests.
`skipIf()` and `skipUnless()` - skip with conditions.

The test can raise SkipTest directly to cause the test to be skipped.

`subTest`:
```python
def test_with_subtest(self):
    for pat in ['a', 'B', 'c', 'D']:
        with self.subTest(pattern=pat):
            self.assertRegex('abc', pat)
```

`expectFailure`:
```python
@unittest.expectedFailure
def test_never_passes(self):
    self.assertTrue(False)
```

## trace

```python
import trace


tracer = trace.Trace(count=False, trace=True)
tracer.run('example(1)')
```

Or using the tool:
```console
python3 -m trace example.py
```

## pdb

Interactive debugger.

`inspect` - inspect live objects.

## pyclbr

Class browser: scan Python source files to find both classes and stand-alone functions.

## System

`sys` - focused on interpreter settings.

`os` - provides access to the operating system.

`platform` - system version information.

`sysconfig` - interpreter compile-time configuration.

```python
sys.stdin.read()
```

## Importlib

Exposes the underlying implementation of the import mechanism used by the interpreter, can be used to import modules dynamically.

## Memory management and limits

CPython uses reference counting and garbage collection to perform automatic memory management.

## Tools

venv:
```console
python3 -m venv .venv                             
source .venv/bin/activate
```

docs:
```console
pydoc -p 5000
```

## Links

[Python 3 Standard Library by Example](https://www.amazon.com/Python-Standard-Library-Example-Developers-ebook/dp/B072QZZDV7/) by Doug Hellmann
