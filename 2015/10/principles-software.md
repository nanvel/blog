labels: Blog
		SoftwareDevelopment
created: 2015-10-24T14:41
modified: 2022-09-22T11:15
place: Kyiv, Ukraine
comments: true

# Principles from software development

[TOC]

## [5 Whys](https://en.wikipedia.org/wiki/5_Whys)

The primary goal of the technique is to determine the root cause of a defect or problem by repeating the question "Why?" Each question forms the basis of the next question. The "5" in the name derives from an empirical observation on the number of iterations typically required to resolve the problem.

The technique was formally developed by Sakichi Toyoda and was used within the Toyota Motor Corporation during the evolution of its manufacturing methodologies.

The benefits of asking why (according to [GTD](https://www.amazon.com/Getting-Things-Done-Stress-Free-Productivity/dp/0142000280)):

- it defines success
- it creates decision-making criteria
- it aligns resources
- it motivates
- it clarifies focus
- it expands options

## [AAR](https://en.wikipedia.org/wiki/After-action_review)

An **A**fter **A**ction **R**eview is a structured review or de-brief process for analyzing what happened, why it happened, and how it can be done better.

To apply this tool ask yourself:

- What was supposed to happen?
- What did happen?
- What are some improvements?
- What are some sustainments?
- What can be done to improve the result?
- Summary.

## [Brooks's law](https://en.wikipedia.org/wiki/Brooks's_law)

Adding manpower to a late software project makes it later.

## Dependency Injection (DI)

A form of inversion of control, dependency injection aims to separate the concerns of constructing objects and using them, leading to loosely coupled programs.

### Dependency vs Composition vs Agregation

If the contained object cannot exist without the existence of container object, then it is called composition (engine and a car).

Aggregation: the child object can exist outside the parent object (driver and a car).

## DRY

**D**on’t **R**epeat **Y**ourself.

A software engineering principle stating that "Every piece of knowledge must have a single, unambiguous, authoritative representation within a system." It first appeared in the book The Pragmatic Programmer by Andy Hunt and Dave Thomas.

> Every piece of knowledge must have a single, unambiguous, authoritative representation within a system.
>
> The Pragmatic Probrammer by Andy Hunt and Dave Thomas

## EAFP

**E**asier to **a**sk for **f**orgiveness than **p**ermission.

```python
try:
    x = my_dict["key"]
except KeyError:
    # say sorry
```

## Fail fast

A system design approach recommending that errors should be reported as early as possible.

## Imperative vs Declarative style of programming

Declarative style of programming tells a computer what to do without specifying how, while an imperative style style of programming describes how to do it.

## KISS

Stands for "**K**eep **I**t **S**imple, **S**tupid."
Simplest solution is often the best.

This calls for seeking the simplest possible solution, with the fewest moving parts. The phrase was coined by Kelly Johnson, a highly accomplished aerospace engineer who worked in the real Area 51 designing some of the most advanced aircraft of the 20th centure.

## Live and die by documentation

> Live and die by documentation.
>
> Matthew Ginnard

Software design, decisions, plans have to be documented.

## Minimum viable product

MVP is the product with the highest return on investment versus risk. It is the sweet spot between products without the required features that fail at sunrise and the products with too many features that cut return and increase risk. The term was coined and defined by Frank Robinson, and popularized by Steve Blank, and Eric Ries.

> The first step is to enter the Build phase as quickly as possible with a minimum viable product (MVP). The MVP is that version of the product that enables a full turn of the Build-Measure-Learn loop with a minimum amount of effort and the least amount of development time.
>
> Eric Ries

![Minimum viable product](mvp.jpg)

## OOP

A programming paradigm based on the concept of "objects", which are data structures that contain data, in the form of fields, often known as attributes; and code, in the form of procedures, often known as methods.

There are four main principles:

- Encapsulation
- Abstraction
- Inheritance

!!! note "Code smell"
	Code smell - a symptom of bad OO design.

### Encapsulation

In programming languages, encapsulation is used to refer to one of two related but distinct notions, and sometimes to the combination thereof:

- A language mechanism for restricting access to some of the object's components.
- A language construct that facilitates the bundling of data with the methods (or other functions) operating on that data.

### Abstraction

Abstraction is a technique for managing complexity of computer systems. It works by establishing a level of complexity on which a person interacts with the system, suppressing the more complex details below the current level.

### Inheritance

> [We] started to push on the inheritance idea as a way to let novices build on frameworks that could only be designed by experts.
>
> Alan Kay, [The Early History of Smalltalk](http://worrydream.com/EarlyHistoryOfSmalltalk/)

Inheritance is when an object or class is based on another object (prototypal inheritance) or class (class-based inheritance), using the same implementation (inheriting from an object or class) specifying implementation to maintain the same behavior (realizing an interface; inheriting behavior).

## Pareto principle

For many events, roughly 80% of the effects come from 20% of the causes.

80 percent of results will come from just 20 percent of the action.
Vilfredo Federico Damaso Pareto one day noticed that 20 percent of the pea plants in his garden generated 80 percent of the healthy peapods. Then he discovered that 80 percent of the land in Italy was owned by just 20 percent of the population, 80 percent of production typically came from just 20 percent of the companies.

## Pastel's law

Or robustness principle.

Be conservative in what you do, be liberal in what you accept from others.

## PDD

**P**urpose-**d**riven **d**evelopment.

Links:

- [Purpose Driven Development - PDD](http://jacekratzinger.blogspot.com/2012/01/purpose-driven-development-pdd.html)

## Principle of simplicity

Simpler is better.

## Reinventing the wheel

Do something again, from the beginning, especially in a needless or inefficient effort.

## Rubber duck debugging

Rubber duck debugging is an informal term used in software engineering for a method of debugging code. The name is a reference to a story in the book The Pragmatic Programmer in which a programmer would carry around a rubber duck and debug their code by forcing themselves to explain it, line-by-line, to the duck.

My case:

![Mio and Haruhi](rdd.jpg)

## SOLID

**S**ingle responsibility
**O**pen-closed
**L**iskov substitution
**I**nterface segregation
**D**ependency inversion

### Single responsibility (SRP)

> Gather together those things that change for the same reason, and separate those things that change for different reasons.
>
> Robert C. Martin, Single Responsibility Principle

According to [Wikipedia](https://en.wikipedia.org/wiki/Single_responsibility_principle):

In object-oriented programming, the single responsibility principle states that every class should have responsibility over a single part of the functionality provided by the software, and that responsibility should be entirely encapsulated by the class. All its services should be narrowly aligned with that responsibility.

Links:

- [SRP: The Single Responsibility Principle](http://www.objectmentor.com/resources/articles/srp.pdf)

### Open-closed (OCP)

Software entities (classes, modules, functions, etc.) should be open for extension, but closed for modification.

### Liskov substitution (LCP)

States that, in a computer program, if S is a subtype of T, then objects of type T may be replaced with objects of type S (i.e., objects of type S may substitute objects of type T) without altering any of the desirable properties of that program (correctness, task performed, etc.)

### Interface segregation (ISP)

ISP splits interfaces which are very large into smaller and more specific ones so that clients will only have to know about the methods that are of interest to them. Such shrunken interfaces are also called role interfaces.[2] ISP is intended to keep a system decoupled and thus easier to refactor, change, and redeploy.

### Dependency inversion (DIP)

A. High-level modules should not depend on low-level modules. Both should depend on abstractions.
B. Abstractions should not depend on details. Details should depend on abstractions.

## Shiny Object Syndrome

or SOS - [Eclectic Thoughts on Shiny Distractions](https://myshinyobjectsyndrome.com/what-is-shiny-object-syndrome/).

## TDD

**T**est-**d**riven **d**esign (also seen test-driven development).

## The next action

A powerful principle from [GTD](https://en.wikipedia.org/wiki/Getting_Things_Done) technique: Next action must be defined.

> The secret of getting ahead is getting started. The secret of getting started is breaking your complex overwhelming tasks into small, manageable tasks, and then starting on the first one.
>
> Mark Twain

Next action - the next physical, visible activity that progress something toward completion. It is specific enough so that you know where it happens, and with what tools (if any). What "doing" looks like.

## [The twelve-factor app](http://12factor.net/)

The twelve-factor app is a methodology for building software-as-a-service apps.

## The Zen of Python

[PEP-20](https://www.python.org/dev/peps/pep-0020/) by Tim Peters:

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one - and preferably only one - obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than **right** now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea - let's do more of those!

## Using common sense

Your common sense is your natural ability to make good judgments and to behave in a practical and sensible way.

## YAGNI

Stands for "**Y**ou **A**in't **G**onna **N**eed **I**t."

A slogan to avoid implementing functionality that is not immediately necessary based on assumptions about future needs.
