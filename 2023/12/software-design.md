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

## Layered achitecture

- Data access layer (infrastructure layer) - also includes integration with the various external information providers
- Business logic layer (domain layer, model layer, core layer)
- Service layer (application layer, use case layer) - defines an application's boundary with a layer of services that establishes a set of available operations and coordinates the application's response in each operation
- Presentation layer (user interface)

## Ports and adapters architecture

Known as:

- hexagonal architecture
- onion architecture
- clean architecture

![ports and adapters](ports_and_adapters.png)

- business logic layer: entities, rules, processes
- application layer: actions
- infrastructure layer: database, ui framework, external provider, message bus

Abstract ports are resolved into concrete adapters in the infrastructure layer either through dependency injection or by bootstrapping.

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

## Command-query responsibility segregation (CQRS)

## Event sourcing

https://learn.microsoft.com/en-us/azure/architecture/patterns/event-sourcing

The accepted name for the database that is used for persisting events is event store.

[Versioning in an Event Sourced System](https://leanpub.com/esversioning/read) by Greg Young.

## Other patterns

### Forgetable payload

Sensetive information is encrypted, when has to be deleted - only the encryption ckey is being deleted.

## Links

- [Domain-Driven Design](https://www.amazon.com/Domain-Driven-Design-Tackling-Complexity-Software-ebook/dp/B00794TAUG/) by Eric Evans
- [Design Patterns](https://learn.microsoft.com/en-us/azure/architecture/patterns/) at Azure Architecture Center
- [Learning Domain-Driven Design](https://www.amazon.com/Learning-Domain-Driven-Design-Vlad-Khononov-ebook/dp/B09J2CMJZY/) by Vlad Khononov
