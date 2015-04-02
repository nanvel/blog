DynamoDB in examples, Example 2.3: Pagination
=============================================

`Table of contents <http://nanvel.com/p/dynamodb>`__

Let's add pagination for the page views example.

.. code-block:: python

    class DDBPageView(DDBTable):

        ...

        def page_views(self, page_id, last=None, limit=10):
            ddb_query = self._dynamodb(operation='Query')
            kwargs = {
                'TableName': self._get_table_name(),
                'IndexName': 'by_page_id',
                'KeyConditions': {
                    'page_id': {
                        'AttributeValueList': [{
                            'S': str(page_id),
                        }],
                        'ComparisonOperator': 'EQ'
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
        ddb_page_view = DDBPageView()
        ddb_page_view.create_table()
        pages = []
        for i in range(3):
            pages.append(uuid4())
        users = []
        for i in range(10):
            user_id = uuid4()
            users.append(user_id)
            for j in range(3):
                ddb_page_view.view(page_id=random.choice(pages), user_id=user_id)
        views, last = ddb_page_view.page_views(page_id=pages[0], limit=2)
        print(views, last)
        # [{'page_id': '83017f95-e4ca-4c25-a56b-d521897c0f70', 'user_id': 'a70d66d7-7fe7-41a3-bae3-1d8428918c9a', 'created': '2015-03-29 13:15:55.433674', 'page_id_user_id': '83017f95-e4ca-4c25-a56b-d521897c0f70_a70d66d7-7fe7-41a3-bae3-1d8428918c9a'}, {'page_id': '83017f95-e4ca-4c25-a56b-d521897c0f70', 'user_id': '2ea9bdf9-d0e6-4939-973c-977059f70761', 'created': '2015-03-29 13:15:55.494103', 'page_id_user_id': '83017f95-e4ca-4c25-a56b-d521897c0f70_2ea9bdf9-d0e6-4939-973c-977059f70761'}]
        # {'page_id': {'S': '83017f95-e4ca-4c25-a56b-d521897c0f70'}, 'created': {'S': '2015-03-29 13:15:55.494103'}, 'page_id_user_id': {'S': '83017f95-e4ca-4c25-a56b-d521897c0f70_2ea9bdf9-d0e6-4939-973c-977059f70761'}}
        views, last = ddb_page_view.page_views(page_id=pages[0], last=last, limit=2)
        print(views, last)
        # [{'page_id': '83017f95-e4ca-4c25-a56b-d521897c0f70', 'user_id': 'e1b98531-b366-460a-8aca-994e03171a80', 'created': '2015-03-29 13:15:55.293803', 'page_id_user_id': '83017f95-e4ca-4c25-a56b-d521897c0f70_e1b98531-b366-460a-8aca-994e03171a80'}, {'page_id': '83017f95-e4ca-4c25-a56b-d521897c0f70', 'user_id': 'c3c728d5-1db0-465e-935c-0bcf34151546', 'created': '2015-03-29 13:15:55.355471', 'page_id_user_id': '83017f95-e4ca-4c25-a56b-d521897c0f70_c3c728d5-1db0-465e-935c-0bcf34151546'}]
        # {'page_id': {'S': '83017f95-e4ca-4c25-a56b-d521897c0f70'}, 'created': {'S': '2015-03-29 13:15:55.355471'}, 'page_id_user_id': {'S': '83017f95-e4ca-4c25-a56b-d521897c0f70_c3c728d5-1db0-465e-935c-0bcf34151546'}}

^^ This way is preferable.

Alternative:

.. code-block:: python

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
                'IndexName': 'by_page_id',
                'KeySchema': [{
                        'AttributeName': 'page_id',
                        'KeyType': 'HASH'
                    }, {
                        'AttributeName': 'page_id_user_id_created',
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
            'page_id_user_id_created': DDBStrField,
            'created': DDBStrField,
        }

        def _get_endpoint_url(self):
            return DDB_LOCAL_URL

        def view(self, page_id, user_id):
            page_id_user_id = '{page_id}_{user_id}'.format(page_id=page_id, user_id=user_id)
            created = datetime.datetime.now()
            try:
                self._dynamodb(operation='PutItem').call(
                    TableName=self._get_table_name(),
                    Item=self.encode_item(data={
                        'page_id_user_id': page_id_user_id,
                        'created': str(created),
                        'page_id_user_id_created': '{page_id_user_id}_{created}'.format(
                            page_id_user_id=page_id_user_id, created=created),
                        'page_id': str(page_id),
                        'user_id': str(user_id)}),
                    ConditionExpression='attribute_not_exists(page_id_user_id)')
            except AmazonException as e:
                if e.code == 'ConditionalCheckFailedException':
                    return False # already exists
                raise e
            return True

        def page_views(self, page_id, last_page_id_user_id_created=None, limit=10):
            ddb_query = self._dynamodb(operation='Query')
            kwargs = {
                'TableName': self._get_table_name(),
                'IndexName': 'by_page_id',
                'KeyConditions': {
                    'page_id': {
                        'AttributeValueList': [{
                            'S': str(page_id),
                        }],
                        'ComparisonOperator': 'EQ'
                    },
                    'page_id_user_id_created': {
                        'AttributeValueList': [{
                            'S': str(last_page_id_user_id_created or page_id),
                        }],
                        'ComparisonOperator': 'GT'
                    },
                },
                'Limit': limit,
                'ScanIndexForward': True,
            }
            result = ddb_query.call(**kwargs)
            return [self.decode_item(item) for item in result.get('Items')]


    if __name__ == '__main__':
        ddb_page_view = DDBPageView()
        ddb_page_view.create_table()
        pages = []
        for i in range(3):
            pages.append(uuid4())
        users = []
        for i in range(10):
            user_id = uuid4()
            users.append(user_id)
            for j in range(3):
                ddb_page_view.view(page_id=random.choice(pages), user_id=user_id)
        views = ddb_page_view.page_views(page_id=pages[0], limit=2)
        print(views)
        # [{'page_id': '02246f83-140b-4850-9893-967229a37aef', 'page_id_user_id': '02246f83-140b-4850-9893-967229a37aef_2a45c61d-29df-4ea6-9eb4-9b5e17f1a5dd', 'page_id_user_id_created': '02246f83-140b-4850-9893-967229a37aef_2a45c61d-29df-4ea6-9eb4-9b5e17f1a5dd_2015-03-29 13:36:08.069563', 'user_id': '2a45c61d-29df-4ea6-9eb4-9b5e17f1a5dd', 'created': '2015-03-29 13:36:08.069563'}, {'page_id': '02246f83-140b-4850-9893-967229a37aef', 'page_id_user_id': '02246f83-140b-4850-9893-967229a37aef_58b78382-a5e8-412e-9e32-15a35d1cd30c', 'page_id_user_id_created': '02246f83-140b-4850-9893-967229a37aef_58b78382-a5e8-412e-9e32-15a35d1cd30c_2015-03-29 13:36:07.878259', 'user_id': '58b78382-a5e8-412e-9e32-15a35d1cd30c', 'created': '2015-03-29 13:36:07.878259'}]
        views = ddb_page_view.page_views(
            page_id=pages[0], last_page_id_user_id_created=views[-1]['page_id_user_id_created'],
            limit=2)
        print(views)
        # [{'page_id': '02246f83-140b-4850-9893-967229a37aef', 'page_id_user_id': '02246f83-140b-4850-9893-967229a37aef_79603222-1e31-4b1e-93a9-381d90d00945', 'page_id_user_id_created': '02246f83-140b-4850-9893-967229a37aef_79603222-1e31-4b1e-93a9-381d90d00945_2015-03-29 13:36:07.714803', 'user_id': '79603222-1e31-4b1e-93a9-381d90d00945', 'created': '2015-03-29 13:36:07.714803'}, {'page_id': '02246f83-140b-4850-9893-967229a37aef', 'page_id_user_id': '02246f83-140b-4850-9893-967229a37aef_bc75c6b9-da95-4cec-b232-a0eac6a53033', 'page_id_user_id_created': '02246f83-140b-4850-9893-967229a37aef_bc75c6b9-da95-4cec-b232-a0eac6a53033_2015-03-29 13:36:07.692193', 'user_id': 'bc75c6b9-da95-4cec-b232-a0eac6a53033', 'created': '2015-03-29 13:36:07.692193'}]

Query response `limited to 1MB <http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Limits.html>`__.
If You need to iterate through all query results:

.. code-block:: python

    class DDBPageView(DDBTable):

        ...

        def scan_page_views(self, page_id):
            ddb_query = self._dynamodb(operation='Query')
            last = None
            while True:
                kwargs = {
                    'TableName': self._get_table_name(),
                    'IndexName': 'by_page_id',
                    'KeyConditions': {
                        'page_id': {
                            'AttributeValueList': [{
                                'S': str(page_id),
                            }],
                            'ComparisonOperator': 'EQ'
                        },
                    },
                    'ScanIndexForward': True,
                }
                if last:
                    kwargs['ExclusiveStartKey'] = last
                result = ddb_query.call(**kwargs)
                for item in result.get('Items', []):
                    data = self.decode_item(item)
                    print(data)
                last = result.get('LastEvaluatedKey')
                if last is None:
                    break


    if __name__ == '__main__':
        ddb_page_view = DDBPageView()
        ddb_page_view.create_table()
        pages = []
        for i in range(2):
            pages.append(uuid4())
        users = []
        for i in range(100):
            user_id = uuid4()
            users.append(user_id)
            for j in range(3):
                ddb_page_view.view(page_id=random.choice(pages), user_id=user_id)
        ddb_page_view.scan_page_views(page_id=pages[0])

.. info::
    :tags: DynamoDB
    :place: KLIA2, Malaysia
