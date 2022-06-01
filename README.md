## 📝 Git branch convention

> [Repository](https://github.com/letgodchan0/Al_IS_Well.git) clone으로 받기

<hr>

```bash
# 브랜치 만들면서 이동
$ git switch -c letgodchan0/0602

# 브랜치 확인
$ git branch
```

1. 문제 업로드 전 브랜치 생성 및 이동

<br>

```bash
ex) 1주차/0602/찬영/

# 각자 폴더에 문제 올라가 있는지 확인
$ git status

# add
$ git add .

# 커밋
$ git commit -m "Add 문제 이름"			// 오타거나 재업로드일 경우 "Set 문제이름"

# 푸쉬
$ git push origin letgodchan0/0602
```

1. 오늘의 문제 풀기 진행!
2. 문제 풀기 완료 후 각자 이름으로 폴더 만든 후 commit, push

<br>

![z](README.assets/z.jpg)

1. GitHub에서 내가 푸쉬한 내용 `pull request` 하기
2. 다른 팀원들이 `pull request` 확인 후 `merge`
3. GitHub에 반영 된 상태!!
4. 각 팀원들 로컬로 돌아와서 브랜치 `master`로 변경 후 GitHub에서 `pull` 하기

```
# 브랜치 변경
$ git switch master

# GitHub에서 프로젝트 변경사항 반영하기
$ git pull origin master
```

1. 로컬에 `pull` 하면서 프로젝트 변경사항이 반영이 되었음, 이제 기존의 사용했던 브랜치 삭세

```
$ git branch -d letgodchan0/0602

# master와 관계 없이 강제로 삭제하려면 
$ git branch -D letgodchan0/0602
```