labels: Blog
        Databases
        DynamoDB
created: 2015-04-12T12:45

# DynamoDB in examples, Example 3: Toys store orders

Lets imagine that we working on online toys store. Current task is:

- track orders processing
- save user/product purchases for analysing in future
- save user purchases history

User order status may be equal to:

- in_progress
- completed
- canceled

We need next methods to modify order:

- create new order
- update order status

Methods to get orders:

- get user orders completed and in progress
- get product orders in_progress
- get product orders completed
- get product orders canceled

```python
import datetime
import random

from uuid import uuid4

from ddb_table import DDBTable, DDBUUIDField, DDBIntField, DDBInt_IntField


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
                    'AttributeName': 'order_status_created',
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
            'IndexName': 'for_product_id',
            'KeySchema': [{
                    'AttributeName': 'product_id',
                    'KeyType': 'HASH'
                }, {
                    'AttributeName': 'order_status_created',
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
        'order_status_created': DDBInt_IntField,
    }

    def _get_endpoint_url(self):
        return DDB_LOCAL_URL

    def create_order(self, user_id, product_id):
        order_id = uuid4()
        created = datetime.datetime.utcnow().timestamp()
        order_status = self.ORDER_IN_PROGRESS
        order_status_created = '{order_status}_{created}'.format(
            order_status=order_status, created=created)
        data = {
            'order_id': order_id,
            'user_id': user_id,
            'product_id': product_id,
            'created': created,
            'order_status': order_status,
            'order_status_created': order_status_created,
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
            UpdateExpression='SET order_status = :order_status, order_status_created = :order_status_created',
            ExpressionAttributeValues={
                ':order_status': {
                    'N': str(order_status),
                },
                ':order_status_created': {
                    'S': '{order_status}_{created}'.format(
                        order_status=order_status,
                        created=item['created']),
                }
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
                'order_status_created': {
                    'AttributeValueList': [{
                        'S': '{order_status}_0'.format(order_status=self.ORDER_IN_PROGRESS - 1),
                    }, {
                        'S': '{order_status}_0'.format(order_status=self.ORDER_COMPLETED + 1),
                    }],
                    'ComparisonOperator': 'BETWEEN'
                },
            },
            'Limit': limit
        }
        if last:
            kwargs['ExclusiveStartKey'] = last
        result = ddb_query.call(**kwargs)
        return (
            [self.decode_item(item) for item in result.get('Items')],
            result.get('LastEvaluatedKey'))

    def get_product_orders(self, product_id, order_status, limit=10, last=None):
        ddb_query = self._dynamodb(operation='Query')
        kwargs = {
            'TableName': self._get_table_name(),
            'IndexName': 'for_product_id',
            'KeyConditions': {
                'product_id': {
                    'AttributeValueList': [{
                        'S': str(product_id),
                    }],
                    'ComparisonOperator': 'EQ'
                },
                'order_status_created': {
                    'AttributeValueList': [{
                        'S': '{order_status}_0'.format(order_status=order_status - 1),
                    }, {
                        'S': '{order_status}_0'.format(order_status=order_status + 1),
                    }],
                    'ComparisonOperator': 'BETWEEN'
                },
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
    products = []
    for i in range(10):
        products.append(str(uuid4()))
    users = []
    for i in range(10):
        users.append(str(uuid4()))
    for i in range(20):
        result = ddb_order.create_order(
            user_id=random.choice(users),
            product_id=random.choice(products))
        ddb_order.update_order_status(
            order_id=result['order_id'],
            order_status=random.choice(ddb_order.ORDER_STATUS_CHOICES))
    user_orders = ddb_order.get_user_orders(user_id=users[0])
    print(user_orders)
    orders_in_progress = ddb_order.get_product_orders(
        product_id=products[0], order_status=ddb_order.ORDER_IN_PROGRESS)
    print(orders_in_progress)
    # ([{'product_id': 'ad3ffb1e-f3eb-46bc-bebc-201034f757e6', 'user_id': 'e7aa25d8-2b1b-4fea-a735-4dbeeff06aaa', 'created': 1428791681, 'order_status_created': '201_1428791681', 'order_status': 201, 'order_id': 'f14e47c3-0232-430c-b79c-65b9ab000110'}], None)
    # ([{'product_id': '2d0126e0-92f7-437d-a938-41f95046d502', 'user_id': '917d107b-035e-4c02-a06b-343840fee92e', 'created': 1428791681, 'order_status_created': '101_1428791681', 'order_status': 101, 'order_id': '5ce48b08-2041-4d6b-82b4-7b1814d918ff'}, {'product_id': '2d0126e0-92f7-437d-a938-41f95046d502', 'user_id': '539f35ca-aed1-4353-80c2-0cd496bca092', 'created': 1428791681, 'order_status_created': '101_1428791681', 'order_status': 101, 'order_id': '3e5a8e0d-f76d-48ee-9c41-279f548f19cb'}], None)
```

## Reserved words

Pay attention that I use ```order_status``` instead of ```status``` field name.
DynamoDB has many [reserved words](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/ReservedWords.html) that can't be used inside UpdateExpression.

Place: Phuket, Thailand
