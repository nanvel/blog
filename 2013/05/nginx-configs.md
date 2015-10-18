labels: Blog
        DevOps
created: 2013-05-01T00:00
place: Starobilsk, Ukraine

# Domain configuration in nginx config

Redirect ```www.mydomain.com``` to ```mydomain.com```:
```nginx
server {
    server_name www.mydomain.com;
    return 301 http://domain.com$request_uri;
}

server {
    server_name mydomain.com;
    # The rest of your configuration goes here
}
```

Dot at the end of site domain can cause problems.

```nginx
server {
    server_name mydomain.com;
    if ($http_host ~ "\.$" ) {
        return 301 http://mydomain.com$request_uri;
    }
    # The rest of your configuration goes here
}
```

For old nginx versions:
```diff
- return 301 http://mydomain.com$request_uri;
+ rewrite  ^/(.*)$  http://mydomain.com/$1 permanent;
```

Links:

- [http://habrahabr.ru/post/172999/](http://habrahabr.ru/post/172999/)
- [http://stackoverflow.com/questions/7947030/nginx-no-www-to-www-and-www-to-no-www](http://stackoverflow.com/questions/7947030/nginx-no-www-to-www-and-www-to-no-www)
- [http://wiki.nginx.org/Pitfalls](http://wiki.nginx.org/Pitfalls)
- [http://stackoverflow.com/questions/15452328/nginx-redirect-domain-trailing-dot](http://stackoverflow.com/questions/15452328/nginx-redirect-domain-trailing-dot)
