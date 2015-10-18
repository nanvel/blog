labels: Blog
        Python
created: 2014-11-20T23:15
place: Kyiv, Ukraine

# Python dict.get()

I am amazed how I did this mistake for 2 days in row.

```python
>>> isinstance(a, dict)
True
>>> a.get('a', '')[:100]
'1'
```

I thought it always returns a string ...

```python
>>> a.get('b', '')[:100]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'NoneType' object has no attribute '__getitem__'
```

The dict is:
```python
a = {'a': 1, 'b': None}
```

The proper way is:
```python
>>> (a.get('b') or '')[:100]
''
```
