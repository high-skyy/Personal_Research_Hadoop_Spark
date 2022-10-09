# RPC (Remote Procedure Call)
Process간 통신을 위해 사용하는 IPC(Inter Process Communication) 방법의 한 종류이다.
원격지의 프로세스에 접근하여 procedure 또는 function을 호출 하여 사용한다.

일반적으로 process는 자신의 주소공간 안에 존재하는 함수만 호출하여 실행 가능하다.
하지만, RPC를 이용하면 다른 주소공간에서 동작하는 process의 함수를 실행할 수 있게 된다.
분산 컴퓨터 환경에서 process간 상호 통신 및 컴퓨팅 자원의 효율적인 사용을 위해 사용되는 기술이다.

## 개념
별도의 원격제어를 위한 코딩 없이 다른 주소 공간에서 함수나, procedure를 실행할 수 있게 하는 process간 통신 기술.
> RPC를 이용하면 프로그래머는 함수 또는 procedure가 실행 프로그램이 존재하는 local 위치에 있든, 원격 위치에 있든 상관없이 동일한 기능을 수행할 수 있음


## Reference
- [Reference](https://co-no.tistory.com/28)
- [Reference](https://velog.io/@jakeseo_me/RPC%EB%9E%80)