[tornado] Asynchronous botocore
===============================

AWS services and boto project are great things, but that we can't use them asynchronously in tornado is a big disadvantage.

This article inspired me to search for a way to use boto asynchronously:
http://blog.joshhaas.com/2011/06/marrying-boto-to-tornado-greenlets-bring-them-together/

I found that it is easy to rewrite code in botocore and use tornado ``AsyncHTTPClien`` instead of ``urllib``.
The idea is to rewrite ``botocore.operation.call`` to make it uses ``tornado.httpclient.AsyncHTTPClient``. After some experiments I got a simple wrapper for botocore that allows to use it in tornado asynchronously.

Repository: https://github.com/nanvel/tornado-botocore

PyPI: https://pypi.python.org/pypi/tornado-botocore

Installation:

.. code-block:: bash

    pip install tornado-botocore

Usage example:

.. code-block:: python

    from tornado.ioloop import IOLoop
    from tornado_botocore import Botocore


    def on_response(response):
        http_response, response_data = response
        print response_data


    if __name__ == '__main__':
        ec2 = Botocore(
            service='ec2', operation='DescribeInstances',
            region_name='us-east-1')
        ec2.call(callback=on_response)
        IOLoop.instance().start()

.. info::
    :tags: AWS, Tornado, Botocore
    :place: Kyiv, Ukraine
