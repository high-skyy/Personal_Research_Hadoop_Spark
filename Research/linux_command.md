# Linux Command

## 기본 명령어
```commandline
cd /OO      # 절대 경로
cd OO       # 상대 경로 (순차 적으로 왔다갔다 가능)
cd ..       # 상위 디렉토리로 이동
cd .        # 현재 디렉토리
cd + ~      # 홈 디렉토리
cd + -      # 이전 디렉토리
tty         # 터미널 번호 확인
who         # 현재 접속된 계정 확인
whoami      # 현재 계정
id          # 해당 id에 대한 정보
pwd         # 현재 위치 확인
ps          # 사용중인 계정 확인
useradd +계정명        # 계정 추가
userdel +계정명        # 계정 삭제
passwd  +계정명        # 계정비밀번호 설정 및 변경
echo + 문자열          # 문자열 출력
echo + $+변수명        # 변수 내용 보여줌
echo + $+ ?             # 명령어가 제대로 실행시 0 아니면 0이 아닌 값
history               # 사용했던 명령어 역사
```

```
ls          # 현재 디렉토리 안에 있는 파일 보기
-l          # 파일 허용여부, 소유자, 그룹, 크기 ,날짜등을 출력
-i           # incode table 번호 표시
-lih        # 크기의 단위 표시
-li         # 파일 위치, 파일명, 퍼미션, 등등 상세히 보여주며 incode table 번호도 표시됨
-m          # 파일을 쉼표로 구분하여 가로로 출력
-F          # 디렉토리 내의 모든 파일 출력
-ld         # 디렉토리의 권한 확인
-R          # 서브 디렉토리의 내용을 포함하여 출력
-S          # vkdlf 크기의 순서로 출력
-ldi        # ld + i
```
```
alias 단축키설정='명령어'       # 명령어를 단축키로 지정
mkdir + 이름                  # 디렉토리 생성
which                       # 명령어 위치 확인
W                           # 현재 서버에 접속한 사용자의 접속 정보 및 작업정보를 확인하는 명령어
```

## Cat
```
Cat                         # 텍스트 파일 내용을 표준 출력장치로 출력
Cat + > + 파일명               # 파일 생성 명령어
Cat + >> + 파일명              # 파일에 내용 추가
!Cat                        # 가장 최근에 사용한 cat를 재실행
```



## 퍼미션
> chmod + **(퍼미션 값)** : 파일 권한 변경  
```
U : User
G : Group
O : Others
a : all
r : read
w : write
x : execute
+ : 권한 추가
- : 권한 제거
= : 해당권한만 부여, 나머지 제거
```

## 파일 복사(CP)
> cp [복사할 원본 경로][목적지 경로]
```
cp etd/passwd .(현재 디렉토리)
```

## linux 전역 변수 설정
```commandline
PATH = $PATH:$HOME/.local/bin:$HOME/bin     # PATH의 값 밑에 HOME/.local/bin추가 또 그 밑에 HOME/bin 추가
$PATH       # 원래 PATH가 가지고 있는 값

```
