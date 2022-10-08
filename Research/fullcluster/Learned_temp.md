# full cluster settings

## virtualbox installation
> personal C:\Program Files\Oracle\VirtualBox\

### specific information
- DHCP (Dynamic Host Configuration Protocol)  
호스트(서버)에서 보유하고 있는 IP를 유동적으로 관리하는 프로토콜 (IP 자동 할당과 분배 기능)

- IPv4 : Internet protocol version 4

- NAT 방식 network  
컴퓨터 안에 또 하나의 네트워크 대역이 구성되는 것이다. 같은 네트워크 대역 끼리만 통신이 가능하기 때문에 외부의 컴퓨터에서는 접근이 안된다.  
즉, 해당하는 가상머신은 별도의 가상 네트워크에 할당되어 HOST의 게이트웨이를 경유하여 인터넷에 연결됩니다.  
NAT 어댑터는 게스트 OS가 호스트OS의 IP를 통해 외부 인터넷에 연결해주는 가장 간단한 방법이다.  
외부 인터넷과의 연결을 통해 wget등의 명령어로 필요한 모듈들을 설치한. 하지만 게스트OS간의 통신이 불가능하다.

- NIC (Network Interface Controller)  
컴퓨터를 네트워크에 연결하여 통신하기 위해 사용하는 하드웨어 장치입니다.

- HOST-ONLY Network  
내부 네트워크와 비슷하지만, HOST와 연결이 가능하다. 외부 인터넷은 안된다.  
Host가 외부와 net0를 통해 통신하고 있다면 Host의 net1은 Host only virtual NIC

## Reference
[Reference](https://spidyweb.tistory.com/266?category=910416)
[DHCP](https://extrememanual.net/8698)
[NAT](https://wookoa.tistory.com/107)
[virtualbox 설치](https://mine-it-record.tistory.com/420)