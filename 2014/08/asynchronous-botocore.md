labels: Blog
        Tornado
        AWS
created: 2014-08-30T00:00
place: Kyiv, Ukraine

# [tornado] Asynchronous botocore

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
