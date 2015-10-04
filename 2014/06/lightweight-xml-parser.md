labels: Blog
        XML
created: 2014-06-22T00:00

# Lightweight xml parser

Dom parsers may consume over gigabytes of memory while parsing big amounts of xml data, sax parser works more effectively. This is an example how to use sax to transform xml into python data object.

```python
TEST_DATASET = [{
    # no keys specified
    'xml': """
<xml>
  <data>test</data>
</xml>""",
    'keys': [],
    'lists': [],
    'data': {},
    }, {
    # nonexistent key
    'xml': """
<xml>
  <data>test</data>
</xml>""",
    'keys': ['xml.data', 'xml.nonexistent'],
    'lists': [],
    'data': {'xml': {'data': 'test'}},
    }, {
    # attributes
    'xml': """
<xml>
  <data id="100"/>
</xml>""",
    'keys': ['xml.data.id'],
    'lists': [],
    'data': {'xml': {'data': {'id': "100"}}},
    }, {
    # lists
    'xml': """
<xml>
  <data>
    <item id="1">
        <color>purple</color>
    </item>
    <item id="2">
        <color>cyan</color>
    </item>
  </data>
</xml>""",
    'keys': ['xml.data.item.id', 'xml.data.item.color'],
    'lists': ['xml.data.item'],
    'data': {
        'xml': {
            'data': {
                'item': [
                    {'color': 'purple', 'id': '1'},
                    {'color': 'cyan', 'id': '2'}
                ]
            }
        }
    }},
]
```

Gist: [https://gist.github.com/nanvel/f944eae1f02d47b6d6a4](https://gist.github.com/nanvel/f944eae1f02d47b6d6a4)

```python
from xml import sax


class XMLParser(sax.handler.ContentHandler):

    def __init__(self, keys=[], lists=[], *args, **kwargs):
        """
        :param keys: list of data keys have to be available in data
        :param lists: list of nodes have be represented as list

        :example keys: 'messages.status', 'home.categories.item.label'
        :example lists: 'home.categories.item'
        """
        sax.handler.ContentHandler.__init__(self, *args, **kwargs)
        self.keys = keys
        self.lists = lists
        self.data = {}
        self.current_path = ''
        self.current_attrs = {}
        self.content = ''
        # short keys - keys without last element (used to parse attributes)
        self.short_keys = []
        for key in keys:
            parts = key.split('.')
            if len(parts) < 2:
                continue
            self.short_keys.append('.'.join(parts[:-1]))

    def startDocument(self):
        pass

    def startElement(self, name, attrs):
        self.current_attrs[name] = attrs
        if self.current_path:
            self.current_path += '.'
        self.current_path += name
        if self.current_path in self.lists:
            # create new item in list
            block = self.data
            path = self.current_path.split('.')
            for i, p in enumerate(path):
                if i == len(path) - 1:
                    if p not in block:
                        block[p] = [{}]
                    else:
                        block[p].append({})
                    break
                if '.'.join(path[:i + 1]) in self.lists:
                    block = block[p][-1]
                else:
                    if p not in block:
                        block[p] = {}
                    block = block[p]

    def characters(self, content):
        self.content += content

    def addValue(self, path_str, value):
        block = self.data
        path = path_str.split('.')
        for i, p in enumerate(path):
            if i == len(path) - 1:
                block[p] = value
                break
            if '.'.join(path[:i + 1]) in self.lists:
                block = block[p][-1]
            else:
                if p not in block:
                    block[p] = {}
                block = block[p]

    def endElement(self, name):
        if self.current_path in self.keys:
            self.addValue(self.current_path, self.content.strip())
        elif self.current_path in self.short_keys:
            # parse attributes
            attrs = self.current_attrs[self.current_path.split('.')[-1]]
            for k in attrs.keys():
                path = '{path}.{attr}'.format(path=self.current_path, attr=k)
                if path in self.keys:
                    self.addValue(path, attrs[k])
        self.current_path = '.'.join(
            self.current_path.split('.')[:-1])
        self.content = ''

    def endDocument(self):
        pass


TEST_DATASET = [{
    # no keys specified
    'xml': """
<xml>
  <data>test</data>
</xml>""",
    'keys': [],
    'lists': [],
    'data': {},
    }, {
    # nonexistent key
    'xml': """
<xml>
  <data>test</data>
</xml>""",
    'keys': ['xml.data', 'xml.nonexistent'],
    'lists': [],
    'data': {'xml': {'data': 'test'}},
    }, {
    # attributes
    'xml': """
<xml>
  <data id="100"/>
</xml>""",
    'keys': ['xml.data.id'],
    'lists': [],
    'data': {'xml': {'data': {'id': "100"}}},
    }, {
    # lists
    'xml': """
<xml>
  <data>
    <item id="1">
        <color>purple</color>
    </item>
    <item id="2">
        <color>cyan</color>
    </item>
  </data>
</xml>""",
    'keys': ['xml.data.item.id', 'xml.data.item.color'],
    'lists': ['xml.data.item'],
    'data': {
        'xml': {
            'data': {
                'item': [
                    {'color': 'purple', 'id': '1'},
                    {'color': 'cyan', 'id': '2'}
                ]
            }
        }
    }},
]


if __name__ == '__main__':
    for test_data in TEST_DATASET:
        parser = XMLParser(
            keys=test_data['keys'],
            lists=test_data['lists'])
        sax.parseString(test_data['xml'], parser)
        assert parser.data == test_data['data'], '{0} != {1}'.format(
            parser.data, test_data['data'])
```

Place: Kyiv, Ukraine
