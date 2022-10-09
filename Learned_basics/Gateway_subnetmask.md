# Gateway and subnetmask

## Subnet Mask Definition
- Every device has an IP address with two pieces: the client or host address and the server or network address.  
- IP addresses are either configured by a DHCP server or manually configured.
- The subnet mask splits the IP addresses into the host and network addresses, theryby defining which part of the IP address belongs to the device and which part belongs to the network.
> subnet mask는 IP의 주소를 host와 network 주소로 나누어서 둘을 정의가 가능하게 한다.
- 32-bit number created by seting host bits to all 0s and setting network bits to all 1s
> 모든 host의 bit를 0으로 만들고 network의 bit를 전부 1로 만든다. (host와 network주소를 실제 나누는 implementation)
- detail : the "255" address is always assigned to a broadcast address, and the "0" address is always assigned to a network address.
- When organizations need additional subnetworking, subnetting divides the host element of the IP address further into a subnet.
> subnetworking이 필요한 경우에는 IP address의 host element를 추가적으로 나눈다.
- The goal of subnet masks are simply to enable the subnetting process.

## IP address and Subnet Mask
- 32-bit IP address uniquely identify -> Single device on an IP network
- IP 주소는 4개의 8-bit octet으로 나누어진다.
  - ex) 172.16.254.1 -> (172 bin).(16 bin).(254 bin).(1 bin)
  - ex) 위의 IP주소의 subnet mask -> 255.255.255.0 로 설정
    - 172.16.254 -> 해당 network의 주소
    - 1 -> 해당 subnetwork에서 사용되는 주소
### details
- Class A subnet mask
  - network portion : first octet
  - hosts portion : 2,3,4 octet (networks with more than 65,536 hosts.)
  - 255.0.0.0
- Class B subnet mask
  - network portion : 1, 2 octet
  - host portion : 3,4 octet
  - 255.255.0.0
- CIDR 표기
  - /32 : 255.255.255.255 (1개의 bit)
  - /24 : 255.255.255.0   (32 -24 = 8 bit를 subnet으로 사용하겠다.)
## Gateway
![Gateway_submasks](https://user-images.githubusercontent.com/105041834/194744292-6ff92288-ae06-4f4a-a9c3-789bc7f69d47.jpg)
- Brief : device on a network which sends local network traffic to other networks
- The device called a gateway or default gateway connects local devices to other network.
- When a local device wants to send information to a device at an IP address on another network, it first sends its packets to the gateway.
  - Then forwards the data on to its destination outside of the local network.
> Gateway를 통해서 local device 들은 다른 network와 연결이 된다.
> 
> Local device가 packet(전송하고자 하는 정보)를 다른 network에 있는 IP주소에게 보내기 위해서는 gateway로 packet을 보낸다. 그 이후에
> gateway에서 해당 data는 원하는 destination으로 forward된다.

## Reference
- [Reference](https://avinetworks.com/glossary/subnet-mask/)