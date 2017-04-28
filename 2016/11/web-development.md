labels: Draft
		SoftwareDevelopment
		WebDevelopment
created: 2016-11-29T11:56
modified: 2017-02-12T12:58
place: Phuket, Thailand
comments: true

# Web development

## To investigate

Server sent events (https://www.youtube.com/watch?v=8-PxeTgTx6s).
[Splash - A javascript rendering service](http://splash.readthedocs.io/en/stable/).
[The Unofficial Guide to Rich Hickey's Brain](http://www.flyingmachinestudios.com/programming/the-unofficial-guide-to-rich-hickeys-brain/)

[Code Smells](https://sourcemaking.com/refactoring/smells)

## img title vs image alt

**Alt** text is meant to be an alternative information source for those people who have chosen to disable images in their browsers and those user agents that are simply unable to “see” the images. Google officially confirmed it mainly focuses on alt text when trying to understand what an image is about.

Image **title** should provide additional information and follow the rules of a regular title: it should be relevant, short, catchy, and concise (A title “offers advisory information about the element for which it is set.“).

Source: [Image Alt Text Vs. Image Title: What’s the Difference?](https://www.searchenginejournal.com/image-alt-text-vs-image-title-whats-the-difference/).

## HTML parsing

Replace tags and more:
http://w3lib.readthedocs.io/en/latest/w3lib.html

## Python batteries

[textract](https://github.com/deanmalmgren/textract) - extract text from pdf, odt, csv, etc.
[Python dictionaries validation](https://github.com/nicolaiarocci/cerberus)

## Exceptions

> Do you keep an endpoint on your site that purposely causes an exception to test changes to 
exception handling? Asking for a friend.
>
> Mark Roddy @digitallogic

## Async

Async frameworks use a single thread as much as possible.
Uses modern operation system's IO multiplexing functions: select(), poll() and epoll().
If we are single-threaded , we don't suffer the costs of context switches and save resources that extra thread required.
The largest benefit of single thread is code simplicity, writing thread-safe code is more difficult.

## Naming conventions

Compound names: "from less specific to more specific" works best in the most cases.

## Schema validation

[validictory - general purpose python data validator](https://pypi.python.org/pypi/validictory)

## Complex universal vs simple specific

Vote for simple specific. KISS.

## Thoughts on scale

### Queues

Help to handle spikes, scale horizintally and make system more reliable.

### Big data?

Big data if amount of data or resources to process it is the current system limit.

Throughput:

- low = <100/s
- medium = <5000/s
- high = >5000/s

[High Scalability: Building bigger, faster, more reliable websites](http://highscalability.com/)
[Data Pipeline Architect - Resources to help you with data planning and plumbing](http://datapipelinearchitect.com/articles/)
[Why You Shouldn’t Build Your Own Data Pipeline](https://blog.stitchdata.com/why-you-shouldnt-build-your-own-data-pipeline-16c767fd8f46)

## Vocabulary

### RFC

RFC - request for comments.

### Directed acyclic graph

[Directed acyclic graph](https://en.wikipedia.org/wiki/Directed_acyclic_graph) (DAG) is a finite directed graph with no directed cycles. That is, it consists of finitely many vertices and edges, with each edge directed from one vertex to another, such that there is no way to start at any vertex v and follow a consistently-directed sequence of edges that eventually loops back to v again. Equivalently, a DAG is a directed graph that has a topological ordering, a sequence of the vertices such that every edge is directed from earlier to later in the sequence.

See [airflow](https://airflow.incubator.apache.org/).
