# Yarn(Yet Another Resource Nagotiator)
> mapreduce의 단점을 극복하기 위해 제안된 YARN 

![YARN](https://user-images.githubusercontent.com/105041834/190896703-b53ebbb6-b2e0-4196-ad7f-57ad1ed31a98.jpg)  
[출처](https://opentutorials.org/course/2908/17248)

각 어플리케이션(HBase, MapReduce ...)에 필요한 리소스(CPU, 메모리, 디스크 등)을 할당하고 모니터링 하는 업무  
Yarn(하둡 2.0)에서
Job Tracker의 기능을 ResourceManager, Application Manager 두 가지의 프로세스로 나누고  
Task Tracker의 기능은 NodeManager가 대신하게 되었다.

## Yarn 구성요소 각각에 대해
- Resource Manager  
  - Client의 Job 제출을 받는다.
  - App master로 부터 slaves nodes 정보(데이터 위치, cpu, memory)등을 제공받아 최상의 리소스 할당하고, Application master에게 node의 디테일한 정보들을 전달한다.
  - Slave node에 이상이 생기면 -> app master가 프로세스를 완료할 수 있도록 새로운 container를 할당한다.
클러스터에 1개 존재하며, 클러스터의 전반적인 자원 관리와 Scheduler Application manager를 조정한다.
Client로부터 App 실행 요처을 받으면, 그 실행을 책임질 Application Master를 실행  
Cluster 내의 Node Manager들과 통시능ㄹ 해서 할당된 자원과 사용중인 자원의 상황을 알 수 있다.


- Scheduler  
  - slave node에 있는 임의의 container 중 하나를 Application master로 할당한다.
Node Manager들의 자원 상태를 관리하며 부족한 리소스를 할당한다.  
자원의 상태에 따라서 Task의 실행 여부를 허가해주는 역할인 Scheduling 작업만 담당한다.
Node Manager들의 자원 상태를 Resource Manager에게 통지한다.

- Application Manager
  - Client로 부터 받은 Job의 가능성을 체크하고 scheduler에게 job을 넘겨준다.
Node Manager에서 특정 작업을 위해 Application Manager를 실행하고, Application의 실행 상태를 관리하여 그 상태를 Resource Manager에게 통지한다.

- Node Manager  
  - scheduler가 새로운 app을 시작할 수 있도록 하기 위해, 주기적으로 자신의 노드에서 현재 이용가능한 resource의 상태를 resource manager에게 알려준다.

노드 당 한개씩 존재하며, Container의 리소스 사용량을 모니터링하고, 관련 정보를 Resource Manager에게 알리는 역할을 한다.

- Application Master
  - Scheduler로 부터 container를 할당 받는다.
  - slaves nodes상의 데이터 위치, cpu, memory등을 관리하고 resource manager에 제공함으로써 Application Master 외의 container들을 조율한다.
  - Container를 실행시키기 위해 제안된 slave node 상의 node manager에게 요청을 보낸다.
  - Job이 실행되는 동안 container들의 resource를 관리한다. 와료되면 resource manager에게 알려준다.
Yarn에서 실행되는 하나의 task를 관리하는 마스터 서버를 말한다. (APP 당 1개)  
Scheduler로부터 적절한 Containter를 할당 받고, 프로그램의 실행 상태를 모니터링, 관리한다.

- Container

CPU, Disk, Memory등의 리소스로 정의 된다.  
모든 작업은 여러개의 task로 세분화 되고, 각 task는 하나의 container에서 실행된다.

필요한 자원의 요청은 Application Manager가 담당하며, 승인 여부는 Resource Manager가 담당합니다.  


## 도식표와 flow

![YARN 도식표](https://user-images.githubusercontent.com/105041834/190896995-80e7107a-dca3-42bd-81c7-f5f9e0c6243c.jpg)  
[출처](https://opentutorials.org/course/2908/17248)

1. Client가 제출하는 Job 이 ResourceManager에게 제출이 된다.
2. Master node의 Application Manager는 제출된 job의 유효성을 체크하고, 자원 할당을 위해 Scheduler에게 넘겨준다.
3. Scheduler는 임의의 slave node에 있는 컨테이너 중 하나를 Application Master로 할당한다.
4. Application Master는 slave nodes상의 데이터 위치, cpu, memory 등을 Resource Manager에 제공함으로써 Application Master 외의 Containter들을 조율한다.  
5. Resource Manager는 최상의 resource들을 할당하고, Application master에 node의 디테일한 정보들을 전달한다.
6. Application master는 container들을 실행시키기 위해 제안된 slave node상의 node manager에게 요청을 보낸다.
7. Application master는 job이 실행되는 동안, 요청된 container들의 resource를 관리한다. 실행이 되면, resource manager에게 알려준다.
8. Node manager는 Scheduler가 새로운 application을 시작할 수 있도록 하기 위해, 주기적으로 자신의 노드에서 현재 이용가능한 resource 상태를 resource manager에게 알려준다.
9. Slave node에서 이상이 생긴 경우, resource manager는 application master가 프로세스를 완료할 수 있도록 새로운 container를 할당한다.

## Reference
[Reference](https://opentutorials.org/course/2908/17248)