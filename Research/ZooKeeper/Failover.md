# Failover
- Failover : Method of protecting computer systems from failure, in which standby equipment automatically takes over when the main system fails.
- split-brain : Indicates data or availability inconsistencies originating from the maintenance of two separate data sets.

## Components
### Zookeeper
ZooKeeper is a centralized service for maintaining configuration information, naming, providing distributed synchronization, and providing group services. All of these kinds of services are used in some form or another by distributed applications

> During the Hadoop Namenode failover process, ZK ensures the name node state is not getting diverged due to failover.

### Journal Node
In order for the Standby node to keep its state synchronized with the Active node, both nodes communicate with a group of separate daemons called “JournalNodes” (JNs).
> Standby node가 Active한 node와 syncronize가 되기 위해 Journalnodes라는 daemon을 사용한다.

#### JournalNode machines
- Machines on which you run the journalnodes.
- JN daemon is lightweight -> reasonably be collocated(used together) with other Hadoop daemons
- There must be at least 3 journalnode daemons, since edit log modifications must be written to a majority of JNs. (This will allow the system to tolerate the failure of a single machine)

### QJM(Quorum Journal Manager)
- Personal settings : ha.zookeeper.quorum
- Allows to share edit logs between the Active and standby nodes
- Using the QJM only one NameNode will ever be allowed to write to the JournalNodes
  - There is no potential for corrupting the file system metadata from split-brain scenario

![ZKFC FAilover](https://user-images.githubusercontent.com/105041834/194750283-f55485e3-749e-4f67-9943-6595e58a30da.jpg)

## ZKFailover Controller
The ZKFC is a new component which is a ZK client which also monitors and manages the state of the NameNode.
> Namenode 전용 간병인(?) 및 치료사

### Health monitoring
- The ZKFC pings its local NameNode on a periodic basis with a health-check command.
- NameNode responds prompt on time -> ZKFC considers the node healthy.
- Node is crashed, frozen, anyways unhealthy state -> health monitor will mark it as unhealthy.

### Zookeeper Session management
- The local NameNode is healthy -> ZKFC holds a session open in ZooKeeper.
- If the local NameNode is active, it also holds a special "lock" znode.
- Lockes uses ZooKeeper's support for "일시적인" nodes. -> session expires lock node automatically deleted.

### ZooKeeper-based election
- Local namenode is healthy and the ZKFC sees no other node currently holds the lock znode. -> it will itself try to aquire the lock.
- Succeeded -> won the election and is responsible for running a failover to make its local NameNode active.

![HDFS HA architecture](https://user-images.githubusercontent.com/105041834/194750812-d1948d31-8612-4bb3-bb62-ea4b24c8e2c9.jpg)

## Automatic Namenode failover process in Hadoop
In a typical HA cluster, two separate machines are configured as namenodes.
At any point in time, **exactly one** of the NameNodes is in an Active state.
And the other is in a Standby state.
The Active NameNode is responsible for all client operations in the cluster.
While the standby is simply acting as a slave, maintaining enough state to provide a fast failover if necessary.

> HA cluster의 경우는 오직 하나의 namenode 만 Active State가 되가 나머지는 Standby-state가 된다.
> Active 한 NN은 모든 client의 operation에 대해 책임을 지고 standby는 slave 처럼 행동 하며 빠른 failover를 가능하게 도와준다.

- Standby Namenode keep state synchronized with Active NameNode -> both nodes communicate with a group of separate daemons called JournalNodes
- When namespace modification performed by Active node -> logs a record to majority of these JNs.
  - Standby node reads these edits from the JNs and apply to its own namespace.
- Failover 발생시 Standby 는 모든 edit를 JournalNode로 부터 읽었는 지 확인을 하고 Active state로 간다.
  - This ensures that the namespace state is fully synchronized before a failover occurs.

## 요약
- NameNode Daemon fail -> Failover controller Daemon takes action.
- Even if entire machine crashes, ZooKeeper server detects it and lock will be expired and other Standby name node will be elected as Active Name node.

## Reference
- [Reference](https://stackoverflow.com/questions/26038391/what-are-the-differences-zookeeper-journal-node-tasks-and-quorum-journal-manage)
- [Reference](https://stackoverflow.com/questions/33311585/how-does-hadoop-namenode-failover-process-works/33313804#33313804)