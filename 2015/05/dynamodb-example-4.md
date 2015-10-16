labels: Blog
        Databases
        DynamoDB
created: 2015-05-17T16:40
place: Rim Ping, Lamphun, Thailand

# DynamoDB in examples, Example 4: Tweets. Throttled reads and caching

Usually, more recent tweets (or frequently retweeted) are more popular than other. So, we may have high reads level on few tweets and comparatively small reads rate on other. This may cause problem known as throttled reads - read latency will increase for item if we will do too much read request simultaneously (DynamoDB handle a lot of simultaneous read requests great if items we trying to read has different hash keys). Obvious resolution of this problem is to use caching, if we will cache the most popular tweets, we will walk around throttled reads problem and significantly decrease provisioned throughput.

```python
import datetime
import json

from uuid import uuid4

import redis

from ddb_table import DDBTable, DDBUUIDField, DDBStrField


DDB_LOCAL_URL = 'http://localhost:8010'


class DDBTweet(DDBTable):

    _redis = redis.StrictRedis()

    REDIS_TWEET_KEY = 'tweet:{tweet_id}'
    REDIS_TWEET_TIMEOUT = 60 * 60  # 1 hr

    TABLE_NAME = 'tweet'
    KEY_SCHEMA = [{
        'AttributeName': 'tweet_id',
        'KeyType': 'HASH',
    }]
    PROVISIONED_THROUGHPUT = {
        'ReadCapacityUnits': 1,
        'WriteCapacityUnits': 1
    }
    FIELDS = {
        'tweet_id': DDBUUIDField,
        'text': DDBStrField,
        'created': DDBStrField,
    }

    def _get_endpoint_url(self):
        return DDB_LOCAL_URL

    def create(self, text):
        tweet_id = uuid4()
        created = str(datetime.datetime.utcnow())
        data = {
            'tweet_id': tweet_id,
            'text': text,
            'created': created,
        }
        response = self._dynamodb(operation='PutItem').call(
            TableName=self._get_table_name(),
            Item=self.encode_item(data=data))
        return data

    def get(self, tweet_id):
        key = self.REDIS_TWEET_KEY.format(tweet_id=tweet_id)
        tweet = self._redis.get(name=key)
        if tweet is None:
            ddb_get_item = self._dynamodb(operation='GetItem')
            kwargs = {
                'TableName': self._get_table_name(),
                'Key': {
                    'tweet_id': {
                        'S': str(tweet_id),
                    },
                },
            }
            result = ddb_get_item.call(**kwargs)
            tweet = result['Item']
            self._redis.setex(
                name=key, time=self.REDIS_TWEET_TIMEOUT,
                value=json.dumps(tweet))
        else:
            tweet = json.loads(tweet.decode('utf-8'))
        return tweet


if __name__ == '__main__':
    ddb_tweet = DDBTweet()
    ddb_tweet.create_table()
    tweet = ddb_tweet.create(text='Example tweet.')
    print(ddb_tweet.get(tweet_id=tweet['tweet_id']))
    print(ddb_tweet.get(tweet_id=tweet['tweet_id']))
    # {'tweet_id': {'S': 'aead2db2-0216-43e5-9769-bd7153217e61'}, 'created': {'S': '2015-05-17 14:17:10.531644'}, 'text': {'S': 'Example tweet.'}}
    # {'tweet_id': {'S': 'aead2db2-0216-43e5-9769-bd7153217e61'}, 'text': {'S': 'Example tweet.'}, 'created': {'S': '2015-05-17 14:17:10.531644'}}
```
