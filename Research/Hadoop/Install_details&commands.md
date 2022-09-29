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


## Hadoop Startup
> Hadoop cluster를 시작하기 위해서는 HDFS와 YARN cluster가 모두 필요하다.

```
# HDFS를 처음 실행 시 반드시 formatt 되어야 한다.
$ $HADOOP_HOME/bin/hdfs namenode -format

# HDFS NameNode 실행
$ $HADOOP_HOME/bin/hdfs --daemon start namenode

# HDFS DataNode 실행
$ $HADOOP_HOME/bin/hdfs --daemon start datanode

# 만약 /etc/hadoop/worders 과 ssh trusted access가 configured 되면 모든 HDFS의 프로세스를 아래 명령어로 실행 가능.
$ $HADOOP_HOME/sbin/start-dfs.sh

# YARN 실행 (지정된 ResourceManager)
$ $HADOOP_HOME/bin/yarn --daemon start resourcemanager

# Start NodeManager on each 지정된 host
$ $HADOOP_HOME/bin/yarn --daemon start nodemanager

# Start a standalone WebAppProxy server. Run on the WebAppProxy server as yarn. If multiple servers are used with load balancing it should be run on each of them
$ $HADOOP_HOME/bin/yarn --daemon start proxyserver

# /etc/hadoop/worders과 ssh trusted access is configured 아래와 같은 명령어로 한번에 실행 가능
$ $HADOOP_HOME/sbin/start-yarn.sh

# MapReduce JobHistory Server 시작
$ $HADOOP_HOME/bin/mapred --daemon start history server
```
- [Reference](https://hadoop.apache.org/docs/r3.3.4/hadoop-project-dist/hadoop-common/ClusterSetup.html)

## Hadoop Shutdown
```
$ $HADOOP_HOME/bin/hdfs --daemon stop namenode
$ $HADOOP_HOME/bin/hdfs --daemon stop datanode
$ $HADOOP_HOME/sbin/stop-dfs.sh
$ $HADOOP_HOME/bin/yarn --daemon stop resourcemanager
$ $HADOOP_HOME/bin/yarn stop proxyserver
$ $HADOOP_HOME/bin/mapred --daemon stop historyserver
```
- [Reference](https://hadoop.apache.org/docs/r3.3.4/hadoop-project-dist/hadoop-common/ClusterSetup.html)



## Reference
[Reference](https://hadoop.apache.org/docs/r3.1.1/hadoop-project-dist/hadoop-common/ClusterSetup.html)