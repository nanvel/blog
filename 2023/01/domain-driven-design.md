labels: Draft
        SoftwareDesign
created: 2023-01-21T13:29
modified: 2023-12-20T19:51
place: Bangkok, Thailand

# Domain Driven Design

loc: 270

[TOC]

Presentation:
- Eric evans, years
- books / links
- why do we need it?
- strategic design
- tactical design
- rlation to TDD

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

Our pace of development was accelerating at a stage where most of projects are beginning to bog down in the mass and complexity of what has already been built.

To have a project accelerate as development proceeds - rather than get weighed by its own legacy - demands a design that is pleasure to work with, invting to change. A supple design:
- ubiquitous language
- intention-revealing interfaces
- side-effect-free functions
- assertions
- conceptual contours

A supple design helps limit mental oveload, primarily by reducing dependencies and side effects.

Name classes and operations to describe their effect and purpose, without reference to the means by which they do what they promise.

Operations divided into two categories:
- commands (modifiers)
- queries

No side effects: a function can call on other functions without worrying about the depth of nesting. They are easier to test.

When a function is presented through an intention-revealing interface, a developer can use it wihtout understanding the detail of its implementation.

Intention-revealing interfaces allow clients to present objects as units of meaning rather than just mechanisms.

Low coupling is a basic way to reduce conceptual overload.

Many XP practices are aimed at this specific problem of maintaining a coherent design that is being constantly changed by many people.

The facade belong in the bounded context of the other system. It just presents a friendlier face specialized for your needs.

An adapter is a wrapper that allows a client to use a different protocol than that understood by the implementer of the behavior.

Creating distinctive software comes tback to a stable team acculating specialized knowledge and crunching it into a rich model.

With the tools and technology we already have, we can build systems much more valuable than most projects do today. We can write software that is a pleasure to use and a pleasure to work on, software that doesn't box us in as it grows but creates new opportunities and continues to add value for its owners.

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

Layers are partitions of a system in which the members of each partition are aware of and are able to use the services of the layers below, but unaware of and independent of the layers above.

## Aggregates

A cluster of associated objects that are treated as a unit for the purpose of data changes. External references are restricted to one member of the aggregate, designated as the root. A set of consistency rules applies within the aggregate's boundaries.

Tighten up the model itself by defining clear ownership and boundaries, avoiding a chaotic, tangled web of objects.

Example: car (root entity), the aggregate includes wheels, tires, etc.

Factories and repositories operate on aggregates, encapsulating the complexity of specific life cycle transitions.

## Factories

A program element whose responsbility is the creation of other objects is called a factory.

When creation of an object, or an entire aggregate, becomes complicated or reveals too much of the internal structure, factories provide encapsulation.

Problems arise from overloading a complex object with responsibility for its own creation.

Doesn't own the product once it is created.

Ways to design a factory:
- factory method
- abstract factory
- builder

## Repositories

Find an object based on its relationship to another.

Reconstitution - creation of an object from stored data.

Benefits:
- simple model for obtaining persistent objects and managing their life cycle
- decouple application and domain design from persistence technology / database strategies / data sources
- communicate design decissions about object access
- easy subsitution of a dummy implementation fro testing

The factory makes new objects; the repository finds old objects.

## Domain

Should not try to reduce domain modelling to a cookbook or a toolkit. Mideling and design call for creativity.

A deep model makes possible an expressive design. At the same time, a design can actually feed insight into the model discovery process.

## Specification

Can test any object to see if it satisfies the specified criteria.

## Vocabulary

Cohesion - logical agreement and dependence.

Command (aka modifier) - an operation that effects some change to the system. An operation that intentionally creates a side effect.

Domain - a sphere of knowledge, influence, or activity.

Entity - an object fundamentally defined not by its attributes, but by a thread of continuity and identity.

Factory - a mechanism for encapsulating complex creation logic and abstracting the type of created object for the sake of a client.

Intention-revealing interface - a design in which the names of classes, methods, and other elements convey both the original developer's purpose in creating them and their value to a client developer.

Model - a system of abstractions that describes selected aspects of a domain and can be used to solve problems related to that domain.

Model-driven design - a design in which some subset of software elements corresponds closely to elements of a model. Also, a process of codeveloping a model and an implementation that stay aligned with each other.

Repository - a mechanism for encapsulating storage, retrieval, and search behavior which emulates a collection of objects.

Service - an operation oferred as an interface that stands alone in the model, with no encapsulated state.

Ubiquitous language - a language structured around the domain model and used by all team members to connect all the activities of the team with the software.

Value object - an object that describes some characteristic or attribute but carries no concept of identity.

## Links

- [Domain-Driven Design by Eric Evans](https://www.amazon.com/Domain-Driven-Design-Tackling-Complexity-Software-ebook/dp/B00794TAUG/)
- [Learning Domain-Driven Design](https://www.amazon.com/Learning-Domain-Driven-Design-Vlad-Khononov-ebook/dp/B09J2CMJZY/) by Vlad Khononov
- [Architecture Patterns with Python](https://www.amazon.com/Architecture-Patterns-Python-Domain-Driven-Microservices-ebook/dp/B085KB31X3/) by Harry Percival, Bob Gregory
- [Implementing Domain-Driven Design](https://www.amazon.com/Implementing-Domain-Driven-Design-Vaughn-Vernon-ebook/dp/B00BCLEBN8/) by Vernon Vaughn
- [Domain-Driven Design Europe](https://www.youtube.com/@ddd_eu) on YouTube
