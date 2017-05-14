labels: Blog
        Tornado
        AWS
        Asynchronous
created: 2014-08-30T00:00
modified: 2017-05-14T15:25
place: Kyiv, Ukraine
comments: true

# [tornado] Asynchronous botocore

[TOC]

## `tornado-botocore`

AWS services and boto project are great things, but that we can't use them asynchronously in tornado is a big disadvantage.

This article inspired me to search for a way to use boto asynchronously:
[http://blog.joshhaas.com/2011/06/marrying-boto-to-tornado-greenlets-bring-them-together/](http://blog.joshhaas.com/2011/06/marrying-boto-to-tornado-greenlets-bring-them-together/)

I found that it is easy to rewrite code in botocore and use tornado ```AsyncHTTPClien``` instead of ```urllib```.
The idea is to rewrite ```botocore.operation.call``` to make it uses ```tornado.httpclient.AsyncHTTPClient```. After some experiments I got a simple wrapper for botocore that allows to use it in tornado asynchronously.

Repository: [https://github.com/nanvel/tornado-botocore](https://github.com/nanvel/tornado-botocore)

PyPI: [https://pypi.python.org/pypi/tornado-botocore](https://pypi.python.org/pypi/tornado-botocore)

Installation:
```bash
pip install tornado-botocore
```

Usage example:
```python
from tornado.ioloop import IOLoop
from tornado_botocore import Botocore


def on_response(response):
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            print instance['InstanceId']


if __name__ == '__main__':
    ec2 = Botocore(
        service='ec2', operation='DescribeInstances',
        region_name='us-east-1')
    ec2.call(callback=on_response)
    IOLoop.instance().start()
```

Another one:
```python
@gen.coroutine
def send(self, ...):
    ses_send_email = Botocore(
        service='ses', operation='SendEmail',
        region_name='us-east-1')
    source = 'example@mail.com'
    message = {
        'Subject': {
            'Data': 'Example subject'.decode('utf-8'),
        },
        'Body': {
            'Html': {
                'Data': '<html>Example content</html>'.decode('utf-8'),
            },
            'Text': {
                'Data': 'Example content'.decode('utf-8'),
            }
        }
    }
    destination = {
        'ToAddresses': ['target@mail.com'],
    }
    res = yield gen.Task(ses_send_email.call,
        Source=source, Message=message, Destination=destination)
    raise gen.Return(res)
```

## HTTP client independent approach

UPD: 2017-05-14

```python
from threading import Lock

from botocore.endpoint import Endpoint
import botocore.session


class BotocoreRequest(Exception):

    def __init__(self, request, *args, **kwargs):
        super(BotocoreRequest, self).__init__(*args, **kwargs)
        self.method = request.method
        self.url = request.url
        self.headers = dict(request.headers)
        self.headers['User-Agent'] = 'my-useragent'
        self.body = request.body and request.body.read()


def _send_request(self, request_dict, operation_model):
    request = self.create_request(request_dict, operation_model)
    raise BotocoreRequest(request=request)


class AWSClient(object):
    """
    client = AWSClient(
        service='s3',
        access_key='<access key>',
        secret_key='<secret key>',
        region='<s3 region>'
    )

    request = client.request(
        method='head_object',
        Bucket='<s3 bucket>',
        Key='<key>'
    )

    See botocore api reference: http://botocore.readthedocs.io/en/latest/reference/index.html
    """
    def __init__(self, service, access_key, secret_key, region, timeout=30):
        session = botocore.session.get_session()
        session.set_credentials(
            access_key=access_key,
            secret_key=secret_key
        )
        self.client = session.create_client(service, region_name=region)
        self.timeout = timeout

    def request(self, method, **kwargs):
        _send_request_original = Endpoint._send_request
        lock = Lock()
        try:
            lock.acquire()
            Endpoint._send_request = _send_request
            getattr(self.client, method)(**kwargs)
        except BotocoreRequest as e:
            return {
                'method': e.method,
                'url': e.url,
                'headers': e.headers,
                'body': e.body
            }
        finally:
            Endpoint._send_request = _send_request_original
            lock.release()
```
