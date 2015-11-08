labels: Blog
        Python
created: 2013-02-16T00:00
place: Starobilsk, Ukraine
comments: true

# Python way to create unix daemon

We can easily put program into background using '&':
```bash
python myprogram.py &
```

But that does not correctly detach the process from the terminal session that started it. So, if I'll close terminal, program will be terminated.

Here are the steps to create proper daemon:
[http://www.steve.org.uk/Reference/Unix/faq_2.html#SEC16](http://www.steve.org.uk/Reference/Unix/faq_2.html#SEC16).

[python-daemon](http://pypi.python.org/pypi/python-daemon/1.6) package allows us to create proper unix daemon with ease.

This is small example of the daemon that saves current time to file every 10 seconds:
```python
# mydaemon.py
import os
import time

from daemon import runner
from datetime import datetime


class App():

    def __init__(self):
        self.stdin_path = '/dev/null'
        self.stdout_path = '/dev/tty'
        self.stderr_path = '/dev/tty'
        self.pidfile_path = '/var/run/mydaemon.pid'
        self.pidfile_timeout = 5

    def run(self):
        filepath = '/tmp/mydaemon/currenttime.txt'
        dirpath = os.path.dirname(filepath)
        while True:
            if not os.path.exists(dirpath) or not os.path.isdir(dirpath):
                os.makedirs(dirpath)
            f = open(filepath, 'w')
            f.write(datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S'))
            f.close()
            time.sleep(10)


app = App()
daemon_runner = runner.DaemonRunner(app)
daemon_runner.do_action()
```

Usage:
```bash
> python mydaemon.py
usage: md.py start|stop|restart
> python mydaemon.py start
started with pid 8699
> python mydaemon.py stop
Terminating on signal 15
```

Links:

- [http://www.steve.org.uk/Reference/Unix/faq_2.html#SEC16](http://www.steve.org.uk/Reference/Unix/faq_2.html#SEC16)
- [http://www.python.org/dev/peps/pep-3143/](http://www.python.org/dev/peps/pep-3143/)
- [http://pypi.python.org/pypi/python-daemon/1.6](http://pypi.python.org/pypi/python-daemon/1.6)
- [https://github.com/arnaudsj/python-daemon](https://github.com/arnaudsj/python-daemon)
- [http://www.gavinj.net/2012/06/building-python-daemon-process.html](http://www.gavinj.net/2012/06/building-python-daemon-process.html)
- [http://stackoverflow.com/questions/10924309/how-can-i-run-my-python-script-in-the-background-on-a-schedule](http://stackoverflow.com/questions/10924309/how-can-i-run-my-python-script-in-the-background-on-a-schedule)
