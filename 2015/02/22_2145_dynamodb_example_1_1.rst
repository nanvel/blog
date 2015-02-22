DynamoDB in examples, Example 1.1: DDBTable class
=================================================

I refactored previous example into:

.. code-block:: python

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

        def update(self, user_id, balance):
            message = self._dynamodb(operation='UpdateItem').call(
                TableName=self._get_table_name(),
                Key=self.encode_item(data={'user_id': user_id}),
                AttributeUpdates=self.encode_item(data={'balance': balance}, update=True))
            return message

        def get(self, user_id):
            message = self._dynamodb(operation='GetItem').call(
                TableName=self._get_table_name(),
                Key=self.encode_item(data={'user_id': user_id}))
            return self.decode_item(item=message['Item'])


    if __name__ == '__main__':

        user_id = uuid.uuid4()

        user_wallet = DDBUserWallet()
        user_wallet.create_table()
        user_wallet.update(user_id=user_id, balance=100)
        print(user_wallet.get(user_id=user_id))

        # output:
        # user_wallet table already exists.
        # {'user_id': '975ddae9-312e-472b-8aec-f7a3825132eb', 'balance': 100}

DDBTable and fields classes:

.. code-block:: python

    import botocore.session
    import logging
    import re
    import six
    import uuid

    from functools import partial


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


    class Botocore(object):

        _session = None

        def __init__(self, service, operation, region_name, endpoint_url=None):
            session = Botocore._session
            if session is None:
                session = botocore.session.get_session()
                Botocore._session = session
            service = session.get_service(service_name=service)
            self.endpoint = service.get_endpoint(
                region_name=region_name, endpoint_url=endpoint_url)
            self.operation = service.get_operation(operation_name=operation)

        def call(self, **kwargs):
            response, message = self.operation.call(endpoint=self.endpoint, **kwargs)
            if response.status_code != 200:
                raise AmazonException(
                    message='DynamoDB request error: {message}.'.format(
                        message=message.get('Error', {'Message': 'unknown'})['Message']),
                    code=message.get('Error', {'Code': 'unknown'})['Code'])
            return message


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
            return Botocore(
                service='dynamodb', operation=operation,
                region_name=self.REGION_NAME, endpoint_url=self._get_endpoint_url())

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

If You use tornado, try `tornado-botocore <https://github.com/nanvel/tornado-botocore>`__:

.. code-block:: python

    # pip install tornado-botocore
    from tornado_botocore import Botocore

to do requests asynchronously.

.. info::
    :tags: DynamoDB
    :place: Phuket, Thailand
