labels: Draft
        SoftwareDesign
created: 2023-12-21T09:40
modified: 2023-12-21T09:40
place: Bangkok, Thailand

# Software Design

[TOC]

Low coupling between modules and high cohesion within them.

Low coupling and high cohesion are general design principles.

There is a limit to how many things a person can think about at once (low coupling).

Projects have to make pragmatic trade-offs.

## Transaction script

> Organizes business logic by procedures where each procedure handles a single request from the presentation.
>
> Martin Fowler

Each operation should either succeed or fail but can never result in an invalid state.

## Active record

> An object that wraps a row in a database table or view, encapsulates the database access, and adds domain logic on that data,
>
> Martin Fowler

There is nothing wrong using active records when the business logic is simple.

When the business logic is simple but operates on complicated data structures.

## Domain model

## Message bus

Outbox pattern for publishing messages after committing changes to another database.

## Event sourcing

https://learn.microsoft.com/en-us/azure/architecture/patterns/event-sourcing

## Links

- [Domain-Driven Design](https://www.amazon.com/Domain-Driven-Design-Tackling-Complexity-Software-ebook/dp/B00794TAUG/) by Eric Evans
- [Design Patterns](https://learn.microsoft.com/en-us/azure/architecture/patterns/) at Azure Architecture Center
