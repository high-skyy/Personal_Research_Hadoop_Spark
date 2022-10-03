# Linux Command

## 자주 써서 익히자
```
$ tar -zxvf (파일명.tar.gz) -C (해당 폴더들을 넣을 폴더명 / 미리 만들어져 있어야함)           # tar.gz 파일 압축 풀기
$ tar -zcvf (파일명.tar.gz) [폴더명]   # 폴더명을 파일명.tar.gz로 압축
$ rm [옵션] [삭제할 파일 위치/이름]      
# -r : 일반 파일은 그냥 지우고 디렉토리면 디렉토리 하위 경로 파일을 모두 지운다
$ pwd : 현재 경로 출력
ls -a : 디렉토리 내의 모든 파일 출력

# 입출력 재지정
# > : 새로 지정
# >> : append
cat > lazy_dog.txt          
cat lazy_dog.txt
# The quick brown fox jumped over the lazy dog

# permission
chmod OGW file이름        
# Owner, Group, World / 앞부터 차례대로 8진법 / OGW 앞에 +면 추가 -면 제거
```

## 압축 및 해제 정리
[참고](https://brownbears.tistory.com/161)

## 기본 명령어
```
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

## 메타 문자
- ~ : 홈 디렉토리 / . : 현재 디렉토리 / .. : 상위 디렉토리 / # : 주석 / $ : 쉘 변수
- & : 백그라운드 작업 / ? : 한 문자 와일드 카드
- (*) : 임의의 문자열을 나타내는 특수 문자로 흔히 사용하는 특수 문자 중 하나입니다. (0개 이상의 문자로 대체 된다.)
  - 주로 여러 파일의 이름을 하나하나 작업하기 힘들때 이름을 간단하게 표시하는데 사용한다.
  - 명령을 실행할 때 파일의 이름을 적어야 하는 자리에 (*)을 사용하면 모든 파일을 나타낸다.
- ; : 쉘 구분 명령자
  - 연결된 명령을 왼쪽부터 차례로 실행
- | : 파이프
  - 왼쪽 명령의 실행결과를 오른쪽 명령의 입력으로 전달한다.
- < , > : 표준 출력을 바꾸는 특수문자
  - 파일을 바꿀 때 ex) echo "안녕하십니까" > aaa
- << , >> : 파일에 내용을 추가하는 역할로 활용
  - 파일에 append 시켜준다.

- [Reference](https://hack-cracker.tistory.com/26)

## rm
deleting files
> rm (option) (filename)

```
$ rm -r (filename)
$ rm -rf *          # Force deletion of everything in the current directory/working directory
$ rm -rf .          # Force deletion of current folder and subfolders
```

## (*)


## 퍼미션
### chmod
> chmod + **(퍼미션 값)** : 파일 권한 변경  
```
$ chmod u+w [File]              # 파일 소유 사용자에게 쓰기 권한 추가.
$ chmod g+w [File]              # 파일 소유 그룹에게 쓰기 권한 추가.
$ chmod u=rwx [File]            # 파일 소유 사용자에게 읽기, 쓰기, 실행 권한 추가.
$ chmod 755
```
- U : User / G : Group / O : Others / a : all
- r : read(4) / w : write(2) / x : execute (1)
- + : 권한 추가 / - : 권한 제거 / = : 해당권한만 부여, 나머지 제거
- option
  - (-R) : 지정한 모드를 파일과 디렉토리에 대해 재귀적으로 적용
  - (-f) : 에러 메시지 출력하지 않음
- [Reference](https://recipes4dev.tistory.com/175)

### chown, chgrp
> chown {소유권자}:{그룹식별자} {소유권을 변경하고 싶은 파일명 or 디렉토리명}
```
chown aaa:bbb test.sh
chown -R aaa:bbb test.sh        # 하위 디렉토리 까지 변경 옵션 : -R
```
- [Reference](https://araikuma.tistory.com/117)

## 파일 복사(CP)
> cp [복사할 원본 경로][목적지 경로]
```
cp etd/passwd .(현재 디렉토리)
```

## linux 전역 변수 설정
```
PATH = $PATH:$HOME/.local/bin:$HOME/bin     # PATH의 값 밑에 HOME/.local/bin추가 또 그 밑에 HOME/bin 추가
$PATH       # 원래 PATH가 가지고 있는 값
```

## VIM 편집기
### 모드
1. 일반 모드(명령모드)
vi를 실행시켰을때 가장 먼저 켜지는 화면이다. 각기 다른모드에서 esc키를 누르면 항상 일반모드로 돌아오게 되어있다.
2. 입력 모드(편집모드)
실질적으로 코드편집을 하는 단계이다. 좌측 하단을 보면 --INSERT--라고 나타나있는 경우에 해당된다.
3. 비주얼 모드
V나 v키로 접근하며 일반적으로 여러행을 선택할 때 주로 사용한다.
4. ex 모드
[:] 콤마를 누름으로써 모드에 입장할 수 있다. 이 모드에서는 저장, 종료, 검색, 치환을 주로 사용한다.

### 일반 모드에서의 명령어
- i : 입력모드 전환, 커서왼에 삽입된다.  
방향 키로 움직인다.  

![vim 일반모드에서 명령](https://user-images.githubusercontent.com/105041834/190977190-62888004-f115-40ff-b56f-855ff0bedd41.jpg)  
[출처](https://m.blog.naver.com/zbqmgldjfh/222086097819)  

#### 복사,삭제 및 되돌리기
- y : 복사
- yy : 커서를 포함하는 행 복사
- dd : 커서를 포함하는 행 잘라내기
- dw : 한 단어 잘라내기
- x : 커서 위치 삭제
- X : 커서 앞글자 삭제
- u : 되돌리기 (undo)

#### 빠른이동
- ] : 다음 함수의 block 시작지점으로 이동
- [ : 이전 함수의 block 시작지점으로 이동
- 0 or ^ : 행의 시작지접으로 이동
- & 행의 끝 부분으로 이동
- gg 문서 맨 처음으로 이동
- G 문서 맨 끝으로 이동

#### 검색, 치환 및 행번호
> regular expression을 사용한다.
- /(찾을내용)
- n : 다음으로 찾은 대상으로 이동
- N : 이전으로 찾은 대상으로 이동
- %s/원래단어/바꿀 단어/g        # 끝에 g 들어가면 전부 다 바꾼다. (:) 누를시
- set number 행번호 추가

#### 저장 및 종료
> : 눌러 줘야 함
- w : 저장
- q : 종료
- wq : 저장후 종료
- q! : 강제 종료(저장안함)

## Reference
[Reference](https://m.blog.naver.com/zbqmgldjfh/222086097819)