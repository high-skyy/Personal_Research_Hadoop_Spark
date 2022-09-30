# Error handling(Installation & execution)

- Issue : localhost:9000 failed on connection exception: java.net.ConnectException:
  - Reason (not sure)
    - 하둡이 실행되는 와중에 비정상적으로 종료되면 Safe Mode로 들어간다?
  - [Reference](https://seunghuni96.tistory.com/109)
  - Solved
```
stop-all.sh # 하둡을 정상적인 방법으로 종료시키고
start-all.sh # 다시 정상적인 방법으로 실행시킨다.
```
- Issue : 2022-09-19 21:10:49,010 WARN hdfs.DataStreamer: DataStreamer Exception org.apache.hadoop.ipc.RemoteException(java.io.IOException): File /user/wordcountPJ/shakespeare/histories/kingrichardiii._COPYING_ could only be written to 0 of the 1 minReplication nodes. There are 0 datanode(s) running and 0 node(s) are excluded in this oper
  - Reason (not sure)
    - 비정상적으로 종료가 된 경우 해당 datanode에 대한 내용들이 남아 있는 것 같다.
  - Solved
    - delete all files in /tmp -> type hadoop namenode -format command
```
hadoop namenode -format
```
- Issue : Error copying file from local to HDFS
  - Reason
    - HDFS DFS 명령어와 hadoop 명령어 차이 : HDFS DFS 오직 file system 내 에서의 명령어
    - 명령어 이해 부족(명령어 자세히 알아보고 쓰자.)
  - Solved
    - Local에 있는 File을 HDFS에 올리고 싶은 경우에는 hadoop 명령을 사용하자.
```
$ hadoop fs -put [파일이름] [hdfs에서의 파일위치]      # local에서 파일이 있는 디렉토리에 있는 상태에서 실행해야함
```

- Issue : pipemapred.waitoutputthreads(): subprocess failed with code 1  
  - Reason
    - Mapper와 Reducer가 동시에 실행되어서 발생하는 에러.
    - Hadoop Streaming에서는 명령어 pipeline을 적용하려면 스트리밍 명령어에서 Interpreter를 따로 파일 이름 앞에 적어주어야 한다.
  - [Reference](https://earthconquest.tistory.com/245)
  - Solved
```
# 맞는 예시
- mapper 'python3 Mapper.py'
# 오류 발생 예시
- reducer 'python3 Reducer.py'
```

- Issue : Mapper 파일과 Reducer 파일을 Windows 환경에서 Linux 환경으로 복사해서 붙이게 되면 ^M이 개행이 될 때 마다 발생함.
  - Reason
    - Window와 다른 OS에서 줄바꿈을 정의하는 방식의 차이
  - [Reference](https://www.adminschoice.com/how-to-remove-m-in-linux-unix#:~:text=Control%20M%20(%20%5EM)%20characters,pasted%20from%20a%20windows%20machine.)
  - Solved
```
$ vi -b [file name]  # vi 편집기로 해당하는 .py 파일을 열어서 ^M 문자들을 삭제하자.
:%s/\r//g                          # Regular expression으로 삭제 할 수 있다. 끝나고 wq쓰기
```

- Issue : ERROR: Cannot set priority of journalnode process 6520
  - Reason
    - Configuration에서 보면 journal node는 /dfs/journalnode이라는 파일에 있는데 해당 파일에 대해 user(hadoop)이 권한이 없으면 오류가 발생
  - Solved
  - [Reference](https://stackoverflow.com/questions/56052827/error-cannot-set-priority-of-journalnode-process-6520)
```
$ ls -l /         # 권한 확인하고
$ chown (user 이름) (해당 directory)           # 파일 주인 바꿔 주기
$ chgrp (소유 group) (해당 directory)         # 파일 
```