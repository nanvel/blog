labels: Blog
        Python
created: 2015-11-22T21:33
modified: 2016-11-29T18:30
place: Kyiv, Ukraine
visible: true
comments: true

# Python, the language notes

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

The sharing of string literals is an optimization technique called interning. CPython also uses it for small numbers.

#### Non-ASCII identifiers in Python 3

Python 3 allows [non-ASCII identifiers](https://www.python.org/dev/peps/pep-3131/) in sourse code:
```bash
>>> こ = 'ko'
```

May be useful for teaching children programming.

### Objects

Everything in Python is an object:
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

#### object to type relation

The classes object and type have unique relationship: object is an instance of type, and type is a subclass of object. This is magic.

#### ```==``` vs ```is```

The ```==``` operator compares the values (uses ```__eq__()``` method) of objects (the data they hold), while ```is``` compares their identities.

#### Private attributes

> Never, ever use two leading underscores. This is annoyingly private. If name clashes are a concern, use explicit name mangling insted (e.g, ```_MyThing_blahblah```). This is essentially the same thing as double-underscore, only it's transparent where double underscore obscures.
>
> Ian Bicking, creator of pip, virtualenv and many other projects

```bash
>>> class A(object):
...   __a = 1
...   def get(self):
...     return self.__a
...
>>> a = A()
>>> a.__a
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'A' object has no attribute '__a'
>>> a.get()
1
>>> a._A__a
1
```

#### ```__str__``` vs ```__repr__```

```__repr__``` returns a string representing the object sa the developer wants to see it.
```__str__``` returns a string representing the object as the user wants to see it.

#### Magic methods

Why we use ```len(collection)``` instead of ```collection.length()``` or why we use ```a == b``` instead of ```a.is_equal(b)```?

The answer is: following [Python data model](https://docs.python.org/3/reference/datamodel.html) API allows your own objects play well with the most idiomatic language features.

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

### Classes

Class is an object. Therefore each class must be an instance of some other class. By default, Python classes are instances of ```type```. To avoid infinite regress, type is an instance of itself.

```bash
>>> object.__class__
<class 'type'>
>>> type.__class__
<class 'type'>
```

#### Inheritance

Multiple inheritance in Python is allowed but it is bad practice.
In many cases inheritance may be replaced by [composition](http://learnpythonthehardway.org/book/ex44.html).

### Functions

Functions in Python are first-class objects (like integers, strings, dictionaries):

- created on runtime
- assigned to variable or element in a data structure
- passed as an argument to a function
- returned as the result of a function

!!! note "First-class object"
    In programming, something is said to be a first-class citizen when it can be used as a value, meaning it can be passed into a function, returned from a function, and assigned to a variable.

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

Python 3 provides syntax to attach metadata to the parameters of a function declaration and it's return value.

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

When Python compiles the body of the ```b``` function, it decides that ```id``` is a local variable because it is assigned within the function.

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

#### Modification in place

When we pass mutable object as argument to function where it would be modified. This type of functions must return None value (it makes clear to the caller that the object itself was changed, and no new object was created).

```bash
>>> a = {'a': 1}
>>> def f(x):
...   x['a'] += 1
...
>>> f(a)
>>> a
{'a': 2}
```

#### Closures

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

Two strings are canonical equivalents but different sequences. We need to normalize strings before comparison (see [unicodedata.normalize](https://docs.python.org/3.5/library/unicodedata.html#unicodedata.normalize)).

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

### Dicts

Dicts are fast but have significant memory overhead (because of hash table usage). They provide fast access regardless of the size of the dictionary.

Modifying the contents of a dict while iterating through it is a bad idea. Python may decide to rebuild the hash table and so positions of elements in the table may be changed.

In Python 3, the ```.keys()```, ```.items()``` and ```.values()``` methods return dictionary views, so they immediately reflect any changes to the dict.

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
- It's easy to compute the length of a slice or range when start and stop are given: just subtract ```stop - start```
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

Sorting algorithm Python uses in [Timsort](https://en.wikipedia.org/wiki/Timsort), an adaptive algorithm that switches from insertion sort to merge sort strategies depending on how ordered the data is.

### Iterators

Every collection in Python is iterable.
```bash
>>> s = 'abc'
>>> for c in s:
...   print(c)
...
a
b
c
```

If an object has ```__getitem__``` and ```__len__``` methods, it is iterable:
```bash
>>> class C(object):
...   _a = (1, 2, 3)
...   def __len__(self):
...     return len(self._a)
...   def __getitem__(self, index):
...     return self._a[index]
...
>>> for c in C():
...   print(c)
...
1
2
3
```

Another way to create an iterable object is to define ```__iter__``` method that returns an iterator:
```bash
>>> class C(object):
...   def __init__(self):
...     self._a = (1, 2, 3)
...   def __iter__(self):
...     return self._a.__iter__()
...
>>> for c in C():
...   print(c)
...
1
2
3
```

We can create our own iterator, it sould be a class with ```__iter__``` and ```__next__``` methods. ```__iter__``` should return ```self``` and ```__next__``` should raise ```StopIteration``` when there are no further items:
```bash
>>> class CIterator(object):
...   def __init__(self, items):
...     self._items = items
...     self._position = 0
...   def __iter__(self):
...     return self
...   def __next__(self):
...     if self._position >= len(self._items):
...       raise StopIteration()
...     self._position += 1
...     return self._items[self._position - 1]
...
>>> class C(object):
...   def __init__(self):
...     self._items = (1, 2, 3)
...   def __iter__(self):
...     return CIterator(items=self._items)
...
>>> for c in C():
...   print(c)
...
1
2
3
```

Also we can return a generator as iterator:
```bash
>>> class C(object):
...   def __init__(self):
...     self._items = (1, 2, 3)
...   def __iter__(self):
...     return (i for i in self._items)
...
>>> for c in C():
...   print(c)
...
1
2
3
```

#### Iterator vs iterable

Any object from which the iter built-in function can obtain an iterator is iterable. Objects implementing an ```__iter__``` method returning an iterator are iterable. Sequences are always iterable; as are objects implementing a ```__getitem__``` method that takes 0-based indexes.

Any object that implements the ```__next__``` no-argument method that returns the next item in a series or raises ```StopIteration``` when there are no more items. Python iterators also implement the ```__iter__``` method, so they are iterable as well.

### Generators

There are two ways to define a generator:

- generator comprehension
- function with yield statement

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

#### Generator vs iterator

Every generator is an iterator: generators fully implement the iterator interface.
Generator retrieves items from a collection, while a generator can produce items "out of thin air."

In the Python community lingo iterator and generator are fairly close synonyms.

#### Generator vs function

According to [Improve Your Python: 'yield' and Generators Explained](https://www.jeffknupp.com/blog/2013/04/07/improve-your-python-yield-and-generators-explained/) by Jeff Knupp:

When we call a normal Python function, execution starts at function's first line and continues until a return statement, exception, or the end of the function (which is seen as an implicit return None) is encountered. Once a function returns control to its caller, that's it. Any work done by the function and stored in local variables is lost. A new call to the function creates everything from scratch.

This is all very standard when discussing functions (more generally referred to as subroutines) in computer programming. There are times, though, when it's beneficial to have the ability to create a "function" which, instead of simply returning a single value, is able to yield a series of values. To do so, such a function would need to be able to "save its work," so to speak.

I said, "yield a series of values" because our hypothetical function doesn't "return" in the normal sense. return implies that the function is returning control of execution to the point where the function was called. "Yield," however, implies that the transfer of control is temporary and voluntary, and our function expects to regain it in the future.

#### New in Python 3.3: Delegating to a Subgenerator

See [PEP 380: Syntax for Delegating to a Subgenerator](https://docs.python.org/3/whatsnew/3.3.html#pep-380).

```python
def subgenerator():

  for i in (0, 1, 2, 3):
    yield i


def generator():

  # For Python < 3.3:
  # for i in subgenerator():
  #     yield i

  yield from subgenerator()


if __name__ == '__main__':
  for i in generator():
    print(i)
```

### Coroutines

> - Generators produce data for iteration
> - Coroutines are consumers of data
> - To keep your brain from exploding, you don't mix the two concepts together
> - Coroutines are not related to iteration
> - Note: There is a use of having yield produce a value in a coroutine, but it's not tied to iteration.
>
> David Beazley, A Curious Course on Coroutines and Concurrency

An ability of generators to accept data was added in 2005, see [PEP-342](https://www.python.org/dev/peps/pep-0342/).

As for me, the essential of coroutine is that it consumes data while generator can only produce it:
```bash
>>> def coroutine():
...   print("Start")
...   for i in range(2):
...     x = yield
...     print("Received:", x)
...   print("Finish")
...
>>> c = coroutine()
>>> next(c)
Start
>>> c.send(1)
Received: 1
>>> c.send(2)
Received: 2
Finish
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
```

For comprehensive explanation see: [Coroutines at wla.berkeley.edu](http://wla.berkeley.edu/~cs61a/fa11/lectures/streams.html#coroutines).

#### New in Python 3.5: async and await syntax

See [PEP 492 - Coroutines with async and await syntax](https://www.python.org/dev/peps/pep-0492/).

Since Python 3.5 native coroutines are their own completely distinct type, before they were just [enhanced generators](https://www.python.org/dev/peps/pep-0342/). `async` syntax makes coroutines a native Python language feature, and clearly separates them from generators.

```
@asyncio.coroutine
def py34_coroutine():
    yield from avaitable()


async def py35_coroutine():
    await avaitable()
```

### Exceptions

EAFP stands for **E**asier to **A**sk for **F**orgiveness than **P**ermission.

In Python, ```try/except``` commonly used for control flow, and not just for error handling.

```bash
>>> def f(value):
...   try:
...     value = value + 1
...   except TypeError as e:
...     print("Error:", e)
...   else:
...     print("Success")
...   finally:
...     print('Runs anyway.')
...   return value
...
>>> f(1)
Success
Runs anyway.
2
>>> f('a')
Error: Can't convert 'int' object to str implicitly
Runs anyway.
'a'
```

### Context managers

The context manager protocol consists of the ```__enter__``` and ```__exit__``` methods.

```bash
>>> class ContextManager(object):
...   def __enter__(self):
...     print('Enter')
...   def __exit__(self, exc_type, exc_value, traceback):
...     print('Exit')
...
>>> with ContextManager() as cm:
...   print('Inner')
...
Enter
Inner
Exit
```

The same using ```contextlib```:

```bash
>>> import contextlib
>>> @contextlib.contextmanager
... def context_manager():
...   print('Enter')
...   yield None
...   print('Exit')
...
>>> with context_manager() as cm:
...   print('Inner')
...
Enter
Inner
Exit
```

## Standard library

### asyncio

[asyncio](https://docs.python.org/3/library/asyncio.html) is a part of the standard library since Python 3.4.

asyncio provides infrastructure for writing single-threaded concurrent code using coroutines, multiplexing I/O access over sockets and other resources, running network clients and servers, and other related primitives.

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

### abc

[ABC](https://www.python.org/dev/peps/pep-3119/) stands for **A**bstract **B**ase **C**lasses.

> An abstract class represents an interface.
>
> Bjarne Stroustrup, creator of c++

ABC uses to check if the object has an interface we need (for example, if it can behave like a dict or an iterable). We can check if the object has necessary attributes and so if it walks like a duck and swims like a duck and quacks like a duck, it must be a duck. Alternative way is to check if the object subclasses an ABC that describes necessary interface.

```abc``` module contains decorators that can be used to define abstract methods (methods that must be present).

```bash
>>> import abc
>>> class Duck(metaclass=abc.ABCMeta):
...   @abc.abstractmethod
...   def quack(self):
...     pass
...
>>> class C(Duck):
...   def quack(self):
...     print('quack')
...
>>> c = C()
>>> isinstance(c, Duck)
True
>>> class D(Duck):
...   pass
...
>>> d = D()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: Can't instantiate abstract class D with abstract methods quack
```

### itertools

[itertools](https://docs.python.org/3.5/library/itertools.html) module has a lot of functions to work with iterators and generators.

For example:
```bash
>>> import itertools
>>> counter = itertools.count(0, 0.2)
>>> i = 0
>>> while i < 0.6:
...   i += next(counter)
...   print(i)
...
0
0.2
0.6000000000000001
```

## Thirdparty

### ujson

More efficient ```json``` alternative.

## Vocabulary

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

### Container sequence vs flat sequence

Are represent different memory models of the sequence types.

**Container squence** means some objects contain references to other objects.
Container sequences can be nested because they may contain objects of any type, including their own type.

**Flat sequence** is a sequence type that physically stores the values of its items, and not references to other objects. ```str```, ```bytes```, ```bytearray```, ```memoryview``` and ```array.array``` are flat sequences.

### Deep and shallow copies

Deep copy is a copy of an object in which all the objects that are attributes of the object are themselves also copied.

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

### Descriptor

Descriptor is a class implementing one or more of the ```__get__```, ```__set__``` or ```__delete__``` special methods and one of its instances is used as class attribute of another class, the managed class. Descriptors manage the access and deletion of a managed attributes in the managed class, often storing data in the managed instances.

### Dunder-method

Methods like ```__eq__```, ```__getitem__```.
Also known as special or magic methods.

!!! hint "Magic"
	"Magic method" term was adopted from Ruby. Actually, these methods are opposite to magic, their behavior quite straightforward.

### Future

Also known as promise.

An object which represents the result of a function call which is asynchronous.

### GIL

[GIL](https://wiki.python.org/moin/GlobalInterpreterLock) or Global Interpreter Lock is a mutex that prevents multiple native threads from executing Python bytecodes at once.

Jython and IronPython have no GIL. PyPy and CPython have a GIL.

GIL disadvantage: prevents multithreaded CPython programs from taking full advantage of multiprocessor systems in certain situations. There is no good enough GILless CPython implementation yet.

How to workaround this issue: use [multiprocessing module](https://docs.python.org/3.5/library/multiprocessing.html).

There is a great [talk by David Beazley on PyCon 2015](https://www.youtube.com/watch?v=MCs5OvhV9S4) that shows how Python concurrency works on an example.

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

### Lazy vs eager

An iterable object that builds all its items at once. In Python, a list comprehension is eager and generator comprehension is lazy.

### Metaprogramming

Class metaprogramming is the art of creating or customizing classes at runtime.

Means that we manage object creation, for example: create a class using ```type()``` or overriding ```__new__()``` method to return alternative object instance instead of creating new.

A useful example - register class on class initialization:
```python
class Registry(object):

    _items = {}

    @classmethod
    def register(cls, item):
        if item.__name__ not in cls._items:
            cls._items[item.__name__] = item

    @classmethod
    def get(cls, name):
        return cls._items.get(name)

    @classmethod
    def list(cls):
      return cls._items.values()


class ClassMeta(type):

    def __init__(cls, name, bases, attrs):
        super(ClassMeta, cls).__init__(name, bases, attrs)
        Registry.register(item=cls)


class Class1(object, metaclass=ClassMeta):

  pass


class Class2(object, metaclass=ClassMeta):

  pass


if __name__ == '__main__':
  print(Registry.list())
  # python3.5 meta_example.py
  # dict_values([<class '__main__.Class1'>, <class '__main__.Class2'>])

```

## Links

[Fluent Python](http://www.amazon.com/Fluent-Python-Luciano-Ramalho-ebook/dp/B0131L3PW4/) by Luciano Ramalho
