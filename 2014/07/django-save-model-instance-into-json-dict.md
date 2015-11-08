labels: Blog
        Django
created: 2014-07-06T00:00
place: Kyiv, Ukraine
comments: true

# [Django] Save model instance into json dict

I need to save a dict with numbers, text and django model instances. And I don't know which model instances may be present in the dict.

```python
data = {
    'count': 10,
    'title': 'Example title',
    'user': request.user,
}

# or

data = {
    'content': 'Example content',
    'site': Site.objects.get_current(),
}
```

If I try to dump dicts above, I'll get ```TypeError``` exception:
```python
>>> import json
>>> json.dumps(data)
TypeError: <User: exampleuser> is not JSON serializable
```

Possible solution:
```python
from django.contrib.contenttypes.models import ContentType
from django.db.models import Model


def encode(data):
    new_data = dict(data)
    for node, value in data.iteritems():
        if isinstance(value, Model):
            node_type = ContentType.objects.get_for_model(value.__class__)
            new_data[node] = {
                'app_label': node_type.app_label,
                'model': node_type.model,
                'id': value.id}
    return new_data

def decode(data):
    new_data = dict(data)
    for node, value in data.iteritems():
        if not isinstance(value, dict):
            continue
        if 'app_label' in value and 'model' in value and 'id' in value:
            user_type = ContentType.objects.get(
                app_label=value['app_label'],
                model=value['model'])
            new_data[node] = user_type.get_object_for_this_type(id=value['id'])
    return new_data
```

```python
>>> data
{'count': 10, 'user': <User: exampleuser>, 'title': 'Example title'}
>>> json.dumps(data)
TypeError: <User: exampleuser> is not JSON serializable
>>> encoded = json.dumps(encode(data))
>>> encoded
'{"count": 10, "user": {"model": "user", "id": 1, "app_label": "auth"}, "title": "Example title"}'
>>> decode(json.loads(encoded))
{u'count': 10, u'user': <User: exampleuser>, u'title': u'Example title'}
```
