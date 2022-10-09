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

- Issue : Cannot set priority of journalnode process 6520
  - Reason
    - Configuration에서 보면 journal node는 /dfs/journalnode이라는 파일에 있는데 해당 파일에 대해 user(hadoop)이 권한이 없으면 오류가 발생
  - Solved
  - [Reference](https://stackoverflow.com/questions/56052827/error-cannot-set-priority-of-journalnode-process-6520)
```
$ ls -l /         # 권한 확인하고
$ chown (user 이름) (해당 directory)           # 파일 주인 바꿔 주기
$ chgrp (소유 group) (해당 directory)         # 파일 
```

- Issue : java.net bind exception address already in use
  - Reason
    - log file에서 확인할 수 있음 실제로 해당 포트가 이미 사용되고 있는 경우가 있고 없는 경우도 있다.
  - Solved
  - [Reference](https://community.cloudera.com/t5/Support-Questions/Failed-to-start-namenode-java-net-BindException-Port-in-use/td-p/228570)
```
$ netstat -tnlpa | grep (사용되고 있는 port 번호)
$ kill -9 (해당하는 process id)
# netstat을 했음에도 불구하고 해당 port를 사용하는 process가 나오지 않을 경우에는 재부팅을 해야 한다.
```

- Issue : WebAppProxy not in jps
  - Reason
    - Configuartion file에 WebAppProxy 주소를 입력하지 않았음
  - Solved
    - yarn-site.xml -> yarn.web-proxy.address : 0.0.0.0:8089
  - [Reference](https://tdoodle.tistory.com/entry/Hadoop-Namenode-HA-%EA%B5%AC%EC%84%B1%ED%95%98%EA%B8%B0?category=815463)

- Issue : pinc -c 2 -> result : Name or service not known
  - Reason
  - Solved
  - [Reference](https://intrepidgeeks.com/tutorial/linux-ping-wwwbaiducom-name-or-service-not-known)
```
$ vi /etc/resolv.conf
nameserver 8.8.8.8
nameserver 114.114.114.114
```

- Issue : There are 0 datanodes running ...
  - Reason
    - 전에 사용하던 node의 정보들을 tmp file에 저장이 되어 있어 나중에 이를 reference하기 때문이다.
    - Solved
  - [Reference](https://stackoverflow.com/questions/26545524/there-are-0-datanodes-running-and-no-nodes-are-excluded-in-this-operation)
```
rm -rf /tmp/*         # su root인 상태에서
```

- Issue : namenode not appearing on jps on namenode and rmnode
  - Reason
    - Format을 안해 주었기 때문이다. Namenode의 format과 rmnode의 format은 다르다.
  - Solved
  - [Reference](https://spidyweb.tistory.com/272?category=910416)
```
$ hadoop namenode -format
$ $HADOOP_HOME/bin/hdfs namenode -bootstrapStandby
```

- Issue : httpfs error Operation category READ is not supported in state standby
  - Reason
    - Namenode가 standbynode로 변하게 되어 hdfs에 접근할 수 없게 됨(su root 인 상태에서 hadoop namenode format 해줬을 때 발생했음)
  - Solved
```
# 재부팅 후
$ hadoop namenode -format       # su hadoop인 상태에서
```

- Current issue : spark web UI 접근이 불가능 함
  - 
