labels: Databases
        DynamoDB
created: 2015-06-06T22:09
place: Dream Story, Kyiv, Ukraine
comments: true

# DynamoDB in examples, Example 1.4: DynamoDB and Celery using green threads

Usually we set concurrency [equal to number of processors](http://celery.readthedocs.org/en/latest/configuration.html#concurrency-settings).
But if we using eventlet, we able to set much bigger value, like ~ 1000.
To enable [eventlet pool](http://celery.readthedocs.org/en/latest/userguide/concurrency/eventlet.html) use ```-P``` option to celery worker.

```bash
$ pip install celery
$ pip install eventlet
```

```python
# main.py

import datetime
import logging
import random
import uuid

import botocore.session

from celery import Celery
from celery.task import Task
from celery.registry import tasks


logger = logging.getLogger(__name__)


class Config:

    pass


app = Celery()
app.config_from_object(Config)


class UpdateBalance(Task):

    name = 'update_balance'

    def __init__(self, *args, **kwargs):
        super(UpdateBalance, self).__init__(*args, **kwargs)
        self.amazon_session = botocore.session.get_session()

    def run(self, user_id):
        client = self.amazon_session.create_client('dynamodb', region_name='us-west-2')
        balance = random.randint(1, 1000)  # some hard task calculates user balance
        result = client.put_item(
            TableName='user_wallet',
            Item={
                'user_id': {
                    'S': str(user_id),
                },
                'balance': {
                    'N': str(balance),
                }
            })
        logger.warning(datetime.datetime.now())
        logger.warning(result)


tasks.register(UpdateBalance)


if __name__ == '__main__':
    for i in range(10):
        user_id = str(uuid.uuid4())
        UpdateBalance.delay(user_id=user_id)
```

Results using eventlet:
```bash
$ celery worker -A main -P eventlet -c 1000
$ python main.py

```text
 -------------- celery@nanvel-air.local v3.1.18 (Cipater)
---- **** -----
--- * ***  * -- Darwin-14.3.0-x86_64-i386-64bit
-- * - **** ---
- ** ---------- [config]
- ** ---------- .> app:         __main__:0x1023c92d0
- ** ---------- .> transport:   amqp://guest:**@localhost:5672//
- ** ---------- .> results:     disabled
- *** --- * --- .> concurrency: 1000 (eventlet)
-- ******* ----
--- ***** ----- [queues]
 -------------- .> celery           exchange=celery(direct) key=celery

[2015-06-06 21:57:23,698: WARNING/MainProcess] celery@nanvel-air.local ready.
[2015-06-06 21:57:26,511: WARNING/MainProcess] 2015-06-06 21:57:26.511696
[2015-06-06 21:57:26,512: WARNING/MainProcess] {'ResponseMetadata': {'HTTPStatusCode': 200, 'RequestId': '1BNOL3VSM33D1EUIP7QRP2QTUNVV4KQNSO5AEMVJF66Q9ASUAAJG'}}
[2015-06-06 21:57:26,515: WARNING/MainProcess] 2015-06-06 21:57:26.515920
[2015-06-06 21:57:26,516: WARNING/MainProcess] {'ResponseMetadata': {'HTTPStatusCode': 200, 'RequestId': 'HGVHJ9CRS5U3EJ4KG57C44N53BVV4KQNSO5AEMVJF66Q9ASUAAJG'}}
[2015-06-06 21:57:26,541: WARNING/MainProcess] 2015-06-06 21:57:26.541750
[2015-06-06 21:57:26,542: WARNING/MainProcess] {'ResponseMetadata': {'HTTPStatusCode': 200, 'RequestId': 'RD0J3H6EL29B6CKUKLJ9AQT4HNVV4KQNSO5AEMVJF66Q9ASUAAJG'}}
[2015-06-06 21:57:26,550: WARNING/MainProcess] 2015-06-06 21:57:26.550805
[2015-06-06 21:57:26,551: WARNING/MainProcess] {'ResponseMetadata': {'HTTPStatusCode': 200, 'RequestId': 'SP9M3F114NIEOAUQVQ0UU74JVRVV4KQNSO5AEMVJF66Q9ASUAAJG'}}
[2015-06-06 21:57:26,590: WARNING/MainProcess] 2015-06-06 21:57:26.589971
[2015-06-06 21:57:26,590: WARNING/MainProcess] {'ResponseMetadata': {'HTTPStatusCode': 200, 'RequestId': 'HTB2TU11O98IA1RA5IANC1T8GBVV4KQNSO5AEMVJF66Q9ASUAAJG'}}
[2015-06-06 21:57:26,637: WARNING/MainProcess] 2015-06-06 21:57:26.637958
[2015-06-06 21:57:26,638: WARNING/MainProcess] {'ResponseMetadata': {'HTTPStatusCode': 200, 'RequestId': 'A9B7SON7IO7TBVA8CHCG1HMOSJVV4KQNSO5AEMVJF66Q9ASUAAJG'}}
[2015-06-06 21:57:26,719: WARNING/MainProcess] 2015-06-06 21:57:26.719082
[2015-06-06 21:57:26,719: WARNING/MainProcess] {'ResponseMetadata': {'HTTPStatusCode': 200, 'RequestId': 'HPKGKLUV80OR1I1I679457NV63VV4KQNSO5AEMVJF66Q9ASUAAJG'}}
[2015-06-06 21:57:26,729: WARNING/MainProcess] 2015-06-06 21:57:26.729478
[2015-06-06 21:57:26,729: WARNING/MainProcess] {'ResponseMetadata': {'HTTPStatusCode': 200, 'RequestId': 'AAIKV3SKH2QQJ1UDG0CBHCKKHNVV4KQNSO5AEMVJF66Q9ASUAAJG'}}
[2015-06-06 21:57:26,739: WARNING/MainProcess] 2015-06-06 21:57:26.739881
[2015-06-06 21:57:26,740: WARNING/MainProcess] {'ResponseMetadata': {'HTTPStatusCode': 200, 'RequestId': 'QU4E7KQMC656O1MNB3C7F6A8MFVV4KQNSO5AEMVJF66Q9ASUAAJG'}}
[2015-06-06 21:57:26,766: WARNING/MainProcess] 2015-06-06 21:57:26.766148
[2015-06-06 21:57:26,766: WARNING/MainProcess] {'ResponseMetadata': {'HTTPStatusCode': 200, 'RequestId': 'LLB6K6385US0V5BRBI8SBVTKBRVV4KQNSO5AEMVJF66Q9ASUAAJG'}}
```

Results using prefork:
```bash
$ celery worker -A main -c 2
$ python main.py
```

```text
 -------------- celery@nanvel-air.local v3.1.18 (Cipater)
---- **** -----
--- * ***  * -- Darwin-14.3.0-x86_64-i386-64bit
-- * - **** ---
- ** ---------- [config]
- ** ---------- .> app:         __main__:0x107883850
- ** ---------- .> transport:   amqp://guest:**@localhost:5672//
- ** ---------- .> results:     disabled
- *** --- * --- .> concurrency: 2 (prefork)
-- ******* ----
--- ***** ----- [queues]
 -------------- .> celery           exchange=celery(direct) key=celery

[2015-06-06 21:57:49,982: WARNING/MainProcess] celery@nanvel-air.local ready.
[2015-06-06 21:57:55,286: WARNING/Worker-2] 2015-06-06 21:57:55.286161
[2015-06-06 21:57:55,286: WARNING/Worker-2] {'ResponseMetadata': {'HTTPStatusCode': 200, 'RequestId': 'S217PD538RR7TL4VUDPGUJLAR7VV4KQNSO5AEMVJF66Q9ASUAAJG'}}
[2015-06-06 21:57:55,308: WARNING/Worker-1] 2015-06-06 21:57:55.308731
[2015-06-06 21:57:55,309: WARNING/Worker-1] {'ResponseMetadata': {'HTTPStatusCode': 200, 'RequestId': '5966EVKRRTJI1GJOCR262H1ISFVV4KQNSO5AEMVJF66Q9ASUAAJG'}}
[2015-06-06 21:57:56,483: WARNING/Worker-2] 2015-06-06 21:57:56.483080
[2015-06-06 21:57:56,483: WARNING/Worker-2] {'ResponseMetadata': {'HTTPStatusCode': 200, 'RequestId': 'PQT4RTVJ4QHH39Q2I6IPGSAIAJVV4KQNSO5AEMVJF66Q9ASUAAJG'}}
[2015-06-06 21:57:56,485: WARNING/Worker-1] 2015-06-06 21:57:56.485244
[2015-06-06 21:57:56,485: WARNING/Worker-1] {'ResponseMetadata': {'HTTPStatusCode': 200, 'RequestId': 'JEK3R8F4EN93OTKVJCA6CEEHOVVV4KQNSO5AEMVJF66Q9ASUAAJG'}}
[2015-06-06 21:57:57,646: WARNING/Worker-1] 2015-06-06 21:57:57.646181
[2015-06-06 21:57:57,646: WARNING/Worker-2] 2015-06-06 21:57:57.646156
[2015-06-06 21:57:57,646: WARNING/Worker-1] {'ResponseMetadata': {'HTTPStatusCode': 200, 'RequestId': 'J0PKP3F8PI30D4657SEJHVF49NVV4KQNSO5AEMVJF66Q9ASUAAJG'}}
[2015-06-06 21:57:57,646: WARNING/Worker-2] {'ResponseMetadata': {'HTTPStatusCode': 200, 'RequestId': 'HM07DDU8OJSSC877FEAONPR9D7VV4KQNSO5AEMVJF66Q9ASUAAJG'}}
[2015-06-06 21:57:58,808: WARNING/Worker-2] 2015-06-06 21:57:58.808078
[2015-06-06 21:57:58,808: WARNING/Worker-1] 2015-06-06 21:57:58.808186
[2015-06-06 21:57:58,808: WARNING/Worker-2] {'ResponseMetadata': {'HTTPStatusCode': 200, 'RequestId': 'K6NI9JGQBQ3TEUHPMJHFN9R2BFVV4KQNSO5AEMVJF66Q9ASUAAJG'}}
[2015-06-06 21:57:58,808: WARNING/Worker-1] {'ResponseMetadata': {'HTTPStatusCode': 200, 'RequestId': '4O86RDPPQ5II43FA02LRM3F9MVVV4KQNSO5AEMVJF66Q9ASUAAJG'}}
[2015-06-06 21:58:00,039: WARNING/Worker-1] 2015-06-06 21:58:00.038970
[2015-06-06 21:58:00,039: WARNING/Worker-2] 2015-06-06 21:58:00.039041
[2015-06-06 21:58:00,039: WARNING/Worker-1] {'ResponseMetadata': {'HTTPStatusCode': 200, 'RequestId': 'OP19GVG098LQQ9D415FDIR15VNVV4KQNSO5AEMVJF66Q9ASUAAJG'}}
[2015-06-06 21:58:00,039: WARNING/Worker-2] {'ResponseMetadata': {'HTTPStatusCode': 200, 'RequestId': 'APD8V79PV0TGKD6TTKUJNFPVJVVV4KQNSO5AEMVJF66Q9ASUAAJG'}}
```
