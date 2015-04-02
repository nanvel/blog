DynamoDB in examples, Example 2: Unique page views
==================================================

`Table of contents <http://nanvel.com/p/dynamodb>`__

The simplest case:
    - store user/page views
    - allow to check user already viewed specified page

This example is similar to UserWallet example, the only trick is to use HASH keys like `{page_id}_{user_id}`.

.. code-block:: python

    import re
    import uuid

    from example_1 import DDBTable, DDBField, AmazonException


    DDB_LOCAL_URL = 'http://localhost:8010'


    class DDBUUID_UUIDField(DDBField):

        AMAZON_TYPE = 'S'
        _VALUE_REGEXP = re.compile('[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}_[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}')

        @classmethod
        def _validate(cls, value):
            if not isinstance(value, str):
                value = str(value)
            if cls._VALUE_REGEXP.match(value) is None:
                raise ValueError('UUID_UUID required.')
            return value


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

        def check(self, page_id, user_id):
            page_id_user_id = '{page_id}_{user_id}'.format(page_id=page_id, user_id=user_id)
            response = self._dynamodb(operation='GetItem').call(
                TableName=self._get_table_name(),
                Key=self.encode_item(data={'page_id_user_id': page_id_user_id}))
            return 'Item' in response


    if __name__ == '__main__':
        page_view = DDBPageView()
        page_view.create_table()
        page_id = uuid.uuid4()
        user_id = uuid.uuid4()
        print(page_view.view(page_id=page_id, user_id=user_id))
        print(page_view.view(page_id=page_id, user_id=user_id))
        print(page_view.check(page_id=page_id, user_id=user_id))
        user_id = uuid.uuid4()
        print(page_view.check(page_id=page_id, user_id=user_id))

        # True
        # False
        # True
        # False

Pretty easy, yes?

But what it we need also:
    - get particular page views count
    - get list of pages particular user viewed
    - get list of users who viewed particular page

?

These tasks require counters and indexes to be used.

.. info::
    :tags: DynamoDB, Tutorial
    :place: Phuket, Thailand
