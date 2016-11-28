labels: Draft
        Python
        Asynchronous
created: 2016-11-27T17:12
modified: 2016-11-27T17:12
place: Phuket, Thailand
comments: true

# Python AsyncIO

New in Python 3.4: asyncio included.

gunicorn -b 0.0.0.0:8000 -k aiohttp.worker.GunicornWebWorker -w 9 -t 60 project.app:app
--reload - reload on code change.


Dev static server:
app.router.add_static('/static', '/path/to/static', name='static')
Template: app.router.static.url(filename="...")

@asyncio.coroutine -> async def
yield from -> await

+ Server sent events (https://www.youtube.com/watch?v=8-PxeTgTx6s)

## Libs

aiohttp
aiohttp.web
aiohttp session
aiohttp debugtoolbar
aiopg
aioredis / asyncio_redis
aioes
aiozmq
aio-s3

UVLoop

JSON Schema

yield from can return return statement.

use asyncio.coroutine because yield can be removed and it wouldn't be generator any more.

GIL explained (multiple threads still use a single processor core): https://www.youtube.com/watch?v=MCs5OvhV9S4 (David Beazley - Python Concurrency From the Ground Up: LIVE! - PyCon 2015).

We have no parallelizm.

What is select?

Executors - run in [thread|process]pool.

Debugging:
loop.set_debug(True)

import gc
gc.set_debug(gc.DEBUG_UNCOLLECTABLE)

raise StopIteration -> return

we can use await only in async def.

what is async with / async for

Without GIL it's slower, ~3 times.

## Links

[«Asyncio stack для веб разработчика» Ігор Давиденко LvivPy#4](https://www.youtube.com/watch?v=jqU8l9EBQ54) at YouTube
[«Продвинутый async/await в Python 3.5» Igor Davydenko LvivPy#5](https://www.youtube.com/watch?v=8-PxeTgTx6s) at YouTube
[Введение в aiohttp. Андрей Светлов](https://www.youtube.com/watch?v=F6sa6G0lJCk) at YouTube
[Yury Selivanov - async/await in Python 3.5 and why it is awesome](https://www.youtube.com/watch?v=m28fiN9y_r8)
[Łukasz Langa - Thinking In Coroutines - PyCon 2016](https://www.youtube.com/watch?v=l4Nn-y9ktd4) at YouTube
