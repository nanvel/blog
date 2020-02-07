labels: Draft
        Databases
created: 2019-06-11T10:45
modified: 2019-06-11T10:45
place: Phuket, Thailand

# Gremlin

Gremlin is the name of the graph traversal and query language provided by TinkerPop.

[TOC]

## Gremlin console

Create TinkerGraph:
```groovy
graph = TinkerGraph.open()
```

Load from GraphML:
```groovy
graph.io(graphml()).readGraph('air-routes.graphml')
```

To prevent output, add `[]`:
```groovy
a=g.V().has('code','AUS').out().toList();[]
```

## Query

```groovy
g = graph.traversal()
```

has and hasLabel:
```groovy
g.V().hasLabel('airport').has('code','DFW')
g.V().has('airport','code','DFW')
```

next() - a terminal step:
```groovy
g.V().has('airport','code','DFW').next().getClass()
```
Ends the graph traversal and returns a concrete object that you can work with further in your application.

has():
```groovy
g.V().has('region')
g.V().hasNot('region')
g.V().not(has('region'))
```

groupCount():
```groovy
g.V().groupCount().by(label)
g.V().label().groupCount()
g.V().group().by(label).by(count())

g.V().hasLabel('airport').groupCount().by('country')
g.V().hasLabel('country').group().by('code').by(out().count())
```

path - visited vertices and edges:
```groovy
g.V().has('airport','code','LCY').outE().inV().path()
```

```groovy
g.V().has('airport','code','AUS').out().as('a').out().as('b').
      path().by('code').from('a').to('b').limit(10)
```

If edge exist:
```groovy
g.V().has('code','AUS').out('route').has('code','DFW').hasNext()
```

Select edge between two vertices:
```groovy
g.V().has('code','MIA').outE().as('e').inV().has('code','DFW').select('e')
```

Limit:
```groovy
g.V().hasLabel('airport').limit(20).values('code')
g.V().hasLabel('airport').tail(20).values('code')
g.V().hasLabel('airport').range(0,20).values('code')
```

Locate by id:
```groovy
g.V().hasId(8).values('code')
g.V().has(id,8).values('code')
g.V().hasId(between(1,6))
g.V().has(id,between(1,6))
g.V(3).values('code')
g.V(3,6,8,15).values('code')
```

Labels:
```groovy
g.V().where(label().is(eq('airport'))).count()
g.V().has(label,'airport').count()
g.V().hasLabel('airport').count()
g.V().has(label,neq('airport')).count()
g.V().where(label().is(neq('airport'))).count()
g.V().not(hasLabel('airport')).count()
```

Equal:
```groovy
g.V().has('runways',eq(3)).count()
g.V().has('runways',3).count()
g.V().values('runways').is(3).count()
```

Starts with:
```groovy
g.V().hasLabel('airport').has('city',between('Dal','Dam')).values('city')
g.V().hasLabel('airport').
      filter{ it.get().value('city').startsWith('Dal')}.
      values('city')
```

Boolean:
```groovy
g.V().and(has('code','AUS'),has('icao','KAUS'))
g.V().has('code','AUS').and().has('icao','KAUS')
g.V().hasLabel('airport').
  where(out().count().is(lt(100).and(gt(94)))).
  group().by('code').by(out().count())
```

Where:
```groovy
g.V().has('runways',gt(5))
# is equal to
g.V().where(values('runways').is(gt(5)))

g.V().hasLabel('airport').where(out('route').count().is(gt(60))).count()
```

Finding two vertices in one query:
```groovy
g.V().has('code','NCE').values('region').as('r').
  V().hasLabel('airport').as('a').values('region').
      where(eq('r')).by().
      local(select('a').values('city','code','region').fold())
```

If/than/else (choose):
```groovy
g.V().has('region','US-TX').choose(values('longest').is(gt(12000)),
                                   values('code'),
                                   values('desc'))
```

Case/switch (option):
```groovy
g.V().hasLabel('airport').choose(values('code')).
                            option('DFW',values('desc')).
                            option('AUS',values('region')).
                            option('LAX',values('runways'))
```

Union and group:
```groovy
g.V().has('airport','code','DFW').as('a').
      union(select('a'),out().count()).fold()

[v[8],221]

g.V().has('airport','code','DFW').
      group().by().by(out().count())

[v[8]:221]]
```

sideEffect:
```groovy
g.V(3).sideEffect(out().count().store('a')).
       out().out().count().as('b').select('a','b')
```

aggregate (temporary collection):
```groovy
g.V().has('code','AUS').out().aggregate('nonstop').
     out().where(without('nonstop')).dedup().count()
```

coalesce - return the first has result:
```groovy
g.V(3).coalesce(out('fly'),__.in('contains')).valueMap()
```

simplePath - do not trevel the same path again:
```groovy
g.V().has('code','AUS').
      repeat(out().simplePath()).
        until(has('code','AGR')).
        path().by('code').limit(10)
```

Create if not exist:
```groovy
g.V().has('code','XYZ').fold().coalesce(unfold(),addV().property('code','XYZ'))
```

Delete:
```groovy
# vertices
g.V().has('code','AUS').outE().as('e').inV().has('code','LHR').select('e').drop()

# properties
g.V().has('code','SFO').properties('desc').drop()
```

Properties:
```groovy
g.V().has('code','AUS').property(list,'code','ABIA')
g.V().has('code','AUS').properties().hasValue('ABIA').drop()
g.V(3).property(set,'hw',"hello").property(set,'hw','world')
```

sack - a side effect:
```groovy
g.V().has('code','AUS').sack(assign).by('runways').
  V().has('code','SAF').out().
      sack(minus).by('runways').sack().fold()
```

Profile:
```groovy
g.V().has('region','US-TX').out().has('region','US-CA').
                            out().has('country','DE').profile()
```

### Walk a graph

One vertex is considered to be adjacent to another vertex if there is an edge connecting them.
A vertex and an edge are considered incident if they are connected to each other.

`out` - Outgoing adjacent vertices.
`in` - Incoming adjacent vertices.
`both` - Both incoming and outgoing adjacent vertices.
`outE` - Outgoing incident edges.
`inE` - Incoming incident edges.
`bothE` - Both outgoing and incoming incident edges.
`outV` - Outgoing vertex.
`inV` - Incoming vertex.
`otherV` - The vertex that was not the vertex we came from.

All except `outV`, `inV`, `otherV` can accept labels as parameters.

### Predicates

`eq` - Equal to
`neq` - Not equal to
`gt` - Greater than
`gte` - Greater than or equal to
`lt` - Less than
`lte` - Less than or equal to
`inside` - Inside a lower and upper bound, neither bound is included.
`outside` - Outside a lower and upper bound, neither bound is included.
`between` - Between two values inclusive/exclusive (upper bound is excluded)
`within` - Must match at least one of the values provided. Can be a range or a list
`without` - Must not match any of the values provided. Can be a range or a list

## Best practices

We start from looking for Vertices, and their number is lower than Edges.

### Labels

> As useful as labels are, in larger graph deployments when indexing technology such as Solr or Elasticsearch is often used to speed up traversing the graph, vertex labels typically do not get indexed. Therefore, it is currently recommended that an actual vertex property that can be indexed is used when walking a graph rather than relying on the vertex label. This is especially important when working with large graphs where performance can become an issue.

### Double underscore

`__` - is a result of the previous step. Use to avoid reserved names usage issues (`in` is reserved in groovy).

## Vocabulary

### Traversal

Graph query is often referred to as a traversal.

Traversals that do not start with a V or E step are referred to as "anonymous traversals".

### Modulator step

A modulator is a step that influences the behavior of the step that it is associated with. Examples of such modulator steps are by and as.

### Vertex degree

Vertex degree is used when discussing the number of edges coming into a vertex (in degree), going out from a vertex (out degree) or potentially both coming in and going out (degree).

### Fold and unfold

The unfold step turns the HashMap into a series of HashMap.Node elements.

### Side effect

Can store values during a traversal but has no effect on what is passed on to the next step.

### OLTP vs OLAP

OLTP - Online Transaction Processing
OLAP - Online Analytical Processing

## Links

[Gremlin Graph Guide](https://kelvinlawrence.net/book/Gremlin-Graph-Guide.html)
