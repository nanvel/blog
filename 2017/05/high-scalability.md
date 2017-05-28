labels: Draft
		HighScalability
		SoftwareDevelopment
created: 2017-05-07T20:54
modified: 2017-05-07T20:54
place: Phuket, Thailand
comments: true

# High scalability

[TOC]

Obsticles:

- reads
- writes
- data size
- data complexity
- response time
- access patterns

## CPU

Many applications today are data-intensive. Raw CPU power is rarely a limiting factor.

## Queues

Help to handle spikes, scale horizintally and make system more reliable.

See [Feeds](/2016/08/feeds).

## Big data?

Big data if amount of data or resources to process it is the current system limit.

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

### Stream processing

Send a message to another process, to be handled asynchronously.

### Batch processing

Periodically crunch a large amount of accumulated data.

### Reliability

The system should continue to work correctly even in the face of adversity (hardware or software faults).

### Scalability

As the system grows, there should be reasonable ways of dealing with that growth.

### Maintainability

Over time, many different people will work on the system, and they should be able to work on it productively.

## Links

[High Scalability: Building bigger, faster, more reliable websites](http://highscalability.com/) by Todd Hoff
[Apache Kafka talk on Pycon Ukraine 2017](https://www.youtube.com/watch?v=dKUQFLgtW24) by Taras Voinarovskyy
