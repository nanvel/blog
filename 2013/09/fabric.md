labels: Blog
        DevOps
created: 2013-09-07T00:00

# Fabric helps to escape repeatable and annoying work

![Fabric](fabric.jpg)

Instead of doing something like this:
```bash
ssh deploy@example.com
cd /home/deploy/envs/myproject
git pull origin master
source .env/bin/activate
python manage.py migrate
python manage.py collectstatic
sudo /etc/init.d/project_fastcgi restart
pass
exit
```

with fabric I just do:
```bash
fab deploy
```

Fabric is such sort of things that hard to understand, but when You become familiar with it, many things become much easier to do.

Fabric should be installed only on development machine, so I add ```Fabric``` to ```requirements/dev.txt```.

Next step, after Fabric installation, is creating ```fabfile.py``` (I place it in a project root).

```fabfile.py``` for example:
```python
from os import environ

from django.core.exceptions import ImproperlyConfigured
from fabric.api import run, sudo, cd, env


PROJECT_ROOT = '/home/deploy/envs/project'
SERVER = 'example.com'
USER = 'deploy'
PASSWORD_ENV_VAR = 'MY_SEVER_PASS'

env.hosts = [SERVER]
env.user = USER
try:
    env.password = environ[PASSWORD_ENV_VAR]
except KeyError:
    raise ImproperlyConfigured('%s is not specified' % PASSWORD_ENV_VAR)


def deploy():
    with cd(PROJECT_ROOT):
        run('git pull origin master')
        run('.env/bin/python manage.py migrate')
        run('.env/bin/python manage.py collectstatic --noinput')
        sudo('/etc/init.d/project_fastcgi restart')
```

```run``` function runs a shell command on a remote host.
```sudo``` function runs a shell command on a remote host, with superuser privileges.
```cd``` adds prefix to paths on a remote server.
```env.hosts``` - global host list used when composing per-task host lists.
```env.user``` - username used when making SSH connections (default - local username).
```env.password``` - used to explicitly set your default connection or sudo password if desired.

Password should be specified in MY_SEVER_PASS environment variable:
```bash
export MY_SEVER_PASS=mypass
```

Fabric will prompt you to enter a password if password isn’t set or doesn’t appear to be valid. 

Fabric can run commands on local machine as well:
```python
from fabric.api import local


def commit_and_push():
    local('git commit -a -m "some change"')
    local('git push origin master')
```

```local``` - run a shell command on local machine.

```cd``` works only for path on remote server, for path on local machine ```lcd``` context manager should be used instead.

Next example - create backups on remote server and copy them to local machine:
```python
import datetime

from os import environ, path

from django.core.exceptions import ImproperlyConfigured
from fabric.api import run, cd, env, get


DUMPS_DIR = '/home/iam/projects/dupms/project/'

PROJECT_ROOT = '/home/deploy/envs/project'
MEDIA_ROOT = '/home/deploy/project/media'
SERVER = 'example.com'
USER = 'deploy'
PASSWORD_ENV_VAR = 'MY_PROJECT_PASS'

env.user = USER
env.hosts = [SERVER]


try:
    env.password = environ[PASSWORD_ENV_VAR]
except KeyError:
    raise ImproperlyConfigured('%s is not specified' % PASSWORD_ENV_VAR)


def get_db_dump():
    with cd(PROJECT_ROOT):
        run('bash dump.sh')
        get('dump.gz', path.join(
            DUMPS_DIR,
            datetime.datetime.strftime(
                datetime.datetime.now(), 'db_%Y%m%d_%H%M%S.dump.gz')))

def get_media_dump():
    zip_file = '%s.zip' % MEDIA_ROOT
    run('zip -r %s %s' % (zip_file, MEDIA_ROOT))
    get(zip_file, path.join(
        DUMPS_DIR,
        datetime.datetime.strftime(
            datetime.datetime.now(), 'media_%Y%m%d_%H%M%S.zip')))
    run('rm %s' % zip_file)
```

```get``` - download one or more files from a remote host.
Remote path can be file or directory.

Opposite to ```get``` exists ```put``` command:
```put``` - upload one or more files to a remote host.

Links:

- [http://yuji.wordpress.com/2011/04/09/django-python-fabric-deployment-script-and-example/](http://yuji.wordpress.com/2011/04/09/django-python-fabric-deployment-script-and-example/)
- [http://www.clemesha.org/blog/modern-python-hacker-tools-virtualenv-fabric-pip/](http://www.clemesha.org/blog/modern-python-hacker-tools-virtualenv-fabric-pip/)
- [http://docs.fabfile.org](http://docs.fabfile.org)

[Image](http://www.flickr.com/photos/cogdog/2853087377/) by Alan Levine.

Place: Starobilsk, Ukraine
