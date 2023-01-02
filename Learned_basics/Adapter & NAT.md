# Adapter
- **Adapter** : the component of a computer's internal hardware that is used for communicating over a network with another computer
## enp0s3와 enp0s8
- VirtualBox를 통해 생성할 가상 서버의 네트워크 디바이스 : enp0s3, enp0s8

## NAT (Network Address Translation)
- NAT is the process of reassigning the single IP address space into a further one
by altering the network address data in the IP header of the datapacket while they
are traveling through a network towards the destination node.
> NAT는 IP 주소를 다른 걸로 바꿔주는 역할을 한다.
- Generaly, NAT works on a router or gateway and interconnects two networks with
each other by translating the private
addresses into the registered addresses before the data being transmitted to another network
> NAT는 보통 router와 gateway에서 작용을 하는데 private address를 registered address(설정된 주소)로 바꿔주는 역할을 한다.
- 실제 IPv4에서 사용하는 주소가 많지 않아 NAT를 사용하게 되었음
- NAT is introduced and widely deployed everywhere which permits a network device like a router(or gateway) to behave as an agent between the Internet and the private network.
  - It signifies that a unique IP address can be used to symbolize the overall class of network devices like PCs
> Internet와 private한 network간의 router의 역할을 하게 되는데 한 IP주소가 전체 network device의 class를 의미하게 만든다.
> 
> 다수의 기기가 하나의 IP address에 할당받길 원할 때 사용이 된다.


## Reference
- [Reference](https://thebook.io/006881/part02/ch03/02/02-03/)
- [Reference](https://www.softwaretestinghelp.com/network-address-translation-nat/)
- [Reference](https://www.comptia.org/content/guides/what-is-network-address-translation)