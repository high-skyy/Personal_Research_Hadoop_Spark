# Zookeeper 
> A Distributed Coordination Service for Distributed Applications

Zookeeper is a distributed, open-source coordination service for distributed applications


It exposes a simple set of primitives(기초 요소) that distributed applications can build(컴파일 된 코드를 실제 실행할 수 있는 상태로 만드는 일 / 전처리 + 컴파일 + 패키징 + 테스팅 + 배포)
upon to implement higher level services for synchronization, configuration(Components are arranged to make up the computer system) maintenance, groups and naming
> 분산된 app들을 위한 기본적인 요소들의 set로 higher level service를 가능하게 동기화(연결) 기본적인 세팅을 가능하게 해준다.

Coordination services are notoriously hard to get right.
Thye are expecially prone to errors such as race conditions and deadlock.
The motivation behind Zookeeper is to relieve distributed applications the responsibility of implementing coordination services from scratch.
> Coordination servic의 경우는 race condition이나 deadlock등에 취약하다. zookeeper는 이것을 해결하기 위해 만들었음

## 용어
- Session : temporary and interactive information interchange between two or more computing devices.

## Design goals
### Simple
Zookeeper allows distributed processes to coordinate with each other through a shared hierarchical namespace which is organized similarly to a standard file system.
The namespace consists of data registers - called znodes, in ZooKeeper parlance(말투) - and these are similar to files and directories.
> 주키퍼는 process들이 공유된 계층화 namespace (일반적인 file system이랑 비슷함)를 통해 서로 coordinate를 가능하게 한다.

Zookeeper data is kept in-memory, which means ZooKeeper can achieve high throughput and low latency numbers
The performance aspects of ZooKeeper means it can be used in large, distributed systems.
Ther reliability aspects keep it from being a single point of failure.
The strict ordering means that sophisticated synchronization primitives can be implemented at the client.
> strict order가 있기 때문에 client가 정교한 synchronization 요소들을 구현할 수 있다.

### Replicated
Like the distributed processes it coordinates, Zookeeper itself is intended to be replicated over a set of hosts called an ensemble.
> 분산된 process들 처럼 zookeeper 자체가 host여러 명에게 동일하게 복사가된다. -> enseble이라고 한다.
![zookeeper_1](https://user-images.githubusercontent.com/105041834/193509197-7584789e-7f45-4672-807f-d15dd4233a12.JPG)

The servers that make up the ZooKeeper service must all know about each other.
They maintain an in-memory image of state, along with a transaction logs and snapshots in a persistent store.
> 주키퍼의 service를 구현하는 모든 server들은 서로에 대해서 알 고 있어야 한다. -> in-memory image, transaction logs, snapshots를 통해 이를 구현하는 듯 하다. (메모리가 많이 들지 않을까? 여러 컴퓨터를 사용하는 분산 시스템이라 괜찮은 것 같다.)

Clients connect to a single ZooKeeper server.
The client maintains a TCP connection through which it sends requests, gets responses, get watch events, and sends heart beats.
> Client랑 TCP connection을 통해 정보 전달 등 통신에 대한 기본적인 것들을 한다.

If the TCP connections to the server breaks, the client will connect to a different server

### Ordered
ZooKeeper stamps each update with a number that reflects the order of all Zookeeper transactions.
> **매우 중요** Zookeeper는 일반적으로 모든 업데이트에 대해서 번호를 부과한다. -> 이 번호는 ZooKeeper의 transaction의 모든 순서를 보여준다. (디버깅할 때 매우 필요할 것 같다.)

Subsequent operations can use the order to implement higher-level abstractions, such as synchronization primitives

### fast
It is especially fast in "read-dominant" workloads.
ZooKeeper applications run on thousands of machines, and it performs the best where reads are more common than writes, at ratios of around 10:1
> Hadoop의 경우는 저장에 focus를 맞췄기 때문에 write보다는 read에 유리한데 Hadoop이랑 잘 어울리는 것 같다.

## Data model and the hierarchical namespace
The namspace provided by ZooKeeper is much like that of a standard file system.
A name is a sequence of path elements separated by a slash(/).
Every node in ZooKeeper's namespace is identified by a path

> **중요 한 듯** name은 path들의 순서들이 / 으로 분리된 형태를 띤다. 모든 노드들은 path로 구분된다.

![zookeeper_2](https://user-images.githubusercontent.com/105041834/193510369-2c6f158b-9e92-4c0f-910a-ee72fb9878d5.JPG)
G)

> Tree의 형태다. 파일을 검색하는 방법이랑 비슷하다 ex) /ZooKeeper/file1/....

## Nodes and ephemeral(일시적인) nodes
Unlike standard file systems, each node in a ZooKeeper namespace can have data associated with it as well as children.
It is like having a file-system that allows a file to also be directory.
> node는 본인과 연결된 정보도 있고 child도 가능하다. file + directory의 형태

ZooKeeper was designed to store coordination data: status information, configuration, location information, etc.
> 주키퍼는 현재 상태, configuration, location등을 저장한다. -> znode라고 불림

Znodes maintain a stat structure that includes version numbers for data changes, ACL changes, and timestamps, to allow cache validations and coordinated updates.
> Zone는 data의 변화 (Access control list) changes, time stamp등을 version number를 갖는 stat 구조체에 담는다.

Each time a znode's data changes, the version number increases.
The data stored at each znode in a namespace is read and written atomically.
> Read 까지 atomic 하다. lock을 거는 형태가 아닌 듯 하다.

Reads get all the data bytes associated with a znode and a write replaces all the data.
Each node has an Access Control List that restricts who can do what.

ZooKeeper also has the notion of 일시적인 nodes.
These znodes exists as long as the session that created the znode is active.
When the session ends the znode is deleted.

## Conditional updates and watches
ZooKeeper supports the concept of watches.
Clients can set a watch on a znode.
A watch will be triggered and removed when the znode changes.
When a watch is triggered, the client receives a packet saying that the znode has changed.
> 감시하는 기능을 제공한다. -> znode에 변경사항이 생기면 client에게 packet이 보내지며 알려준다.

If the connection between the client and one of the ZooKeeper servers is broken, the client will receive a local notification
> 만약 client와 ZooKeeper간의 연결이 망가지면 특별한 notification이 간다.

New in 3.6.0 : Clients can also set permanent, recursive watches on a znode that are not removed when triggered
and the trigger for changes on the registered znode as well as any children znodes recursively.
> 당연한 기능인데 왜 이제 넣었지? 과거에는 계속 watch를 달라는 명령을 내렸어야 했던 것 같다.

## Guarantees
- Sequential Consistency : 무조건 명령한 순서대로 update가 진행된다.
- Atomicity : update는 성공하거나 실패한다.
- Single System Image : A client will see the samve view of the service regardless of the server that it connects to Client는 설령 같은 세션의 다른 서버한테 장애 조치를 받더라도 과거의 view는 볼 수 없다.
- Reliablity
- Timeliness - The clients view of the system is guaranteed to be up-to-date within a certain time bound.

## Simple API
- create : creates a node at a location in the tree
- delete : deletes a node
- exists : tests if a node exists at a location
- get data : reads the data from a node
- set data : writes data to a node
- get children : retrieves a list of children of a node
- sync : waits for data to be propagated.

## Implementation
ZooKeeper Components shows the high-level components of the ZooKeeper service.
With the exception of the request processor, each of the servers that make up the ZooKeeper service replicates its own copy of each of the components.


![zookeeper_3](https://user-images.githubusercontent.com/105041834/193515110-11fa483d-f570-4d1c-b816-004567f0a3e8.JPG)

The replicated database is an in-memory database containing the entire data tree.
Updates are logged to disk for recoverability, and writes are serialized to disk before they are applied to the in-memory database.
> database 자체는 in-memory이고 전체 data tree를 가지고 있다. log data는 디스크에 저장. write의 경우는 disk에 저장된다.

Every ZooKeeper service services clients.
Clients connect to exactly one server to submit requests.
Read requests are serviced from the local replica of each server database.
Reqeusts that change the state of the service, write requests, are processed by an agreement protocol.
> Read의 경우는 복사본을 가지고 해결함.

As part of the agreement protocol all write requests from clients are forwarded to a single server, called the leader.
The rest of the ZooKeeper servers, called followers, receive message proposals from the leader and agree upon message delivery.
The messaging layer takes care of replacing leaders on failures and syncing followers with leaders.
> 모든 write으 경우는 leader에게 가고 leader를 따르는 follower들의 경우 message를 받고 동의를 하는 과정을 통해 failure와 sycing을 해결.

ZooKeeper uses a custom atomic messaging protocol.
Since the messaging layer is atomic,
ZooKeeper can guarantee that the local replicas never diverge.
When the leader receives a write request, it calculates what the state of system is when the write is to be applied and transforms this into a transaction that captures this new state.

> ZooKeeper의 messaging layer는 atomic하다. 따라서 local에 있는 복사본들은 서로 다르지 않게 된다.
> Leader가 write request를 받게 되면 write가 발생하는 현재 시스템의 상태를 계산하고 이를 transaction 으로 만들어서 new state를 만든다.

## Reference
- [Reference](https://jaemunbro.medium.com/zookeeper-%EC%A3%BC%ED%82%A4%ED%8D%BC%EC%9D%98-%EA%B8%B0%EB%B3%B8-%ED%8A%B9%EC%A7%95-7da2a51351c5#:~:text=%EC%A3%BC%ED%82%A4%ED%8D%BC%20%EB%8D%B0%EC%9D%B4%ED%84%B0%20%EB%AA%A8%EB%8D%B8,%ED%8A%B8%EB%A6%AC%20%ED%98%95%ED%83%9C%EB%A1%9C%20%EA%B4%80%EB%A6%AC%ED%95%9C%EB%8B%A4.&text=%EC%A3%BC%ED%82%A4%ED%8D%BC%EC%9D%98%20znode%20%EA%B2%BD%EB%A1%9C,%EC%A0%88%EB%8C%80%EA%B2%BD%EB%A1%9C%EB%A7%8C%20%EC%A7%80%EC%9B%90%ED%95%9C%EB%8B%A4.)
- [Reference](https://zookeeper.apache.org/doc/r3.1.2/zookeeperOver.html)