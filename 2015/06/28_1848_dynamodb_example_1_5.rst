DynamoDB in examples, Example 1.5: Distributed system terms
===========================================================

`Table of contents <http://nanvel.com/p/dynamodb>`__

CAP theorem
-----------

`The CAP theorem <https://en.wikipedia.org/wiki/CAP_theorem>`__ (Eric A. Brewer's theorem).

CAP is an acronym of the three characteristics of distributed system:
    - Consistency: all the nodes in a cluster see the same data at any point of time
    - Availability: every request that is received by a non-failing node in the cluster must result in a response
    - Partition-tolerance: a node can still function when communication with other groups of nodes is lost

The theorem states that in a distributed system, only two out of the three characteristics can be attained at the most. For example:
    - BigTable: -Availability
    - DynamoDB, Cassandra: -Consistency

Distributed system without Partition-tolerance makes no sense. So we have two choices: CP, AP.

Compound (aka composite) key
----------------------------

If the primary key contains only one column, the row is a skinny row.
If the primary key contains more than one column, it is called a compound primary key and the row is wide row.

For example, if we need to filter by status and timestamp same time:

.. code-block:: text

    Table: activities
    Hash key: user_id
    Range key: status:created
    # get all account activities
    SELECT activity_id FROM activities where status = 'account' AND created > '2015-01-01';

Or if we need to store user relations:

.. code-block:: text

    Table: relations
    Hash key: user0_id:user1_id
    # get users relation
    SELECT relation FROM relations WHERE user0_id = '...' AND user1_id = '...';

Denormalization
---------------

`Denormalization <https://en.wikipedia.org/wiki/Denormalization>`__ is the process of attempting to optimize the read performance of a database by adding redundant data or by grouping data.

As joins in distributed databases usually cost much more then for single instance databases, it may be more efficient to duplicate data to avoid them.

Eventual consistency
--------------------

It is a weaker form of consistency than the typical Atomic-Consistency-Isolation-Durability (`ACID <https://en.wikipedia.org/wiki/ACID>`__) type consistency is found in the relational databases. It implies that there can be short intervals of inconsistency among the replicated nodes during which the data gets updated among these nodes. In other words, the replicas are updated asynchronously.

Global secondary index (DynamoDB)
---------------------------------

Every `global secondary index <http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GSI.html>`__ must have a hash key, and can have an optional range key.

Think about it as copy of the original table with different hash/range key.

This index has no limitation on size.

Hash
----

Small change in hash function argument leads to drastically change of hash function output. Length of hash function output is fixed and don't depends on input.

.. code-block:: python

    >>> import hashlib
    >>> m = hashlib.md5()
    >>> m = hashlib.md5('input1')
    >>> m.hexdigest()
    'da853c5826b798b82320e42024d97837'
    >>> m = hashlib.md5('input2')
    >>> m.hexdigest()
    '3eaa25d43fac6e39a12c3936942b72c8'

It applies to hash key data and result determines target database instance.

Hash key
--------

Or ``Partition key`` for Cassandra.

Data can't be sorted and retrieved for specified range. We can only get an item for specified key or iterate through all items.

Hash key have to be selected with intention to avoid hot spots.

Hot spots
---------

If the application tends to write or update a sequential block of rows at a time, the writes will not be distributed across the cluster.

Also happens if application tends to read or update a single item of data with high rate.

Idempotent
----------

Idempotent was originally a term in mathematics. But in computer science, idempotent is used more comprehensively to describe an operation that will produce the same result if executed once or multiple times.

For example: blind writes in Cassandra.

Index
-----

A `database index <https://en.wikipedia.org/wiki/Database_index>`__ is a data structure that improves the speed of data retrieval operations on a database table at the cost of additional writes and storage space to maintain the index data structure. Indexes are used to quickly locate data without having to search every row in a database table every time a database table is accessed.

Indexes in distributed databases is more complex comparetevely to classic relational databases.

Usually we have at least one index (primary key index, or Hash key/Partition primary key for distributed databases).

Additionally to primary key indexes, databases may have few additional indexes - secondary indexes. Behind the scenes, it is implemented as a separate hidden table which is maintained automatically by database internal process.

Indexes allows us to retrieve data faster, using less database resources. But writes become more heavy and databases size increases with every new index. Better to think twice on which indexes we really need.

DynamoDB has 2 types of secondary indexes: ``Global`` and ``Local``. `Limitation on indexes count <http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Limits.html>`__: 5 local and 5 global indexes maximum.

Secondary indexes may contains a copy of some or all of the attributes from the table. Which fields to include into secondary index is another great question developer have to ask himself when designing a new database structure.

Local secondary index (DynamoDB)
--------------------------------

A `local secondary index <http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/LSI.html>`__ maintains an alternate range key for a given hash key.

For a table with local secondary indexes, there is a `limit on item collection sizes <http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Limits.html>`__: for every distinct hash key value, the total sizes of all table and index items cannot exceed 10 GB.

May be useful to store sparse data.

Low cardinality
---------------

Low cardinality field (relational database terminology) has many rows that contain fewer unique values.

The secondary index is best on a low cardinality field (for Cassandra).

Range key
---------

Or ``Clustering key`` for Cassandra.

Can't be used without hash key specified. Keys are sorted for specified hash key.
Allows to get bunch of data for specific keys range. For example:

.. code-block:: text

    Table: activities
    Hash key: user_id
    Range key: created
    # returns all user activities created since 2015 year
    SELECT activity_id FROM activities WHERE user_id='123' AND created > '2015-01-01';

Sparse field
------------

Field that contains small amount of values different from null. For example: is_manager in accounts table.

Static column (Cassandra)
-------------------------

`Static column <http://docs.datastax.com/en/cql/3.1/cql/cql_reference/refStaticCol.html>`__ stores only a single instance of value per hash key, although table may has thousands of records belongs to one hash key. Allows to implement behavior similar to join in relational databases.

TTL
---

Time-To-Live in Cassandra (looks like DynamoDB hasn't this feature) is set on columns only. The unit is in seconds. When set on a column, it automatically counts down and will then be expired on the server side without any intervention of the client application.
Typical use cases are for the generation of security token and one-time token automatic purging of outdated columns, and so on.

Unnecessary network traffic between physical nodes
--------------------------------------------------

In a distributed databases we should minimize unnecessary network traffic as much as possible. In other words, the lesser the number of nodes the query needs to work with, the better the performance of the data model (select keys and indexes best match the database purposes, use effective queries).

UUID
----

Universal Unique ID.

Universal Unique ID is an Internet Engineering Task Force (IETF) standard. Request for Comments (RFC) standard, Request for Comments (RFC) 4122, with the intent of enabling distributed systems to uniquely identify information ithout significant central coordination. It is a 128-bit number represented by 32 lowercase hexadecimal digits, displayed in five groups separated by hyphens, for example: 76fcf499-9685-44e3-80fb-965123967b35.

There are `different methods <https://docs.python.org/2/library/uuid.html>`__ to generate UUID, for example:

.. code-block::

    >>> import uuid
    # Generate a UUID from a host ID, sequence number, and the current time.
    >>> uuid.uuid4()
    UUID('e646341c-b4df-4ef3-a26b-3f4ff93ecd32')
    # Generate a random UUID from host ID and random value.
    >>> uuid.uuid1()
    UUID('738edea6-1dae-11e5-9188-283737190a60')

UUID is a replacement for autoincremental field for distributed databases.

.. info::
    :tags: DynamoDB, Distributed system, Databases, Cassandra
    :place: Kyiv, Ukraine
