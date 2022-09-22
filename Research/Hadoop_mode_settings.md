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


### 나중에 작성
[Reference](https://velog.io/@modsiw/%EA%B8%B0%ED%83%80-%ED%95%98%EB%91%A1-%ED%99%98%EA%B2%BD-%EC%84%A4%EC%A0%95-%ED%95%98%EB%A9%B4%EC%84%9C-%EB%AA%B0%EB%9E%90%EB%8D%98-%EA%B3%BC%EC%A0%95-%EA%B0%9C%EB%85%90-%EB%AA%85%EB%A0%B9%EC%96%B4)

## Reference
- [Reference](https://goudacheese.gitlab.io/post/2018-02-24-hadoop_wordcount_example/)
- [Reference](https://hbase.tistory.com/349#:~:text=%ED%95%98%EB%91%A1%20%EC%8A%A4%ED%8A%B8%EB%A6%AC%EB%B0%8D%EC%9D%80%20%EC%9C%A0%EB%8B%89%EC%8A%A4%20%EC%8A%A4%ED%8A%B8%EB%A6%BC,Reducer%EB%A1%9C%20%EC%82%AC%EC%9A%A9%ED%95%A0%20%EC%88%98%20%EC%9E%88%EB%8B%A4.)
- [Reference](https://hadoop.apache.org/docs/r3.1.1/hadoop-project-dist/hadoop-common/ClusterSetup.html)

## 나중에 해 보기 (fully-distributed-mode)
[해보기](https://spidyweb.tistory.com/270)
[해보기](https://beomi.github.io/2017/11/27/EMR-and-PySpark/)