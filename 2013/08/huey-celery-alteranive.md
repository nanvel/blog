labels: Blog
        TaskQueue
created: 2013-08-03T00:00
place: Starobilsk, Ukraine
comments: true

# Huey - a nice celery alternative

Documentation: [http://huey.readthedocs.org/en/latest/index.html](http://huey.readthedocs.org/en/latest/index.html)

GitHub: [https://github.com/coleifer/huey](https://github.com/coleifer/huey)

I am going to show a simple example of huey usage in django project.
The problem that huey should solve in this example - handle some hard tasks that should be done when user navigate to particular url.
The 'hard task' in example would be ```time.sleep(10)``` :).
To make sure that task was successfully done, we will calculate ```datetime.now() + 1 day``` and save result to file.

## Installation and configuration

Huey is available on PyPI:
```bash
pip install huey
```

Also we'll need redis:
```bash
pip install redis
```

requirements.txt:
```text
Django==1.5.1
huey==0.4.1
redis==2.7.6
```

```myproject/settings.py```:
```python
HUEY = {
    'backend': 'huey.backends.redis_backend',  # required.
    'name': 'hueytest',
    'connection': {'host': 'localhost', 'port': 6379},
    'always_eager': False, # Defaults to False when running via manage.py run_huey

    # Options to pass into the consumer when running ``manage.py run_huey``
    'consumer_options': {'workers': 4},
}
```

See more about huey settings in [it's documentation](http://huey.readthedocs.org/en/latest/django.html#huey-settings).

```myproject/apps/myapp/tasks.py```:
```python
import datetime
import os
import time

from huey.djhuey import crontab, periodic_task, task


@task()
def hard_task():
    time.sleep(10)
    now = datetime.datetime.now()
    path = os.path.join(
        os.path.dirname(__file__),
        'time_%s.txt' % datetime.datetime.strftime(now, '%Y%d%m_%H%M%S'))
    with open(path, 'w') as f:
        f.write('Task done.')
```

```myproject/apps/myapp/views.py```:
```python
from django.shortcuts import render_to_response, redirect

from .tasks import hard_task


def home(request):
    return render_to_response('home.html')


def hardview(request):
    hard_task()
    return redirect('home')
```

Running consumers:
```bash
python manage.py run_huey
```

I got an error: ``No handlers could be found for logger "huey.consumer":``, but this can be easily fixed:
```python
# myproject/settings.py:
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'syslog': {
            'level':'INFO',
            'class':'logging.handlers.SysLogHandler',
            'address': '/dev/log',
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
       'huey.consumer': {
            'handlers': ['syslog'],
            'level': 'INFO',
            'propagate': True,
       }
    }
}
```

Logs (see ```/var/logs/syslog```):
```text
Jul 28 22:15:26 nanvel-ws Setting signal handler
Jul 28 22:15:26 nanvel-ws Huey consumer initialized with following commands#012+ hard_task
Jul 28 22:15:26 nanvel-ws 4 worker threads
Jul 28 22:15:26 nanvel-ws Starting scheduler thread
Jul 28 22:15:26 nanvel-ws Starting worker threads
Jul 28 22:15:26 nanvel-ws Starting periodic task scheduler thread
Jul 28 22:15:43 nanvel-ws Executing <hueytest.testapp.tasks.queuecmd_hard_task object at 0x1c96250>
```

If you'll open ```reverse('hardview')```, huew task should be created and file similar to ```myapp/time_20132807_142719.txt``` should be created.

## Running huey consumers on production

Author advised us to use [supervisor](http://supervisord.org/): [https://github.com/coleifer/huey/issues/15](https://github.com/coleifer/huey/issues/15).

> A well-behaved Unix daemon process is tricky to get right
>
> For code clarity, this is not provided as a part of 'huey'. Adding this would require a dependency outside the standard lib, which I'm not > really interested in adding. If you want, though, you should be able to very easily use:
> [http://pypi.python.org/pypi/python-daemon/](http://pypi.python.org/pypi/python-daemon/)
> I run all my web apps and consumers using supervisord.

So, let's install and configure it.

```bash
sudo pip install supervisor
echo_supervisord_conf > supervisord.conf
vim supervisord.conf
```

Add this to supervisord.conf:
```text
[program:huey]
command=/home/deploy/envs/hueytest/.env/bin/python manage.py run_huey
directory=/home/deploy/envs/hueytest
user=deploy
sudo ln -s /usr/local/bin/supervisord /usr/bin/supervisord
sudo ln -s /usr/local/bin/supervisorctl /usr/bin/supervisorctl
wget https://raw.github.com/Supervisor/initscripts/master/debian-norrgard
sudo mv debian-norrgard /etc/init.d/supervisord
sudo chmod +x /etc/init.d/supervisord
sudo update-rc.d supervisord defaults
sudo service supervisord start
```

Check is all ok:
```bash
sudo supervisorctl
huey                             RUNNING    pid 31875, uptime 0:00:24
supervisor> exit
ps aux | grep huey
deploy   30451  2.1  0.5 520764 22836 ?        Sl   22:23   0:00 /home/deploy/envs/hueytest/.env/bin/python manage.py run_huey
deploy   31248  0.0  0.0  13584   920 pts/4    S+   22:24   0:00 grep --color=auto huey
```

Stopping process:
```bash
supervisor> stop huey
huey: stopped
supervisor> exit
```

more commands:
```bash
supervisor> help

default commands (type help <topic>):
=====================================
add    clear  fg        open  quit    remove  restart   start   stop  update
avail  exit   maintail  pid   reload  reread  shutdown  status  tail  version
```

Huey has next useful features:

- [Executing tasks in the future](http://huey.readthedocs.org/en/latest/getting-started.html#executing-tasks-in-the-future)
- [Retrying tasks that fail](http://huey.readthedocs.org/en/latest/getting-started.html#retrying-tasks-that-fail)
- [Executing tasks at regular intervals](http://huey.readthedocs.org/en/latest/getting-started.html#executing-tasks-at-regular-intervals)

Read more in [documentation](http://huey.readthedocs.org/en/latest/index.html).

Links:

- [http://huey.readthedocs.org/en/latest/index.html](http://huey.readthedocs.org/en/latest/index.html)
- [http://supervisord.org/](http://supervisord.org/)
