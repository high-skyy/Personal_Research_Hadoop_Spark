# Netstat
네트워크 및 통계라는 단어에서 파생 된 Netstat는 시스템 관리자가 네트워크 통계를 분석하는 데 사용하는 명령 줄 유틸리티입니다.
호스트 시스템의 열린 포트 및 해당 주소, 라우팅 테이블 및 연결과 같은 전체 방식의 통계를 표시합니다.

```
# 활성 또는 수동 소켓을 표시하는 옵션을 지원합니다.

$ netstat -tnlpa | grep (해당 port)
```
> netstat -tnlpa 로 출력된 내용들을 오른쪽 명령어의 input 으로 준다.

## Reference
- [Reference](https://ko.linux-console.net/?p=554#gsc.tab=0)