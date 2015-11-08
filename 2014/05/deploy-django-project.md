labels: Blog
        Django
        DevOps
created: 2014-05-04T00:00
place: Starobilsk, Ukraine
comments: true

# A way to deploy a django project, detailed instruction

![Deploy a Django project](djangodeploy.jpg)

I am going to show how to deploy [hello world django project](https://bitbucket.org/nanvel/helloworld) on VPS.

[TOC]

## Step 1 - Get VPS

Go to [digitalocean.com](http://digitalocean.com) and create new droplet (vps).

In this example I'll use Ubuntu 14.04 x64.

After droplet will be created (few minutes), you'll receive a letter similar to this:
```text
Your new droplet has been created!

You can access it using the following credentials:
IP Address: xxx.xxx.xxx.xxx
Username: root
Password: xxxxxxxxxxxx
```

## Step 2 - Update system

```bash
ssh root@xxx.xxx.xxx.xxx
apt-get update
apt-get upgrade
```

## Step 3 - Create user

```bash
useradd -m deploy
passwd deploy
# remember the password :)
vim /etc/sudoers
# add 'deploy  ALL=(ALL:ALL) ALL'
usermod deploy -s /bin/bash
exit
```

## Step 4 - Use ssh key to access the server instead of enter password

```bash
# on development machine
ssh-copy-id deploy@xxx.xxx.xxx.xxx
ssh deploy@xxx.xxx.xxx.xxx
```

## Step 5 - Install necessary packages

```bash
sudo apt-get install git nginx python-dev python-virtualenv postgresql postgresql-server-dev-9.3
```

## Step 6 - Generate ssh keys (to configure access to your private repository)

```bash
ssh-keygen -t rsa
cat ~/.ssh/id_rsa.pub
# add key to your repository ssh keys
```

## Step 7 - Create folders and clone the project source

```bash
mkdir sites
cd sites/
mkdir helloworld
cd helloworld/
git clone https://nanvel@bitbucket.org/nanvel/helloworld.git
mkdir media
mkdir static
mkdir conf
```

Result:
```
/home/deploy/sites/
- helloworld
-- helloworld
-- media
-- static
-- conf
```

## Step 8 - Create virtual environment and install necessary python packages

```bash
cd helloworld/
virtualenv .env --no-site-packages
source .env/bin/activate
pip install -r requirements.txt
pip install psycopg2 flup
```

## Step 9 - Create database, configure postgresql

```bash
sudo su - postgres
postgres@geekblog:~$ psql template1
template1=# CREATE USER helloworld WITH PASSWORD 'helloworld';
template1=# CREATE DATABASE helloworld;
template1=# GRANT ALL PRIVILEGES ON DATABASE helloworld to helloworld;
template1=# \q

vim /etc/postgresql/9.3/main/pg_hba.conf
# add 'local   helloworld     helloworld                               password'
```

## Step 10 - Update the project settings

Set admins, database credentials, SECRET_KEY, etc.

```helloworld/helloword/settings/local.py```:
```python
from .utils import rel


DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('My Name', 'myemail@mail.com'),
)

MANAGERS = ADMINS

ALLOWED_HOSTS = ['mydomain.com']

SECRET_KEY = 'somenewkey....'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'helloworld',
        'USER': 'helloworld',
        'PASSWORD': 'helloworld',
        'HOST': '',
        'PORT': '',
    }
}

MEDIA_ROOT = rel('../media/')
STATIC_ROOT = rel('../static/')
```

```bash
cd /home/deploy/sites/helloworld/helloworld/
source .env/bin/activate
python manage.py syncdb
python manage.py collectstatic
```

## Step 11 - Nginx configuration

```/etc/nginx/fastcgi_params```:
```nginx
fastcgi_param QUERY_STRING $query_string;
fastcgi_param REQUEST_METHOD $request_method;
fastcgi_param CONTENT_TYPE $content_type;
fastcgi_param CONTENT_LENGTH $content_length;
fastcgi_param PATH_INFO $fastcgi_script_name;
fastcgi_param REQUEST_URI $request_uri;
fastcgi_param DOCUMENT_URI $document_uri;
fastcgi_param DOCUMENT_ROOT $document_root;
fastcgi_param SERVER_PROTOCOL $server_protocol;
fastcgi_param GATEWAY_INTERFACE CGI/1.1;
fastcgi_param SERVER_SOFTWARE nginx/$nginx_version;
fastcgi_param REMOTE_ADDR $remote_addr;
fastcgi_param REMOTE_PORT $remote_port;
fastcgi_param SERVER_ADDR $server_addr;
fastcgi_param SERVER_PORT $server_port;
fastcgi_param SERVER_NAME $server_name;
```

```/etc/nginx/nginx.conf```:
```nginx
user deploy;
worker_processes 2;
pid /run/nginx.pid;

events {
    worker_connections 200;
    # multi_accept on;
}

http {
    sendfile on;
    tcp_nopush on;
    tcp_nodelay on;
    keepalive_timeout 65;
    types_hash_max_size 2048;
    # server_tokens off;

    server_names_hash_bucket_size 64;
    # server_name_in_redirect off;

    include /etc/nginx/mime.types;
    default_type application/octet-stream;

    ##
    # Logging Settings
    ##

    access_log /var/log/nginx/access.log;
    error_log /var/log/nginx/error.log;

    ##
    # Gzip Settings
    ##

    gzip on;
    gzip_disable "msie6";

    # gzip_vary on;
    # gzip_proxied any;
    # gzip_comp_level 6;
    # gzip_buffers 16 8k;
    # gzip_http_version 1.1;
    # gzip_types text/plain text/css application/json application/x-javascript text/xml application/xml application/xml+rss text/javascript;

    #include /etc/nginx/naxsi_core.rules;

    #passenger_root /usr;
    #passenger_ruby /usr/bin/ruby;

    include /home/deploy/sites/helloworld/conf/nginx.conf;
}
```

```/home/deploy/sites/helloworld/nginx.conf```:
```nginx
server {
    server_name  www.mydomain.com;
    rewrite  ^/(.*)$  http://mydomain.com/$1 permanent;
}

server {
    listen       80;
    server_name  mydomain.com;

    charset utf-8;

    if ($http_host ~ "\.$" ) {
        rewrite ^/(.*)$ http://$host$1 permanent;
    }

    location /media {
        root /home/deploy/sites/helloworld;
        expires 30d;
    }

    location /static {
        root /home/deploy/sites/helloworld;
        expires 30d;
    }

    location / {
        include /etc/nginx/fastcgi_params;
        fastcgi_pass unix:/home/deploy/sites/helloworld/conf/helloworld.sock;
    }

    error_page   500 502 503 504  /50x.html;
    location = /50x.html {
        root   html;
    }
}
```

! change ```mydomain.com``` to proper name.

## Step 12 - Configure fastcgi

```/etc/init.d/fastcgi_helloworld```:
```bash
#! /bin/bash

### BEGIN INIT INFO
# Provides:          start_fastcgi
# Required-Start:    $all
# Required-Stop:     $all
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: starts the fastcgi
# Description:       starts fastcgi
### END INIT INFO

FCGIUSER=deploy
FCGIGROUP=deploy
PYTHONBIN=/home/deploy/sites/helloworld/helloworld/.env/bin/python
FCGIAPP=/home/deploy/sites/helloworld/helloworld/manage.py
FCGISOCKET=/home/deploy/sites/helloworld/conf/helloworld.sock
PIDFILE=/home/deploy/sites/helloworld/conf/helloworld.pid
DESC="FastCGI starter for Django"

# Gracefully exit if the package has been removed;

start() {
  $PYTHONBIN $FCGIAPP runfcgi method=threaded socket=$FCGISOCKET pidfile=$PIDFILE
  chown $FCGIUSER $FCGISOCKET
}
stop() {
  kill -QUIT `cat $PIDFILE` || echo -en "\n not running"
}
restart() {
  kill -HUP `cat $PIDFILE` || echo -en "\n can't reload"
  deactivate
}
case "$1" in
  start)
    echo -n "Starting $DESC: "
    start
  ;;
  stop)
    echo -n "Stopping $DESC: "
    stop
  ;;
  restart|reload)
    echo -n "Restarting $DESC: "
    stop
    sleep 1
    start
  ;;
  *)
    echo "Usage: $SCRIPTNAME {start|stop|restart|reload}" >&2
    exit 3
  ;;
esac
exit $?
```

```bash
sudo chmod +x /etc/init.d/fastcgi_helloworld
sudo update-rc.d fastcgi_helloworld defaults
sudo /etc/init.d/fastcgi_helloworld start
sudo /etc/init.d/nginx restart
```

**This is not the best configuration, even not preferred one, this one is just 'works for me'.
If You use it, keep in mind that only you responsible for possible damage caused by using this material.**
