labels: Blog
        Tornado
        Django
created: 2015-07-04T14:07
place: Kyiv, Ukraine
comments: true

# Django or Tornado?

It depends on ...

## Project size

Django is MVC(MTV) framework, while Tornado is just basics need to build a service (includes controller, simple templates processing engine and no ORM by default). Django has strict well described project structure, while, working with Tornado, developers invents their own.
For bigger projects Django is better choice because of to support it and add new features is easier.

## Testing

Django has its tests runner that makes writing and running tests smooth, especially if You use Django orm.
Testing asynchronous code in Tornado is a bit more complicated compared to ordinary synchronous code.
Be ready that You will need some extra effort to cower code with tests if You choose Tornado.

## Project growth

When project grow we may need more developers to support it, find developer who already worked with Django is easier compared to Tornado. Although Tornado is easy to understand, new team member will need some time to fill comfortable with asynchronous code and new project structure.
Django uses years proven structure allows to make project development easier.

## Technology stack

Django has much bigger community compared to Tornado. As result, we have a great amount of ready to use solutions, great documentation, a lot of resources ready to help with problems appears.
Tornado works great when code works asynchronously, but there are a big chance that library You want to use doesn't work asynchronously, so You'll need to search for alternatives or patch the library or write Your own. So, if You going to use some specific library, check that it has version compatible with Tornado (some code works fast enough and don't need to be runned asynchronously, for example: redis, datetime, etc.).

## Performance

Tornado works faster and requires less resources (if You use it properly).
Although, Django close to it (if gunicorn uses).

## Summary

If project is small, and we can make code works asynchronously - choose Tornado.
If project is big (You need more than month to rewrite it): split it into microservices (see [Building Microservices](http://www.amazon.com/Building-Microservices-Sam-Newman-ebook/dp/B00T3N7XB4/) book by Sam Newman) and select language/framework for each microservices that best suit it.

If time is valuable: choose Django.
