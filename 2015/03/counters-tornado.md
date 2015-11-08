labels: Blog
        Tornado
created: 2015-03-08T20:55
place: Phuket, Thailand
comments: true

# Efficient actions counter using tornado IOLoop.add_timeout

Redis used as temporary storage and sqlite3 as persistent storage for counters.

```bash
pip install tornado==4.1
pip install redis
```

Create sqlite table:
```bash
(.env)nanvel-air:tornado_counter nanvel$ sqlite3 actions.sqlite3
SQLite version 3.8.5 2014-08-15 22:37:57
Enter ".help" for usage hints.
sqlite> CREATE TABLE counters(action TEXT PRIMARY KEY, count INTEGER DEFAULT 0);
```

```python
import datetime
import logging
import os
import sqlite3

import redis

from tornado import web, ioloop, gen, options


logger = logging.getLogger(__name__)


class ActionHandler(web.RequestHandler):

    ALLOWED_ACTIONS = ['open_browser', 'open_new_tab', 'enter_search_term', 'scroll', 'click_on_link']
    REDIS_COUNTER_KEY = 'actions:counter:{action}'
    REDIS_TASK_KEY = 'actions:task:{action}'
    UPDATE_PERIOD = 30 # seconds

    def inc_count(self, action):
        key = self.REDIS_COUNTER_KEY.format(action=action)
        counter_key = self.REDIS_COUNTER_KEY.format(action=action)
        task_key = self.REDIS_TASK_KEY.format(action=action)
        count, delted_counter, deleted_task = self.application.redis.pipeline(
            ).get(counter_key).delete(counter_key).delete(task_key).execute()
        if not count:
            return
        with sqlite3.connect(self.application.db_path) as connection:
            cursor = connection.cursor()
            result = cursor.executescript("INSERT OR REPLACE INTO counters(action, count) VALUES ('{action}', COALESCE((SELECT count + 1 FROM counters WHERE action = '{action}'), 1));".format(
                count=count, action=action))
            logger.warning('Saved to sqlite3.')

    def post(self):
        action = self.get_body_argument('action')
        if action in self.ALLOWED_ACTIONS:
            counter_key = self.REDIS_COUNTER_KEY.format(action=action)
            task_key = self.REDIS_TASK_KEY.format(action=action)
            count, task_exists = self.application.redis.pipeline().incr(counter_key, 1).get(task_key).execute()
            if not task_exists:
                ioloop.IOLoop.instance().add_timeout(
                    deadline=datetime.timedelta(seconds=self.UPDATE_PERIOD),
                    callback=self.inc_count,
                    action=action)
                self.application.redis.setex(task_key, self.UPDATE_PERIOD * 2, 1)
        logger.warning('Incremented.')
        self.write('Ok')


class CounterApplication(web.Application):

    def __init__(self, *args, **kwargs):
        handlers = [(r'/action', ActionHandler)]
        kwargs['debug'] = True
        self.db_path = os.path.join(
            os.path.dirname(os.path.realpath(__file__)), 'counters.sqlite3')
        self.redis = redis.StrictRedis(host='localhost')
        super(CounterApplication, self).__init__(handlers, *args, **kwargs)


if __name__ == "__main__":
    options.parse_command_line()
    CounterApplication().listen(5000)
    ioloop.IOLoop.instance().start()

    # curl --data "action=open_browser" http://localhost:5000/action
    # [W 150308 20:27:00 app:46] Incremented.
    # [I 150308 20:27:00 web:1825] 200 POST /action (::1) 7.90ms
    # [W 150308 20:27:01 app:46] Incremented.
    # [I 150308 20:27:01 web:1825] 200 POST /action (::1) 1.74ms
    # [W 150308 20:27:02 app:46] Incremented.
    # [I 150308 20:27:02 web:1825] 200 POST /action (::1) 1.81ms
    # [W 150308 20:27:05 app:32] Saved to sqlite3.
    # [W 150308 20:27:10 app:46] Incremented.
    # [I 150308 20:27:10 web:1825] 200 POST /action (::1) 1.56ms
    # [W 150308 20:27:11 app:46] Incremented.
    # [I 150308 20:27:11 web:1825] 200 POST /action (::1) 1.29ms
    # [W 150308 20:27:12 app:46] Incremented.
    # [I 150308 20:27:12 web:1825] 200 POST /action (::1) 1.38ms
    # [W 150308 20:27:12 app:46] Incremented.
    # [I 150308 20:27:12 web:1825] 200 POST /action (::1) 1.38ms
    # [W 150308 20:27:13 app:46] Incremented.
    # [I 150308 20:27:13 web:1825] 200 POST /action (::1) 1.29ms
    # [W 150308 20:27:14 app:46] Incremented.
    # [I 150308 20:27:14 web:1825] 200 POST /action (::1) 1.72ms
    # [W 150308 20:27:15 app:32] Saved to sqlite3.
```

```bash
(.env)nanvel-air:tornado_counter nanvel$ sqlite3 counters.sqlite3
SQLite version 3.8.5 2014-08-15 22:37:57
Enter ".help" for usage hints.
sqlite> select * from counters;
open_new_tab|3
open_browser|21
```
