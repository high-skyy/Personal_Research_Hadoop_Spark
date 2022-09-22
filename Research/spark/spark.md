# Spark

## MR과 Spark 비교
- MR
HDFS에서 data read -> 동작 실행(map) -> HDFS 결과 기록 -> 업데이트 된 데이터 읽기 -> 다음 동작(Reduce) -> HDFS에 기록

- Spark
HDFS에서 data read -> 동작 및 결과값 HDFS 입력 동작이 동시 진행

HDFS가 Disk I/O로 작용 Spark는 인 메모리상에서 동작

## Spark 구조  
![spark](https://user-images.githubusercontent.com/105041834/191177917-992c2aea-aab5-45e9-b678-cb0f8cc6f9bb.jpg)  



## Apache Spark의 개념 이해
아파치 스파크는 빅데이터 분석 framework(하둡 보완)  
MR 방식은 HDFS에 저장된 파일 데이터 기반 배치 분석 (DISK의 I/O)  
스파크는 disk나 기타 다른 저장소(DB등)에 저장된 데이터를 메모리로 올려서 분석하는 방식으로 배치 분석 뿐만 아니라, 스트리밍 데이터 양쪽 분석을 모두 지원한다.

## 기본 동작 원리 및 architecture  
![spark 구조](https://user-images.githubusercontent.com/105041834/191178319-205c7083-0d98-495e-920d-c5f3e2aa8b6a.jpg)  

스파크 클러스터의 구조는 크게 Master node와 worker 노드로 구성  
Master Node는 전체 클러스터를 관리하고 분석 프로그램을 수행 (사용 자가 만든 프로그램 : Driver program)  
분석 프로그램을 스파크 클러스터에 실행 -> Job 생성  

Job이 외부 저장소(HDFS와 같은 파일 시스템)으로 부터 데이터를 로딩하는 경우, 이 데이터는 스파크 클러스터 Worker node에 로딩이 된다.  
로딩된 데이터는 여러 서버의 메모리에 분산되어 로딩이 된다. 이렇게 스파크 메모리에 저장된 데이터 객체를 RDD라고 한다.

로딩 된 데이터는 애플리케이션 로직에 의해서 처리되는데, 하나의 JOB이 여러 worker node에 분산된 데이터를 이용해서 분산되어 실행 하기 때문에,  
하나의 JOB는 여러개의 TASK로 분리되어 실행이 된다. 이렇게 나눠진 Task를 실행하는 것을 Executor라고 한다.  

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

## 클러스터 매니저(Cluster Manager)
분산 처리하기 위해서 하나의 cluster 내에 여러대의 머신, 워커(worker)들로 구성된다.  
하나의 Job이 여러대의 worker에 분산되서 처리되기 위해서는 하나의 JOB를 여러개의 TASK로  
나눈 후에, 적절하게 이 TASK들을 여러 서버에 분산해서 배치 해야 한다. 또한 클러스터 내의 워크 들도 관리를 해 줘야 하는데,  
이렇게 cluster내의 worker resource를 관리하고 TASK를 배치하는 역할 -> cluster manager.  

type : Standalone, Yarn, SIMR 타입  
- Standalone : 하나의 머신 내에서 스파크 운영 (local 개발 환경에 적합)  
- 하둡 2.X의 resource manager인 YARN을 사용하여 Cluster내에 TASK를 배치하도록 하는 방법.  
- 하둡 1.X 이하를 사용할 경우 맵리듀스안에 맵 작업으로 스파크 TASK를 맵핑하는 Spark in MR (SIMR) 방식이 있다.

## Storage
스파크는 메모리 베이스로 데이터를 처리하지만 외부 스토리지는 포함하고 있지 않기 때문에 별도의 외부 스토리지를 사용해야 한다.  
대표적으로 사용 되는 것이 하둡(HDFS) 분산 파일 시스템, 클라우드의 경우 AWS  
DB로는 분산 노드에서 데이터를 동시에 읽어 드려야 하기 때문에, 분산 처리를 잘 지원할 수 있는 NoSQL인 HBase등이 널리 사용된다.  

## File Format
Spark Data를 파일로 저장할 경우 여러 파일 포맷 사용 가능
- CSV, JSON : 일반적으로 사용하는 TEXT기반의 파일 포맷, 사람이 읽을 수 있찌만 압축이 되지 않았기 때문에 용량이 크다.
- Parquet(columna) : 스파크와 함께 가장 잘 사용되는 파일 포맷으로 바이너리 format. 데이터 뿐만 아니라 컬럼명, 데이터 타입, 기본적인 통계 데이타 등의 메타 데이터도 포함한다. 
CSV, Json과는 다르게 기본적인 압축 알고리즘 사용 -> snappy와 같은 압축 방식을 사용했을 때 최대 75% 까지 압축이 가능하다.
  - WORM(Write Once Read Many) -> 쓰는 속도는 느리지만, 읽는 속도가 빠르다. 컬럼 베이스의 스토리지로 컬럼 단위로 저장을 하기 때문에,
전체 테이블에서 특정 컬럼 만 쿼리하는데 있어서 빠른 성능을 낼 수 있다.
- Avro(Row) : Avro는 Paquet과 같이 bianry format. Avro는 row base로 데이터를 저장. Avro는 binary로 데이터를 저장하고
스키마는 JSON 파일에 별도로 저장한다. 사용자가 JSON 만으로 전체적인 Data format 이해 가능.



![cluster manager 구조](https://user-images.githubusercontent.com/105041834/191179214-3cddb0ba-8409-4cd3-b434-38efb1afd421.jpg)  


## Reference
[Reference](https://bcho.tistory.com/1387#:~:text=%EC%8A%A4%ED%8C%8C%ED%81%AC%EB%8A%94%20%EB%8D%B0%EC%9D%B4%ED%84%B0%EB%A5%BC%20%EB%B6%84%EC%82%B0,%EB%B6%84%EC%82%B0%ED%95%B4%EC%84%9C%20%EB%B0%B0%EC%B9%98%20%ED%95%B4%EC%95%BC%20%ED%95%9C%EB%8B%A4.)
[Reference](https://m.blog.naver.com/acornedu/221083892521)
[Reference](https://zzsza.github.io/data/2018/05/29/apache-spark-intro/)