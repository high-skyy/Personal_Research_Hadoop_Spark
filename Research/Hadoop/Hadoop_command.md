# Basic Instructions

## 하둡(hdfs)기본 사용법
시스템과의 상호작용은 hadoop 이라는 명령어를 통해서 합니다. 만약 터미널을 열고, 인자 없이 명령어를 실행하면 도움말이 나옵니다.
> 대부분 rmdir cat linux와 비슷한데 앞에 -만 붙여주면 된다.

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


## hadoop basic command

```
$ hdfs namenode -format         # datanode 초기화
$ start-all.sh                  # namenode, datanode, nodemanager, secondarynamenode, yarn daemon 실행
# 이거 대신에 start-dfs.sh 하고 start-yarn.sh 하는게 더 좋다?
$ hdfs dfsadmin -report         # 현재 상태에 대해서 알려줌
$ jps                           # type of command to check all the hadoop daemons
```

### 디렉토리 조회 및 생성
> hadoop fs는 hadoop을 포함한 여러 파일 시스템과 상호작용할 수 있는 일반적인 명령이며, hdfs dfs는 HDFS에만 해당하는 명령어이다.
```
$ hadoop fs -l /      # root 디렉터리를 조회한다
$ hadoop fs -ls /user   # 특정 디렉토리를 조회할 때 /user와 같은 디렉토리 명을 사용한다.
$ hdfs dfs -ls          # 해당 폴더에 디렉터리가 있는지 확인
$ hdfs dfs -mkdir /user/...         # 을 통해 새로운 디렉토리 생성
# hadoop file system을 다룰때에는 hdfs를 직접적으로 사용하자
```

### 파일 업로드
```
$ hadoop fs -put [파일이름] [hdfs에서의 파일위치]      # local에서 파일이 있는 디렉토리에 있는 상태에서 실행해야함
$ gunzip -c access_log.gz \ | hadoop fs -put [hdfs 상의 파일 위치]  # 압축 풀면서 한번에 저장
# 명령어 A | 명령어 B         를 할 경우 명령어 A를 실행한 뒤 명령어 B를 실행한다.

$ hadoop fs -get [HDFS 경로] [로컬 경로]      # hdfs에 있는 파일을 local로 옮기고 싶을 경우
$ hdfs dfs -copyFromLocal [로컬 파일 경로] [HDFS 경로]
```




## Reference
- [Reference](https://12bme.tistory.com/152#:~:text=%ED%95%98%EB%91%A1%20HDFS%20%EA%B8%B0%EB%B3%B8%20%EC%82%AC%EC%9A%A9%EB%B2%95,%EC%95%84%EB%9E%98%20%EB%AA%85%EB%A0%B9%EC%96%B4%EB%A5%BC%20%EC%8B%A4%ED%96%89%ED%95%A9%EB%8B%88%EB%8B%A4.&text=hadoop%20%EB%AA%85%EB%A0%B9%EC%96%B4%EB%8A%94%20%EC%97%AC%EB%9F%AC%EA%B0%9C%EC%9D%98%20%EC%84%9C%EB%B8%8C%20%EC%8B%9C%EC%8A%A4%ED%85%9C%EC%9C%BC%EB%A1%9C%20%EC%84%B8%EB%B6%84%ED%99%94%20%EB%90%98%EC%96%B4%EC%9E%88%EC%8A%B5%EB%8B%88%EB%8B%A4.)
- [Reference](https://hadoop.apache.org/docs/r3.3.4/hadoop-project-dist/hadoop-common/ClusterSetup.html)