labels: Blog
        Databases
        DynamoDB
created: 2015-05-10T23:08
place: Chiang Mai, Thailand
comments: true

# DynamoDB in examples, Example 3.3: Mark item as deleted

Sometimes we need to delete an item but don't wanna remove it permanently. For example - comments. If comment contains an inappropriate content, we need to remove it, but we may still have references to this comment. Or user may change his mind and will want to restore removed comment.

I have few ideas how to handle item remove:

- remove permanently and remove all references (we may run into problem if we will have a lot of references)
- copy content to another table -> update references -> remove content from the table
- copy comment content with meta to another storage and remove all references and comment
- mark comment as removed

The last variant looks best for me for comments.

The way it has to work here is similar to Example 3.2. We can't just add field ```is_removed``` or similar. We need RANGE key starts from is_deleted marker, so we will be able to use Query request to get all items except deleted. Even better idea is to use status marker instead, so we will be able to mark comment as ```live```, ```deleted_by_author``` or ```deleted_due_to_inappropriate```.

Index example:

```python
GLOBAL_SECONDARY_INDEXES = [{
    'IndexName': 'for_item_id',
    'KeySchema': [{
            'AttributeName': 'item_id',
            'KeyType': 'HASH'
        }, {
            'AttributeName': 'deleted_created',
            'KeyType': 'RANGE'
        }
    ],
}]
# 'deleted_created' -> '{deleted}_{created}'.format(deleted=1 if deleted else 0, created=created)
```
