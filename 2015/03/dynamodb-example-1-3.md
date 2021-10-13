labels: DynamoDB
        Testing
        Databases
created: 2015-03-08T13:30
place: Phuket, Thailand
comments: true

# DynamoDB in examples, Example 1.3: DynamoDB local and testing

May be useful for:

- development without steady internet connection
- testing
- reduce ddb usage costs

See [DynamoDB local documentation](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Tools.DynamoDBLocal.html).

I use Makefile to run DynamoDB locally:
```makefile
dynamodb:
	java -Djava.library.path=./bin/DynamoDBLocal_lib -jar ./bin/DynamoDBLocal.jar -port 8010 -inMemory # -dbPath ./bin/db.bin
```

And usually I run it with ```inMemory``` key, that allows to have a clean database after restart.

You can download DynamoDB local binaries from [DynamoDB local documentation page](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Tools.DynamoDBLocal.html).
I place binaries in ./bin folder of the project:
```
- project
    - bin
        - DynamoDBLocal.jar
        - DynamoDBLocal_lib
    - Makefile
```

To use DynamoDB local instead of amazon service, we need to set endpoint url to our DynamoDB local server url:
```
http://localhost:8010
```

Let's write a functional test for our previous example to see how it works:
```python
import unittest
import uuid

from example_1 import DDBUserWallet
from unittest import mock


DDB_LOCAL_URL = 'http://localhost:8010'


class DDBUserWalletTestCase(unittest.TestCase):

    @mock.patch('example_1.DDBUserWallet._get_endpoint_url')
    def test_update_and_get(self, _get_endpoint_url_mock):
        _get_endpoint_url_mock.return_value = DDB_LOCAL_URL
        user_wallet = DDBUserWallet()
        user_wallet.create_table()
        user_id = uuid.uuid4()
        for balance in [100, 123]:
            user_wallet.update(user_id=user_id, balance=balance)
            self.assertEqual(user_wallet.get(user_id=user_id)['balance'], balance)


if __name__ == '__main__':
    unittest.main()
    # (.env)nanvel-air:example_1_3 nanvel$ python example_1_3.py
    # .
    # ----------------------------------------------------------------------
    # Ran 1 test in 0.323s
    #
    # OK
```

You also may use decorator like this instead ```@mock.patch```:
```python
import functools

from mock import patch


DDB_LOCAL_URL = 'http://localhost:8010'


def with_ddb_local(method):

    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        return patch(
            'example_1.DDBUserWallet._get_endpoint_url',
            new=lambda x: DDB_LOCAL_URL)(
                method)(self, *args, **kwargs)
    return wrapper
```
