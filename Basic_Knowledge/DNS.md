# DNS(Domain Name System)
> Domain : 로마자로 나타낸 인터넷 사이트 주소. (숫자로만 구성된 IP 주소의 단점을 보완) [Reference](google 사전)
## Basics
- Identifier : 정확히 무엇을 식별하기 위한 number 또는 name
  - Ip address(32 bit) : 컴퓨터가 서로를 정확하게 인식하기 위한 unique identifier
  - (Host)name : Ip의 경우는 인간이 식별하기 힘들기 때문에 인간은 name으로 이를 식별한다.
    - 결국 이 IP 주소와 (Host)name을 mapping 시켜주는 과정이 필요하게 된다.

## Brief
- Distributed database implemented in hierarchy of many name servers
- Application-layer protocol: hosts, name servers communicate to resolve names.
> 많은 name server들의 layer들을 통해 IP주소 들을 name과 mapping을 시킨다.

## Services and Structure
- DNS services
  - Translation between hostname and IP address
    - 위에서 언급했던 것 과 같이 인간이 식별하는 (Host)name과 IP address를 mapping 해주는 역할을 한다.

- Distributed, hierarchical database
![DNS 구조](https://user-images.githubusercontent.com/105041834/194742528-0d4fcbcf-9b12-4e9f-bd7f-bb1a6d9c8d81.jpg)
- When a Client wants the IP address (example)
  1. Client queries the root server to find .com DNS server.
  2. Client queries .com DNS server to get amanzon.com DNS server
  3. Client queries amazon.com DNS server to get the IP address for www.amazon.com

## Cashing
- Issue
  - 매번 root DNS server로 접속하게 될 경우에 DNS server에 큰 traffic이 놓여질 가능성이 다분하다.
- Solution
  - name server들은 한번 접속된 주소들을 cache를 통해 저장하게 된다.
  - 저장된 Cache들은 지정된 timeout time(TTL) 이후에 없어진다. 

### Details

#### types of servers
- Top-level domain(TLD) servers:
  - Responsible for com, org, net ... and top-level contry domains, e.g. kr, uk, fr, ca
  - VeriSign maintains server for .com TLD
  - Educause for .edu TLD
    - VeriSign Educause : Company or society that provides domain name registry services and internet infrastructure(global provider)

- Authoritative DNS servers
  - Organization's own DNS server providing authoritative hostname to IP mappings for organization's named hosts
  - Can be maintained by organization or service provider.

#### DNS Records
Distributed database storing resource records (RR)
- RR format: (name, value, type ,ttl)
  - type=A
    - name : hostname
    - value : IP address
  - type=NS
    - Name : domain (e.g., foo.com)
    - value : hostname of authoritative name server for this domain
  - type=CNAME
    - name : alias for some (the real) name
    - ex) www.ibm.com is really servereast.backup2.ibm.com
    - value : canonical(real) name
  - type=MX
    - value : name of mail server associated with name

#### DNS Message Format
![DNS message Format](https://user-images.githubusercontent.com/105041834/194743317-9724b3b9-1ca4-4dc3-beaf-4c3fe98ab54f.jpg)

Query and reply message, both with same message format
- Message header
  - Identification : 16 bit num for query, reply to query uses same number
  - Flags
    - Query or reply
    - more...
  - Questions
    - Name, type fields for a query
  - answers
    - RRs in response to query
  - Authority
    - Records for authoritative servers
  - Additional info
    - Additional "helpful" info that may be used

## Reference
- [Reference](학교 ppt 자료)