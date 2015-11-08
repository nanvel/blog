labels: Blog
        Django
created: 2012-09-29T00:00
place: Alchevs'k, Ukraine
comments: true

# [Django] Get admin page url

```python
from django.contrib.contenttypes.models import ContentType
from django.core.urlresolvers import reverse

from my_project.apps.my_app.models import MyModel

...

    content_type = ContentType.objects.get_for_model(MyModel)
    url = reverse('admin:{app_label}_{model}_changelist'.format(
        app_label=content_type.app_label,
        model=content_type.model))
```

Other url-patterns:
```
'admin:index'
'admin:{app_label}_{model}_add'
'admin:{app_label}_{model}_change' choice.id
```

UPD, simple helper:
```python
from django.core.urlresolvers import reverse


class AdminURLs(object):

    urls = {}

    @classmethod
    def url(cls, obj, action='change', id=None):
        """
        :param obj: model class or object
        :param action: [add|change]
        :param id: id of object to change
        """
        table = obj._meta.db_table
        key = '{table}&{action}'.format(table=table, action=action)
        if key in cls.urls:
            url = cls.urls[key]
        else:
            if hasattr(obj._meta, 'model'):
                url = reverse('admin:{app_label}_{model}_{action}'.format(
                    app_label=obj._meta.app_label,
                    model=obj._meta.model,
                    action=action.replace('change', 'changelist')))
            else:
                url = reverse('admin:{app_label}_{model}_{action}'.format(
                    app_label=obj._meta.app_label,
                    model=obj._meta.module_name,
                    action=action.replace('change', 'changelist')))
            cls.urls[key] = url
        if id:
            url = '{url}{item_id}/'.format(url=url, item_id=id)
        return url

# usage:
# url = AdminURLs.url(obj=user, action='change', id=123)
```
