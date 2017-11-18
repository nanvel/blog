labels: Draft
        HighScalability
        SoftwareDevelopment
created: 2017-05-07T20:54
modified: 2017-11-06T15:01
place: Phuket, Thailand
comments: true

# High scalability

[TOC]

Loc 2089

Obsticles:

- reads
- writes
- data size
- data complexity
- response time
- access patterns

Instruments to solve:

- NoSQL
- message queues
- caches
- search indexes
- batch and stream processing frameworks

## Load

Checking what happens when increasing load:

- increase load, keep the system resources unchanged, see how is the system performance affected
- increase load, see how much resources you need to add to keep the system performance unchanged

Describing performance:

- throughput (number of records/requests we process per some period of time)
- response time (the time between request was sent and response was received)

## CPU

Many applications today are data-intensive. Raw CPU power is rarely a limiting factor.

## Queues

Help to handle spikes, scale horizintally and make system more reliable.

See [Feeds](/2016/08/feeds).

## Big data?

Big data - if amount of data or resources to process it is the current system limit.

Throughput:

- low = <100/s
- medium = <5000/s
- high = >5000/s

Numbers:

- Airbnb, [100k messages being sent on mobile per hour](https://medium.com/airbnb-engineering/messaging-sync-scaling-mobile-messaging-at-airbnb-659142036f06)

[High Scalability: Building bigger, faster, more reliable websites](http://highscalability.com/)
[Data Pipeline Architect - Resources to help you with data planning and plumbing](http://datapipelinearchitect.com/articles/)
[Why You Shouldn’t Build Your Own Data Pipeline](https://blog.stitchdata.com/why-you-shouldnt-build-your-own-data-pipeline-16c767fd8f46)
[Spark talk on PyCon Ukraine 2017](https://www.youtube.com/watch?v=vieASGQ6FP0) by Taras Lehinevych

## Vocabulary

### Data-intensive applications

Limiting factors are the amount of data, the complexity of data, the speed at which it is changing.

### Compute-intensive application

Where CPU cycles are the bottleneck.

### Stream processing

Send a message to another process, to be handled asynchronously.

### Batch processing

Periodically crunch a large amount of accumulated data.

### Reliability

The system should continue to work correctly even in the face of adversity (hardware or software faults).

### Scalability

As the system grows, there should be reasonable ways of dealing with that growth.

Vertical scaling (scaling up) - moving to a more powerful machine.
Horizontal scaling (scaling out) - distributing the load across multiple machines.

!!! tip "Be pragmatic"
    Using several fairly powerful machines can still be simpler and cheaper than a large number of small virtual machines.

### Maintainability

Over time, many different people will work on the system, and they should be able to work on it productively.

### Latency vs response time

Response time - what a client sees (includes network and queuing delays).

Latency - is the time a request is waiting to be handled (during this period the request is latent).

### MapReduce

MapReduce is a programming model for processing large amounts of data in bulk across many machines.

MapReduce is neither a declarative query language nor a fully imperative query API, but somewhere in between.

## Links

[High Scalability: Building bigger, faster, more reliable websites](http://highscalability.com/) by Todd Hoff
[Apache Kafka talk on Pycon Ukraine 2017](https://www.youtube.com/watch?v=dKUQFLgtW24) by Taras Voinarovskyy
