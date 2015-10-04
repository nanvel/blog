labels: Blog
        Databases
        DynamoDB
created: 2015-07-05T17:32

# DynamoDB in examples, Example 1.6: DynamoDB alternatives

List of databases allows to store data so huge that it doesn't fit on server.

I worked only with DynamoDB and Cassandra, information about all other databases was taken from the internet (don't verified).

## [DynamoDB](http://aws.amazon.com/documentation/dynamodb/)

License: Proprietary

Interface: HTTP/REST/JSON, console, web interface

Written in: Java

The biggest advantage of DynamoDB that it is easy to maintain for end user, in fact, You need only to configure table structure in DynamoDB web interface or using API and to set provisioned throughput. And instead of spin up more servers, You need only to increase provisioned throughput, it takes less then minute.

Features:

- Master-less replication
- Replication across data centers
- Schema-less: (except primary key fields)
- Pay for storage + provisioned throughput
- Secondary indexes (limited)
- Strong consistency (optional)
- AWS management console
- Amazon Elastic MapReduce, Lambda and other Amazon services integration

## [Cassandra](http://cassandra.apache.org/)

License: Apache

Interface: CQL (similar to SQL)

Written in: Java

Features:

- Tunable trade-offs for distribution and replication (consistency)
- Time to live
- Blazing fast writes
- Reliable cross-datacenter replication
- Counter datatype
- Secondary index
- Master-less replication (peer-to-peer architecture)
- Efficient compaction
- Static field as join replacement (efficient denormalization)
- Compound key implementation
- List, map, set, time UUID, custom object data types

## [MongoDB](https://www.mongodb.org/)

License: AGPL (Drivers: Apache)

Interface: Custom, binary (BSON)

Written in: C++

Features:

- Master/slave replication + built-in sharding
- Server-side javascript functions
- Integrated text search
- Geospatial indexing
- Allows to execute complex queries (uses map/reduce tasks on each node)

## [CouchDB](http://couchdb.apache.org/)

License: Apache

Interface: HTTP/REST

Written in: Erlang

Features:

- Master-master replication
- Embedded mapreduce

## [HBase](http://hbase.apache.org/)

License: Apache

Interface: HTTP/REST

Written in: Java

Features:

- Hadoop's HDFS as storage
- Mapreduce with Hadoop
- A cluster consists of several different types of nodes

## [Riak](http://docs.basho.com/riak/latest/)

License: Apache

Interface: HTTP/REST or custom binary

Written in: Erlang & C, some JavaScript 

Features:

- Tunable trade-offs for distribution and replication
- Pre- and post-commit hooks in JavaScript or Erlang, for validation and security
- Mapreduce in JavaScript or Erlang

Place: Kyiv, Ukraine
