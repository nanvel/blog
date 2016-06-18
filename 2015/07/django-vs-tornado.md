labels: Blog
        Tornado
        Django
created: 2015-07-04T14:07
place: Kyiv, Ukraine
comments: true

# Django or Tornado?

It depends on ...

## Project size

Django is a MVC (MTV) framework, while Tornado is just a basics needs to build a service (includes controller, simple templates processing engine and no ORM by default). Django has a strict well described project structure, and working with Tornado developers must to invent their own.
For bigger projects Django is a better choice because of easier code maintenance.

## Testing

Django has its tests runner that makes writing and running tests smooth, especially if You use Django orm.
Testing asynchronous code in Tornado is a bit more complicated if to compare to ordinary synchronous code.
Be ready to spend some extra time on writing tests if You choose Tornado.

## Project growth

When project is growing, we may need to extend team in order to support it; finding a developer who has experience with Django is much easier comparing to Tornado. Although Tornado is easy to start with, a new team member will need some time to get feeling comfortable with asynchronous code and new project structure.
Django uses a project structure that is proven by years of usage and allows to make project development easier.

## Technology stack

Django has much bigger community comparing to Tornado. As a result, we have a lot of ready to use solutions, great documentation, huge knowledge database on StackOverflow and other resources.
Tornado works great when code runs asynchronously, but there is a big chance that library You want to use doesn't work asynchronously, so You'll need to search for alternatives or patch the library or write Your own.

## Performance

Tornado works faster and requires less resources (if You use it properly).

## Summary

If project is small, and we can make code works asynchronously - choose Tornado.
If project is big (You need more than month to rewrite it): split it into microservices (see [Building Microservices](http://www.amazon.com/Building-Microservices-Sam-Newman-ebook/dp/B00T3N7XB4/) book by Sam Newman) and select language/framework for each microservice that best suits it.

If a project is time driven: choose Django.
