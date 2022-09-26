# MR

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