labels: Databases
        Draft
created: 2017-01-03T15:39
modified: 2017-01-03T15:39
place: Phuket, Thailand
comments: true

# MongoDB

## Connection

```python
client = MongoClient("mongodb://mongodb0.example.net:27017")

db = client.my_db
# or client['my_db']

collection = db.my_collection
# or db['my_collection']
```

## Create documents

```
fb.my_collection.insert_one({
	'field': 'value'
})
```

## Vocabulary

### Collection

Collections are analogous to tables (but does not require its documents to have the same schema).

### Database

Databases hold groups of logically related collections.
MongoDB creates new databases implicitly upon their first use.

### Document id

Documents stored in a collection must have a unique `_id` field that acts as a primary key.

!!! note "PyMongo"
	If the document passed to the `insert_one()` method does not contain the _id field, MongoClient automatically adds the field to the document and sets the field’s value to a generated ObjectId.
