labels: Draft
        SoftwareDesign
created: 2023-01-21T13:29
modified: 2023-12-20T19:51
place: Bangkok, Thailand

# Domain Driven Design

loc: 110

[TOC]

> It is not about drawing pictures of a domain; it is about how you think of it, the language you use to talk about it, and how you organize your software to reflect your improving understanding of it.
>
> Ralph Johnson

> Really powerful domain models evolve over time, and even the most experienced modelers find that they gain their best ideas after the initial releases of the system.
>
> Martin Fowler

When complexity gets out o hand, developers can no longer understand the software well enough to change or extend it easily and safely.

Extreme Programming recognizes the importance of design decisions, but it strongly resists upfront design. Instead, it puts and admirable effort into communication and improving the project's ability to change course rapidly.

The XP process assumes that you can improve a design by refactoring, and that you will do this often and rapidly.

XP advocates using no extra design documents at all and letting the code speak for itself.
A document shouldn't try to do what the code already does well.
Documents can clarify design intent when the programming language does not support a straight-forward implementation of a concept.

The building blocks of a model-driven design condenses a core of best practices in object-oriented domain modelling into a set of basic building blocks.

Deep undestanding of the domain comes from diving in, implementing an initial design based on a probably naive model, and then transforming it again and again.

A model is a simplification. It is an interpretation of reality that abstracts the aspects relevant to solving the problem at hand and ignores extraneous detail.

A model is a selectively simplified and consciously structured form of knowledge.
It is like movie-making, loosely representing reality to a particular purpose.

Developers should watch for ambiguity ir inconsistency that will trip up design.

Using standard patterns also adds to the ubiquitous language, which all team members can use to discuss model and design decisions.

Following proven patterns for individual elements helps to produce a model that is practical to implement.

Layered achitecture: User interface (presentation latyer) -> Application -> Domain -> Infrastructure.
The essential principal is that any element of a layer dependes only on other elements in the same layer or on elements of the layers beneath it.
The domain layer is where the model lives.

Isolating the domain implementation is a prerequisite for domain-driven design.

Domain-driven design pays off best for ambitious projects, and it does require strong skills. Not all projects are ambitious.

A common, costrly mistake is to build a complex infrastructure and use industrial-strength tools for a project that doesn't need them.

## Components

Value and Identity objects
Model
Services
Utilities
Repository
Factory

## Tactical

Model elements:
- Entities (something with continuity and identity, tracked through different states and implementations)
- Value objects
- Services (more clearly expressed as actions or operations)

### Entity

aka reference objects.

An object defined primarily by its identity is called an entity.
Identities must be defined so that they can be effectively tracked.

Distinguished by its identity, rather than its attributes.

Example: a person, a city, a car, a lottery ticket, a bank transaction.

### Value objects

Describe some characteristics of a thing.

An object that represents a descriptive aspect of the domain with conceptual identity is called a value object.
For objects that we care about only what they are, not who or which they are.

Making choices about copying, sharing, and immutability.

Share one instance and point to it many times (flyweight).

### Services

Sometimes, it is just isn't a thing.

There are important domain operations that can't find a natural home in an entity or value object.

Use "Manager" suffix?

Defined purely in terms of what it can do for a client.

A good service characteristics:
- not a natural part of an etity or value object
- the interface is defined in terms of other elements of the domain model
- the operation is stateless

## Layered structure

Services into layers:
- application
- domain
- infrastructure

## Links

- [Domain-Driven Design by Eric Evans](https://www.amazon.com/Domain-Driven-Design-Tackling-Complexity-Software-ebook/dp/B00794TAUG/)
- [Learning Domain-Driven Design](https://www.amazon.com/Learning-Domain-Driven-Design-Vlad-Khononov-ebook/dp/B09J2CMJZY/) by Vlad Khononov
- [Architecture Patterns with Python](https://www.amazon.com/Architecture-Patterns-Python-Domain-Driven-Microservices-ebook/dp/B085KB31X3/) by Harry Percival, Bob Gregory
- [Implementing Domain-Driven Design](https://www.amazon.com/Implementing-Domain-Driven-Design-Vaughn-Vernon-ebook/dp/B00BCLEBN8/) by Vernon Vaughn
