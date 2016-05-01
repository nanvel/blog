labels: Blog
		Tornado
created: 2016-05-01T10:24
place: Kyiv, Ukraine
comments: true

# Tornado utils. Settings

There is [options](http://www.tornadoweb.org/en/stable/options.html) module in tornado similar to what I call settings, it allows to parse options passed via command line or settings file. The options module doesn't cover a few features I use widely: load settings from environ variables and initialize class variables with settings values (options must be available on class initialization, i.e. import). Things I don't like from the options: I usually must execute ```parse_command_line``` or ```parse_config_file``` before using options, there are two options (```tornado.options``` and ```tornado.options.options```) that confuses a bit, I want options to be immutable (there must be a special method to change them in runtime). I had tried different approaches to overcome the issues and came up with small patch of tornado options and few conventions.

## Usage example

All settings located in the ```defines.py``` file, similar to what we have in options:
```python
# ...
Setting(name='MY_SETTING', content_type=int, default=100, description="My setting.")
```

There are two ways to change the default setting value:

- set environment variable (```export PROJECT_MY_SETTING=101```)
- execute app.py with arguments (```app.py --MY_SETTING=101```)

To retrieve setting value just get attribute with the same name:
```
from project.settings import settings


class MyClass:

    MY_CONST = settings.MY_SETTING
```

## The implementation

Project structure:
```text
- project/
  - app.py
  - project/
  	- common/
  	- settings/
  	   - __init__.py
  	   - defines.py
  	   - models.py
  	   - tests.py
  	- __init__.py
```

```project/app.py```:
```python
from project.settings import settings

from tornado.ioloop import IOLoop
from tornado.web import Application as BaseApplication


class Application(BaseApplication):

    def __init__(self, **kwargs):
        kwargs['debug'] = settings.DEBUG
        super(Application, self).__init__(handlers=[], **kwargs)


if __name__ == '__main__':

    application = Application()
    application.listen(port=settings.PORT)

    IOLoop.instance().start()
```

```project/project/settings/__init__.py```:
```python
from .models import *
from .tests import *
```

project/project/defines.py:
```python
from collections import namedtuple


__all__ = ('DEFINES',)


Setting = namedtuple(typename='Setting', field_names=('name', 'content_type', 'default', 'description'))


DEFINES = (
    Setting(name='DEBUG', content_type=bool, default=True, description="Enable debug mode."),
    Setting(name='PORT', content_type=int, default=8000, description="Port, default: 8000."),
)
```

```project/project/models.py```:
```
import os

from tornado import options

from .defines import DEFINES


__all__ = ('settings',)


class Settings:

    ENV_PREFIX = 'PROJECT'

    _setting_parsers = {}

    def __init__(self, defines):
        for setting_define in defines:
            if setting_define.name.upper() != setting_define.name:
                raise ValueError("Setting name must be uppercase.")
            if setting_define.content_type not in self._setting_parsers:
                raise ValueError("Unknown setting content type.")
            if setting_define.name in self.__dict__:
                raise ValueError("Invalid setting name.")

            default = os.getenv(
                '{prefix}_{attr}'.format(
                    prefix=self.ENV_PREFIX,
                    attr=setting_define.name),
                setting_define.default
            )

            parser = self._setting_parsers[setting_define.content_type]

            options.define(
                setting_define.name,
                type=parser.OPTIONS_TYPE,
                default=parser.decode(value=default),
                help=setting_define.description
            )

        options.parse_command_line()

    def __setattr__(self, key, value):
        if key in options.options:
            raise RuntimeError("Settings are immutable.")
        super(Settings, self).__setattr__(key=key, value=value)

    def __getattr__(self, item):
        return options.options[item]

    @classmethod
    def register_content_type(cls, content_type_name, content_type_cls):
        if content_type_name in cls._setting_parsers:
            raise ValueError("Duplicate setting content type.")
        cls._setting_parsers[content_type_name] = content_type_cls

    def update_setting(self, name, value):
        setattr(options.options, name, value)


class SettingTypeMeta(type):

    def __init__(cls, name, bases, attrs):
        super(SettingTypeMeta, cls).__init__(name, bases, attrs)
        if getattr(cls, 'CONTENT_TYPE_NAMES', None):
            for content_type_name in cls.CONTENT_TYPE_NAMES:
                Settings.register_content_type(content_type_name=content_type_name, content_type_cls=cls)


class SettingType(metaclass=SettingTypeMeta):

    CONTENT_TYPE_NAMES = None
    OPTIONS_TYPE = None


class IntegerSettingType(SettingType):

    CONTENT_TYPE_NAMES = (int, 'int', 'integer')
    OPTIONS_TYPE = int

    @classmethod
    def decode(cls, value):
        if isinstance(value, int):
            return value
        return int(value)


class StringSettingType(SettingType):

    CONTENT_TYPE_NAMES = (str, 'str', 'string')
    OPTIONS_TYPE = str

    @classmethod
    def decode(cls, value):
        if isinstance(value, str):
            return value
        return str(value)


class BooleanSettingType(SettingType):

    CONTENT_TYPE_NAMES = (bool, 'bool', 'boolean')
    OPTIONS_TYPE = bool

    @classmethod
    def decode(cls, value):
        if isinstance(value, bool):
            return value
        if str(value).lower() in ('t', 'true', 'y', 'yes'):
            return True
        return False


settings = Settings(defines=DEFINES)
```

```project/project/settings/tests.py```:
```python
import os
import sys

from unittest import TestCase

from .defines import Setting
from .models import Settings


__all__ = ('TornadoSettingsTestCase',)


class TornadoSettingsTestCase(TestCase):

    SETTING_NAME = 'SETTINGS_TEST'
    ENV_SETTING_NAME = '{prefix}_{name}'.format(prefix=Settings.ENV_PREFIX, name=SETTING_NAME)

    def setUp(self):
        self.assertNotIn(self.ENV_SETTING_NAME, os.environ)
        self._sys_argv = tuple(sys.argv)

    def test_settings(self):
        DEFAULT_VALUE = 10
        ENVIRON_VALUE = 20
        COMMAND_LINE_VALUE = 30

        defines = (
            Setting(name=self.SETTING_NAME, content_type=int, default=DEFAULT_VALUE, description="Test."),
        )
        settings = Settings(defines=defines)
        self.assertEqual(getattr(settings, self.SETTING_NAME), DEFAULT_VALUE)

        os.environ[self.ENV_SETTING_NAME] = str(ENVIRON_VALUE)
        settings = Settings(defines=defines)
        self.assertEqual(getattr(settings, self.SETTING_NAME), ENVIRON_VALUE)

        sys.argv.insert(1, '--{name}={value}'.format(name=self.SETTING_NAME, value=COMMAND_LINE_VALUE))
        settings = Settings(defines=defines)
        self.assertEqual(getattr(settings, self.SETTING_NAME), COMMAND_LINE_VALUE)

    def test_edit_setting(self):
        DEFAULT_VALUE = 10
        NEW_VALUE = 20

        defines = (
            Setting(name=self.SETTING_NAME, content_type=int, default=DEFAULT_VALUE, description="Test."),
        )
        settings = Settings(defines=defines)
        self.assertEqual(getattr(settings, self.SETTING_NAME), DEFAULT_VALUE)

        self.assertRaises(RuntimeError, setattr, settings, self.SETTING_NAME, NEW_VALUE)

        self.assertEqual(getattr(settings, self.SETTING_NAME), DEFAULT_VALUE)
        settings.update_setting(name=self.SETTING_NAME, value=NEW_VALUE)
        self.assertEqual(getattr(settings, self.SETTING_NAME), NEW_VALUE)

    def tearDown(self):
        if self.ENV_SETTING_NAME in os.environ:
            del os.environ[self.ENV_SETTING_NAME]
        sys.argv = list(self._sys_argv)
```
