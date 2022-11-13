# Join Strategies 

## Broadcast Hash Join
- Hash join
  - Performed by first creating a Hash Table based on join_key of smaller relation and then looping over larger relation to match the hashed join_key values.
  - (only supported for '=' join)
In broadcast hash join, copy of one of the join relations are being sent to all the worker nodes and it shaves shuffling cost.
This is useful when you are joining a large relation with a smaller one.
It is also known as map-side join.

Spark deploys this join strategy when the size of one of the join relations is less than the threshold values.
The spark property which defines this threshold is spark.sql.autoBroadcastJoinThreshold(configurable)

Broadcast relations are shared amon executors using the BitTorrent protocol.
It is a peer to peer protocol in which block of files can be shared by peers amongst each other.
Hence, they don't need to rely on a single node.

- Feature
  - Broadcasted relation should fit completely into the memory of each executor as well as the driver. In Driver, because driver will start the data transfer.
  - Only supported for "=" join
  - Supported for all join types(innter, left, right) except full outer joins.
  - When the broadcast size is small, it is usually faster than other join strategies.
  - Copy of relation is broadcasted over the network. Therefore, being a network-intensive operation could cause out of memory errors or performance issues when broadcast size is big
    - For instance, when explicitly specified to use broadcast join/changes in the default threshold.
  - You can't make changes to the broadcasted relation, after broadcast.
    - Even if you do, they won't be available to the worker nodes (because the copy is already shipped)

### Shuffle hash join
Shuffle Hash Join involves moving data with the same value of join key in the same executor node followed by hash Join.
Using the join condition as output key, data is shuffled amongst executor nodes and in the last step, data is combined using Hash Join
as we know data of the same key will be present in the same executor.
- Features
  - Only supported for '=' join
  - The join keys don't need to be sortable
  - Supported for all join types except full outer joins
  - Involves both shuffling and hashing. Maintaining a hash table requires memory and computation.

### Shuffle sort-merge join
Shuffle sort-merge join involves, shuffling of data to get the same join_key with the same worker, and then performing sort-merge join operation at the partition level in the worker nodes.
- Features
  - Only supported for '=' join
  - The join keys need to be sortable
  - Supported for all join types

### Broadcast nested loop join
Generally, a fallback option when no other join type can be applied.
Spark handles this using BroadcastNestedLoopJoinExec operator that broadcasts the appropriate side of the query, so you can think that at least some chunk of results will be broadcasted to improve performance.
- Features
  - Supports both '=' and non-equi-joins
  - Supports all the join types.

### How spark selects join strategy
- If it is an '=' join
  - Broadcast Hint : Pick **broadcast hash join** if the join type is supported.
  - Sort merge Hint : Pick **sort-merge join** if join keys are sortable.
  - shuffle hash hint: Pick **shuffle hash join** if join type is supported.
  - shuffle replicate NL hint : Pick **cartesian product** if join type is inner like.
...

### Shuffling
#### What is shuffling?
Apache Spark processes queries by distributing data over multiple nodes and calculating the values separately on every node.
However, occasionally the nodes need to exchange the data.
After all, that's the purpose of Spark - processing data that doesn't fit on a single machine.
**Shuffling is the process of exchanging data between partitions.**
As a result, data rows can move between nodes when their source partition and the target partition reside on a different machine.
Spark doesn't move data between nodes randomly.
Shuffling is a time-consuming operation, so it happens only when there is no other option

#### When do we need shuffling?
When you explicitly request data repartitioning (using the repartition functions), when you join DataFrames or group data by a column value.
We can control the number of buckets using the **spark.sql.shuffle.partitions.** parameter.


## Reference
- [Reference](https://towardsdatascience.com/strategies-of-spark-join-c0e7b4572bcf)
- [Reference]