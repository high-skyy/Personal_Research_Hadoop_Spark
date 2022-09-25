# HDFS & MR


## Dataflow
![data flow](https://user-images.githubusercontent.com/105041834/190895957-24752832-3e5b-4bbf-a744-cd1673b050b1.jpg)  
[출처](https://opentutorials.org/course/2908/17055)  
1. APP가 HDFS 클라이언트에게 파일 저장을 요청하면, 
-> HDFS 클라이언트는 네임노드에게 파일 블록들이 저장될 경로 생성을 요청
-> name node는 해당 파일 경로가 존재하지 않으면 경로를 생성한 후, 다른 클라이언트가 해당 경로를 수정하지 못하도록 락을 검.
-> 그 후, 네임노드는 클라이언트에게 해당 파일 블록들을 저장할 데이터 노드의 목록을 반환
2. 클라이언트는 첫 번째 노드에게 데이터 전송 -> 두 번째 데이터 노드로 전송 -> 세번 째 data node로 전송 
3. ACK다 받아내면 블록 위치를 NameNode에게 알려주고 client에게도 알려준다.

## Read flow
![Read flow](https://user-images.githubusercontent.com/105041834/190896134-484f5338-ff01-4fc9-9afd-41e394550124.jpg)  
[출처](https://opentutorials.org/course/2908/17055)  
1. APP이 client에게 파일 읽기를 요청
2. client가 namenode에게 요청된 파일이 어떤 블록에 저장되어 있는지 정보를 요청
3. meta data를 통해 파일이 저장된 블록 리스트를 반환
4. client는 datanode에 접근하여 블록 조회 요청
5. data node는 클라이언트에게 요청된 블록을 전송
6. client는 App에게 데이터 전달

## Hadoop MapReduce

### 도식표
![map-reduce](https://user-images.githubusercontent.com/105041834/190896278-9a42f106-fd1a-4cec-afbb-8581a8117f88.jpg)  

### Brief explanation & current frameworks
Map-Reduce의 경우는 대량의 machine들이 data를 process 할 수 있도록 하는 processing framework이다.  
Hadoop 은 Map-Reduce를 이용해 Hadoop cluster에 분산되어 있는 데이터를 process한다.  
Data가 여러 노드에 있는 경우 program을 복사해서 data가 있는 곳에 복사를 해 주는 framework가 필요하다. (이게 map-reduce)
> Data-locality : Potentioal to move the computations closer to the actual data location on the machines.  

현재는 Spark가 굉장히 popular한 framework이다. (Map-Reduce는 요즘 인기 X)  
Map-Reduce framework 구성요소 : Driver code, Mapper(for transformation) and reducer (for aggregation)  
Driver code which is called job (for processing data)  
If we are using Java for processing we need to initiate this driver class with the job object  

- Brief Working of Mapper  
Mapper 는 dataset오 첫 번째로 interaction 하는 코드이다.  
> ex) 100 Data-Block이 있으면 100 Mapper program과 process과 machine들 위에서 parallel하게 작동한다. 

그리고 output으로 나온 intermediate output은 hdfs가 아닌 local disk에 저장이 된다.  
이 intermediate output은 reducer의 input으로 활용된다.  

- Brief working of reducer
Mapper의 output은 key-value pair로 reducer의 input으로 작용한다.  
Reducer로 가기 전에 shuffle과 sorting이 key-value에 의해서 작동한다.  
Reducer의 output이 이제 HDFS에 저장이 된다.

### map reduce system의 구성
![map reduce system 구성](https://user-images.githubusercontent.com/105041834/190896444-66b6230f-a8e0-4c86-950e-64fe51155265.jpg)  
[출처](https://opentutorials.org/course/2908/17055)

> Job : Client가 수행하려는 작업단위(입력데이터, 맵리듀스 프로그램, 설정 정보)

- 맵 리듀스 시스템 -> Client, JobTracker(NameNode), TaskTracker(Datanode)  
- Client : 분석하고자 하는 데이터를 Job의 형태로 JobTracker에게 전달
- JobTracker : Hadoop Cluster에 등록된 전체 job을 스케줄링하고 모니터링(프로세스 / 작업을 알맞는 tasktracker에서 할당합니다.) 실패 시 다른 TaskTracker에게 재할당 합니다.
- TaskTracker : DataNode에서 실행되는 데몬이고, 사용자고 설정한 map-reduce program을 실행하며  
JobTracker로부터 작업을 요청받고 요청받은 맵과 리듀스 개수만큼 맵 task와 reduce task를 생성.




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


## HDFS 기본 컨셉
![HDFS](https://user-images.githubusercontent.com/105041834/190892174-f9372133-884f-4bc6-9074-823eca90ed66.jpg)  
[출처](https://12bme.tistory.com/153?category=737765)

## HDFS Architecture
![Hadoop Architecture](https://user-images.githubusercontent.com/105041834/190895900-6f726c87-c0ac-4448-8b78-f3c8421fa917.jpg)  
[출처](https://opentutorials.org/course/2908/17055)


### HDFS의 file 저장 방식
- File은 block 단위로 분할됩니다. (block = 64MB or 128MB) (180 -> 64,64,64)
- 데이터가 로드 될 때 여러 machine에 분산되어 저장됩니다.
  - 같은 file의 다른 block들은 서로 다른 machine에 저장됨
  - 이를 통해 효율적인 mapreduce처리가 가능
- Block들은 여러 machine에 복제되어 Data node에 저장된다.
  - 기본 replication은 3개 (각 block은 서로 다른 3개의 machine에 저장되어 있다는 것을 의미)
- Name node라 불리는 master node는 어떤 block들이 file을 구성하고 있고, 어느 위치에 저장되어 있는지에 대한 정보를 meta data로 관리합니다.  
![HDFS_@](https://user-images.githubusercontent.com/105041834/190892414-dcd5a546-3ead-4d71-b20a-cf9fe73df9ab.jpg)  
[출처](https://12bme.tistory.com/153?category=737765)  

File이 64MB 또는 128MB의 block으로 분할 될 때, file이 block의 크기보다 작은 경우에는 block 크기 전체를 사용하지 않게 됩니다.  
Block들은 Hadoop configuration에 설정된 디렉터리를 통해 저장됩니다.  
NameNode의 metadata를 사용하지 않으면, HDFS에 접근할 수 있는 방법이 존재하지 않습니다.  

- 클라이언트 어플리케이션이 file에 접근하는 경우 : 
NameNode와 통신하여 file을 구성하고 있는 block들의 정보와 DataNode의 Block의 위치 정보를 제공받습니다.  
이후 데이터를 읽기 위해 DataNode와 직접 통신을 하게 됩니다. **결과적으로 읽기 작업만 일어나는 NameNode는 bottleneck이 되지 않습니다.**

### HDFS 접근 방법
HDFS 접근하는 방법에는 Shell 커맨드라인을 사용하거나 Java API 그리고 Ecosystem 프로젝트를 사용하는 방법이 있습니다.  
대표적으로는 Flume(network source로 부터 데이터 수집), Sqoop(HDFS와 RDBMS 사이의 데이터 전송), Hue(Web 기반의 interface UI로 browse, upload, download, file view 등의 기능) 이 있다.

### HDFS 파일 저장과 조회
![HDFS_예씨](https://user-images.githubusercontent.com/105041834/190892740-87a5ecb9-d326-42f8-83c2-6a2361b834d7.jpg)  
[출처](https://12bme.tistory.com/153?category=737765)  
네임노드의 메타 데이터 정보를 통해 /logs/031412.log 파일은 B1, B2, B3 블럭에 /logs/041213.log 파일은 B4,B5 블럭에 존재한다는 것을 알아 낼 수 있습니다.  
다시 블럭 B1은 A, B, D 노드에 있다는 정보를 알아 낼 수 있습니다.  
전체 노드 중 idle이 높은 노드를 선택하여 해당 노드로 부터 데이터를 액세스하게 됩니다.

### HDFS namenode의 가용성
NameNode daemon은 반드시 항상 실행되고 있어야 합니다. 만약, NameNode가 중단되면, 클러스터는 접근이 불가능합니다.  
따라서 고가용성 모드 2개의 네임 노드를 구성(Active와 Standby)를 하기도 합니다.  
일반적인 Classic mode에서는 1개의 네임노드와 또 다른 "helper" 노드는 SecondaryNameNode로 구성됩니다.  
이때, helper 노드는 백업 목적이 아니며, 네임노드를 복사할 수 있는 정보를 가지고 있는 PC입니다. 따라서 장애 발생시 NameNode를 대신하는 것이 불가능합니다.

### 추가사항
- 한번 저장한 데이터는 수정할 수 없고, 읽기만 가능해서 데이터 무결정성 유지
- 데이터 수정은 불가능 하지만 파일이동, 삭제, 복할 수 있는 인터페이스를 제공
- 데이터 노드는 주기적으로 네임노드에서 블록 리포트를 전송하고 이를 통해 네임노드는 데이터 노드가 정사 작동하는지 확인.


## MR (Map-Reduce) concept
Map Reduce는 여러 노드에 태스크를 분배하는 방법으로 각 노드 프로세스 데이터는 가능한 경우, 해당 노드에 저장됩니다.  
맵리듀스 태스크는 맵(Map)과 리듀스(Reduce) 총 두단계로 구성됩니다.  
하둡에서는 큰 데이터가 들어왔을 때 64MB단위 블럭으로 분할합니다. 각각 블럭에 대한 연산을 합니다.
> ex) word를 counting 하는 작업 : 텍스트 파일을 64MB 단위로 잘라내어 각 블럭에 대해서 특정 단어가 몇번 출현했는지를 계산하는 것입니다.

이후, Map 작업을 수행한 각각의 블럭의 결과 정보를 합치는 작업(Reduce)를 수행하게 되는 방식이다.  
하둡에서는 계산시, 큰 파일을 블럭단위로 나누고 모든 블럭은 같은 Map 작업을 수행하고 이후 Reduce 작업을 수행하게 됩니다.


### Map Reduce
MapReduce는 Hadoop 클러스터의 데이터를 처리하기 위한 시스템으로 총 2개(Map, Reduce)의 phase로 구성됨.  
Map과 Reduce 사이에는 shuffle과 sort라는 스테이지가 존재합니다.  
각 Map task는 전체 데이터 셋에 대해서 별개의 부분(각자 다른 데이터)에 대한 작업을 수행하게 되는데, 기본적으로 하나의 HDFS block을 대상으로 수행하게 됩니다.  
모든 Map Task가 종료되면, MapReduce 시스템은 intermediate 데이터를 Reduce phase를 수행할 노드로 분산하여 전송합니다.  

DFS(Distributed File system)에서 수행되는 MapReduce 작업이 끝나면 HDFS에 파일이 써지고,  
Map Reduce 작업이 시작할때는 HDFS로 부터 파일을 가져오는 작업이 수행됩니다.



## 추가
[Reference](https://icecello.tistory.com/33)

## Reference
[Reference](https://12bme.tistory.com/153?category=737765)  
[Reference](https://hbase.tistory.com/349#:~:text=%ED%95%98%EB%91%A1%20%EC%8A%A4%ED%8A%B8%EB%A6%AC%EB%B0%8D%EC%9D%80%20%EC%9C%A0%EB%8B%89%EC%8A%A4%20%EC%8A%A4%ED%8A%B8%EB%A6%BC,Reducer%EB%A1%9C%20%EC%82%AC%EC%9A%A9%ED%95%A0%20%EC%88%98%20%EC%9E%88%EB%8B%A4.)
[Reference](https://www.geeksforgeeks.org/hadoop-mapreduce-data-flow/)
[Reference](https://opentutorials.org/course/2908/17055)