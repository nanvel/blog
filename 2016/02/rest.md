labels: SoftwareDevelopment
        Blog
created: 2016-02-14T08:59
modified: 2016-03-26T21:15
place: New York, USA
comments: true

# RESTful API design conventions

[TOC]

## REST

**RE**presentational **S**tate **T**ransfer is the software architectural style of the World Wide Web.
The term representational state transfer was introduced and defined in 2000 by Roy Fielding in his doctoral dissertation at UC Irvine.

Goals:

- Performance
- Scalability
- Simplicity
- Modifiability
- Visibility
- Portability
- Reliability

## Semantic versioning

Pattern: ```major.minor.patch```.

Example:

```1.0.0``` - initial version.
```1.0.1``` - minor bug fixes, there are no new features was added and interface exactly the same as in the previous version.
```1.1.0``` - some new features was added, the interface were extended. The API is fully compatible with the previous version.
```2.0.0``` - there are changes in the API interface made it incompatible with the previous version.

Major version increment == backward incompatibility.
Minor version increment == extended but fully compatible.
Patch version increment == bug fixes.

See [Semantic Versioning 2.0.0](http://semver.org/) (authored by Tom Preston-Werner, inventor of Gravatars and cofounder of GitHub) for details.

## Semantic methods

Use ```POST``` to create an object.
Use ```PUT``` to modify an object.
Use ```DELETE``` to delete an object.
Use ```GET``` to retrieve data.
Use ```HEAD``` to check object exists.

Body for ```DELETE```, ```GET``` and ```HEAD``` must be empty because it does not supported by a lot of clients and proxies.
But it can be used, for instance, Elasticsearch api accepts body in ```GET``` requests, and it looks more semantic and easier than using ```POST``` or complex url params encoding.

## URL

URL must represent a path to the object we going to modify or retrieve.

For example:
```
/accounts/123
/store/123/products
/store/123/products/123
```

It may be useful for large applications to prefix URL with module name:
```
/mymodule/myobjects/objid
```

### Underscore, dash or CamelCase

There are a lot of ways to split words in an url making it more readable we can found on the Internet:
```
/products/myFavouriteProduct
/products/my_vavourite_product
/products/my-favourite-product
```

You can use even a colon as a splitter.
Using dash looks the best practice. You are allowed to use what you think is right, but mixing them is a bad decision.

## Request body format

HTML forms uses ```application/x-www-form-urlencoded``` (or ```multipart/form-data``` if contains binary data), a request body looks like:
```
parameter=value&also=another
```

Using Python we can encode data into this format using urllib:
```bash
>>> from urllib.parse import urlencode
>>> urlencode({'parameter': 'value', 'also': 'another'})
'parameter=value&also=another'
```

JSON format is also popular same for request body and response. Use proper content type:
```
Content-Type: 'application/json; charset=UTF-8'
```

## Response

If you use JSON format for response, **response must be an object**, not list. Object may be extended any time you need, you'll be able to add ```total```, ```next``` or other fields.
In case if you need to return a list of results, use a ```results``` node:
```json
{
   "results": [
      {
         "attr": 1
      },
      {
         "attr": 2
      }
   ]
}
```

### Status codes

```200``` - Success
```201``` - Created
```400``` - Error
```401``` - Unauthorized
```403``` - Forbidden
```404``` - Not found
```500``` - Unknown error

See more: [List of HTTP status codes](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes).

### Empty response

Empty response must be empty. Bad practice:
```json
{
   "success": true,
   "code": 0
}
```

Use status codes to show that transaction succeeded.

### Error response

May contains a ```message```, ```code```, ```errors``` and ```traceback``` nodes.

Example:
```json
{
   "message": "Error ....",
   "code": 10,
   "errors": [
      {
         "field": "email",
         "message": "Invalid email address."
      }
   ]
}
```

## Pagination

Don't mix offset and cursor pagination, better use cursor pagination everywhere.

## Vocabulary

### Semantic

Relating to meaning in language or logic.

## Links

[Representational state transfer](https://en.wikipedia.org/wiki/Representational_state_transfer)
[How to do stuff RESTful](http://restcookbook.com/) ([source](https://github.com/restcookbook/restcookbook))
