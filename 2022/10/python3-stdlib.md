labels: Draft
        Python
created: 2022-10-22T16:45
modified: 2022-11-27T17:36
place: Bangkok, Thailand
comments: true

# Python 3 standard library notes

loc: 4359

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

## Tools

venv:
```console
python3 -m venv .venv                             
source .venv/bin/activate
```

## Links

[Python 3 Standard Library by Example](https://www.amazon.com/Python-Standard-Library-Example-Developers-ebook/dp/B072QZZDV7/) by Doug Hellmann
