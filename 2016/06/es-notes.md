labels: Draft
        SearchEngines
        Elasticsearch
created: 2016-06-04T10:33
modified: 2016-06-28T13:12
place: Kyiv, Ukraine
comments: true

# Elasticsearch notes

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

### Elasticsearch status

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

### Cluster health

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

### Check whether a document exists

```text
HEAD /myindex/mytype/1
```

Response status code == 200 if the document was found or 404 otherwise.

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

There are two DSLs:

- query DSL (asks: how well does this document match?)
- filter DSL (yes or no for document, uses only with exact values, do not calculate relevance)

Filter examples:

- the date is in range ...
- does it contain the field
- is the coordinates field within 10km of a specified point?

Query examples:

- full text search, best matching results
- documents containing specified tags - the more tags, the more relevant the document

Filters are more efficient in the most cases, they are easy to calculate and cache.

!!! note "The goal of filters"
    The goal of filters is to reduce the number of documents that have to be examined by the query.

As a general rule, use query clauses for full-text search or for any condition that should effect the relevance score, and use filter clauses for everything else.

Available filters:

- term filter (filter by exact values)
- terms filter (allows to specify multiple filters to match)
- range filter (find numbers or dates that fall into a specified range)
- exists and missing filters (has one or more values or doesn't have any values)
- bool filter (used to combine multiple filter clauses)

Available queries:

- match_all query (matches all documents)
- match query (use it for a full-text or exact value)
- multi_match query (match on multiple fields)
- bool query (combine multiple query clauses, calculates a relevance score)

See also [filtered query](https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl-filtered-query.html) and [combining queries together](https://www.elastic.co/guide/en/elasticsearch/guide/current/combining-queries-together.html).

!!! caution "Filter order"
    More specific filters must be placed before less-specific filters in order to exclude as many documents as possible, as early as possible.
    Cached filters are very fast, so they should be placed before filters that are not cacheable.

### Validate a query

```text
GET /myindex/mytype/_validate/query[?explain]
{
  "query": {

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
```

```json
{
  "acknowledged": true
}
```

See also:

- [refresh_interval](https://www.elastic.co/guide/en/elasticsearch/reference/current/indices-update-settings.html).

### Specifying field mapping

Mapping attributes: index and analyzer ("whitespace", "simple", "english", ...).

The index attribute controls how the string will be indexed:

- analyzed (default): analyze -> index
- not_analyzed: index the value exactly as specified
- no: don't index the field

```text
PUT /myindex
{
  "mappings": {
    "mytype": {
      "properties": {
        "mystr": {
          "type": "string",
          "analyzer": "english"
        },
        "mynumber": {
          "type": "long"
        }
      }
    }
  }
}
```

```json
{
  "acknowledged": true
}
```

It is possible to add a new field type with
```text
PUT /myindex/_mapping/newfield
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

equal to:
```text
GET /_search
{
  "query": {
    "match_all": {}
  }
}
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

See [languages elasticsearch supports](https://www.elastic.co/guide/en/elasticsearch/reference/current/analysis-lang-analyzer.html).

For language detection see [chromium-compact-language-detector](https://github.com/mikemccand/chromium-compact-language-detector).

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

Same as:
```json
{
  "query": {
    "match": {
      "attr1": "lorem ipsum",
      "type": "phrase"
    }
  }
}
```

The match_phrase query first analyses the query string to produce a list of terms. It then searches for all the terms, but keeps only documents that contain **all** of the search terms, **in the same position** relative to each other.

### Wildcard queries

Wildcards available:

- ? matches any character
- * matches zero or more characters

```json
{
  "query": {
    "wildcard": {
      "postcode": "w?F*HW"
    }
  }
}
```

See also [regexp query](https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl-regexp-query.html).

### Fuzzy query

The fuzzy query is the fuzzy equivalent of the term query. See [fuzzy query](https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl-fuzzy-query.html) documentation for details.

### Combining multiple clauses

Clauses can be as follows:

- Leaf clause (match)
- Compaund clauses (combine other other query clauses, including other compound clouses)

Compaund clause:
```json
{
  "bool": {
    "must": {},
    "must_not": {},
    "should": {}
  }
}
```

### Filtering a query

```json
{
  "query": {
    "filtered": {
      "query": {

      },
      "filter": {

      }
    }
  }
}
```

Filtering multiple values:
```json
{
  "query": {
    "filtered": {
      "filter": {
        "terms": {
          "price": [20, 30]
        }
      }
    }
  }
}
```

### A query as a filter

```json
{
  "query": {
    "filtered": {
      "filter": {
        "bool": {
          "must": {

          },
          "query": {

          }
        }
      }
    }
  }
}
```

### Boosting

```json
{
  "query": {
    "bool": {
      "should": {
        "match": {
          "myfield": {
            "query": "some query",
            "boost": 2
          }
        }
      }
    }
  }
}
```

Practically, there is no simple formula for deciding on the "correct" boost value for a particular query clause. It's a matter of try-it-and-see.

It id possible to [boost an index](https://www.elastic.co/guide/en/elasticsearch/reference/current/search-request-index-boost.html).

The boosting logic can be much more intelligent, refer the documentation for details.

### Sorting / ordering

By default, Elasticsearch orders matching results by their relevance score.

```json
{
  "query": {

  },
  "sort": {
    "myfield": {
      "order": "desc"
    }
  }
}
```

Multilevel sorting:

```json
{
  "query": {

  },
  "sort": [
    {
      "myfield": {
        "order": "desc"
      },
    },
    {
      "_score": {
        "order": "desc"
      }
    }
  ]
}
```

[Sorting on Multivalue Fields (arrays)](https://www.elastic.co/guide/en/elasticsearch/guide/current/_sorting.html#_sorting_on_multivalue_fields).

### Pagination

Use size and from keywords.
The size indicates the number of results that should be returned, default to 10.
The from indicates the number of initial results that should be skipped, default to 0.

[Deep pagination](https://www.elastic.co/guide/en/elasticsearch/guide/current/pagination.html) is inefficient in Elasticsearch. Keep (from + size) under 1000.

### Aggregation

Two main concepts:

- buckets: collections of documents that meet a criterion (similar to grouping in SQL)
- metrics: statistics calculated on the documents in a bucket (similar to count(), sum(), etc. in SQL)

```text
GET /myindex/mytype/_search?search_type=count
{
  "aggs": {
    "aggname": {
      "terms": {
        "field": "myfield"
      }
    }
  }
}
```

Elasticsearch supports [nested aggregations](https://www.elastic.co/guide/en/elasticsearch/reference/current/search-aggregations-bucket-nested-aggregation.html) and combining aggregations and search.

## Features

### Highlight

Highlights fragments from the original text.

[Highlighting](https://www.elastic.co/guide/en/elasticsearch/reference/current/search-request-highlighting.html)

### Aggregations

Allows to generate sophisticated analytics over your data.

[Aggregations](https://www.elastic.co/guide/en/elasticsearch/reference/current/search-aggregations.html)

### Geolocation

Elasticsearch allows us to combine geolocation with full-text search, structured search, and analytics.

There are four geo-point filters:

- geo_bounding_box: find geo-points that fall within the specified rectangle
- geo_distance: find geo-points within the specified distance of a central point
- geo_distance_range: find geo-points within specified minimum and maximum distance from a central point
- geo_polygon: find geo-points that fall within the specified polygon (very expensive)

There are a lot of geolocation search optimizations including [geohashes](https://www.elastic.co/guide/en/elasticsearch/guide/current/geohashes.html) and [geoshapes](https://www.elastic.co/guide/en/elasticsearch/reference/1.4/mapping-geo-shape-type.html).

### Relations

Elasticsearch, like most NoSQL databases, treats the world as though it were flat.

The FlatWorld advantages:

- indexing is fast and lock-free
- searching is fast and lock-free
- massive amounts of data can be spread across multiple nodes, because each document is independent of the others

If relations is required, consider these techniques:

- [application-side joins](https://www.elastic.co/guide/en/elasticsearch/guide/current/application-joins.html)
- [data denormalization](https://www.elastic.co/guide/en/elasticsearch/guide/current/denormalization.html)
- [nested objects](https://www.elastic.co/guide/en/elasticsearch/guide/current/nested-objects.html)
- [parent/child relationship](https://www.elastic.co/guide/en/elasticsearch/guide/current/parent-child.html)

## Best practices

### Index per time period (for time based data)

It may be one day or month for example.

### Index templates

Index templates can be used to control which settings should be applied to newly created indexes.

See [Index templates](https://www.elastic.co/guide/en/elasticsearch/reference/current/indices-templates.html).

### Index the same data into multiple fields (use different analysis)

A common technique for fine-tuning relevance is to index the same data into multiple fields, each with its own analysis chain.

### Dealing with redundant data

```text
PUT /myindex
{
  "mappings": {
    "user": {
      "first_name": {
        "type": "string",
        "copy_to": "full_name"
      },
      "last_name": {
        "type": "string",
        "copy_to": "full_name"
      },
      "full_name": {
        "type": "string"
      }
    }
  }
}
```

There also search time solution exists.

### Use scroll with deep pagination

The scroll API can be used to retrieve large numbers of results (or even all results) from a single search request.

See [Scroll documentation](https://www.elastic.co/guide/en/elasticsearch/reference/current/search-request-scroll.html).

### Field-level index-time boost

Don't use it, use [query-time boost](https://www.elastic.co/guide/en/elasticsearch/guide/current/query-time-boosting.html) instead. Query-time boosting is a much simpler, cleaner, more flexible option.

### [Capacity planning](https://www.elastic.co/guide/en/elasticsearch/guide/current/capacity-planning.html) (how many shards do I need?)

There are too many variables: hardware, size, document complexity, queries, aggregations, etc.

Try to play with a single server node:

- create a cluster consisting of a single server
- create an index with one primary shard and no replicas
- fill it with real documents
- run real queries and aggregations

Push this single shard until it "breaks". Once you define the capacity of a single shard, it is easy to find the number of primary shards required.

### Configuration

Change cluster.name (elasticsearch.yml) to stop your nodes from trying to join another cluster on the same network with the same name.

### Index rename or update

Use [Index aliases](https://www.elastic.co/guide/en/elasticsearch/reference/current/indices-aliases.html).

## Vocabulary

### A node

Is a running instance of Elasticsearch.

### A cluster

Is a group of nodes with the same cluster.name.

One node in the cluster is elected to be the master node, which is in charge of managing cluster-wide changes (does not need to be involved in document-level changes or search).

### A shard

A nodes container, holds a slice of all the data in the index.

Algorithm uses to route documents to shards:
```text
shard = hash(routing) % number_of_primary_shards
```
That's why we can't increase the number of shards for an existing index.

#### Primary vs replica shards

The number of primary shards in an index is fixed at the time that an index is created (defaults to 5).
The number of replica shards can be changed at any time (defaults to 0).

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

See boost and [tie_breaker](https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl-dis-max-query.html).

### Mapping

How the data in each field is interpreted.

Every type has its own mapping (schema definition).

Simple core field types:

- string: ```string```
- number: ```byte```, ```short```, ```integer```, ```long```
- floating point: ```float```, ```double```
- boolean: ```boolean```
- date: ```date```

Complex core field types:

- null
- arrays
- objects

### Analysis

How full text is processed to make it searchable.

Analysis consists of:

- tokenizing a block of text into individual terms suitable for use in an inverted index
- normalizing these terms into a standard form to improve their "searchability"

Built-in analyzers:

- Standard analyzer (splits the text on word boundaries, removes most punctuation, and lowercase all items)
- Simple analyzer (splits the text on anything that isn't a letter, and lowercase the items)
- Whitespace analyzer (splits the text on whitespace, doesn't lowercase)
- [Language analyzers](https://www.elastic.co/guide/en/elasticsearch/reference/current/analysis-lang-analyzer.html) (language specific analyzers)

```text
GET /_analyze?analyzer=standard
"Some text."
```

```json
{
  "tokens": [
    {
      "token": "some",
      "start_offset": 0,
      "end_offset": 4,
      "type": "<ALPHANUM>",
      "position": 0
    },
    {
      "token": "text",
      "start_offset": 5,
      "end_offset": 9,
      "type": "<ALPHANUM>",
      "position": 1
    }
  ]
}
```

Analyzer is a wrapper that combines three functions into a single package:

- character filters (removes html tags, etc.)
- tokenizers (breaks up a string into individual terms)
- token filters (change, add, or remove tokens)

Creating a custom analyzer:
```text
PUT /myindex
{
  "settings": {
    "analysis": {
      "char_filter": {

      },
      "tokenizer": {

      },
      "filter": {

      },
      "analyzer": {

      }
    }
  }
}
```

### Relevance

Relevance is the algorithm that we use to calculate how similar the contents of a full-text field are to a full-text query string.

The standard similarity algorithm used in Elasticsearch is known as "term frequency/inverse document frequency" (TF/IDF).

Term frequency - how often does the term appear in the field.
Inverse document frequency - how often does each term appear in the index.

### How far apart

How many times do you need to move a term in order to make the query and document match.

### Full-text search

Full-text search is a battle between precision - returning as few irrelevant documents as possible - and recall - returning as many relevant documents as possible.

## Instruments

[Kibana](https://www.elastic.co/guide/en/marvel/current/introduction.html) - an open source analytics and visualization platform designed to work with Elasticsearch
[Sense](https://www.elastic.co/blog/found-sense-a-cool-json-aware-interface-to-elasticsearch) - a Cool JSON Aware Interface to Elasticsearch
[Marvel](https://www.elastic.co/guide/en/marvel/current/introduction.html) - enables you to easily monitor Elasticsearch through Kibana

ELK stack (for logging):

- Elasticsearch
- Logstash (collects, parses, and enriches logs before indexing them into Easticsearch)
- Kibana (is a graphic frontend that makes it easy query and visualize what is happening across your network in near real-time)

Clients:
[Elasticsearch Python client](https://elasticsearch-py.readthedocs.io/en/master/)
[Elasticsearch Node.js client](https://www.npmjs.com/package/elasticsearch)

Services:
[Amazon Elasticsearch Service](https://aws.amazon.com/elasticsearch-service/)

## Links

[Elasticsearch: The Definitive Guide by Clinton Gormley and Zachary Tong](https://www.elastic.co/guide/en/elasticsearch/guide/current/index.html)
