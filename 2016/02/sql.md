labels: Databases
        Blog
created: 2016-02-07T19:01
modified: 2016-02-21T12:39
place: New York, USA
comments: true

# SQL

[TOC]

SQL (**S**tructured **Q**uery **L**anguage) is a declarative programming language.
Pronunciation: ```/ˈɛs kjuː ˈɛl/``` (**an** SQL query).

## Database I use in examples

```bash
psql template1
template1=# CREATE USER test WITH PASSWORD 'test';
template1=# CREATE DATABASE test;
template1=# GRANT ALL PRIVILEGES ON DATABASE test TO test;
template1=# \q
psql -d test
```

## Practice

### GROUP BY and aggregate

```sql
SELECT anime.title, COUNT(anime_genre.*) as genre_count FROM anime LEFT JOIN anime_genre USING (anime_key) GROUP BY anime.anime_key;
```

```
anime        | genre_count
Kill La Kill | 2
```

### DISTINCT

Use it carefully, may cause performance problems on large data sets.

### Trees (hierarchical data)

The most obvious solution is to use parent_key field (adjacency list). The solution has its benefits:

- simple
- easy to modify (copy/move tree leaves)

Drawbacks:

- leaf remove is complex (needs to find and remove all leaves in the subtree, ```ON DELETE CASCADE``` solves the problem)

If You need to know how many children has the leave, how many descendants has the tree, etc., in most cases better just to use counters instead of query all the tree each time.

But the simple parent_key solution fails if you need to select all descendants (for instance: get full replies tree).

Exception is two level tree:
```sql
SELECT FROM nodes as n1 LEFT OUTER JOIN nodes as n2 ON n2.parent_id = n1.node_id;
```

There are alternative solutions:

- ```PostgreSQL>=8.4``` supports recursive queries
- Path enumeration technique (drawbacks: no referral integrity)
- Nested sets (drawbacks: hard to insert/delete, complex, no referral integrity)
- Closure table (benefits: allow node to belong to multiple trees, drawback: requires additional table)

### PRIMARY KEY

PRIMARY KEY is a constraint.

PRIMARY KEY needs to:

- Prevent a table from containing duplicate rows (as it creates ```UNIQUE INDEX```)
- Support foreign key reference

How to declare:
```sql
CREATE TABLE artwork (
    artwork_id INTEGER PRIMARY KEY
);

/* or */

CREATE TABLE artwork (
    artwork_id INTEGER,
    PRIMARY KEY (artwork_id)
);

/* or */

CREATE TABLE artwork (
    artwork_id INTEGER
);
ALTER TABLE artwork ADD PRIMARY KEY (artwork_id);
```

Result is the same:
```bash
test=# \d+ artwork
                         Table "public.artwork"
   Column   |  Type   | Modifiers | Storage | Stats target | Description
------------+---------+-----------+---------+--------------+-------------
 artwork_id | integer | not null  | plain   |              |
Indexes:
    "artwork_pkey" PRIMARY KEY, btree (artwork_id)
```

#### PRIMARY KEY name

A good practice is to use next pattern:
```
{table name}_id
```

Fields references the table must have the same name, it allows to use ```JOIN USING``` syntax:
```sql
SELECT artwork.title, author.name FROM artwork JOIN author USING (author_id);

/* instead */

SELECT artwork.title, author.name FROM artwork JOIN author ON author.author_id = artwork.author_id;
```

```artwork.artwork_id``` vs ```artwork.id```: ```artwork_id``` is more clear.

#### PRIMARY KEY value

There are primary key value types:

- autoincrement field
- natural id
- guid (**G**lobally **U**nique **ID**entifier)
- compound (aka composite) primary key

Autoincrement and guid fields known as pseudokeys or surrogate keys.

Most databases provide a mechanism to generate unique integer integer values serially, outside the scope of transaction isolation.

Autoincrement field example (PG):
```sql
CREATE TABLE items (
    item_id SERIAL PRIMARY KEY,
    title VARCHAR(255)
);
INSERT INTO items (title) VALUES ('item1');
INSERT INTO items (title) VALUES ('item2');
SELECT * FROM items;
```

```
 item_id | title
---------+-------
       1 | item1
       2 | item2
```

Natural id, if it is short and unique, usually the best solution for primary key. For example: phone numbers, usernames, etc.

GUID (uuid4 usually) is solution for distributed (horizontally) databases.

Compound key is a good solution for intersection table (there are a lot of cases where it may be used).

### NULL and the third state

Sometimes I hear that the third state is bad, only True and False must be allowed. I am not agree with it, unknown is natural third state. Sometimes we not sure about something, and there is no right answer except "I don't know".

NULL in SQL is the best implementation of unknown I ever seen:
```sql
DO language plpgsql $$
BEGIN
    RAISE NOTICE 'NULL OR TRUE = %', NULL OR TRUE;
    RAISE NOTICE 'NULL AND TRUE = %', NULL AND TRUE;
    RAISE NOTICE 'NULL OR NULL = %', NULL OR NULL;
    RAISE NOTICE 'NULL AND NULL = %', NULL AND NULL;
    RAISE NOTICE 'NULL + 1 = %', NULL + 1;
END
$$;
```

```
NOTICE:  NULL OR TRUE = t
NOTICE:  NULL AND TRUE = <NULL>
NOTICE:  NULL OR NULL = <NULL>
NOTICE:  NULL AND NULL = <NULL>
NOTICE:  NULL + 1 = <NULL>
```

In SQL NONE plays important role: allows to show that there are no value was assigned or no reference exists.

Check field value is NULL:
```sql
SELECT title FROM artwork WHERE autor_id IS NULL;
```

#### COALESCE

The function returns its first not-null argument.

### FOREIGN KEY

```FOREIGN KEY``` if a "key" to consistency.

How to declare:
```sql
CREATE TABLE artwork (
    artwork_id SERIAL PRIMARY KEY,
    author_id INTEGER REFERENCES author
)

/* or */

CREATE TABLE artwork (
    artwork_id SERIAL PRIMARY KEY,
    author_id INTEGER,
    FOREIGN KEY (author_id) REFERENCES author
)

/* or */

CREATE TABLE artwork (
    artwork_id SERIAL PRIMARY KEY,
    author_id INTEGER
)

ALTER TABLE artwork ADD CONSTRAINT artwork_author_id_fk FOREIGN KEY (author_id) REFERENCES author (author_id);
```

#### CASCADE UPDATE/DELETE

Allows to update or delete the parent row and lets the database takes care of any child rows that reference it.

```sql
CREATE TABLE artwork (
    artwork_id SERIAL PRIMARY KEY,
    author_id INTEGER,
    FOREIGN KEY (author_id) REFERENCES author ON UPDATE CASCADE ON DELETE SET DEFAULT
)
```

#### CSV/JSON/etc. or FOREIGN KEY?

Storing lists in a text field is a bad practice:

- We are limited in number of items can be placed into text field (mostly because of performance degradation)
- Foreign Key helps us to keep data consistency on database layer
- Additional validation, encoding/decoding logic may be required on the client side
- Unable to use joins and ```IN``` statement (must use ```LIKE``` or regexp)
- No chance to use the field as part of compound index
- We can't use count (and other aggregation functions) to get number of value usages
- Updates are much easier if you use Foreign Key

About regexp:
> Some people, when confronted with a problem, think, "I know, I'll use regular expressions." Now they have two problems.
> Jamie Zawinski

If you are concerned about performance:

- Joins must work fast enough if number of possible values is small (hundreds and even thousands)
- Use caching to speedup your app
- Remember about YAGNI, caching or demoralisation may not worth time spent on their implementation (do it only if you have evidence that it will improve performance drastically)

Example of Foreign Key constrain usage:
```sql
CREATE TABLE anime (
    anime_key CHAR(255) PRIMARY KEY,
    title CHAR(255) NOT NULL
);
CREATE TABLE genre (
    genre_key CHAR(255) PRIMARY KEY,
    title CHAR(255) NOT NULL
);
CREATE TABLE anime_genre (
    anime_key CHAR(255) REFERENCES anime,
    genre_key CHAR(255) REFERENCES genre,
    PRIMARY KEY (anime_key, genre_key)
);
INSERT INTO anime (anime_key, title) VALUES ('kill-la-kill', 'Kill La Kill');
INSERT INTO genre (genre_key, title) VALUES ('action', 'Action');
INSERT INTO genre (genre_key, title) VALUES ('comedy', 'Comedy');
INSERT INTO anime_genre (anime_key, genre_key) VALUES ('kill-la-kill', 'action');
INSERT INTO anime_genre (anime_key, genre_key) VALUES ('kill-la-kill', 'comedy');
SELECT genre.title FROM anime_genre LEFT JOIN genre USING (genre_key) WHERE anime_genre.anime_key = 'kill-la-kill';
```

```anime_genre``` is an intersection table.

Invalid data example:
```bash
INSERT INTO anime_genre (anime_key, genre_key) VALUES ('unknown-anime', 'comedy');
ERROR:  insert or update on table "anime_genre" violates foreign key constraint "anime_genre_anime_key_fkey"
DETAIL:  Key (anime_key)=(unknown-anime) is not present in table "anime".
```

### DEFAULT

Be careful when alter existing table with great number of rows, it locks database.

### UNION

Query results can be combined with ```UNION``` only if their columns are the same in number and type (provide NULL placeholders for columns that are unique to each table).

### Wildcard in SELECT

There are few thoughts why better to specify columns explicitly:

- when we ask for only fields used in the index: request must be executed faster (no need to query the main table)
- blob and text fields stored separately from main table (it stores only references to them), if don't ask for these fields, we decrease response time and network usage

### FLOAT VS NUMERIC (DECIMAL)

The advantage of NUMERIC (DECIMAL) are that they store rational numbers without rounding, as the FLOAT data types do.

Example:
```sql
CREATE TABLE numbers (
    number_id SERIAL PRIMARY KEY,
    value_float FLOAT,
    value_decimal NUMERIC(10,2)
);
INSERT INTO numbers (value_float, value_decimal) VALUES (1./3, 1./3);
INSERT INTO numbers (value_float, value_decimal) VALUES (1./3, 1./3);
INSERT INTO numbers (value_float, value_decimal) VALUES (1./3, 1./3);
SELECT SUM(value_float) * 1000 as sum_float, SUM(value_decimal) * 1000 as sum_decimal from numbers;
```

```
 sum_float | sum_decimal
-----------+-------------
      1000 |      990.00
```

## Vocabulary

### Antipattern

**Antipattern** is a technique that is intended to solve a problem but that often leads to other problems.

### Intersection table

Aka join table, many-to-may table or mapping table.

Intersection table has foreign keys referencing two tables (implements many-to-many relationship).

### Relational database

A [relational database](https://en.wikipedia.org/wiki/Relational_database) is a digital database whose organization is based on the relational model of data, as proposed by E.F. Codd in 1970.

Alternative technologies:

- object-oriented databases
- key/value stores
- column-oriented databases
- document-oriented databases
- hierarchical databases
- network databases
- map/reduce frameworks
- semantic data stores
- graph databases

### EAV design

Stands for **E**ntity-**A**ttribute-**V**alue. Aka open schema, schemaless or name-value pairs.

## Links

[SQL Antipatterns: Avoiding the Pitfalls of Database Programming](http://www.amazon.com/SQL-Antipatterns-Programming-Pragmatic-Programmers-ebook/dp/B00A376BB2/) by Bill Karwin
