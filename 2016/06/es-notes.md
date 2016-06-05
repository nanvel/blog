labels: Draft
        SearchEngines
        Elasticsearch
created: 2016-06-04T10:33
place: Kyiv, Ukraine
comments: true

# Elasticsearch notes

Loc: 2027

[TOC]

Elasticsearch is a real-time distributed search and analytics engine built on top of Apache Lucene.

- Available under the Apache 2 license
- Created by Shay Banon (the first public release came out in February 2010)
- Provides simple, coherent, RESTful API
- A distributed document store / search engine
- Horizontal scalability, high reliability
- Uses by Wikipedia, The Guardian, Stack Overflow, GitHub, and many other

## Installation

```bash
brew install elasticsearh
curl http://localhost:9200/?pretty
```

## Configuration

Change cluster.name (elasticsearch.yml) to stop your nodes from trying to join another cluster on the same network with the same name.

## API

Default port: 9200.

### Examples

```js
const axios = require('axios')
const co = require('co')


const request = ({uri, method, body=null}) => {
  console.log(`> ${method} ${uri}`)
  if (body) {
    console.log(JSON.stringify(body, null, 2))
  }
  return axios.request({
    method: method,
    url: `http://localhost:9200${uri}`,
    data: body
  }).then(response => ({
    body: JSON.stringify(response.data, null, 2),
    headers: JSON.stringify(response.headers, null, 2),
    status: response.status
  }))
}

co(function *() {
  let response = yield request({
    uri: '/',
    method: 'GET'
  })
  console.log(response.body)
  // console.log(response.headers)
  // console.log(response.status)
}).catch(error => console.log(error))
```

### Status

```text
GET /
```

```json
{
  "name": "Angel Salvadore",
  "cluster_name": "elasticsearch_nanvel",
  "version": {
    "number": "2.3.2",
    "build_hash": "b9e4a6acad4008027e4038f6abed7f7dba346f94",
    "build_timestamp": "2016-04-21T16:03:47Z",
    "build_snapshot": false,
    "lucene_version": "5.5.0"
  },
  "tagline": "You Know, for Search"
}
```

Response headers and status code:
```text
{
  "content-type": "application/json; charset=UTF-8",
  "content-length": "331"
}
200
```

### Index a document

```text
PUT /myindex/mytype/1
{
  "attr1": "val1",
  "attr2": 42
}
```

```json
{
  "_index": "myindex",
  "_type": "mytype",
  "_id": "1",
  "_version": 1,
  "_shards": {
    "total": 2,
    "successful": 1,
    "failed": 0
  },
  "created": true
}
```

Elasticsearch creates an index and type automatically if they don't exist.

### Get a document

```text
GET /myindex/mytype/1
```

```json
{
  "_index": "myindex",
  "_type": "mytype",
  "_id": "1",
  "_version": 1,
  "found": true,
  "_source": {
    "attr1": "val1",
    "attr2": 42
  }
}
```

### Delete a document

```text
DELETE /myindex/mytype/1
```

```json
{
  "found": true,
  "_index": "myindex",
  "_type": "mytype",
  "_id": "1",
  "_version": 2,
  "_shards": {
    "total": 2,
    "successful": 1,
    "failed": 0
  }
}
```

### Checking whether a document exists

```text
HEAD /myindex/mytype/1
```

Response status code == 200 if the document was found or 404 otherwise.

### Search lite

[Search Lite](https://www.elastic.co/guide/en/elasticsearch/guide/current/search-lite.html) expects all search parameters to be passed in the query string.

```text
GET /myindex/mytype/_search?q=attr2:42
```

```json
{
  "took": 42,
  "timed_out": false,
  "_shards": {
    "total": 5,
    "successful": 5,
    "failed": 0
  },
  "hits": {
    "total": 1,
    "max_score": 0.30685282,
    "hits": [
      {
        "_index": "myindex",
        "_type": "mytype",
        "_id": "1",
        "_score": 0.30685282,
        "_source": {
          "attr1": "val1",
          "attr2": 42
        }
      }
    ]
  }
}
```

### Search with Query DSL

Query DSL - the flexible, powerful query language used by Elasticsearch.
Expects all search parameters to be passed in the body json.

```text
GET /myindex/mytype/_search
{
  "query": {
    "match": {
      "attr2": 42
    }
  }
}
```

```json
{
  "took": 6,
  "timed_out": false,
  "_shards": {
    "total": 5,
    "successful": 5,
    "failed": 0
  },
  "hits": {
    "total": 1,
    "max_score": 0.30685282,
    "hits": [
      {
        "_index": "myindex",
        "_type": "mytype",
        "_id": "1",
        "_score": 0.30685282,
        "_source": {
          "attr1": "val1",
          "attr2": 42
        }
      }
    ]
  }
}
```

### Index settings

```text
PUT /myindex2
{
  "settings": {
    "number_of_shards": 3,
    "number_of_replicals": 1
  }
}

```json
{
  "acknowledged": true
}
```

### Cluster

```text
GET /_cluster/health
```

```json
{
  "cluster_name": "elasticsearch_nanvel",
  "status": "yellow",
  "timed_out": false,
  "number_of_nodes": 1,
  "number_of_data_nodes": 1,
  "active_primary_shards": 5,
  "active_shards": 5,
  "relocating_shards": 0,
  "initializing_shards": 0,
  "unassigned_shards": 5,
  "delayed_unassigned_shards": 0,
  "number_of_pending_tasks": 0,
  "number_of_in_flight_fetch": 0,
  "task_max_waiting_in_queue_millis": 0,
  "active_shards_percent_as_number": 50
}
```

Status names:

- green: all primary and replica shards are active
- yellow: all primary shards are active, but not all replica shards are active
- red: not all primary shards are active

### Marvel

```text
/_plugin/marvel/
/_plugin/marvel/sense/
```

## Queries

### The empty search

Returns all documents.

```text
GET /_search

All types in the index/indexes:
GET /myindex/_search
GET /myindex,anotherindex/_search
GET /my*,another*/_search

Search type in the index:
GET /myindex/mytype/_search

Search type inside all indexes:
GET /_all/mytype/_search
```

```json
{
  "took": 14,
  "timed_out": false,
  "_shards": {
    "total": 13,
    "successful": 13,
    "failed": 0
  },
  "hits": {
    "total": 4,
    "max_score": 1,
    "hits": [
      ...
    ]
  }
}
```

### Exact match

```json
{
  "query": {
    "match": {
      "attr2": 42
    }
  }
}
```

### Full text search

```text
GET /myindex/mytype/_search
{
  "query": {
    "match": {
      "attr1": "ipsum"
    }
  }
}
```

```json
{
  "took": 6,
  "timed_out": false,
  "_shards": {
    "total": 5,
    "successful": 5,
    "failed": 0
  },
  "hits": {
    "total": 1,
    "max_score": 0.19178301,
    "hits": [
      {
        "_index": "myindex",
        "_type": "mytype",
        "_id": "_search",
        "_score": 0.19178301,
        "_source": {
          "attr1": "lorem ipsum ...",
          "attr2": 1
        }
      }
    ]
  }
}
```

### Phrase Search

```json
{
  "query": {
    "match_phrase": {
      "attr1": "lorem ipsum"
    }
  }
}
```

Doesn't return "lorem something ipsum", but returns "lorem ipsum something".

### Ordering

By default, Elasticsearch orders matching results by their relevance score.

### Pagination

Use size and from keywords.
The size indicates the number of results that should be returned, default to 10.
The from indicates the number of initial results that should be skipped, default to 0.

Deep pagination is inefficient in Elasticsearch. Keep (from + size) under 1000.

## Vocabulary

### A node

Is a running instance of Elasticsearch.

### A cluster

Is a group of nodes with the same cluster.name.

One node in the cluster is elected to be the master node, which is in charge of managing cluster-wide changes (does not need to be involved in document-level changes or search).

### A shard

A nodes container, holds a slice of all the data in the index.

#### Primary vs replica shards

The number of primary shards in an index is fixed at the time that an index is created.
The number of replica shards can be changed at any time.

A replica shard is just a copy of a primary shard. Used to provide redundant copies of your data to protect against hardware failure, and to serve more read requests.

By default, indexes are assigned five primary shards.

Any newly indexed document will first be stored on a primary shard, and then copied in parallel to the associated replica shard(s).

### Indexing

The act of storing data in Elasticsearch.

### Document and type

In Elasticsearch, a document belongs to a type, and those types live inside an index.

Parallels to a traditional relational database:

- Databases -> Indexes
- Tables -> Types
- Rows -> Documents
- Columns -> Fields

Every type has its own mapping or schema definition.
Every field in a document is indexed and can be queried.

### An index

A logical namespace that points to one or more physical shards.

### Document id

The id is a string that, when combined with the _index and _type, uniquely identified a document in Elasticsearch.

### Inverted index

An inverted index consists of a list of all the unique words that appear in any document, and for each word, a list of the documents in which it appears.

### A full-text search

Finds all documents matching the search keywords, and returns them ordered by relevance.

### Relevance score

How well the document matches the query.

### Mapping

How the data in each field is interpreted.

### Analysis

How full text is processed to make it searchable.

## Other features

### Highlight

Highlights fragments from the original text.

[Highlighting](https://www.elastic.co/guide/en/elasticsearch/reference/current/search-request-highlighting.html)

### Aggregations

Allows to generate sophisticated analytics over your data.

[Aggregations](https://www.elastic.co/guide/en/elasticsearch/reference/current/search-aggregations.html)

## Instruments

[Kibana](https://www.elastic.co/guide/en/marvel/current/introduction.html)

Clients:
[Elasticsearch Python client](https://elasticsearch-py.readthedocs.io/en/master/)
[Elasticsearch Node.js client](https://www.npmjs.com/package/elasticsearch)

## Links

[Elasticsearch: The Definitive Guide by Clinton Gormley and Zachary Tong](https://www.elastic.co/guide/en/elasticsearch/guide/current/index.html)
