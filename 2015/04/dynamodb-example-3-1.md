labels: Databases
        DynamoDB
created: 2015-04-18T10:56
place: Phuket, Thailand
comments: true

# DynamoDB in examples, Example 3.1: Does DynamoDB fits my requirements?

I'll start from explaining why I used DynamoDB for previous 3 examples:

1. User wallet
    - Very simple structure, only set/get operation required
    - Needs scaling with users amount increase
2. Unique page views
    - We may have a great amount of page views
    - Needs to scale (size and throughput) database with pages/users amount we have
3. Toys store orders
    - Toys store may have periods when it is much more popular then usual (Christmas, Saint Valentine's day, etc) and we will need more resources for this time, although for other time we will don't

When I'll better use DynamoDB:

- when load on my database may increase significantly and I know when it happens (flash sales, holidays, etc.)
- when I have significant amount of data and don't wan't to deal with servers/databases administration and want amazon does it for me

When better not use DynamoDB:

- if I have constant amount of data (list of product categories, list of cities, etc.)
- when load is unpredictable (You'll need to hold higher throughput than You really use)
