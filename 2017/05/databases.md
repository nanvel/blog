labels: Draft
        Databases
created: 2017-05-10T12:38
modified: 2018-03-01T15:20
place: Phuket, Thailand
comments: true

# Databases

[TOC]

## How to choose a DB

If short:

1. Use MongoDB (joke)
2. PostgreSQL
3. It depends

See [PyCon Ukraine 2016, lighting talks](https://www.youtube.com/watch?v=mgPBtKaDQww).

There is no quick and easy rule for determining which type of storage engine is better for the use case, it worth testing empirically.

## DB types

- [relational databases](/2016/02/sql)
- object-oriented databases
- key/value stores
- column-oriented databases
- document-oriented databases
- hierarchical databases
    a tree, each node has one parent.
- network databases (CODASYL model)
    like hierarchical, but a record can have multiple perents.
    The only way of accessing a record is from a root record along chains of links (access path).
- map/reduce frameworks
- semantic data stores
- graph databases

By storage:

- in memory
- disk

## Relational model

Proposed by Edgar Codd in 1970. Active usage - since mid-1980s (SQL, RDBMSs). The dominance of relational databases has lasted around 25-30 years.

Data is organized into relations (called tables in SQL), where each relation is an unordered collection of tuples (rows in SQL).

## Column oriented storage

Don't store all the values from one row together, but store all the values from each column together.

The column-oriented storage layour relies on each column file containing the rows in the same order. If you need to reassemble an entire row, you can take the N-th entry from each of the individual column files and put them together to form the N-th row of the table.

## Network model and hierarchical model

1970s-1980s.

## Object oriented model

Appeared in 1980s, 1990s.

## Document oriented model

Back to hierarchical model: storing nested records (one-to-many relations).
Schema flexibility, better performance due to locality (data is not splitted across multiple tables).
For highly interconnected data, the document model is awkward.

Target use cases where data comes in self-contained documents and relationships between one document and another are rare.

## XML model

2000s.

## Relational model

## Graph model

For highly interconnected data is the most natural model, target use cases where anything is potentially related to everything.

A graph consists of two kinds of objects: vertices (entities) and edges (relationships of arcs).

Languages: Cypher, SPARQL (a query language for triple-stores), Datalog, Gremlin.

## Databases

### Couchbase

Weak durability by writing to disk asynchronously.

### Redis

Weak durability by writing to disk asynchronously.

See also [Redis, usage examples](/2015/08/redis-rethink).

### AWS RedShift

Hosted version of ParAccel.

## Miscelenous

### Primary vs secondary indexes

Both are key: document/row pairs.
Primary index keys are unique, secondary index keys can be not unique.

### Durable RAM

Battery powered RAM.

### SQL-on-Hadoop projects

Apache Hive, Spark SQL, Cloudera Impala, Facebook Presto, Apache Tajo, Apache Drill.

### Parquet

A columnar storage format that supports a document data model, based on Google's Dremel.

## Vocabulary

### SQL injection

An SQL injection:

- Hi, this is you sons school, we're having some computer trouble.
- Oh, dear - did he break something? In a way -)
- Do you really name your son "Robert'); DROP TABLE Students;"?
- Oh, yes. Little Bobby tables we call him.
- Well, we've lost this year's student records. I hope yo're happy.
- And I hope you've learned to sanitize your database inputs.

### Columnal database

> The Tables Have Turned.
>
> Vertica slogan

### Levenshtein automaton

pass

### Data warehouse

A separate database for analytics purposes. A trend from late 1980s and early 1990s.
The process of getting data in the warehouse is known as Extract-Transform-Load (ETL).

### Star schema

Aka dimensional modeling.
Star - event and connections to dimension tables like the rays of a star.
There is a fact table represents events and dimension tables represent who, when (allows to represent additional information, like publick holidays), where, what, how and why.

### Replication and Partitioning

**Replication** - keeping a copy of the same data on several different nodes:

- latency (keep data geographically close to users)
- availability
- scalability (read throughput)

Variations:

- single-leader
- multi-leader
- leaderless

**Partitioning** (aka sharding) - Splitting a big database into smaller subsets called partitions so that different partitions can be assigned to different nodes. Distribute large dataset across many disks, distribute query load across many processors.

Partition aka:

- **Shard** in: MongoDB, Elasticsearch, SolrCloud.
- **Region** in: HBase.
- **Tablet** in: Bigtable.
- **Vnode** in: Cassandra and Riak.
- **vBucket** in Couchbase.

Keys distribution:

- by keys range
- by key hash range (hash function makes data uniformly distributed, Cassandra and MongoDB use MD5)

### Service discovery in distributed databases

Knowledge about partitions may be stored in:

- each node
- a routing tier
- in a client

Many use ZooKeeper (LinkedIn's Expresso/Helix, HBase, SolrCloud, Kafka). 

Kassandra and Reak use gossip protocol (there is no external coordination service).

### NoSQL

A catchy Twitter tag, retroactively reinterpreted as Not Only SQL.

### Query optimizer

In a relational database, the query optimizer automatically decides which parts of the query to execute in which order, and which indexes to use.

### Schemaless

`schema-on-read` - the structure of the data is implicit, and only interpreted when the data is read.
`schema-on-write` - the schema is explicit and the database ensures all written data conforms to it.

## Databases index

HBase (opensource BigTable)
Ketama

## Links

[Designing Data-Intensive Applications](https://www.amazon.com/Designing-Data-Intensive-Applications-Reliable-Maintainable/dp/1449373321) by Martin Kleppmann
