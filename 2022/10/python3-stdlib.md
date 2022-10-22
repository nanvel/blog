labels: Draft
        Python
created: 2022-10-22T16:45
modified: 2022-10-22T16:45
place: Bangkok, Thailand
comments: true

# Python 3 standard library notes

loc: 1503

## Regexp

```python
# finditer() returns an iterator that produces Match instances instead of strings returned by findall()
r = re.compile(r'(\d+)')

list(r.finditer('1, 100'))
# [<re.Match object; span=(0, 1), match='1'>,
#  <re.Match object; span=(3, 6), match='100'>]
```

## Tools

venv:
```console
python3 -m venv .venv                             
source .venv/bin/activate
```

## Links

[Python 3 Standard Library by Example](https://www.amazon.com/Python-Standard-Library-Example-Developers-ebook/dp/B072QZZDV7/) by Doug Hellmann
