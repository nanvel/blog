labels: Draft
		Databases
created: 2017-05-10T12:38
modified: 2017-05-21T13:15
place: Phuket, Thailand
comments: true

# Databases

[TOC]

## How to choose a DB

1. Use MongoDB (joke)
2. PostgreSQL
3. It depends

See [PyCon Ukraine 2016, lighting talks](https://www.youtube.com/watch?v=mgPBtKaDQww).

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

## Databases

### Couchbase

Weak durability by writing to disk asynchronously.

### Redis

Weak durability by writing to disk asynchronously.

See also [Redis, usage examples](/2015/08/redis-rethink).

## Miscelenous

### Primary vs secondary indexes

Both are key: document/row pairs.
Primary index keys are unique, secondary index keys can be not unique.

### Durable RAM

Battery powered RAM.

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
