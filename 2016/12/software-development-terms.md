labels: Blog
        SoftwareDevelopment
created: 2016-12-22T22:25
modified: 2019-05-24T10:33
place: Phuket, Thailand
comments: true

# Software development terms

[TOC]

See also [Principles from software development](/2015/10/principles-software) and [DynamoDB in examples, Example 1.5: Distributed system terms](/2015/06/dynamodb-example-1-5).

## Accidental complexity

Complexity is accidental if it is not inherent in the problem that the software solves (as seen by the users) but arises only from the implementation.

"Out of the Tar Pit" by Ben Moseley and Peter Marks

## Architecture

Architecture is "... the important stuff. Whatever that is." ([Who needs an Architect?](http://files.catwell.info/misc/mirror/2003-martin-fowler-who-needs-an-architect.pdf)).

The important stuff - what we think will be difficult to change without significantly increasing complexity.

"... significant design decisions (where significant is measured by the cost of change)" (Grady Booch).

Turns a big problem into smaller, more manageable.
Shows developers how to work together.
Provides a vocabulary for talking about complex ideas.
Enables agility: software is like water, able to take any shape, and architecture is a container that holds it.

[Design It!: From Programmer to Software Architect](https://www.amazon.com/Design-Programmer-Architect-Pragmatic-Programmers/dp/1680502093)

## Async frameworks

Async frameworks use a single thread as much as possible. Uses modern operation system's IO multiplexing functions: `select()`, `poll()` and `epoll()`. If we are single-threaded, we don't suffer the costs of context switches and save resources that extra thread requires.

The largest benefit of single thread is code simplicity, writing thread-safe code is more difficult.

## Code smell

Code smell - a symptom of bad OO design. Smells are certain structures in the code that indicate violation of fundamental design principles and negatively impact design quality.

## Complex universal vs simple specific

Vote for simple specific. [KISS](/2015/10/principles-software#kiss).

## Composition vs inheritance

> Favor object composition over class inheritance.
>
> Design Patterns by Gamma et al.

## Concurrency vs parallelism

> Concurrency is about dealing with lots of things at once.
> Parallelism is about doing lots of things at once.
> Not the same, but related.
> One is about structure, one is about execution.
> Concurrency provides a way to structure a solution to solve a problem that may (but not necessary) be parallelizable.
>
> Rob Pike, Co-inventor of the Go language

## Deterministic

The same operation produces the same result.

## Duck typing

> When I see a bird that walks like a duck and swims like a duck and quacks like a duck, I call that bird a duck.
>
> James Whitcomb Riley

A form of polymorphism where functions operate on any object that implements the appropriate methods, regardless of their classes or explicit interface declarations.

## Functional programming

It is a declarative programming paradigm, which means programming is done with expressions.

## Hacker

A hacker - someone who strives to solve problems in elegant and ingenious ways.

## Implementation vs interface

> The design must be simple, both in implementation and interface. It is more important for the implementation to be simple than the interface. Simplicity is the most important consideration in a design.
>
> Richard P. Gabriel, The rise of Worse is Better

## Large and complex

There are two schools of thought about teaching computer science. We might caricature the two views this way:

- The conservative view: Computer programs have become too large and complex to encompass in a human mind. Therefore, the job of computer science education is to teach people how to discipline their work in such a way that 500 mediocre programmers can join together and produce a program that correctly meets its specification.
- The radical view: Computer programs have become too large and complex to encompass in a human mind. Therefore, the job of computer science education is to teach people how to expand their minds so that  the programs can fit, by learning to think in a vocabulary of larger, more powerful, more flexible ideas than the obvious ones. Each unit of programming thought must have a big payoff in the capabilities of the program.

Brian Harvey and Matthew Wright, Preface by [Simply Scheme](https://people.eecs.berkeley.edu/~bh/ss-toc2.html)

## Lazy implementation

A lazy implementation postpones producing values to the last possible moment. This saves memory and may avoid useless processing as well.

## Programming

> Programming is science dressed up as art because most of us don't understand the physics of software and it's rarely, if ever, taught.
> ...
> This is the science of programming: make building blocks that people can understand and use easily, and people will work together to solve the very largest problems.
>
> zguide

## Technical debt

> Technical debt is the gap between your software system's current design and the disign you need it to have so you can continue to deliver value.
>
> Design It! by Michael Keeling

## Thread safety

> [Thread-safe code](http://mindprod.com/jgloss/threadsafe.html) is code that will work even if many threads are executing it simultaneously within the same process.

[Thread safety](https://en.wikipedia.org/wiki/Thread_safety) is a computer programming concept applicable to multi-threaded code. Thread-safe code only manipulates shared data structures in a manner that guarantees safe execution by multiple threads.

Software libraries can provide certain thread-safety guarantees. For example, concurrent reads might be guaranteed to be thread-safe, but concurrent writes might not be:

- Thread safe: Implementation is guaranteed to be free of race conditions when accessed by multiple threads simultaneously
- Conditionally safe: Different threads can access different objects simultaneously, and access to shared data is protected from race conditions
- Not thread safe: Code should not be accessed simultaneously by different threads

Ways to achieve thread safety:

- avoid shared state (thread-local storage, immutable objects)
- synchronization (ensure only one thread writes or reads the same data at any time, atomic)

See [Thread Synchronization Mechanisms in Python](http://effbot.org/zone/thread-synchronization.htm).

## Ugly code

> Ugly code hides problems and makes it hard for others to help you. You might get used to meaningless variable names, but people reading your code won't. Use names that are real words, that say something other than "I'm too careless to tell you what this variable is really for". Use consistent indentation and clean layout. Write nice code and your world will be more comfortable.
>
> zguide
