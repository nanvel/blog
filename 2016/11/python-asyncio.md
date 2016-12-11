labels: Blog
        Python
        Asynchronous
created: 2016-11-27T17:12
modified: 2016-11-30T14:52
place: Phuket, Thailand
comments: true

# Python AsyncIO

[TOC]

## Timeline

**May 2001**: [PEP 255](https://www.python.org/dev/peps/pep-0255/) was created, Simple Generators
**October 2002**: Twisted (Python network programming framework uses ioloop and futures) released
**May 2005**: [PEP 342](https://www.python.org/dev/peps/pep-0342/) was created, generator functions are coroutines
**September 2012**: Python 3.3 with `yield from` statement ([PEP 380](https://www.python.org/dev/peps/pep-0380/)).
**December 2012**: asyncio (formerly tulip) [was proposed as an enhancement of Python](https://www.python.org/dev/peps/pep-3156/) in order to add asynchronous I/O support.
**October 2013**: asyncio 0.1.1 released
**October 2013**: aiohttp 0.1 released
**March 2014**: Python 3.4 with asyncio in the standard library
**September 2015**: Python 3.5 with async/await statements ([PEP 492](https://www.python.org/dev/peps/pep-0492/))

## New syntax for generators/coroutines

There is a great [talk by David Beazley on PyCon 2015](https://www.youtube.com/watch?v=MCs5OvhV9S4) that shows how to use generators to simplify asynchronous code.

My notes on [generators](/2015/11/python-the-language#generators) and [coroutines](/2015/11/python-the-language#coroutines).

### yield from

The syntax is proposed for a generator to delegate part of its operations to another generator.

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

# Python 2.7:
# SyntaxError: invalid syntax
# Python 3.3:
# 0
# 1
# 2
# 3
```

In case of coroutine:

```python
def subcoroutine():

	while True:
		i = (yield)
		print(i)


def coroutine():

	sc = subcoroutine()

	# For Python < 3.3
	# sc.send(None)
	# while True:
	# 	try:
	# 		i = (yield)
	# 		sc.send(i)
	# 	except StopIteration:
	# 		pass

	yield from sc


if __name__ == '__main__':
	c = coroutine()
	c.send(None)
	for i in (0, 1, 2, 3):
		c.send(i)
```

Subgenerator is allowed to return with a value, and the value is made available to the delegating generator.

`return` statement:

```python
def subgenerator():

	a = (0, 1, 2, 3)
	for i in a:
		yield i
	# raises
	# SyntaxError: 'return' with argument inside generator
	# in Python < 3.3 (must use raise StopIteration() instead)
	return len(a)


def generator():
	# subgenerator return value is available
	value = yield from subgenerator()
	print(value)


if __name__ == '__main__':
	for i in subgenerator():
		print(i)

# 0
# 1
# 2
# 3

	for i in generator():
		print(i)

# 0
# 1
# 2
# 3
# 4
```

### async/await

asyncio required that all generators meant to be used as a coroutine had to be decorated with asyncio.coroutine.

```python
@asyncio.coroutine
def py34_coroutine():
    yield from avaitable()
```

Since Python 3.5 native coroutines are their own completely distinct type, before they were just [enhanced generators](https://www.python.org/dev/peps/pep-0342/). `async` syntax makes coroutines a native Python language feature, and clearly separates them from generators.

```
async def py35_coroutine():
    await avaitable()
```

Features:

- async def functions are always coroutines, even if they do not contain await expressions
- It is a `SyntaxError` to have yield or yield from expressions in an async function
- It is a `SyntaxError` to use await outside of an async def function (like it is a `SyntaxError` to use yield outside of def function)
- It is a `TypeError` to pass anything other than an awaitable object to an await expression
- await expressions do not require parentheses around them most of the times

### async for, async with

Support for asynchronous calls is limited to expressions where yield is allowed syntactically, limiting the usefulness of syntactic features, such as with and for statements ([PEP 492](https://www.python.org/dev/peps/pep-0492/)).

The new async with statement lets Python programs perform asynchronous calls when entering and exiting a runtime context, and the new async for statement makes it possible to perform asynchronous calls in iterators. An asynchronous context manager is a context manager that is able to suspend execution in its enter and exit methods.

```python
class AsyncContextManager:
    async def __aenter__(self):
        await log('entering context')

    async def __aexit__(self, exc_type, exc, tb):
        await log('exiting context')
```

An asynchronous iterable is able to call asynchronous code in its iter implementation, and asynchronous iterator can call asynchronous code in its next method.

```python
class AsyncIterable:
    def __aiter__(self):
        return self

    async def __anext__(self):
        data = await self.fetch_data()
        if data:
            return data
        else:
            raise StopAsyncIteration

    async def fetch_data(self):
        ...
```

## Debug

```python
loop.set_debug(True)
```

In debug mode many additional checks are enabled.

```python
import gc
gc.set_debug(gc.DEBUG_UNCOLLECTABLE)
```

When a native coroutine is garbage collected, a RuntimeWarning is raised if it was never awaited on.

## Libs

```
aiohttp
aiohttp.web
aiohttp session
aiohttp debugtoolbar
aiopg
aioredis / asyncio_redis
aioes
aiozmq
aio-s3
...
```

### aiohttp.web

#### Server example

```python
from aiohttp import web


def index(request):
    return web.Response(text="Welcome home!")


my_web_app = web.Application()
my_web_app.router.add_route('GET', '/', index)
```

#### Static files serving while development

```python
app.router.add_static('/static', '/path/to/static', name='static')
```
URL reverse:
```python
app.router.static.url(filename="...")
```

#### Deployment

http://aiohttp.readthedocs.io/en/v0.22.3/gunicorn.html

```bash
pip install gunicorn

gunicorn -b 0.0.0.0:8000 -k aiohttp.worker.GunicornWebWorker -w 9 -t 60 project.app:app
```

Flags:

- `--reload` - reload on code change
- `--bind` (`-b`) - server's socket address (e.g. `localhost:8080`)
- `--worker-class` (`-k`) - set custom worker subclass (e.g. `aiohttp.worker.GunicornWebWorker`)
- `--workers` (`-w`) - number of workers to use for handling requests (`(2 x $num_cores) + 1`)

Links:

[How to Deploy Python WSGI Apps Using Gunicorn HTTP Server Behind Nginx](https://www.digitalocean.com/community/tutorials/how-to-deploy-python-wsgi-apps-using-gunicorn-http-server-behind-nginx)

### UVLoop

[uvloop](https://github.com/MagicStack/uvloop) is a fast, drop-in replacement of the built-in asyncio event loop. uvloop is implemented in Cython and uses libuv under the hood.

There is a gunicorn worker for it: `aiohttp.worker.GunicornUVLoopWebWorker`.

## Links

[«Asyncio stack для веб разработчика» Ігор Давиденко LvivPy#4](https://www.youtube.com/watch?v=jqU8l9EBQ54) at YouTube, [slides](http://igordavydenko.com/talks/lvivpy-4/)
[«Продвинутый async/await в Python 3.5» Igor Davydenko LvivPy#5](https://www.youtube.com/watch?v=8-PxeTgTx6s) at YouTube
[Введение в aiohttp. Андрей Светлов](https://www.youtube.com/watch?v=F6sa6G0lJCk) at YouTube
[Yury Selivanov - async/await in Python 3.5 and why it is awesome](https://www.youtube.com/watch?v=m28fiN9y_r8) at YouTube
[Łukasz Langa - Thinking In Coroutines - PyCon 2016](https://www.youtube.com/watch?v=l4Nn-y9ktd4) at YouTube
[How the heck does async/await work in Python 3.5?](http://www.snarky.ca/how-the-heck-does-async-await-work-in-python-3-5) by Brett Cannon

[PEP 342](https://www.python.org/dev/peps/pep-0342/) - Coroutines via Enhanced Generators
[PEP 380](https://www.python.org/dev/peps/pep-0380/) - Syntax for Delegating to a Subgenerator
[PEP 492](https://www.python.org/dev/peps/pep-0492/) - Coroutines with async and await syntax
[PEP 3156](https://www.python.org/dev/peps/pep-3156/) - Asynchronous IO Support Rebooted: the "asyncio" Module
