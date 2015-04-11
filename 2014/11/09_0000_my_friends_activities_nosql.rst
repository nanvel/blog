Select my friends activities, nosql way
=======================================

Related to: http://stackoverflow.com/questions/26820983/get-my-friends-activities-using-redis-redis-join-alternative

Goal: understand is it makes sense to use redis here or continue using postgres is a right choice.

The task
--------

We have two tables:
    - Activities (user_id, activity_id, timestamp)
    - Friends (user_id, friend_id)

We need to get paginated list of friends activities for specified user_id. In SQL it looks like:

.. code-block:: sql

    SELECT act.activity_id, act.timestamp from activities act
    JOIN friends fr ON fr.friend_id=act.user_id AND fr.user_id='{user_id}'
    WHERE act.timestamp < {last}
    ORDER BY act.timestamp DESC
    LIMIT {limit};

Let's try to use redis for this task. Simplified plan is next:
    - we fill set of user friends in redis database (``friends:{user_id}``)
    - and zset of user_ids sorted by last activity (``activities``)
    - and user activities sorted by timestamp (``activities:{user_id}``)
    - interstore ``test:activities`` and ``test:friends:{user_id}`` -> friends
    - ``tmp:{user_id} = []``
    - for friend_id, timestamp in friends:
    - zunionstore ``tmp:{user_id}`` and ``activities:{friend_id}`` -> ``tmp:{user_id}``
    - if len(zrzngebyscore ``tmp:{user_id}`` timestamp, last) >= limit: break
    - endfor
    - return zrange ``tmp:{user_id}``, 0, limit
    - del ``tmp:{user_id}``

To do all this things on the redis side I wrote lua script:

.. code-block:: python

    def search(self, user, last, limit):
        SCRIPT = """
        redis.call("ZINTERSTORE", "test:tmp:" .. ARGV[1], 2, "test:last_user_activity", "test:friends:" .. ARGV[1], "AGGREGATE", "MAX")
        local users = redis.call("ZREVRANGE", "test:tmp:" .. ARGV[1], 0, -1, "WITHSCORES")
        if users == nil then
            return {}
        end
        redis.call("DEL", "test:tmp:" .. ARGV[1])
        local counter = 0
        local lastval = users[1]
        for k, v in pairs(users) do
            if (counter % 2 == 0) then
                lastval = v
            else
                redis.call("ZUNIONSTORE", "test:tmp:" .. ARGV[1], 2, "test:tmp:" .. ARGV[1], "test:user_activities:" .. lastval, "AGGREGATE", "MAX")
                redis.call("ZREMRANGEBYSCORE", "test:tmp:" .. ARGV[1], ARGV[2], ARGV[3])
                if redis.call("ZCOUNT", "test:tmp:" .. ARGV[1], v, ARGV[2]) >= tonumber(ARGV[4]) then break end
            end
            counter = counter + 1
        end
        local users = redis.call("ZREVRANGE", "test:tmp:" .. ARGV[1], 0, ARGV[4] - 1)
        redis.call("DEL", "test:tmp:" .. ARGV[1])
        return users
        """
        return self.conn.eval(SCRIPT, 0, user, last, get_timestamp(), limit)

Full script and it's output see on gist: https://gist.github.com/nanvel/8725b9c71c0040b0472b

Briefly about results
---------------------

Redis vs Postgresql, both were running on my laptop.

Postgres tables and indexes:

.. code-block:: sql

    DROP TABLE IF EXISTS activities;
    DROP TABLE IF EXISTS friends;
    CREATE TABLE activities (
        id SERIAL,
        user_id VARCHAR(100),
        activity_id VARCHAR(100),
        timestamp BIGSERIAL
    );
    CREATE TABLE friends (
        id SERIAL,
        user_id VARCHAR(100),
        friend_id VARCHAR(100)
    );
    CREATE INDEX activities_user_id_index ON activities (user_id);
    CREATE INDEX activities_timestamp_index ON activities (timestamp);
    CREATE INDEX friends_user_id_index ON friends (user_id);
    CREATE INDEX friends_friend_id_index ON friends (friend_id);

Activities count: 30000

Friends count: 25000

My friends count: 15000

Activities per page: 10

Page 1: 0.161883 s for postgres vs 0.025598 s for redis.

Page 2: 0.203902 s for postgres vs 0.026051 s for redis.

Page 10: 0.149319 s for postgres vs 0.048609 s for redis.

How You solve problems similar to described above? Is redis good for this task?
Does graph database may solve the problem?

.. info::
    :tags: Database, NoSQL, Redis, Lua
    :place: Kyiv, Ukraine
