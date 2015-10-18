labels: Blog
        Databases
        DynamoDB
created: 2015-05-01T14:52
place: Phuket, Thailand

# DynamoDB in examples, Example 3.2: FilterExpression and pagination issue

You may noticed that in the Example 3 we used pretty weird index field: 'order_status_created'.
I had two reasons to use it instead of [filter expression](http://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_Query.html#DDB-Query-request-FilterExpression):

- it is more efficient
- pagination issue

In this example I am going to show that pagination doesn't work properly if You use filter expression.

```python
import datetime

from ddb_table import DDBTable, DDBUUIDField, DDBIntField, DDBInt_IntField
from uuid import uuid4


DDB_LOCAL_URL = 'http://localhost:8010'


class DDBOrder(DDBTable):

    ORDER_IN_PROGRESS = 101
    ORDER_COMPLETED = 201
    ORDER_CANCELED = 301

    ORDER_STATUS_CHOICES = [
        ORDER_IN_PROGRESS,
        ORDER_COMPLETED,
        ORDER_CANCELED,
    ]

    TABLE_NAME = 'purchase'
    KEY_SCHEMA = [{
        'AttributeName': 'order_id',
        'KeyType': 'HASH',
    }]
    PROVISIONED_THROUGHPUT = {
        'ReadCapacityUnits': 1,
        'WriteCapacityUnits': 1
    }
    GLOBAL_SECONDARY_INDEXES = [{
            'IndexName': 'for_user_id',
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
        }]
    FIELDS = {
        'order_id': DDBUUIDField,
        'user_id': DDBUUIDField,
        'product_id': DDBUUIDField,
        'created': DDBIntField,
        'order_status': DDBIntField,
    }

    def _get_endpoint_url(self):
        return DDB_LOCAL_URL

    def create_order(self, user_id, product_id):
        order_id = uuid4()
        created = datetime.datetime.utcnow().timestamp()
        order_status = self.ORDER_IN_PROGRESS
        data = {
            'order_id': order_id,
            'user_id': user_id,
            'product_id': product_id,
            'created': created,
            'order_status': order_status,
        }
        response = self._dynamodb(operation='PutItem').call(
            TableName=self._get_table_name(),
            Item=self.encode_item(data=data))
        return data

    def update_order_status(self, order_id, order_status):
        if order_status not in self.ORDER_STATUS_CHOICES:
            raise ValueError('Wrong order status.')
        response = self._dynamodb(operation='GetItem').call(
            TableName=self._get_table_name(),
            Key=self.encode_item(data={
                'order_id': order_id,
            }))
        item = self.decode_item(response['Item'])
        response = self._dynamodb(operation='UpdateItem').call(
            TableName=self._get_table_name(),
            Key=self.encode_item(data={
                'order_id': order_id,
            }),
            UpdateExpression='SET order_status = :order_status',
            ExpressionAttributeValues={
                ':order_status': {
                    'N': str(order_status),
                },
            },
            ReturnValues='ALL_NEW')
        return self.decode_item(response['Attributes'])

    def get_user_orders(self, user_id, limit=10, last=None):
        """ Returns user orders with order_status in [self.ORDER_IN_PROGRESS, self.ORDER_COMPLETED] """
        ddb_query = self._dynamodb(operation='Query')
        kwargs = {
            'TableName': self._get_table_name(),
            'IndexName': 'for_user_id',
            'KeyConditions': {
                'user_id': {
                    'AttributeValueList': [{
                        'S': str(user_id),
                    }],
                    'ComparisonOperator': 'EQ'
                },
            },
            'FilterExpression': 'order_status IN (:status_in_progress, :status_completed)',
            'ExpressionAttributeValues': {
                ':status_in_progress': {
                    'N': str(self.ORDER_IN_PROGRESS),
                },
                ':status_completed': {
                    'N': str(self.ORDER_COMPLETED),
                }
            },
            'Limit': limit
        }
        if last:
            kwargs['ExclusiveStartKey'] = last
        result = ddb_query.call(**kwargs)
        return (
            [self.decode_item(item) for item in result.get('Items')],
            result.get('LastEvaluatedKey'))


if __name__ == '__main__':
    ddb_order = DDBOrder()
    ddb_order.create_table()
    user_id = str(uuid4())
    for i in range(20):
        result = ddb_order.create_order(
            user_id=user_id,
            product_id=str(uuid4()))
        if i in [1, 6, 10, 15]:
            ddb_order.update_order_status(
                order_id=result['order_id'],
                order_status=ddb_order.ORDER_CANCELED)
        else:
            ddb_order.update_order_status(
                order_id=result['order_id'],
                order_status=ddb_order.ORDER_COMPLETED)

    user_orders = ddb_order.get_user_orders(user_id=user_id, limit=10)
    print(len(user_orders[0]))
    # 7
    user_orders = ddb_order.get_user_orders(user_id=user_id, limit=10, last=user_orders[1])
    print(len(user_orders[0]))
    # 9
```

As we can see, ```get_user_orders``` returns only 7 results while limit set to 10.
