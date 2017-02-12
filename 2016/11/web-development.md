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