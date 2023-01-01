# HDFS

## Write flow (파일 저장)
![data flow](https://user-images.githubusercontent.com/105041834/190895957-24752832-3e5b-4bbf-a744-cd1673b050b1.jpg)  
[출처](https://opentutorials.org/course/2908/17055)  
1. APP가 HDFS 클라이언트에게 파일 저장을 요청하면, 
-> HDFS 클라이언트는 네임노드에게 파일 블록들이 저장될 경로 생성을 요청
-> name node는 해당 파일 경로가 존재하지 않으면 경로를 생성한 후, 다른 클라이언트가 해당 경로를 수정하지 못하도록 락을 검.
-> 그 후, 네임노드는 클라이언트에게 해당 파일 블록들을 저장할 데이터 노드의 목록을 반환
2. 클라이언트는 첫 번째 노드에게 데이터 전송 -> 두 번째 데이터 노드로 전송 -> 세번 째 data node로 전송 (본인의 local에 저장.)
3. ACK다 받아내면 블록 위치를 NameNode에게 알려주고 client에게도 알려준다.

## Read flow (파일 읽기)
![Read flow](https://user-images.githubusercontent.com/105041834/190896134-484f5338-ff01-4fc9-9afd-41e394550124.jpg)  
[출처](https://opentutorials.org/course/2908/17055)  
1. APP이 client에게 파일 읽기를 요청
2. client가 namenode에게 요청된 파일이 어떤 블록에 저장되어 있는지 정보를 요청
3. meta data를 통해 파일이 저장된 블록 리스트를 반환
4. client는 datanode에 접근하여 블록 조회 요청
5. data node는 클라이언트에게 요청된 블록을 전송
6. client는 App에게 데이터 전달


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

- file이 block의 크기보다 작은 경우

File이 64MB 또는 128MB의 block으로 분할 될 때, file이 block의 크기보다 작은 경우에는 block 크기 전체를 사용하지 않게 됩니다.  
Block들은 Hadoop configuration에 설정된 디렉터리를 통해 저장됩니다.  
NameNode의 metadata를 사용하지 않으면, HDFS를 통해 접근할 수 있는 방법이 존재하지 않습니다.  

- 클라이언트 어플리케이션이 file에 접근하는 경우
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

### 추가사항
- 한번 저장한 데이터는 수정할 수 없고, 읽기만 가능해서 데이터 무결정성 유지
- 데이터 수정은 불가능 하지만 파일이동, 삭제, 복사할 수 있는 인터페이스를 제공
- 데이터 노드는 주기적으로 네임노드에서 블록 리포트를 전송하고 이를 통해 네임노드는 데이터 노드가 정상 작동하는지 확인.

## Reference
- [Reference](https://opentutorials.org/course/2908/17055)
- [Reference](https://12bme.tistory.com/153?category=737765) 