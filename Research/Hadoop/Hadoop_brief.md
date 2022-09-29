# Hadoop
> HDFS(하둡 분산 파일 시스템) 하둡 환경에서 분산 파일 시스템 기능을 담당하는 하둡의 주요 모듈  

HDFS + MapReduce

## Mode 3가지
### HDFS 설치방식
- Stand alone(독립실행모드) : 기본 실행모드, 분산저장 안함, 코딩 가능
- Pseudo-distributed(가상분산모드) : 하나의 컴퓨터에 설치
- Fully-distributed(완전분산모드) : 여러 대의 컴퓨터에 설치

### Hadoop Pseudo-distributed mode
5개의 프로세스 : Name node, Secondary Namenode, Data node, Job tracker, Tast tracker
- hadoop-env.sh : 환경변수 설정
- core-site.xml : HDFS와 MapReduce에서 공통적으로 사용할 환경정보 설정
- hdfs-site.xml : HDFS에서 사용할 환경정보 설정
- mapred-site.xml : MapReduce에서 사용할 환경정보 설정

### Hadoop Fully-distributed mode
#### Workers file
> personal directory : ~/hadoop/hadoop-3.3.4/etc/hadoop  
- slave로써 사용할 호스트명을 입력
```
$ vim workers           # List all worker hostnames or IP addresses in your
ex)
#localhost              # localhost 주석 처리
rmnode1                 # stand-by name node
datanode1
datanode2
```

### Hadoop Cluster
#### Concept
하둡 클러스터란 네트워크로 서로 연결된 일련의 컴퓨터(컴퓨터 = node)를 말합니다.  
이렇게 한데 모아서 빅데이터 세트에서 이런 종류의 병렬 연산을 수행하도록 한 것입니다.
> 병렬 컴퓨팅이다. 엄청나게 큰 빅 데이터를 분해해서 각각에 대해 연산을 해서 효율적으로 빅데이터를 처리하는 과정

하둡 클러스터는 여러 컴퓨터 클러스트와는 달리 대량의 구조적, 비구조적 데이터를 분산형 컴퓨팅 환경에 저장하고 분석하는 데 특화되어 있습니다.  
하둡 클러스터는 서로 연결된 마스터, 슬레이브 노드 네트워크로 구성되어 있습니다.  
(노드는 고가용성, 저가 상용 하드웨어를 활용합니다.)  
선형적으로 확장하여 볼륨 수요에 따라 신속하게 노드를 더하거나 뺄 수 있다는 점 때문에 크기가 무척 다양한 데이터 세트를 다루는 빅데이터 분석 작업에 적합합니다.  
> 가성비 컴퓨터로 마스터와 여러 대의 슬레이브 구조이고 빅 데이터의 크기에 따라 쉽게 슬레이브들을 추가하고 제거가 가능하다는 말

### Hadoop Cluster Architecture
  
시스템 전체에 걸쳐 다양한 작업을 오케스트레이션, 실행하는 여러 마스터 노드와 작업자 노드로 구성된 네트워크로 이루어져 있습니다.  
마스터 노드는 보통 (NameNode, Secondary NameNode 와 JobTracker)등 고품질 하드웨어를 활용하며, 각각이 별도의 시스템에서 실행됩니다.  
작업자 노드는 가상머신으로 구성되며 상용 하드웨어에서 DataNode와 TaskTraker를 둘 다 실행하고 마스터 노드의 지시에 따라 실제로 작업을 저장하고 처리하는 실무를 담당합니다.  
시스템을 이루는 마지막 부분을 클라이언트 노드라고 하는데, 이 노드는 데이터를 로드하고 결과를 가져오는 역할을 담당합니다.
- 마스터 노드는 MapReduce를 사용해 데이터에서 병렬식 연산을 실행하는 등 데이터를 HDFS에 저장하고 주요 작업을 감독합니다.
- 작업자 노드는 하둡 클러스터 내 대부분의 가상 머신으로 구성되어 데이터를 저장하고 연산을 수행하는 작업을 담당합니다. 각각의 작업자 노드는 DataNode와 TaskTracker라는 서비스를 실행하는데, 이는 마스터 노드에서 지침을 받는 데 쓰입니다.
- 클라이언트 노드는 데이터를 클러스터에 노드하는 역할을 맡습니다. 클라이언트 노드는 우선 MapReduce 작업을 제출하여 데이터를 어떻게 처리해야 하는지 설명하고, 그런 다음 처리가 끝나면 결과를 가져옵니다.
#### 장점
- 노드의 손 쉬운 추가가 가능해 처리량 증가 시킬 수 있고 처리 속도 일정하게 유지 가능
- 하둡 클러스터는 분산형 파일 시스템 전체에 걸쳐 데이터 세트를 복제하여 데이터 손실과 클러스터 오류가 발생해도 복원력을 확보합니다.
- 하둡 클러스터를 이용하면 여러 가지 다양한 소스 시스템과 데이터 형식에서 얻은 데이터를 통합하여 활용할 수 있다.

#### 문제점
- 하둡은 대량의 작은 파일 (하둡 블록 크기인 128MB나 기본값인 256MB보다 작은 것)을 다룰 때 특히 고전합니다.
- 처리 오버헤드 부담 : 하둡이 메모리 내 처리를 할 수 없고 디스크를 통해 데이터를 읽고 쓰기 때문에 Read, Write 작업이 갑작스레 증가할 수 있다.
- 배치 처리만 지원됨 : 수집과 저장을 모두 마친 후에야 처리를 시작할 수 있다. 짧은 레이턴시로 실시간 처리를 할 수 없다는 뜻
- 반복 처리 : 하둡의 데이터 흐름 구조는 순차적인 단계로 설정되어 있으므로 반복 처리하거나 ML에 사용하기는 불가능합니다.



## Reference
- [Reference](https://goudacheese.gitlab.io/post/2018-02-24-hadoop_wordcount_example/)
- [Reference](https://www.databricks.com/kr/glossary/hadoop-cluster#:~:text=%ED%95%98%EB%91%A1%20%ED%81%B4%EB%9F%AC%EC%8A%A4%ED%84%B0%EB%8A%94%20%EB%B6%84%EC%82%B0%ED%98%95,%ED%86%B5%ED%95%A9%ED%95%98%EC%97%AC%20%ED%99%9C%EC%9A%A9%ED%95%A0%20%EC%88%98%20%EC%9E%88%EC%8A%B5%EB%8B%88%EB%8B%A4.)
