labels: Blog
        Django
created: 2013-03-11T00:00
place: Starobilsk, Ukraine
comments: true

# [Django] Logging to syslog

By default, Django has following logging configuration:
```python
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
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
```

If I want to use custom logger like this:
```python
import logging


my_logger = logging.getLogger('myapp.mylogger')
my_logger.info('Hi!')
```

I have to add the logger to LOGGING dict:
```python
'loggers': {
    'django.request': {
        'handlers': ['mail_admins'],
        'level': 'ERROR',
        'propagate': True,
    },
    'myapp.mylogger': {
        'handlers': ['mail_admins'],
        'level': 'INFO',
        'propagate': True,
    },
}
```

Logging to syslog:
```python
from logging.handlers import SysLogHandler


    'handlers': {
        ...
        'syslog': {
            'level':'INFO',
            'class':'logging.handlers.SysLogHandler',
            'formatter': 'verbose',
            'facility': SysLogHandler.LOG_LOCAL2,
            'address': '/dev/log',
        },
    },
    ...
    'loggers': {
        ...
        'myapp.mylogger': {
            'handlers': ['syslog'],
            'level': 'INFO',
            'propagate': True,
        },
    },
```

Logs will be available in ```/var/log/syslog```.

Links:

- [https://docs.djangoproject.com/en/dev/topics/logging/](https://docs.djangoproject.com/en/dev/topics/logging/)
- [http://stackoverflow.com/questions/6205254/how-to-setup-sysloghandler-with-django-1-3-logging-dictionary-configuration](http://stackoverflow.com/questions/6205254/how-to-setup-sysloghandler-with-django-1-3-logging-dictionary-configuration)
- [http://docs.python.org/2/library/logging.handlers.html#sysloghandler](http://docs.python.org/2/library/logging.handlers.html#sysloghandler)
