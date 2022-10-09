# Spark

## Spark 구조  
![spark](https://user-images.githubusercontent.com/105041834/191177917-992c2aea-aab5-45e9-b678-cb0f8cc6f9bb.jpg)  


## Apache Spark의 개념 이해
- Apache Spark는 빅데이터 분석 framework(하둡의 단점 보완)  
- Hadoop MR은 Disk(HDFS)에 저장된 file data를 기반으로 배치 분석
- Spark는 Secondary memory에 저장된 data를 MM에 올려서 분석하는 방식(배치 분석, 스트리밍 data 지원)


## 기본 동작 원리 및 architecture  
![spark 구조](https://user-images.githubusercontent.com/105041834/191178319-205c7083-0d98-495e-920d-c5f3e2aa8b6a.jpg)  

- Spark Cluster의 구조는 크게 Master node(Name Node)와 Worker Node(Data Node)로 구성  
- Master Node는 전체 cluster를 관리하고 분석 프로그램을 수행
- 사용자가 만든 분석 프로그램을 (Driver Program)-> (Spark Cluster에 실행) -> Job 생성

- 외부 저장소(HDFS, DB)로 부터 데이터 loading -> 여러 server의 memory에 분산되어 loading
- Spark Memory에 저장된 data 객체를 RDD(Resilient Distributed Dataset)라고 한다. 
- 하나의 JOB이 여러 worker node에 분산된 데이터를 이용해서 실행해야 하기 때문에 TASK로 분리되어 실행된다.


## 클러스터 매니저(Cluster Manager)

![cluster manager 구조](https://user-images.githubusercontent.com/105041834/191179214-3cddb0ba-8409-4cd3-b434-38efb1afd421.jpg)  

- 분산 처리하기 위해서 하나의 cluster 내에 여러대의 머신, 워커(worker)들로 구성된다.  
- 하나의 Job이 여러대의 worker에 분산되서 처리되기 위해서는 하나의 JOB를 여러개의 TASK로 나눈 후에, 적절하게 이 TASK들을 여러 서버에 분산해서 배치 해야 한다.
- Work Resource 관리 TASK 배치 역할
  - 하둡 2.x의 resource manager인 YARN을 이용하여 Cluster내에 Task를 배치하도록 한다.


## Storage
- Spark는 메모리 베이스로 데이터를 처리하지만, 외부 스토리지를 포함하지 않는다.
  - 외부 스토리지 따로 사용해주어야 한다. (ex : HDFS, Google Cloud)
- Data Base로는 분산 처리를 잘 지원할 수 있는 NoSQL인 HBase등이 널리 사용된다.


## File Format
- CSV, JSON : 일반적으로 사용하는 TEXT기반의 파일 포맷, 사람이 읽을 수 있지만 압축이 되지 않았기 때문에 용량이 크다.
- Parquet(columna) : 스파크와 함께 가장 잘 사용되는 파일 포맷으로 바이너리 format
  - 데이터 뿐만 아니라 컬럼명, 데이터 타입, 기본적인 통계 데이타 등의 메타 데이터도 포함한다. 
  - CSV, Json과는 다르게 기본적인 압축 알고리즘 사용 -> snappy와 같은 압축 방식을 사용했을 때 최대 75% 까지 압축이 가능하다.
  - 특징 : WORM(Write Once Read Many) -> 쓰는 속도는 느리지만, 읽는 속도가 빠르다.
    - 컬럼 베이스의 스토리지로 컬럼 단위로 저장을 하기 때문에, 전체 테이블에서 특정 컬럼 만 쿼리하는데 있어서 빠른 성능을 낼 수 있다.
- Avro(Row) : Avro는 Paquet과 같이 binary format
  - Avro는 row base로 데이터를 저장.
  - Avro는 binary로 데이터를 저장하고 스키마는 JSON 파일에 별도로 저장한다.
  - 사용자가 JSON 만으로 전체적인 Data format 이해 가능.


### RDD (Resilient Distributed Dataset)
- 오류 자동복구 기능이 포함된 가상의 리스트
- cluster내에서 데이터를 처리
- 다양한 계산(map, reduce, count, fileter, join)을 수행할 수 있으며, 메모리에 저장
- 작업을 병렬적으로 처리
- 여러 작업을 설정한 후, 결과를 얻을 때 lazy하게 계산
- Lineage : 클러스터 중 일부 고장으로 작업이 실패해도 리니지를 통해 데이터를 복구  
> RDD는 리스트를 만들어도 실제로 메모리에 올리진 않고, 정보만 가지고 있음 operator가 실행될 때 진행

#### Operation
- Transformations : RDD의 data를 다른 형태로 변환
  - 실제로 데이터 변환 X -> 어떻게 바꾸는지에 대한 정보를 기록
  - 실제 변환은 Action이 수행되는 시점에서 진행
  - map, fileter, flatMap, mapPartitions...

- Actions : Transformations에 담긴 RDD의 정보를 계산
  - reduce, collect, count, first, take, saveAsTextFile, countByKey, for each




## Reference
- [Reference](https://bcho.tistory.com/1387#:~:text=%EC%8A%A4%ED%8C%8C%ED%81%AC%EB%8A%94%20%EB%8D%B0%EC%9D%B4%ED%84%B0%EB%A5%BC%20%EB%B6%84%EC%82%B0,%EB%B6%84%EC%82%B0%ED%95%B4%EC%84%9C%20%EB%B0%B0%EC%B9%98%20%ED%95%B4%EC%95%BC%20%ED%95%9C%EB%8B%A4.)
- [Reference](https://zzsza.github.io/data/2018/05/29/apache-spark-intro/)