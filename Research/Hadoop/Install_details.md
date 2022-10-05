# Install_file_details 

## Configure file
> 각자의 소프트웨어에 대해 특정한 설정을 저장하는데 사용된다.
- Read-only default configuration(변경 불가인 기본 저장)
  - core-default.xml, hdfs-default.xml, yarn-default.xml and mapred-default.xml
- Site-specific configuration(변경 가능인 기본 설정)
  - etc/hadoop/core-site.xml, etc/hadoop/hdfs-site.xml, etc/hadoop/yarn-site.xml etc/hadoop/mapred-site.xml

Hadoop scripts 조절 가능 (bin/ ) directory of distribution에서  
-> etc/hadoop-env.sh 와 etc/hadoop/yarn-env.sh를 통해서 site-specific value set 시키자.

- HDFS daemons (NameNode, SecondaryNameNode, DataNode)
- Yarn daemons (ResourceManager, NodeManager, WebAppProxy)


## core-site.xml
> etc/hadoop/core-site.xml

- fs.defaultFS
  - **personal settings** : hdfs://mycluster
  - value : NameNode URI
  - hdfs://host:port/
  - The default path prefix used by the Hadoop FS client when none is given
    - 만약 Hadoop FS client에게 기본 default 주소가 주어지지 않으면 해당 주소를 사용한다.
  - Optionally, you may now configure the default path for Hadoop clients to use the new HA- enabled logical URI. If you used "mycluster" as the nameservice Id earlier, this will be the value of the authority portion of all of your HDFS paths.
    - Default path를 이제는 HA-enbabled logical URI로 사용이 가능하다.
> Datanode가 namenode의 주소를 받는데 여기를 본다 (using RPC) [Reference](https://community.cloudera.com/t5/Support-Questions/difference-between-fs-defaultFS-and-dfs-namenode-http/td-p/214958#:~:text=The%20fs.,create%20the%20distributed%20file%20system.)

- ha.zookeeper.quorum
  - **personal settings** : namenode1:2181,rmnode1:2181,datanode1:2181
  - This lists the host-port pairs running the ZooKeeper service

## hdfs-site.xml
> 설정 순서가 중요치 않다.

- dfs.client.failover.proxy.provider.mycluster
  - **personal settings** : org.apache.hadoop.hdfs.server.namenode.ha.ConfiguredFailoverProxyProvider
  - The Java class that HDFS clients use to contact the Active Namenode
    - DFS Java class를 DFS Client에게 알려줌으로 써 현재 어떤 NameNode가 active하고 어떤 NameNode가 현재 Client의 요청을 받는지 알려준다.
    
- dfs.namenode.name.dir
  - **personal settings** : /hadoopdata/dfs/namenode
  - Value
    - Path on the local filesystem where the NameNode stores the namespace and transactions logs persistently
  - Notes
    - If this is a comma-delimited list of directories then the name table is replicated in all of the directories, for redundancy

- dfs.datanode.name.dir
  - **personal settings** : /hadoopdata/dfs/datanode
  - Value
    - Comma seperated list of paths on the local filesystem of a DataNode where it should store its blocks
  - Notes
    - Comma-delimited list of directories -> data will be stored in all named directories

- dfs.journalnode.edits.dir
  - **personal settings** : /hadoopdata/dfs/journalnode
  - The path where the JournalNode daemon will store its local state (edits and other local state used by JournalNodes will be stored)
  - Redundancy for this data is provided by running multiple separate JournalNodes

- dfs.nameservices (nameservice ID)
  - **personal settings** : mycluster
  - The logical name for this nameservice
    - Choose a logical name for this nameservice, for example "mycluster", and use this logical name for the value of this config option The name you choose is arbitrary. It will be used both for configuration and as the authority component of absolute HDFS paths in the cluster
    - Logical 이름을 nameservice에게 붙인다. 나중에 configuration과 authority component of HDFS 절대 경로에 사용된다.

- dfs.ha.namenodes.mycluster(NameNode IDs)
  - **personal settings** : namenode1, rmnode1
  - Unique identifiers for each NameNode in the nameservice
  - DataNode가 모든 NameNode를 결정하는데 사용된다.

- dfs.namenode.rpc-address.mycluster.namenode1
  - **personal settings**: namenode1:8020
  - The fully-qualified RPC address for each NameNode to listen on
  - 이전에 정했던 NameNode의 ID들의 전체 주소와 IPC port를 정해준다. (실제 hostname과 rpc address)
- dfs.namenode.rpc-address.mycluster.rmnode1
  - **personal settings**: rmnode1:8020

- dfs.namenode.http-address.mycluster.namenode1
  - **personal settings** : namenode1:9870
  - The fully-qualified HTTP addresses for each NameNode to listen on
  - NameNode의 HTTP server가 listen 할 address를 설정한다.
- dfs.namenode.http-address.mycluster.rmnode1
  - **personal settings** : rmnode1:9870

- dfs.namenode.shared.edits.dir
  - **personal settings** :qjournal://namenode1:8485;rmnode1:8485;datanode1:8485/mycluster
  - The URI which identifies the group of JournalNodes where the NameNodes will write/read edits
  - This is where one configures the addresses of the JournalNodes which provide the shared edits storage, written to by the Active nameNode and read by the Standby NameNode to stay up-to-date with all the file system changes the Active NameNode makes
    - 공유하는 edit storage를 가지고 있는 Journal Node의 address (Active nameNode가 write Standby NameNode가 최신화)

- dfs.ha.automatic-failover.enabled
  - **personal settings** : true
- dfs.ha.fencing.methods
  - **personal settings** : sshfence
  - A list of scripts or Java classes which will be used to fence the Active NameNode during a failover
  - When using the Quorum Journal Manager, only one NameNode will ever be allowed to write to the JournalNodes, so there is no potential for corrupting the file.
  - sshfence : SSHes to the target node and uses fuser to kill the process listening on the service's TCP port. In order for this fencing option to work, it must be able to SSH to the target node without provicing a passphrase. Thus, one must also configure the below option
- dfs.ha.fencing.ssh.private-key-files
  - **personal settings** : /home/hadoop/.ssh/id_rsa

## yarn-site.xml
- yarn.nodemanager.aux-services
  - **personal settings** : mapreduce_shuffle
  - Shuffle service that needs to be set for Map Reduce applications

- yarn.nodemanager.aux-services.mapreduce_shuffle.class
  - **personal settings** : org.apache.hadoop.mapred.ShuffleHandler

- yarn.nodemanager.local-dirs
  - **personal settings** : /hadoopdata/yarn/system/nm-local-dir
  - Value
    - Comma-separated list of paths on the local filesystem where intermediate data is writeen

- yarn.resourcemanager.hostname
  - **personal settings** : rmnode1
  - ResourceManager host

- yarn.resourcemanager.address
  - **personal settings** : rmnode1:8032
  - (ResourceManager host : port) for clients to submit jobs.

- yarn.application.classpath

## 정리
- zookeeper-service
  - namenode1:2181,rmnode1:2181,datanode1:2181
- dfs.namenode.name.dir
  - /hadoopdata/dfs/namenode
- dfs.datanode.name.dir
  - /hadoopdata/dfs/datanode
- dfs.journalnode.edits.dir
  - /hadoopdata/dfs/journalnode
- dfs.namenode.rpc-address.mycluster.namenode1
  - namenode1:8020
- dfs.namenode.rpc-address.mycluster.rmnode1
  - rmnode1:8020
- dfs.namenode.http-address.mycluster.namenode1
  - namenode1:9870
- dfs.namenode.http-address.mycluster.rmnode1
  - rmnode1:9870
- dfs.namenode.shared.edits.dir
  - qjournal://namenode1:8485;rmnode1:8485;datanode1:8485/mycluster
- yarn.nodemanager.local-dirs
  - /hadoopdata/yarn/system/nm-local-dir
- yarn.resourcemanager.hostname
  - rmnode1
- yarn.resourcemanager.address
  - rmnode1:8032


## 리소스 관리자
```
https://(namenode ip):8088
```


### Configuration
## Reference
[Reference](https://hadoop.apache.org/docs/r3.1.1/hadoop-project-dist/hadoop-common/ClusterSetup.html)
[Reference](https://hadoop.apache.org/docs/stable/hadoop-project-dist/hadoop-hdfs/HDFSHighAvailabilityWithNFS.html)
[Reference](https://www.edureka.co/community/1401/meaning-of-fs-defaultfs-property-in-core-site-xml-in-hadoop)