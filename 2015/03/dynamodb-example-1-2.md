labels: Blog
        DynamoDB
        Tornado
created: 2015-03-01T15:23
place: Phuket, Thailand

# DynamoDB in examples, Example 1.2: Asynchronous api calls (tornado)

The trick is to use tornado AsyncHTTPClient instead of one used in botocore.
tornado-botocore just patch botocore code, it is dirty workaround but I didn't found easier way to make it works.
I use it with botocore version 0.65.0 and It may be incompatible with other versions.

```bash
pip freeze
botocore==0.65.0
tornado==4.1
tornado-botocore==0.1.6
```

Updated User Wallet example:
```python
import logging
import re
import six
import uuid

from functools import partial

from tornado import gen
from tornado.ioloop import IOLoop
from tornado_botocore import Botocore


logger = logging.getLogger()


class AmazonException(Exception):

    def __init__(self, message, code='unknown'):
        self.message = message
        self.code = code

    def __str__(self):
        return self.message


class DDBException(AmazonException):

    ITEM_ENCODE_ERROR = 'ItemEncodeError'
    ITEM_DECODE_ERROR = 'ItemDecodeError'


class DDBField(object):

    @classmethod
    def _validate(cls, value):
        raise NotImplementedError('Not implemented.')

    @classmethod
    def decode(cls, value):
        try:
            return cls._validate(value)
        except (TypeError, ValueError):
            raise DDBException(
                message='Invalid value for {cls} decode.'.format(cls=cls.__name__),
                code=DDBException.ITEM_DECODE_ERROR)

    @classmethod
    def encode(cls, value):
        try:
            return str(cls._validate(value))
        except (TypeError, ValueError):
            raise DDBException(
                message='Invalid value for {cls} encode.'.format(cls=cls.__name__),
                code=DDBException.ITEM_ENCODE_ERROR)


class DDBIntField(DDBField):

    AMAZON_TYPE = 'N'

    @classmethod
    def _validate(cls, value):
        if isinstance(value, int):
            return value
        return int(value)


class DDBUUIDField(DDBField):

    AMAZON_TYPE = 'S'
    _UUID_REGEXP = re.compile('[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}')

    @classmethod
    def _validate(cls, value):
        if not isinstance(value, str):
            value = str(value)
        if cls._UUID_REGEXP.match(value) is None:
            raise ValueError('UUID required.')
        return value


class DDBTable(object):

    TABLE_NAME = ''
    REGION_NAME = 'us-west-2'
    KEY_SCHEMA = []
    LOCAL_SECONDARY_INDEXES = []
    GLOBAL_SECONDARY_INDEXES = []
    PROVISIONED_THROUGHPUT = {}
    FIELDS = {}

    _AMAZON_SESSION = None

    def _get_table_name(self):
        return self.TABLE_NAME

    def _get_table_kwargs(self):
        key_fields = set()
        for key in self.KEY_SCHEMA:
            key_fields.add(key['AttributeName'])
        for index in self.LOCAL_SECONDARY_INDEXES:
            for key in index['KeySchema']:
                key_fields.add(key['AttributeName'])
        for index in self.GLOBAL_SECONDARY_INDEXES:
            for key in index['KeySchema']:
                key_fields.add(key['AttributeName'])
        attribute_definitions = []
        for field_name in key_fields:
            attribute_definitions.append({
                'AttributeName': field_name,
                'AttributeType': self.FIELDS[field_name].AMAZON_TYPE
            })
        kwargs = {
            'TableName': self._get_table_name(),
            'AttributeDefinitions': attribute_definitions,
            'KeySchema': self.KEY_SCHEMA,
            'ProvisionedThroughput': self.PROVISIONED_THROUGHPUT,
        }
        if getattr(self, 'LOCAL_SECONDARY_INDEXES', None):
            kwargs['LocalSecondaryIndexes'] = self.LOCAL_SECONDARY_INDEXES
        if getattr(self, 'GLOBAL_SECONDARY_INDEXES', None):
            kwargs['GlobalSecondaryIndexes'] = self.GLOBAL_SECONDARY_INDEXES
        return kwargs

    def _get_endpoint_url(self):
        return None

    def _dynamodb(self, operation):
        if DDBTable._AMAZON_SESSION is None:
            ddb_operation = Botocore(
                service='dynamodb', operation=operation,
                region_name=self.REGION_NAME, endpoint_url=self._get_endpoint_url())
            DDBTable._AMAZON_SESSION = ddb_operation.session
        else:
            ddb_operation = Botocore(
                service='dynamodb', operation=operation,
                region_name=self.REGION_NAME, endpoint_url=self._get_endpoint_url(),
                session=DDBTable._AMAZON_SESSION)
        return ddb_operation

    def create_table(self):
        try:
            message = self._dynamodb(operation='DescribeTable').call(
                TableName=self._get_table_name())
        except AmazonException as e:
            if e.code != 'ResourceNotFoundException':
                raise e
            logger.warning('Creation {table_name} table ...'.format(
                table_name=self._get_table_name()))
            message = self._dynamodb(operation='CreateTable').call(
                **self._get_table_kwargs())
        else:
            logger.warning('{table_name} table already exists.'.format(
                table_name=self._get_table_name()))

    def encode_item(self, data, keys=None, update=False):
        if not data:
            return {}
        keys = keys or data.keys()
        item = {}
        for key in keys:
            if key not in data:
                continue
            val = self.FIELDS[key].encode(value=data[key])
            if update:
                item[key] = {
                    'Value': {
                        self.FIELDS[key].AMAZON_TYPE: val
                    },
                    'Action': 'PUT'
                }
            else:
                item[key] = {
                    self.FIELDS[key].AMAZON_TYPE: val
                }
        return item

    def decode_item(self, item, keys=None):
        data = {}
        for key, val in six.iteritems(item):
            if key not in self.FIELDS:
                continue
            if keys and key not in keys:
                continue
            data[key] = self.FIELDS[key].decode(
                val[self.FIELDS[key].AMAZON_TYPE])
        return data


class DDBUserWallet(DDBTable):

    TABLE_NAME = 'user_wallet'
    KEY_SCHEMA = [{
        'AttributeName': 'user_id',
        'KeyType': 'HASH',
    }]
    PROVISIONED_THROUGHPUT = {
        'ReadCapacityUnits': 1,
        'WriteCapacityUnits': 1
    }
    FIELDS = {
        'user_id': DDBUUIDField,
        'balance': DDBIntField,
    }

    @gen.coroutine
    def update(self, user_id, balance):
        message = yield gen.Task(self._dynamodb(operation='UpdateItem').call,
            TableName=self._get_table_name(),
            Key=self.encode_item(data={'user_id': user_id}),
            AttributeUpdates=self.encode_item(data={'balance': balance}, update=True))
        raise gen.Return(message)

    @gen.coroutine
    def get(self, user_id):
        message = yield gen.Task(self._dynamodb(operation='GetItem').call,
            TableName=self._get_table_name(),
            Key=self.encode_item(data={'user_id': user_id}))
        data = self.decode_item(item=message['Item'])
        raise gen.Return(data)

    # not required, just for example

    def update_(self, user_id, balance):
        """ Synchronous method
        """
        message = self._dynamodb(operation='UpdateItem').call(
            TableName=self._get_table_name(),
            Key=self.encode_item(data={'user_id': user_id}),
            AttributeUpdates=self.encode_item(data={'balance': balance}, update=True))
        return message

    def get_(self, user_id, callback):
        """ Example without coroutine
        """
        return self._dynamodb(operation='GetItem').call(
            TableName=self._get_table_name(),
            Key=self.encode_item(data={'user_id': user_id}),
            callback=callback)


if __name__ == '__main__':

    user_id = uuid.uuid4()

    user_wallet = DDBUserWallet()
    user_wallet.create_table()

    # You still can run code synchronous if required
    user_wallet.update_(user_id=user_id, balance=100)

    # run asynchronous with callback
    user_wallet.get_(user_id=user_id, callback=print)

    # You even can run methods wrapped with @coroutine synchronously
    ioloop = IOLoop.instance()
    result = ioloop.run_sync(partial(user_wallet.get, user_id=user_id))
    print(result)

    # output:
    # WARNING:root:user_wallet table already exists.
    # {'Item': {'user_id': {'S': 'badff6d6-41d4-46fb-ae74-ba19a2e69cb1'}, 'balance': {'N': '100'}}, 'ResponseMetadata': {'RequestId': '469JL4V0C9GQQJUHCF512VUGVNVV4KQNSO5AEMVJF66Q9ASUAAJG'}}
    # {'user_id': 'badff6d6-41d4-46fb-ae74-ba19a2e69cb1', 'balance': 100}
```

Tornado application:
```python
from main import DDBUserWallet
from tornado import web, ioloop, gen, options


class UserWalletHandler(web.RequestHandler):

    @gen.coroutine
    def post(self, user_id):
        balance = self.get_body_argument('balance')
        user_wallet = DDBUserWallet()
        yield user_wallet.update(user_id=user_id, balance=int(balance))
        self.write('Updated\n')

    @gen.coroutine
    def get(self, user_id):
        user_wallet = DDBUserWallet()
        response = yield user_wallet.get(user_id=user_id)
        self.write('{balance}\n'.format(balance=response['balance']))


application = web.Application([
    (r'/wallet/(?P<user_id>\w{8}-\w{4}-\w{4}-\w{4}-\w{12})', UserWalletHandler),
], debug=True)


if __name__ == "__main__":
    options.parse_command_line()
    DDBUserWallet().create_table()
    application.listen(5000)
    ioloop.IOLoop.instance().start()


# nanvel-air:example_1_2 nanvel$ curl --data "balance=123" http://localhost:5000/wallet/aa4d10c5-dd78-42ca-a077-3789b52ebbe3
# Updated
# nanvel-air:example_1_2 nanvel$ curl http://localhost:5000/wallet/aa4d10c5-dd78-42ca-a077-3789b52ebbe3
# 123
```
