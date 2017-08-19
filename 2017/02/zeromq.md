labels: Draft
        Distributed
created: 2017-02-26T22:42
modified: 2017-02-26T22:42
place: Phuket, Thailand
comments: true

# ZeroMQ notes

> Connect your code in any language, on any platform.

> Looks like an embeddable networking library but acts like a concurrency framework.

ZeroMQ: an efficient, embeddable library that solves most of the problems an application needs to become nicely elastic across a network, without much cost.

Transports: in-process, inter-process, TCP and multicast.

Patterns: fan-out, pub-sub, task distribution, request-reply.

## Patterns

### Request - reply

### Publish/subscribe

One way data distribution.

Server pushes updates to a set of clients.
A subscribed can set many subscriptions.

### Parallel pipeline

## Encoding/decoding messages

Protocol Buffers.

## RabbitMQ

### Acknowledgements vs publisher confirms

Acknowledgements: delivery processing acknowledgements from consumers to RabbitMQ.
Publisher confirms: broker acknowledgements to publishers.

### Prefetch count

Prefetch count - max number of unacknowledged deliveries that are permitted on a channel.

### [Dead Letter Exchanges](https://www.rabbitmq.com/dlx.html)

Messages from a queue can be 'dead-lettered'; that is, republished to another exchange when rejected.

## Terms

### Slow joiner

### Context

Context is a container for all sockets in single process and acts as as the transport for inproc sockets, which are the fastest way to connect threads in one process.

### HWM (high-water mark)

Protects against memory overflows.

### Server vs client

To create a connection between two nodes, you use `zmq_bind()` in one node and zmq_connect() in the other. As a general rule of thumb, the node that does `zmq_bind()` is a "server", sitting on a well-known network address, and the node which does `zmq_connect()` is a "client", with unknown or arbitrary network addresses. Thus we say that we "bind a socket to an endpoint" and "connect a socket to an endpoint", the endpoint being that well-known network address.

## Links

[ZeroMQ home page](http://zeromq.org/)

