labels: Blog
        DynamoDB
        Databases
created: 2015-03-14T21:04

# DynamoDB in examples, Example 2.1: Key schema and counters

DynamoDB table may have two variants of [key schema](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DataModel.html#DataModel.PrimaryKey):

- HASH key
- HASH key + RANGE key

The main points You need to understand:

- HASH key generates from content inside HASH field (hash field may contains string, number, binary data, etc.) using [hash function](http://en.wikipedia.org/wiki/Hash_function)
- depends on hash key DynamoDB selects server to store the item. It allows to scale horizontally with easily (see [hash ring](http://en.wikipedia.org/wiki/Consistent_hashing))
- HASH field is unsorted and RANGE - sorted
- RANGE field index stores on single server (selects depends on HASH key)

These points will help us to find out which key schema will work for us best.
For now, it should be clear that table items stores on great amount of servers and to count them is a difficult task.
So DynamoDB haven't items count feature (like ```SELECT count(*) FROM page_views WHERE page_id = '{page_id}';```), and developers have to implement it themselves (actually, we can see items count in dynamodb table console, but it updates only once per day).

With current ```page_views``` table implementation, the only way to count particular page views count is [scan](http://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_Scan.html) all items:
```python
class DDBPageView(DDBTable):

    ...

    def page_views_count(self, page_id):
        ddb_scan = self._dynamodb(operation='Scan')
        last = None
        query = {
            'TableName': self._get_table_name(),
            'ReturnConsumedCapacity': 'TOTAL',
        }
        count = 0
        while True:
            if last is not None:
                query['ExclusiveStartKey'] = last
            result = ddb_scan.call(**query)
            items = result.get('Items', [])
            print('page:', len(items), len(json.dumps(result)))
            for item in items:
                data = self.decode_item(item=item)
                if data['page_id_user_id'].startswith(str(page_id)):
                    count += 1
            last = result.get('LastEvaluatedKey', None)
            if last is None:
                break
        return count


if __name__ == '__main__':
    ddb_page_view = DDBPageView()
    ddb_page_view.create_table()
    # create page views
    page_id1 = uuid4()
    page_id2 = uuid4()
    for i in range(100):
        print(i)
        if i % 2 == 0:
            ddb_page_view.view(page_id=page_id1, user_id=uuid4())
        if i % 3 == 0:
            ddb_page_view.view(page_id=page_id2, user_id=uuid4())
    # get views count
    print(ddb_page_view.page_views_count(page_id=page_id1))
    print(ddb_page_view.page_views_count(page_id=page_id2))
    # page: 5611 589278
    # 50
    # page: 5611 589278
    # 34
    # If we will have only ~5000 page views,
    # we will need to retrive and process about half of megabite of data
```

**DON'T DO LIKE THIS! ^**

If we will have index on page_id, it may be much more efficient (and also we can use FilterExpression), but still not good.

If You need to know views count only once per year, it may be best solution. But if you need these numbers be uptodate, best way is to use counters.

```python
from uuid import uuid4
from ddb_table import (
    DDBTable, DDBUUIDField, DDBUUID_UUIDField,
    DDBStrField, DDBIntField, AmazonException)


DDB_LOCAL_URL = 'http://localhost:8010'


class DDBPage(DDBTable):

    TABLE_NAME = 'page'
    KEY_SCHEMA = [{
        'AttributeName': 'page_id',
        'KeyType': 'HASH',
    }]
    PROVISIONED_THROUGHPUT = {
        'ReadCapacityUnits': 1,
        'WriteCapacityUnits': 1
    }
    FIELDS = {
        'page_id': DDBUUIDField,
        'title': DDBStrField,
        'content': DDBStrField,
        'views_count': DDBIntField,
    }

    def _get_endpoint_url(self):
        return DDB_LOCAL_URL

    def create(self, title, content):
        data = {
            'page_id': uuid4(),
            'title': title,
            'content': content,
        }
        result = self._dynamodb(operation='PutItem').call(
            TableName=self._get_table_name(),
            Item=self.encode_item(data=data))
        return data['page_id']

    def get(self, page_id):
        result = self._dynamodb(operation='GetItem').call(
            TableName=self._get_table_name(),
            Key=self.encode_item(data={'page_id': page_id}))
        return self.decode_item(result['Item'])

    def increment_views_count(self, page_id):
        result = self._dynamodb(operation='UpdateItem').call(
            TableName=self._get_table_name(),
            UpdateExpression="ADD views_count :n",
            ExpressionAttributeValues={
                ':n': {
                    'N': u'1',
                }
            },
            Key=self.encode_item(data={'page_id': page_id}),
            ReturnValues='ALL_NEW')
        return self.decode_item(result['Attributes'])['views_count']


class DDBPageView(DDBTable):

    TABLE_NAME = 'page_view'
    KEY_SCHEMA = [{
        'AttributeName': 'page_id_user_id',
        'KeyType': 'HASH',
    }]
    PROVISIONED_THROUGHPUT = {
        'ReadCapacityUnits': 1,
        'WriteCapacityUnits': 1
    }
    FIELDS = {
        'page_id_user_id': DDBUUID_UUIDField,
    }

    def _get_endpoint_url(self):
        return DDB_LOCAL_URL

    def view(self, page_id, user_id):
        """ Returns True if item was created, else: returns False """
        page_id_user_id = '{page_id}_{user_id}'.format(page_id=page_id, user_id=user_id)
        try:
            self._dynamodb(operation='PutItem').call(
                TableName=self._get_table_name(),
                Item=self.encode_item(data={'page_id_user_id': page_id_user_id}),
                ConditionExpression='attribute_not_exists(page_id_user_id)')
        except AmazonException as e:
            if e.code == 'ConditionalCheckFailedException':
                return False # already exists
            raise e
        return True


if __name__ == '__main__':
    ddb_page_view = DDBPageView()
    ddb_page_view.create_table()
    ddb_page = DDBPage()
    ddb_page.create_table()
    # create page views
    page_id1 = ddb_page.create(title='Page 1', content='Content 1')
    page_id2 = ddb_page.create(title='Page 2', content='Content 2')
    for i in range(100):
        print(i)
        if i % 2 == 0:
            created = ddb_page_view.view(page_id=page_id1, user_id=uuid4())
            if created:
                ddb_page.increment_views_count(page_id=page_id1)
        if i % 3 == 0:
            created = ddb_page_view.view(page_id=page_id2, user_id=uuid4())
            if created:
                ddb_page.increment_views_count(page_id=page_id2)
    # get views count
    print(ddb_page.get(page_id=page_id1)['views_count'])
    print(ddb_page.get(page_id=page_id2)['views_count'])
    # 50
    # 34
```

Be careful when selecting place for counters: in my example, if single page will have a lot of views same time, we may have throttled writes problem.

Place: Phuket, Thailand
