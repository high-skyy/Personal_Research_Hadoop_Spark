# Basic Instructions


## 하둡(hdfs)기본 사용법
시스템과의 상호작용은 hadoop 이라는 명령어를 통해서 합니다. 만약 터미널을 열고, 인자 없이 명령어를 실행하면 도움말이 나옵니다.
> 대부분 rmdir cat linux와 비슷한데 앞에 -만 붙여주면 된다.
### Exploring HDFS
시스템과의 상호작용은 hadoop 이라는 명령어를 통해서 합니다.
1. 하둡 프로그램에서 HDFS와 관련된 서브 시스템은 FsShell 이라고 한다. 이 서브 시스템은 fs 명령어로 실행할 수 있다.
```
$ hadoop          # 도움말이 요청됨 (인자가 없을 경우)
$ hadoop fs       # 서브 시스템의 모든 며령어에 대한 설명을 볼 수 있따.
```

### 디렉토리 조회 및 생성
> hadoop fs는 hadoop을 포함한 여러 파일 시스템과 상호작용할 수 있는 일반적인 명령이며, hdfs dfs는 HDFS에만 해당하는 명령어이다.
```
$ hadoop fs -l /      # root 디렉터리를 조회한다
$ hadoop fs -ls /user   # 특정 디렉토리를 조회할 때 /user와 같은 디렉토리 명을 사용한다.
$ hdfs dfs -ls          # 해당 폴더에 디렉터리가 있는지 확인
$ hdfs dfs -mkdir /user/...         # 을 통해 새로운 디렉토리 생성
# hadoop file system을 다룰때에는 hdfs를 직접적으로 사용하자
```

### 파일 업로드
```
$ hadoop fs -put [파일이름] [hdfs에서의 파일위치]      # local에서 파일이 있는 디렉토리에 있는 상태에서 실행해야함
$ gunzip -c access_log.gz \ | hadoop fs -put [hdfs 상의 파일 위치]  # 압축 풀면서 한번에 저장
# 명령어 A | 명령어 B         를 할 경우 명령어 A를 실행한 뒤 명령어 B를 실행한다.

$ hadoop fs -get [HDFS 경로] [로컬 경로]      # hdfs에 있는 파일을 local로 옮기고 싶을 경우
```

### 오류
- localhost:9000 failed on connection exception: java.net.ConnectException:
```
stop-all.sh         # 하둡을 정상적인 방법으로 종료
start-all.sh        # 다시 정상적인 방법으로 실행
```
## Reference
[Reference](https://12bme.tistory.com/152#:~:text=%ED%95%98%EB%91%A1%20HDFS%20%EA%B8%B0%EB%B3%B8%20%EC%82%AC%EC%9A%A9%EB%B2%95,%EC%95%84%EB%9E%98%20%EB%AA%85%EB%A0%B9%EC%96%B4%EB%A5%BC%20%EC%8B%A4%ED%96%89%ED%95%A9%EB%8B%88%EB%8B%A4.&text=hadoop%20%EB%AA%85%EB%A0%B9%EC%96%B4%EB%8A%94%20%EC%97%AC%EB%9F%AC%EA%B0%9C%EC%9D%98%20%EC%84%9C%EB%B8%8C%20%EC%8B%9C%EC%8A%A4%ED%85%9C%EC%9C%BC%EB%A1%9C%20%EC%84%B8%EB%B6%84%ED%99%94%20%EB%90%98%EC%96%B4%EC%9E%88%EC%8A%B5%EB%8B%88%EB%8B%A4.)
[Reference](https://seunghuni96.tistory.com/109)
[Reference](https://sungwookkang.com/1359#:~:text=HDFS%EC%97%90%20%EB%8D%B0%EC%9D%B4%ED%84%B0%EB%A5%BC%20%EC%A0%80%EC%9E%A5,get%20%EB%AA%85%EB%A0%B9%EC%9D%84%20%EC%82%AC%EC%9A%A9%ED%95%9C%EB%8B%A4.)
[Reference](https://reference-m1.tistory.com/197#:~:text=%EA%B0%84%EB%8B%A8%ED%9E%88%20%EC%A0%95%EB%A6%AC%ED%95%98%EB%A9%B4%20hadoop%20fs,%EC%97%90%EB%A7%8C%20%ED%95%B4%EB%8B%B9%ED%95%98%EB%8A%94%20%EB%AA%85%EB%A0%B9%EC%96%B4%EC%9D%B4%EB%8B%A4.)