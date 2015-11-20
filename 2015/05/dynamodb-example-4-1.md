labels: Blog
        Databases
        DynamoDB
created: 2015-05-30T16:56
place: Chasopys, Kyiv, Ukraine
comments: true

# DynamoDB in examples, Example 4.1: Search

```python
import datetime

from uuid import uuid4

from ddb_table import DDBTable, DDBUUIDField, DDBStrField


DDB_LOCAL_URL = 'http://localhost:8010'


class DDBTweet(DDBTable):

    TABLE_NAME = 'tweet'
    KEY_SCHEMA = [{
        'AttributeName': 'tweet_id',
        'KeyType': 'HASH',
    }]
    PROVISIONED_THROUGHPUT = {
        'ReadCapacityUnits': 1,
        'WriteCapacityUnits': 1
    }
    GLOBAL_SECONDARY_INDEXES = [{
        'IndexName': 'by_text',
        'KeySchema': [{
                'AttributeName': 'upper_first',
                'KeyType': 'HASH'
            }, {
                'AttributeName': 'upper_rest',
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
        'tweet_id': DDBUUIDField,
        'text': DDBStrField,
        'created': DDBStrField,
        'upper_first': DDBStrField,
        'upper_rest': DDBStrField,
    }

    def _get_endpoint_url(self):
        return DDB_LOCAL_URL

    def create(self, text):
        tweet_id = uuid4()
        created = str(datetime.datetime.utcnow())
        upper = text.upper()
        data = {
            'tweet_id': tweet_id,
            'text': text,
            'created': created,
            'upper_first': upper[:2],
            'upper_rest': upper[2:],
        }
        response = self._dynamodb(operation='PutItem').call(
            TableName=self._get_table_name(),
            Item=self.encode_item(data=data))
        return data

    def search(self, text, last=None, limit=10):
        if not text:
            return ([], None)
        upper = text.upper()
        ddb_query = self._dynamodb(operation='Query')
        kwargs = {
            'TableName': self._get_table_name(),
            'IndexName': 'by_text',
        }
        if len(text) > 1:
            kwargs.update({
                'KeyConditions': {
                    'upper_first': {
                        'AttributeValueList': [{
                            'S': upper[:2],
                        }],
                        'ComparisonOperator': 'EQ'
                    },
                    'upper_rest': {
                        'AttributeValueList': [{
                            'S': upper[2:],
                        }],
                        'ComparisonOperator': 'BEGINS_WITH'
                    }
                }
            })
        else:
            kwargs.update({
                'KeyConditions': {
                    'upper_first': {
                        'AttributeValueList': [{
                            'S': upper[:2],
                        }],
                        'ComparisonOperator': 'EQ'
                    },
                }
            })
        if last:
            kwargs['ExclusiveStartKey'] = last
        result = ddb_query.call(**kwargs)
        return (
            [self.decode_item(item) for item in result.get('Items')],
            result.get('LastEvaluatedKey'))


if __name__ == '__main__':
    ddb_tweet = DDBTweet()
    ddb_tweet.create_table()
    for text in ['text1', 'text2', 'text3', 'Text4', 'Another text']:
        ddb_tweet.create(text=text)
    print(ddb_tweet.search(text='t'))
    print(ddb_tweet.search(text='text4'))
    print(ddb_tweet.search(text='not found'))

    # ([{'upper_first': 'TE', 'upper_rest': 'XT1', 'tweet_id': '5aac3887-3da4-41c3-b158-4d9624248e46', 'text': 'text1', 'created': '2015-05-30 13:43:01.174688'}, {'upper_first': 'TE', 'upper_rest': 'XT2', 'tweet_id': '95b8330a-0d56-41b8-9389-a8ae4fd27d70', 'text': 'text2', 'created': '2015-05-30 13:43:01.265926'}, {'upper_first': 'TE', 'upper_rest': 'XT3', 'tweet_id': 'd079d36b-e902-4f0e-91de-03b285756d27', 'text': 'text3', 'created': '2015-05-30 13:43:01.290698'}, {'upper_first': 'TE', 'upper_rest': 'XT4', 'tweet_id': '67e6c96b-f828-42dc-89b9-770f309e920e', 'text': 'Text4', 'created': '2015-05-30 13:43:01.314380'}], None)
    # ([{'upper_first': 'TE', 'upper_rest': 'XT4', 'tweet_id': '67e6c96b-f828-42dc-89b9-770f309e920e', 'text': 'Text4', 'created': '2015-05-30 13:43:01.314380'}], None)
    # ([], None)
```

Here I want to turn your attention to two points:

- use additional text field with uppercase or lowercase content, it allows to search case insensitive
- hash key == first two letters in text, it allows to spread data and load between nodes in DynamoDB cluster

This example is pretty useless for implemetation search feature in real projects, use search engines like [Amazon CloudSearch](http://aws.amazon.com/cloudsearch/), [Elasticsearch](https://www.elastic.co/products/elasticsearch), [Apache Solr](http://lucene.apache.org/solr/) etc. instead.

But in some cases this functionality may be enough (suggest hash tags for example). And it is pretty fast and scalable.
