labels: Draft
        Python
created: 2022-10-22T16:45
modified: 2022-11-27T17:36
place: Bangkok, Thailand
comments: true

# Python 3 standard library notes

loc: 394

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

## Tools

venv:
```console
python3 -m venv .venv                             
source .venv/bin/activate
```

## Links

[Python 3 Standard Library by Example](https://www.amazon.com/Python-Standard-Library-Example-Developers-ebook/dp/B072QZZDV7/) by Doug Hellmann
