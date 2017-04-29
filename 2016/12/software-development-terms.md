labels: Draft
        SoftwareDevelopment
created: 2016-12-22T22:25
modified: 2017-02-23T18:16
place: Phuket, Thailand
comments: true

# Software development terms

[TOC]

## Code smell

Code smell - a symptom of bad OO design. Smells are certain structures in the code that indicate violation of fundamental design principles and negatively impact design quality.

## Composition vs inheritance

> Favor object composition over class inheritance.
>
> Design Patterns by Gamma et al.

## Concurency vs parallelism

> Concurency is about dealing with lots of things at once.
> Parallelism is about doing lots of things at once.
> Not the same, but related.
> One is about structure, one is about execution.
> Concurency provides a way to structure a solution to solve a problem that may (but not necessary) be parallelizable.
>
> Rob Pike, Co-inventor of the Go language

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

## SQL injection

An SQL injection:

- Hi, this is you sons school, we're having some computer trouble.
- Oh, dear - did he break something? In a way -)
- Do you really name your son "Robert'); DROP TABLE Students;"?
- Oh, yes. Little Bobby tables we call him.
- Well, we've lost this year's student records. I hope yo're happy.
- And I hope you've learned to sanitize your database inputs.

## Columnal database

> The Tables Have Turned.
>
> Vertica slogan

## Programming

> Programming is science dressed up as art because most of us don't understand the physics of softwware and it's rarely, if ever, taught.
> ...
> This is the science of programming: make building blocks that people can understand and use easily, and people will work together to solve the very largest problems.
>
> zguide

## Ugly code

> Ugly code hides problems and makes it hard for others to help you. You might get used to meaningless variable names, but people reading your code won't. Use names that are real words, that say something other than "I'm too careless to tell you what this variable is really for". Use consistent indentation and clean layout. Write nice code and your world will be more comfortable.
>
> zguide
