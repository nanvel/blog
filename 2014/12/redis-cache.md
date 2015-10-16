labels: Blog
        Databases
created: 2014-12-28T01:46
place: Kyiv, Ukraine

# Caching using redis get/setex issue

Let's imagine that we have a function that returns results that changes very slow comparatively to requests to show them. This is a place where caching can help a lot.

Take a look at from_cache_simple, it have to be very straightforward. It works great while we have only few app instances. Few instances may found that the key is not exists in redis and run the function almost same time. If we have hundreds requests per second and a function that takes about second to finish, it may cause a problem.

```python
import datetime
import logging

from functools import partial

from redis import StrictRedis
from redis.exceptions import NoScriptError
from tornado import gen, options
from tornado.ioloop import IOLoop


logger = logging.getLogger(__name__)


class Redis(object):

    _REDIS = None

    @classmethod
    def instance(cls):
        if cls._REDIS is None:
            cls._REDIS = StrictRedis(host='localhost')
        return cls._REDIS


class Cache(object):

    _SCRIPT_GET = """
local item = redis.call("GET", ARGV[1])
if item then
    return {item, 0}
else
    local counter = redis.call("INCRBY", ARGV[1] .. ":wait", 1)
    if counter == 1 then
        return {item, 0}
    else
        return {item, 1}
    end
end
"""
    _SCRIPT_SET = """
redis.call("SETEX", ARGV[1], tonumber(ARGV[2]), ARGV[3])
redis.call("DEL", ARGV[1] .. ":wait")
"""
    _RETRIES = 2

    _script_set = None
    _script_get = None
    _redis = Redis.instance()

    @classmethod
    def script_set(cls, key, timeout, item):
        if cls._script_set is None:
            cls._script_set = cls._redis.register_script(script=cls._SCRIPT_SET)
            return cls._script_set(args=[key, timeout, item])
        try:
            return cls._script_set(args=[key, timeout, item])
        except NoScriptError:
            cls._script_set = cls._redis.register_script(script=cls._SCRIPT_SET)
            return cls._script_set(args=[key, timeout, item])

    @classmethod
    def script_get(cls, key):
        if cls._script_get is None:
            cls._script_get = cls._redis.register_script(script=cls._SCRIPT_GET)
            return cls._script_get(args=[key])
        try:
            return cls._script_get(args=[key])
        except NoScriptError:
            cls._script_get = cls._redis.register_script(script=cls._SCRIPT_GET)
            return cls._script_get(args=[key])

    @gen.coroutine
    def from_cache_optimized(self, key, timeout, func):
        retries = 0
        wait = True
        while wait and retries < self._RETRIES:
            retries += 1
            item, wait = self.script_get(key=key)
            if item:
                raise gen.Return(item)
            if wait:
                # wait and try once more
                # async sleep
                yield gen.Task(
                    IOLoop.current().add_timeout,
                    deadline=datetime.timedelta(seconds=1)
                )
        # get item and set to redis
        item = yield func()
        self.script_set(key=key, timeout=timeout, item=item)
        raise gen.Return(item)

    @gen.coroutine
    def from_cache_simple(self, key, timeout, func):
        result = self._redis.get(key)
        if result is None:
            result = yield func()
            self._redis.setex(key, timeout, result)
        raise gen.Return(result)


@gen.coroutine
def hard_task(value=1):
    logger.info('Run hard task with value = {value}'.format(value=value))
    yield gen.Task(
        IOLoop.current().add_timeout,
        deadline=datetime.timedelta(seconds=2))
    raise gen.Return(value)


if __name__ == '__main__':
    options.parse_command_line()
    KEY = 'tests:key:{n}'.format(n=1)
    ioloop = IOLoop.current()
    from_cache = Cache().from_cache_optimized
    result = ioloop.run_sync(partial(
        from_cache,
        key=KEY, timeout=5, func=hard_task))
    logger.info('first result: {result}'.format(result=result))
    result = ioloop.run_sync(partial(
        from_cache,
        key=KEY, timeout=5, func=hard_task))
    logger.info('second result: {result}'.format(result=result))
```

Simple:
```text
console1$ python test_cache.py
[I 141228 01:40:46 test_cache:106] Run hard task with value = 1
[I 141228 01:40:48 test_cache:121] first result: 1
[I 141228 01:40:48 test_cache:125] second result: b'1'
console2$ python test_cache.py
[I 141228 01:40:47 test_cache:106] Run hard task with value = 1
[I 141228 01:40:49 test_cache:121] first result: 1
[I 141228 01:40:49 test_cache:125] second result: b'1'
```

Optimized:
```text
console1$python test_cache.py
[I 141228 01:42:20 test_cache:106] Run hard task with value = 1
[I 141228 01:42:22 test_cache:121] first result: 1
[I 141228 01:42:22 test_cache:125] second result: b'1'
console2$ python test_cache.py
[I 141228 01:42:23 test_cache:121] first result: b'1'
[I 141228 01:42:23 test_cache:125] second result: b'1'
```
