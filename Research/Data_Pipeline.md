# Data Pipeline
> 데이터 파이프라인(Data Pipeline)은 다양한 데이터 소스에서 원시 데이터(raw data)를 수집한 다음 분석을 위해
> 데이터레이크(data lake) 또는 데이터 웨어하우스(data warehouse)와 같은 데이터 저장소로 이전하는 방법이다.  

<br></br>
### What is data lake and data warehouse  
> Data Lake는 Raw Data를 모아 놓은 Repository

> Data Warehouse는 정제된 데이터를 모아 놓은 Repository + 추가적인 기능

- **Data Lake**   

  
    - Data Lake는 대규모의 다양한 Raw data를 기본 형식으로 저장하는 데이터 Repository 유형이다.
    - Data Lake를 사용하면 모든 데이터가 보존되며, Storage에 저장하기 전에 제거되거나 필터링되지 않습니다.
    - 보통 Data Lake에 있는 데이터는 분석을 위해 필요할 때 변환되어 사용되어 진다.
    - Data lake는 데이터를 사용하고 엑세스할 수 있도록 관리가 필요하다. -> 엑세스 불가능하면 (data swamp)가 된다.


- **Data Warehouse**     


  - 분석 가능한 정보의 중앙 리포지토리. 데이터는 Transaction system, Relational Database 등 으로 부터 보통 정기적으로 데이터 웨어하우스로 들어갑니다.
  - 의사 결정권자는 비즈니스 인텔리전스(BI) 도구, SQL 클라이언트 및 기타 분석 응용 프로그램을 통해 데이터를 액세스합니다.


- **Data flow**  

![화면 캡처 2022-09-15 165012](https://user-images.githubusercontent.com/105041834/190346946-840a7a17-0b8d-4e82-8bcf-5db8248d1258.png)

<br></br>
## Data Pipeline types
> Batch processing은 Hadoop 이용, Streaming Data는 Apache Kafka 이용
- 일괄 처리(batch processing)
  - 미리 설정된 시간 간격 동안 저장소에 데이터의 "묶음(batch)"를 로드하며, 일반적으로 사용량이 적은 업무 시간에 업데이트 된다.
  - 한 명령의 출력이 다른 명령의 입력이 되는 시퀀싱된 명령의 워크플로우를 형성. 이 일련의 명령은 데이터가 완전히 변환되어 데이터 저장소에 기록될 때까지 계속됩니다.  
  
- 스트리밍 데이터 (streaming data)
  - 데이터를 지속적으로 업데이트해야 할 때 활용된다.
  - 데이터 이벤트는 발생한 직후에 처리되기 때문에 스트리밍 처리 시스템의 지연 시간이 배치 시스템보다 짧지만, 메세지가 의도치 않게 삭제되거나 대기열에서 오래 대기할 수 있으므로 일괄 처리만큼 안정적인 것으로 간주되지 않는다.
  
## Data Pipeline Architecture  
1. 데이터 수집(Data extract)
  - 데이터는 다양한 데이터 구조를 포함하는 다양한 데이터 소스에서 수집됩니다.
2. 데이터 변환(Data transformation)
  - 일련의 작업이 실행되어 대상 데이터 저장소에서 요구하는 형식으로 데이터를 처리한다.
3. 데이터 저장(Data load)
  - 그런 다음 변환된 데이터는 다양한 이해 관계자들에게 노출될 수 있는 데이터 저장소에 저장됩니다.

## Data Pipeline Usage
- 탐색형 데이터 분석(EDA)
  - 데이터 소스를 조작하여 필요한 응답을 얻을 수 있는 최상의 방법을 결정할 수 있도록 지원
- 데이터 시각화
  - 차트, 플롯, 인포그래픽, 애니메이션과 같은 일반적인 그래픽을 통해 데이터를 나타냅니다.
- 머신 러닝
  - 머신 러닝은 데이터와 알고리즘을 사용하여 인간이 학습하는 방식을 모방하고 점진적으로 그 정확도를 향상시키는데 중점을 둔다.

## Reference
- [Reference](https://www.ibm.com/kr-ko/topics/data-pipeline)
- [Reference](https://www.redhat.com/ko/topics/data-storage/what-is-a-data-lake)
- [Reference](https://aws.amazon.com/ko/data-warehouse/)
