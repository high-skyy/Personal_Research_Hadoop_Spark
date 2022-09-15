# Data Pipeline
> 데이터 파이프라인(Data Pipeline)은 다양한 데이터 소스에서 원시 데이터(raw data)를 수집한 다음 분석을 위해
> 데이터레이크(data lake) 또는 데이터 웨어하우스(data warehouse)와 같은 데이터 저장소로 이전하는 방법이다.  
          
        
* ## What is data lake and data warehouse  
  + #### Data Lake
    - Data Lake는 대규모의 다양한 Raw data를 기본 형식으로 저장하는 데이터 Repository 유형이다.
    - Data Lake를 사용하면 모든 데이터가 보존되며, Storage에 저장하기 전에 제거되거나 필터링되지 않습니다.
    - 보통 Data Lake에 있는 데이터는 분석을 위해 필요할 때 변환되어 사용되어 진다.
    - Data lake는 데이터를 사용하고 엑세스할 수 있도록 관리가 필요하다. -> 엑세스 불가능하면 (data swamp)가 된다.
<br></br>
> Data Lake는 Raw data를 모아 놓은 Repository
<br></br>
  + #### Data Warehouse     
    + 분석 가능한 정보의 중앙 리포지토리. 데이터는 Transaction system, Relational Database 등 으로 부터 보통 정기적으로 데이터 웨어하우스로 들어갑니다.
    + 의사 결정권자는 비즈니스 인텔리전스(BI) 도구, SQL 클라이언트 및 기타 분석 응용 프로그램을 통해 데이터를 액세스합니다. <br></br>
  > Data Warehouse는 정제된 데이터를 모아 놓은 Repository + 추가 적인 기능
<br></br>
  + #### Data flow  

![화면 캡처 2022-09-15 165012](https://user-images.githubusercontent.com/105041834/190346946-840a7a17-0b8d-4e82-8bcf-5db8248d1258.png)
  
  
## Reference
- [Reference](https://www.ibm.com/kr-ko/topics/data-pipeline)
- [Reference](https://www.redhat.com/ko/topics/data-storage/what-is-a-data-lake)
- [Reference](https://aws.amazon.com/ko/data-warehouse/)
