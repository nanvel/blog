labels: Blog
        Django
created: 2013-04-16T00:00
place: Starobilsk, Ukraine

# [Django] Pass iterator to response

Sometimes it may be more efficient to transmit response while it being generated.

[https://docs.djangoproject.com/en/dev/ref/request-response/#passing-iterators](https://docs.djangoproject.com/en/dev/ref/request-response/#passing-iterators)

Before use this, notice possible performance issues:

- Django is designed for short-lived requests. Streaming responses will tie a worker process for the entire duration of the response. This may result in poor performance.
- Generally speaking, you should perform expensive tasks outside of the request-response cycle, rather than resorting to a streamed response.

Small example:
```python
def my_iterator():
    yield 'Hi!\n'
    for i in MyModel.objects.all():
        yield '%s\n' % i.field
    yield 'By!\n'


def my_view(request):
    response = HttpResponse(my_iterator(), content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename=sometext.txt'
    return response
```
