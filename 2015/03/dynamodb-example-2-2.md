labels: Blog
        Databases
        DynamoDB
created: 2015-03-21T13:22

# DynamoDB in examples, Example 2.2: Table secondary indexes

DynamoDB table may have two kinds of secondary indexes:

- local
- global

Possible to define up to 5 local and 5 global secondary indexes (see [DynamoDB limits](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Limits.html)).

Local secondary index has a big disadvantage: For every distinct hash key value, the total sizes of all table and index items cannot exceed 10 GB. So, if You don't sure what type of secondary index to choose - choose global secondary index.

Think about secondary index like one another table with different key schema but the same data.
When we create a new item, we need to create it in table and in every secondary index. So, summary consumed write cpacity will increase.
Write throughput for every global secondary index has to be equal to table write throughput.

This is one bad thing about indexes: they increase write throughput we pay for.
Another bad thing: we can't add or remove secondary indexes after table was created.
So, design table structure carefully.

If it happens that we will realize that we really need more secondary indexes but the table already contains data:

- create new table
- migrate all data from old one

Back to unique page views example. New requirements:

- list of pages particular user viewed
- list of users who viewed particular page

We need two global indexes: by user and by page. As range, I'll use created time.

```python
import datetime
import random

from uuid import uuid4
from ddb_table import (
    DDBTable, DDBUUIDField, DDBUUID_UUIDField,
    DDBStrField, AmazonException)


DDB_LOCAL_URL = 'http://localhost:8010'


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
    GLOBAL_SECONDARY_INDEXES = [{
        'IndexName': 'by_user_id',
            'KeySchema': [{
                    'AttributeName': 'user_id',
                    'KeyType': 'HASH'
                }, {
                    'AttributeName': 'created',
                    'KeyType': 'RANGE'
                }
            ],
            'Projection': {
                'ProjectionType': 'ALL',
            },
            'ProvisionedThroughput': {
                'ReadCapacityUnits': 1,
                'WriteCapacityUnits': 1,
            }
        }, {
            'IndexName': 'by_page_id',
            'KeySchema': [{
                    'AttributeName': 'page_id',
                    'KeyType': 'HASH'
                }, {
                    'AttributeName': 'created',
                    'KeyType': 'RANGE'
                }
            ],
            'Projection': {
                'ProjectionType': 'ALL',
            },
            'ProvisionedThroughput': {
                'ReadCapacityUnits': 1,
                'WriteCapacityUnits': 1,
            }
        }]
    FIELDS = {
        'page_id_user_id': DDBUUID_UUIDField,
        'page_id': DDBUUIDField,
        'user_id': DDBUUIDField,
        'created': DDBStrField,
    }

    def _get_endpoint_url(self):
        return DDB_LOCAL_URL

    def view(self, page_id, user_id):
        """ Returns True if item was created, else: returns False """
        page_id_user_id = '{page_id}_{user_id}'.format(page_id=page_id, user_id=user_id)
        try:
            self._dynamodb(operation='PutItem').call(
                TableName=self._get_table_name(),
                Item=self.encode_item(data={
                    'page_id_user_id': page_id_user_id,
                    'created': str(datetime.datetime.now()),
                    'page_id': str(page_id),
                    'user_id': str(user_id)}),
                ConditionExpression='attribute_not_exists(page_id_user_id)')
        except AmazonException as e:
            if e.code == 'ConditionalCheckFailedException':
                return False # already exists
            raise e
        return True

    def page_views(self, page_id):
        ddb_query = self._dynamodb(operation='Query')
        # TODO: pagination
        result = ddb_query.call(
            TableName=self._get_table_name(),
            IndexName='by_page_id',
            KeyConditions={
                'page_id': {
                    'AttributeValueList': [{
                        'S': str(page_id),
                    }],
                    'ComparisonOperator': 'EQ'
                }
            })
        return [self.decode_item(item) for item in result.get('Items')]

    def user_views(self, user_id):
        ddb_query = self._dynamodb(operation='Query')
        # TODO: pagination
        result = ddb_query.call(
            TableName=self._get_table_name(),
            IndexName='by_user_id',
            KeyConditions={
                'user_id': {
                    'AttributeValueList': [{
                        'S': str(user_id),
                    }],
                    'ComparisonOperator': 'EQ'
                }
            })
        return [self.decode_item(item) for item in result.get('Items')]


if __name__ == '__main__':
    ddb_page_view = DDBPageView()
    ddb_page_view.create_table()
    pages = []
    for i in range(10):
        pages.append(uuid4())
    users = []
    for i in range(10):
        user_id = uuid4()
        users.append(user_id)
        for j in range(3):
            ddb_page_view.view(page_id=random.choice(pages), user_id=user_id)
    print(ddb_page_view.page_views(page_id=pages[0]))
    print(ddb_page_view.page_views(page_id=pages[1]))
    print(ddb_page_view.user_views(user_id=users[0]))
    print(ddb_page_view.user_views(user_id=users[1]))
    # [{'user_id': 'c0744a82-ac6e-48c5-97e9-f74f8a8a5c8f', 'page_id': '4f618ed1-fed2-4b6e-8cc6-5cf510dda67e', 'page_id_user_id': '4f618ed1-fed2-4b6e-8cc6-5cf510dda67e_c0744a82-ac6e-48c5-97e9-f74f8a8a5c8f', 'created': '2015-03-21 13:19:44.603397'}, ...]
    # [{'user_id': '4fc8283c-20b5-4326-9432-544f699136a6', 'page_id': '01e379a2-6628-48e9-97ba-b082b3e2112f', 'page_id_user_id': '01e379a2-6628-48e9-97ba-b082b3e2112f_4fc8283c-20b5-4326-9432-544f699136a6', 'created': '2015-03-21 13:19:45.469416'}]
    # [{'user_id': 'b5f76efb-2d9e-4dd0-ac26-9108596c74e6', 'page_id': '8c8a3660-aaf2-4189-a239-3ae3538ff75d', 'page_id_user_id': '8c8a3660-aaf2-4189-a239-3ae3538ff75d_b5f76efb-2d9e-4dd0-ac26-9108596c74e6', 'created': '2015-03-21 13:19:44.270737'}, ...]
    # [{'user_id': 'b80f1750-4069-4d77-a2d1-edb83f8c9230', 'page_id': '6ea0815e-c4f5-4e02-8ce8-97d028f230ed', 'page_id_user_id': '6ea0815e-c4f5-4e02-8ce8-97d028f230ed_b80f1750-4069-4d77-a2d1-edb83f8c9230', 'created': '2015-03-21 13:19:44.440595'}, ...]
```

Place: Phuket, Thailand
