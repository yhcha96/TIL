# Git

> Git은 분산형 버전 관리시스템(DVCS)이다.
>
> 소스코드 형상 관리 도구로, 코드의 이력을 관리 할 수 있다.



## Git 로컬 저장소 활용하기

> Git은 `repository(저장소)` 로 각각 프로젝트르 관리한다.

## 0. 기본설정

Git에서 이력을 남기기 위해 작성자(author) 정보를 추가한다. 매 컴퓨터에서 최초로 한 번만 설정하면 된다.

```bash
$ git config --global user.name edutak {유저네임}
$ git config --global user.email {이메일}
```

* 일반적으로 `{유저네임}`, `{이메일}`에는 github정보를 넣는다.

### 1. 저장소 생성

```bash
git init
Initialized empty Git repository in C:/Users/student/Desktop/test/.git/
```

`명령어`만 저장하지 말고 `성공한 결과 값` 까지 저장해라!!!

```bash
student@M13035 MINGW64 ~/Desktop/TIL (master)
$ git add .

student@M13035 MINGW64 ~/Desktop/TIL (master)
$ git status
On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   "image/\353\263\264\353\205\270\353\263\264\353\205\270.jpg"
        new file:   "\353\247\210\355\201\254\353\213\244\354\232\264 \355\231\234\354\232\251\353\262\225.md"
```

## 2. add

> 커밋 대상 파일을 `staging area` 로 이동 시킨다.
>
> 즉, 이력을 남길 파일을 담아 놓는 것이다.

`.` 은 현재 디렉토리(폴더)를 뜻한다.

```bash
# 현재 디렉토리 모두 stage
$git add .

#특정 파일만 stage
$git add git.md

# 특정 폴더만 stage
$git add images/
```

항상 `git status` 명령어를 통해 상태를 확인하자.

## 3. commit

> git에서 이력을 남기기 위해서는 커밋을 진행

```bash
$ git commit -m 'Git 기초'
[master c724016] Git 기초
 1 file changed, 13 insertions(+)
 create mode 100644 Git.md

```

* 이력을 확인하기 위해서는 `git log`를 활용한다.

```bash
$ git log
commit c724016bb57a7e2c209ee951064b2e478b4fc46e (HEAD -> master)
Author: yhcha96 <yhcha.h@gmail.com>
Date:   Thu Dec 5 12:41:05 2019 +0900

    Git 기초

commit 093ac46f8eda96078d17af5d33f1a9364a4eec66
Author: yhcha96 <yhcha.h@gmail.com>
Date:   Thu Dec 5 12:38:51 2019 +0900

    Git 기초

```

## Git 원격 저장소 활용하기

### 0. 기본설정

> 원격 저장소를 생성한다. (예 - github)

### 1. 원격 저장소 등록

`origin` 이라는 이름으로 해당 url을 원격 저장소로 등록

최초에 한번만 하면 된다.

```bash
$ git remote add origin https://github.com/yhcha96/TIL.git
```

```bash
$ git remote -v #원격 저장소 목록
origin  https://github.com/yhcha96/TIL.git (fetch)
origin  https://github.com/yhcha96/TIL.git (push)
```



### 2. 원격 저장소 push

앞으로 변경되는 사항이 있으면 항상 `add`, `commit`, `push`를 진행한다.

```bash
$ git push -u origin master
Everything up-to-date
Branch 'master' set up to track remote branch 'master' from 'origin'.
```

