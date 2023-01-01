# MR (Map-Reduce)
MR은 Map 단계와 Reducer 단계로 이루어 진다.

## 도식표 Example
![map-reduce](https://user-images.githubusercontent.com/105041834/190896278-9a42f106-fd1a-4cec-afbb-8581a8117f88.jpg)  

1. Splitting : 문자열 데이터를 라인별로 나눈다.
2. Mapping : 라인별로 문자열을 입력받아, <key, value> 형태로 출력.
3. Shuffling : 같은 key를 가지는 데이터끼리 분류
4. Reducing : 각 key 별로 빈도수를 합산해서 출력
5. Final Result : Reduce의 출력 데이터를 합쳐서 HDFS에 저장.

## Introduction
Map-Reduce의 경우는 대량의 machine들이 data를 process 할 수 있도록 하는 processing framework이다.  
Hadoop 은 Map-Reduce를 이용해 Hadoop cluster에 분산되어 있는 데이터를 process한다.  
Data가 여러 노드에 있는 경우 program이 각 data가 있는 노드에서 작동할 수 있도록 program을 복사를 해 주는 framework가 필요하다. (이게 map-reduce)

> 보통의 framework의 경우 data가 single location에 위치할 경우에 사용된다.
> 여러 대의 machine에 저장되어 있는 data를 다루는 경우 HDFS가 필요하다.

## MR (Map-Reduce) concept
- **Map Reduce는 여러 노드에 태스크를 분배하는 방법.**
- MR 작업이 시작할 때는 HDFS로 부터 파일을 가져오는 작업이 가장 먼저 수행된다.
- MapReduce는 Hadoop 클러스터의 데이터를 처리하기 위한 시스템으로 총 2개(Map, Reduce)의 phase로 구성됨.
- Map과 Reduce 사이에는 shuffle과 sort라는 스테이지가 존재한다.
- Detail
  - Hadoop에서는 용량이 큰 data가 입력이 되면 64MB 단위 블럭으로 분할 합니다. (모든 block에 동일한 MR program이 사용된다.)
  - ex) word를 counting 하는 작업 : 텍스트 파일을 64MB 단위로 잘라내어 각 블럭에 대해서 특정 단어가 몇번 출현했는지를 계산하는 것입니다.

## Components
Driver code, Mapper(Transformation / 다루기 편하도록), Reducer (aggregation)
- Driver code(Job)
  - MR 시작 버튼

- Mapper
  - Initially interacts with the input dataset. (initial line of code)
  - 100 Data-Blocks -> 100 mapper programs or process that runs parallel on nodes.
  - produced output(intermediate output) -> stored on Local Disk (**Not on HDFS**)
  - The produced output acts as input of Reducer (key-value pair의 형태)

- Reducer
  - 사용하기 전 key값에 따라 shuffle이랑 sorting이 발생한다.
  - 주로 computation 작업에 사용 된다. (addition, filtration, aggregation)
  - Reducer의 output은 HDFS에 저장된다.

## MR의 DataFlow
Example (10TB file)
1. 10TB의 data가 HDFS에 의해 여러 노드로 분산된다. (이후 process를 위해서 MR이 사용됨)
2. Driver code(**Job**) initiation이 필요하다. (자동차의 시동 버튼)
3. Mapper 작용 (key-value pair로 만든다.)
4. Mapper의 결과 값은 local disk에 저장되고 key 값에 따라 shuffle sorting이 일어난다.
5. Reducer 작용 (aggregation) -> HDFS 저장 (파일 이름 : part-r-00000)

## map reduce system의 구성
![map reduce system 구성](https://user-images.githubusercontent.com/105041834/190896444-66b6230f-a8e0-4c86-950e-64fe51155265.jpg)  
[출처](https://opentutorials.org/course/2908/17055)

> Job : Client가 수행하려는 작업단위(입력데이터, 맵리듀스 프로그램, 설정 정보로 구성)

- 맵 리듀스 시스템은 Client, JobTracker(NameNode), TaskTracker(Datanode)로 구성된다.  
- Client : 분석하고자 하는 데이터를 Job의 형태로 JobTracker에게 전달
- JobTracker : Hadoop Cluster에 등록된 전체 job을 스케줄링하고 모니터링(프로세스 / 작업을 알맞는 tasktracker에서 할당합니다.) 실패 시 다른 TaskTracker에게 재할당 합니다.
- TaskTracker : DataNode에서 실행되는 데몬이고, 사용자고 설정한 map-reduce program을 실행하며  
JobTracker로부터 작업을 요청받고 요청받은 맵과 리듀스 개수만큼 맵 task와 reduce task를 생성.

## Reference
- [Reference](https://www.geeksforgeeks.org/hadoop-mapreduce-data-flow/)
- [Reference](https://opentutorials.org/course/2908/17055)