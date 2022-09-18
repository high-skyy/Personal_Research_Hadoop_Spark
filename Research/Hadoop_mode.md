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

## Hadoop Streaming
하둡 스트리밍을 통해서 자바 이외에 파이썬이나 루비, Bash 스크립트 증으로 MR 작업을 생성하고 실행할 수 있게 해준다.
### 하둡 스트리밍 동작 방식 
![Streaming flow](https://user-images.githubusercontent.com/105041834/190889398-f2b1e8e4-b370-4cdf-9046-d58df6a212b6.jpg)
[출처](https://hbase.tistory.com/349#:~:text=%ED%95%98%EB%91%A1%20%EC%8A%A4%ED%8A%B8%EB%A6%AC%EB%B0%8D%EC%9D%80%20%EC%9C%A0%EB%8B%89%EC%8A%A4%20%EC%8A%A4%ED%8A%B8%EB%A6%BC,Reducer%EB%A1%9C%20%EC%82%AC%EC%9A%A9%ED%95%A0%20%EC%88%98%20%EC%9E%88%EB%8B%A4.)  
하둡 스트리밍 유틸리티는 Mapper와 Reducer로 지정된 프로그램을 이용해 MR 작업을 생성한 후 하둡 클러스터로 Submit한다. 그리고 Submit된 작업의 실행을 모니터링한다.  
Submit된 MR 작업이 초기화 되는 과정에서 Mapper들이 초기화될 때, 별도 프로세스를 생성해서 Mapper로 사용될 프로그램이나 스크립트를 실행하게 된다.  
> MR 작업이 진행될 때 직접 만든 Mapreducer를 별도의 프로세스로 실행한다.  

이 후, Mapper는 InputFormat에서 만들어진 Key-Value 쌍을 Mapper로 사용될 프로그램의 표준 입력으로 텍스트 라인 형태로 넘겨준다. 기본적으로 Key에 해당하는 문자열과 Value에 해당하는 문자열을 탭 문자(\t)로 붙여서 텍스트로 만든다.
> 그냥 text string으로 입력을 바꿔서 준다.

Mapper는 사용될 프로그램은 표준 입력으로 받은 Key-Value를 처리하고 표준 출력으로 텍스트를 출력한다.  
그러면 Mapper는 이를 Key-Value 쌍으로 다시 변환해서 정렬하고 그루핑해서 Reducre로 넘겨준다.

Reducer도 Mapper의 입출력과 비슷한 입출력 과정을 거친다.

MR 프레임워크와 Mapper 혹은 Reducer로 사용될 프로그램 사이에서는 Key와 Value를 탭(\t) 문자로 붙여서 전달하고 전달 받는다.  
탭 문자가 텍스트 라인에 없다면 라인 전체가 Key이고 Value는 null인 것으로 간주된다.


### 나중에 작성
[Reference](https://velog.io/@modsiw/%EA%B8%B0%ED%83%80-%ED%95%98%EB%91%A1-%ED%99%98%EA%B2%BD-%EC%84%A4%EC%A0%95-%ED%95%98%EB%A9%B4%EC%84%9C-%EB%AA%B0%EB%9E%90%EB%8D%98-%EA%B3%BC%EC%A0%95-%EA%B0%9C%EB%85%90-%EB%AA%85%EB%A0%B9%EC%96%B4)

## Reference
- [Reference](https://goudacheese.gitlab.io/post/2018-02-24-hadoop_wordcount_example/)
- [Reference](https://hbase.tistory.com/349#:~:text=%ED%95%98%EB%91%A1%20%EC%8A%A4%ED%8A%B8%EB%A6%AC%EB%B0%8D%EC%9D%80%20%EC%9C%A0%EB%8B%89%EC%8A%A4%20%EC%8A%A4%ED%8A%B8%EB%A6%BC,Reducer%EB%A1%9C%20%EC%82%AC%EC%9A%A9%ED%95%A0%20%EC%88%98%20%EC%9E%88%EB%8B%A4.)