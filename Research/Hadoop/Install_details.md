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

- **personal settings**
  - fs.defaultFS : hdfs://mycluster
  - ha.zookeeper.quorum : namenode1 :2181, rmnode1:2181, datanode1: 2181

- fs.defaultFS
  - value : NameNode URI
  - hdfs://host:port/
  - The default path prefix used by the Hadoop FS client when none is given
    - 만약 Hadoop FS client에게 기본 default 주소가 주어지지 않으면 해당 주소를 사용한다.
  - Optionally, you may now configure the default path for Hadoop clients to use the new HA- enabled logical URI. If you used "mycluster" as the nameservice Id earlier, this will be the value of the authority portion of all of your HDFS paths.
    - Default path를 이제는 HA-enbabled logical URI로 사용이 가능하다.
> Datanode가 namenode의 주소를 받는데 여기를 본다 (using RPC) [Reference](https://community.cloudera.com/t5/Support-Questions/difference-between-fs-defaultFS-and-dfs-namenode-http/td-p/214958#:~:text=The%20fs.,create%20the%20distributed%20file%20system.)

## hdfs-site.xml
> 설정 순서가 중요치 않다.

- dfs.nameservices (nameservice ID)
  - **personal settings** : mycluster
  - The logical name for this nameservice
    - Choose a logical name for this nameservice, for example "mycluster", and use this logical name for the value of this config option The name you choose is arbitrary. It will be used both for configuration and as the authority component of absolute HDFS paths in the cluster
    - Logical 이름을 nameservice에게 붙인다. 나중에 configuration과 authority component of HDFS 절대 경로에 사용된다.

- dfs.ha.namenodes.mycluster(NameNode IDs)
  - **personal settings** : nn1,rn1
  - Unique identifiers for each NameNode in the nameservice
  - DataNode가 모든 NameNode를 결정하는데 사용된다.

- dfs.client.failover.proxy.provider.mycluster
  - **personal settings** : org.apache.hadoop.hdfs.server.namenode.ha.ConfiguredFailoverProxyProvider
  - The Java class that HDFS clients use to contact the Active Namenode
    - DFS Java class를 DFS Client에게 알려줌으로 써 현재 어떤 NameNode가 active하고 어떤 NameNode가 현재 Client의 요청을 받는지 알려준다.

- dfs.namenode.rpc-address.mycluster.nn1
  - **personal settings**: namenode1:8020
  - The fully-qualified RPC address for each NameNode to listen on
  - 이전에 정했던 NameNode의 ID들의 전체 주소와 IPC port를 정해준다. (실제 hostname과 rpc address)
- dfs.namenode.rpc-address.mycluster.rn1
  - **personal settings**: rmnode1:8020

- dfs.namenode.http-address.mycluster.nn1
  - **personal settings** : namenode1:9870
  - The fully-qualified HTTP addresses for each NameNode to listen on
  - NameNode의 HTTP server가 listen 할 address를 설정한다.
- dfs.namenode.http-address.mycluster.rn1
  - **personal settings** : rmnode1:9870

- dfs.namenode.shared.edits.dir
  - **personal settings** :qjournal://namenode1:8485;rmnode1:8485;datanode1:8485/mycluster
  - The location of the shared storage directory
  - This is where one configures the path to the remote shared edits directory which the Standby NameNodes use to stay up-to-date with all the file system changes the Active NameNode makes. You should only configure one of these directories. This directory should be mounted r/w on the NameNode machines. The value of this setting should be the absolute path to this directory on the NameNode machines
  - rmnode와 active한 datanode가 서로 공유하는 storage directory이다. update에 대해서 rmnode가 따라 올 수 있도록 한다.

- dfs.ha.automatic-failover.enabled
  - **personal settings** : true
- dfs.ha.fencing.methods
  - **personal settings** : shell(/bin/true)
  - 

- dfs.namenode.name.dir
  - /dfs/namenode
- dfs.datanode.name.dir
  - /dfs/datanode
- dfs.journalnode.edits.dir
  - /dfs/journalnode






- dfs.ha.fencing.ssh.private-key-files
  - /home/hadoop/.ssh/id_rsa

## namenode(web)
```
http://(namenode ip):9870
```

## 리소스 관리자
```
https://(namenode ip):8088
```


### Configuration
## Reference
[Reference](https://hadoop.apache.org/docs/r3.1.1/hadoop-project-dist/hadoop-common/ClusterSetup.html)
[Reference](https://hadoop.apache.org/docs/stable/hadoop-project-dist/hadoop-hdfs/HDFSHighAvailabilityWithNFS.html)
[Reference](https://www.edureka.co/community/1401/meaning-of-fs-defaultfs-property-in-core-site-xml-in-hadoop)