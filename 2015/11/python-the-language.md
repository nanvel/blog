labels: Blog
		Python
created: 2015-11-22T21:33
modified: 2015-11-22T22:53
visible: true

# Python, the language

[TOC]

## Syntax

### Variables

Variables are not boxes, they are labels attached to boxes.

```bash
>>> a = [1, 2, 3]
>>> b = a
>>> a.append(4)
>>> a
[1, 2, 3, 4]
>>> b
[1, 2, 3, 4]
>>> id(a)
4467670856
>>> id(b)
4467670856
>>> c = '123'
>>> d = '123'
>>> id(c)
4469989304
>>> id(d)
4469989304
>>> c = '1234'
>>> id(c)
4469989248
>>> id(d)
4469989304
```

The sharing of string literals is an optimization trchnique called interning. CPython also uses it for small numbers.

#### ```==``` vs ```is```

The ```==``` operator compares the values (uses ```__eq__()``` method) of objects (the data they hold), while ```is``` compares their identities.

### Tuples

Unpacking a tuple:

```bash
>>> a, b = (1, 2)
>>> a
1
>>> a, b, *other = range(5)
>>> a
0
>>> other
[2, 3, 4]
>>> a, *middle, b = range(5)
>>> b
4
>>> a, **middle, b = range(2)
  File "<stdin>", line 1
    a, **middle, b = range(2)
        ^
SyntaxError: invalid syntax
```

### Dicts

Dicts are fast but have significant memory overhead (because of hash table usage). They provide fast access regardless of the size of the dictionary.

Modifying the contents of a dict while iterating through it is a bad idea. Python may decide to rebuild the hash table and so positions of elements in the table may be changed.

In Python 3, the ```.keys()```, ```.items()``` and ```.values()``` methods return dictionary views, so they immediately reflect any changes to the dict.

### Arrays

[Arrays](https://docs.python.org/3/library/array.html) is mutable sequence that may contain only the same type objects. Also it supports additional methods allows to load and dump data to file.

```bash
>>> import array
>>> a = array.array('u')
>>> a.append(u'a')
>>> a.append(u'b')
>>> a.append(u'c')
>>> a
array('u', u'abc')
```

See also [```memoryview```](https://docs.python.org/3/c-api/memoryview.html).

> A memoryview is essentially a generalized NumPy array structure in Python itself (without the math). It allows you to share memory between data-structures (things like PIL images, SQLite databases, NumPy arrays, etc.) without first copying. This is very important for large data sets.
>
> Travis Oliphant

### Strings

Strings comparison:
```bash
>>> s1 = 'café'
>>> s2 = 'cafe\u0301'
>>> s2, s2
('café', 'café')
>>> len(s1), len(s2)
(4, 5)
>>> s1 == s2
False
```

Two strings are canonical equivalents but different sequences. We need to normalize strings before comparizon (see [unicodedata.normalize](https://docs.python.org/3.5/library/unicodedata.html#unicodedata.normalize)).

### Functions

Functions in Python are first-class objects (like integers, strings, dictionaries):

- created on runtime
- assigned to variable or element in a data structure
- passed as an argument to a function
- returned as the result of a function

```bash
>>> dir(a)
['__annotations__', '__call__', ... , '__str__', '__subclasshook__']
>>> a.__str__()
'<function a at 0x10ab872f0>'
```

#### Key-only arguments in Python 3

To specify keyword-only arguments when defining a function, name them after the argument prefixed with ```*```. If you don't wan't to support variable positional arguments but still want keyword-only arguments, put a ```*``` by itself in the signature:

```bash
>>> def f(a, *, b):
...   print(a, b)
... 
>>> f(1, 2)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: f() takes 1 positional argument but 2 were given
>>> f(1, b=2)
1 2
>>> f(1, 2, b=3)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: f() takes 1 positional argument but 2 positional arguments (and 1 keyword-only argument) were given
```

#### Function annotation

Python 3 provides syntax to attach metadata to the parameters of a functiondeclaration and it's return value.

```bash
>>> def f(a:str, b:'int < 10') -> str:
...   return a * b
... 
>>> f('a', 2)
'aa'
>>> f('a', 15)
'aaaaaaaaaaaaaaa'
>>> f(a=1, b=15)
15
>>> f.__annotations__
{'a': <class 'str'>, 'return': <class 'str'>, 'b': 'int < 10'}
```

No processing is done with the annotations. They are merely stored in the ```__annotations__```  attribute of the function and have no meaning to the Python interpreter. Annotations may be used by tools such as IDEs, frameworks, and decorators.

#### Local and global variables

```bash
>>> def a():
...   print(id)
... 
>>> def b():
...   print(id)
...   id = 1
... 
>>> a()
<built-in function id>
>>> b()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 2, in b
UnboundLocalError: local variable 'id' referenced before assignment
>>> def c():
...   global id
...   print(id)
...   id = 1
... 
>>> c()
<built-in function id>
>>> c()
1
```

When Python compiles the body of the ```b``` function, it decides that ```id``` is a local variable because it is assigned whithin the function.

#### Mutable types as parameter defaults

Don't do it.

```bash
>>> def f(a=[]):
...   a.append(1)
...   print(a)
... 
>>> f()
[1]
>>> f()
[1, 1]
```

### List comprehensions

List comprehensions has their own local scope in Python 3:

```bash
# python3.5
>>> [i for i in '123']
['1', '2', '3']
>>> i = 1
>>> [i for i in '123']
['1', '2', '3']
>>> i
1
```

```bash
# python2.7
>>> [i for i in '123']
['1', '2', '3']
>>> i = 1
>>> [i for i in '123']
['1', '2', '3']
>>> i
'3'
```

### Slycing

Excluding the last item in slices and ranges works well:

- It's easy to see the length of a slice or range when only the stop position is given: ```range(3)``` and ```my_list[:3]``` both produce 3 items
- It's easy to compute the length of a slice or range when start and stop are given: just substract ```stop - start```
- It's easy to split a sequence in two parts at any index x, without overlapping: simply get ```my_list[:x]``` and ```my_list[x:]```

```bash
a = (1, 2, 3, 4, 5, 6, 7, 9, 10)
# a = [start:stop:step]
>>> a = (1, 2, 3, 4, 5, 6, 7, 9, 10)
>>> a[0:6:1]
(1, 2, 3, 4, 5, 6)
>>> a[0:6:2]
(1, 3, 5)
>>> a[0:6:3]
(1, 4)
```

Reverse:
```bash
>>> a = '123'
>>> a[::-1]
'321'
```

### Sorting

Sort list in place:
```bash
>>> a = [1, 3, 2]
>>> a.sort()
>>> a
[1, 2, 3]
```

Sort using ```sorted``` function:
```bash
>>> a = [1, 3, 2]
>>> sorted(a)
[1, 2, 3]
>>> a
[1, 3, 2]
```

Sorting algorithm Python uses in [Timsort](https://en.wikipedia.org/wiki/Timsort), an adaptive algotithm that switches from insertion sort to merge sort strategies depending on how ordered the data is.

### Generators

There are two ways to define a generator:

- generator comprehension
- function with yield statemant

```bash
>>> a = (i for i in (1, 2, 3))
>>> type(a)
<class 'generator'>
>>> def b():
...   for i in (1, 2, 3):
...     yield i
... 
>>> type(b)
<class 'function'>
>>> for i in a:
...   print(i)
... 
1
2
3
>>> for i in b():
...   print(i)
... 
1
2
3
```

### Magic methods

Why we use ```len(collection)``` instead of ```collection.length()``` or why we use ```a == b``` instead of ```a.is_equal(b)```?

The answer is: following [Python data model](https://docs.python.org/3/reference/datamodel.html) API allows your own objects play well with the most ideomatic language features.

!!! hint "Object model"
	[object model](https://en.wikipedia.org/wiki/Object_model) is the properties of objects in general in a specific computer programming language.

Talking about ```len```, it is not just a shortcut to ```sequence.__len__()```, it can work even with objects without ```__len__``` method (if the object is iterable, then ```len``` will try to count all items iterating throw them).

Another benefit of ```len``` is that you don't need to memorize which function name you used to return number of items: ```.length()``` or ```.size()```. According to [PEP-20](https://www.python.org/dev/peps/pep-0020/): There should be one-- and preferably only one --obvious way to do it.

[```bool``` function](https://docs.python.org/3/reference/datamodel.html#object.__bool__) also has pretty interesting logic behind:

- returns True for all user defined functions without ```__bool__``` and ```__len__``` by default
- returns True is ```__bool__``` is defined and returns True
- returns True if ```__len__``` is defined and returns number > 0

```bash
>>> class A(object):
...   pass
... 
>>> class B(object):
...   def __bool__(self):
...     return False
... 
>>> class C(object):
...   def __len__(self):
...     return 0
... 
>>> D = []
>>> 
>>> bool(A)
True
>>> bool(B)
True
>>> bool(C)
True
>>> bool(D)
False
```

### Non-ASCII identifiers in Python 3

Python 3 allows [non-ASCII identifiers](https://www.python.org/dev/peps/pep-3131/) in sourse code:
```bash
>>> こ = 'ko'
```

The only usefull purpose is teaching children programming.

### Callables

There are 7 flavors of callbale objects in Python:

- User-defined functions (using def or lambda)
- Built-in functions (functions implemented in C, like time.strftime)
- Built-in methods (like dict.get)
- Methods (functions defined in the body of a class)
- Classes (runs ```__new__``` and ```__init__``` methods)
- Class instances (if a ```__call__``` method is defined)
- Generator functions (returns a generator object)

Use ```callable()``` function to check if object is callable.

### Decorators

## Standard library

### collections.namedtuple

Namedtuple represents object with only data user attributes, it uses less memory and is immutable.

```bash
>>> class A(object):
...   def __init__(self, a, b):
...     self.a = a
...     self.b = b
... 
>>> from collections import namedtuple
>>> B = namedtuple('B', ['a', 'b'])
>>> a = A(a=1, b=2)
>>> b = B(a=1, b=2)
>>> type(a)
<class '__main__.A'>
>>> type(b)
<class '__main__.B'>
>>> a.a
1
>>> b.a
1
>>> a.a = 3
>>> b.a = 3
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: can't set attribute
```

### collections.defaultdict

```bash
>>> a = {}
>>> b = defaultdict(list)
>>> a['x'].append(1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'x'
>>> b['x'].append(1)
>>> a
{}
>>> b
defaultdict(<type 'list'>, {'x': [1]})
>>> dict(b)
{'x': [1]}
```

### map, filter, reduce

Use list/generator comprehensions instead.

```bash
>>> list(map(int, '123'))
[1, 2, 3]
>>> list(filter(lambda i: i > 2, [1, 2, 3]))
[3]
>>> from functools import reduce
>>> from operator import add
>>> reduce(add, [1, 2, 3])
6
```

### functools.lru_cache

[Functools docs](https://docs.python.org/3/library/functools.html#functools.lru_cache).
LRU stands for **L**east **R**ecently **U**sed.

### weekref

> Objects are never explicitly destroyed; hower, when they become unreachable they may be garbage-collected.
>
> "Data Model" chapter of The Python Language Reference

The [weakref module](https://docs.python.org/2/library/weakref.html) allows the Python programmer to create weak references to objects.

A weak reference to an object is not enough to keep the object alive: when the only remaining references to a referent are weak references, garbage collection is free to destroy the referent and reuse its memory for something else. Commonly uses to implement caches.

```bash
>>> import weakref
>>> class A(object):
...   pass
... 
>>> a = A()
>>> b = weakref.ref(a)
>>> id(a)
4359552808
>>> id(b())
4359552808
>>> del(a)
>>> b() is None
True
```

```list``` and ```dict``` types do not directly support weak references.

## QA

### Where is object?

Objects are everywhere.

```bash
>>> type('1')
<class 'str'>
>>> type(1)
<class 'int'>
>>> type(None)
<class 'NoneType'>
>>> import sys
>>> type(sys)
<class 'module'>
>>> def a():
...   pass
... 
>>> type(a)
<class 'function'>
```

## Vocabulary

### Dunder-method

Methods like ```__eq__```, ```__getitem__```.
Also known as special or magic methods.

!!! hint "Magic"
	"Magic method" term was adopted from Ruby. Actually, these methods are oposite to magic, their behavior quite strainforward.

### Immutable

We can't modify it.

Immutable types in Python are: tuple.

```bash
>>> a = (1, 2, 3)
>>> a[0] = 5
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
>>> b = [1, 2, 3]
>>> b[0] = 5
>>> b
[5, 2, 3]
```

### Infix operators

Creates new object and don't touch their operands.

### Modification in place

When we pass mutable object as argument to function where it would be modified. This type of fuctions must return None value (it makes clear to the caller that the object itself was changed, and no new object was created).

```bash
>>> a = {'a': 1}
>>> def f(x):
...   x['a'] += 1
... 
>>> f(a)
>>> a
{'a': 2}
```

### Container sequence vs flat sequence

Are represent different memory models of the sequence types.

**Container squence** means some objects contain references to other objects.
Container sequences can be nested because they may contain objects of any type, including their own type.

**Flat sequences** hold simple atomic types like integers, floats, or characters.
Examples: string, array.

According to The Fluent Python book.

### Hashable

> An object is hashable if it has a hash value which never changes during its lifetime (it needs a ```__hash__()``` method), and can be compared to other objects (it needs an ```__eq__()``` method). Hashable objects which compare equal must have the same hash value.
>
> [Python Glossary](https://docs.python.org/2/glossary.html)

User-defined types are hashable by default because their hash value is their ```id()``` and they all compare not equal.

```bash
>>> a = [1, 2]
>>> hash(a)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'list'
>>> a = (1, 2)
>>> hash(a)
3713081631934410656
```

### Closures

A closure is a function with an extended scope that encompasses nonglobal variables referenced in the body of the function but not defined there (can access nonglobal variables that are defined outside of its body).

An example from the Fluent Python book:
```bash
>>> def make_averager():
...   series = []
...   def averager(value):
...     series.append(value)
...     total = sum(series)
...     return total / len(series)
...   return averager
... 
>>> avg = make_averager()
>>> avg(10)
10.0
>>> avg(11)
10.5
>>> avg(12)
11.0
>>> avg.__code__.co_varnames
('value', 'total')
>>> avg.__code__.co_freevars
('series',)
>>> avg.__closure__[0].cell_contents
[10, 11, 12]
```

Each item in ```avg.__closure__``` corresponds to a name in ```avg.__code__.co_freevars```.

### Deep and shallow copies

Deep copies don't share references of embedded objects.

```bash
>>> class C(object):
...   def __init__(self, a):
...     self.a = a
... 
>>> c = C(a={'x': 1})
>>> id(c.a)
4333741320
>>> id(c)
4334968616
>>> import copy
>>> c1 = copy.copy(c)
>>> c2 = copy.deepcopy(c)
>>> id(c1)
4334968784
>>> id(c2)
4335046952
>>> id(c1.a)
4333741320
>>> id(c2.a)
4335027272
```

```id(c1.a) == id(c.a)``` but ```id(c2.a) != id(c.a)```.

## Links

[Fluent Python](http://www.amazon.com/Fluent-Python-Luciano-Ramalho-ebook/dp/B0131L3PW4/) by Luciano Ramalho
