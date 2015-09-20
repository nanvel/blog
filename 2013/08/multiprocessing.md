labels: Blog
        Python
created: 2013-08-21T00:00

# [Python] Multiprocessing is great

![Multiprocessing](multiprocessing.png)

Multiprocessing is great because it allows to decrease wasting of most expensive thing in our life - time. This is just a little example of using python multiprocessing module. In real projects it can be much more useful.

```python
import datetime
import multiprocessing


PROCESSES = 2


def hard_task(n):
    stop_time = datetime.datetime.now() + datetime.timedelta(seconds=1)
    while stop_time > datetime.datetime.now():
        pass
    return '%d Done!' % n


def main():
    pool = multiprocessing.Pool(PROCESSES)
    results = [pool.apply_async(hard_task, (i,)) for i in range(20)]
    for result in results:
        print result.get()


if __name__ == '__main__':
    main()
```

Just try to change ```PROCESSES``` value.

Place: Starobilsk, Ukraine
