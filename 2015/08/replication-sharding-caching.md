labels: Blog
        Databases
created: 2015-08-08T23:40
place: Kyiv, Ukraine

#Thoughts on replication, sharding and caching

## Replication

Pros:

- we have copies of data, backups is not required
- easy to scale with number of reads grow
- even if master node fails, the system may still operates
- in case of master/slave replication, we can switch one of our slaves to master mode

Cons:

- caching may be more efficient and fast
- with data grow we need to scale vertically i.e. we need more expensive hardware and we need it for every replica
- eventual consistency (data propagation from master to slaves takes some time)

## Sharding

Pros:

- allows to scale horizontally for reads/writes

Cons:

- data rebalancing is hard and may require downtime
- no data replication by default (chances to loose part of data)
- hard to execute complex queries

## Caching

We can cache writes as well as reads. For example: write data that changes frequently into memory and copy it to persistent storage with much low rate.

Pros:

- fast
- works best if we have part of data that much more popular than other and we can put it all into memory
- memory becoming cheaper

Cons:

- complex and error prone cache invalidation/synchronization logic
