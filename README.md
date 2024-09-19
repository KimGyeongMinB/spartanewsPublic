# 프로젝트명 : spartanews

## 📖 목차
1. [프로젝트 소개](#1-프로젝트-소개)
2. [팀소개](#2-팀-소개)
3. [개발기간](#3-개발기간)
4. [주요기능](#4-주요기능)
5. [개발환경](#5-개발환경)
6. [시작하기](#6-시작하기)
7. [ERD](#7-erd)
8. [API명세](#8-api명세)
9. [와이어프레임](#9-와이어프레임)
10. [프로젝트 파일 구조](#10-프로젝트-파일-구조)
11. [역할분담](#11-역할분담)
<br>

## 1. 프로젝트 소개
DRF를 통해 뉴스목록 보여주는 api를 만드는 프로젝트

## 2. 팀 소개
김경민(팀장), 강다영, 김나희, 조민희

 [🍭팀노션 이동](https://www.notion.so/teamsparta/1e2a365b56ad4cf8acd68bff9c3c59c8/)

## 3. 개발기간
- 2024.09.12.(목) ~ 2024.09.13.(금) 필수기능
- 2024.09.14.(토) ~ 2024.09.18.(수) 추가기능

## 4. 주요기능
- **유저기능 관련:**
  <details>
   <summary>이메일인증을 통한 회원가입</summary>
  username, password, email 등을 입력해 회원가입을 요청하고, 입력한 email로 도착한 호스트의 인증메일을 클릭면 가입이 처리됨. 인증메일을 클릭하기 전까지는 해당 계정으로 로그인이 되지 않음.
  </details>
  <details>
  <summary>로그인&로그아웃</summary>
   -
  </details>
  <details>
  <summary>회원탈퇴</summary>
   비밀번호를 입력받고 탈퇴가 처리됨
  </details>
  <details>
  <summary>마이페이지</summary>
  회원정보, 내가 작성한 글, 내가 구독하는 사람이 직렬화되어 반환됨
  </details>
  <details>
  <summary>다른 사용자 구독</summary>
   스스로 구독은 불가함
  </details>
  <details>
  <summary>비밀번호 재설정</summary>
  해당 이메일로 가입된 계정이 있을시, 비밀번호 재설정에 사용할 수 있는 토큰을 이메일로 전송받음.
 </details>   

&nbsp;

- **게시기능 관련:**
  <details>
  <summary>뉴스목록 보기</summary>
   페이지네이션을 사용해 한 페이지마다 글이 5개씩 보이게 함.
  </details>
  <details>
  <summary>뉴스 상세 보기</summary>
   로그인하지 않아도 조회할 수 있음.
  </details>
  <details>
  <summary>뉴스 작성</summary>
   로그인한 사용자만 작성할 수 있음.
  </details>
  <details>
  <summary>뉴스 수정</summary>
   로그인한 사용자만 수정할 수 있음.
  </details>
  <details>
  <summary>뉴스 삭제</summary>
   작성자 본인만 삭제할 수 있음.
  </details>
  <details>
  <summary>뉴스 좋아요하기</summary>
   글 좋아요 / 좋아요취소.
  </details>
  <details>
  <summary>댓글 작성</summary>
   댓글 작성시 댓글의 기본키가 생성됨.
  </details>
  <details>
  <summary>댓글 삭제</summary>
   댓글의 기본키를 이용해 삭제함. 
  </details>
  <details>
  <summary>댓글 추천</summary>
   댓글 추천 / 추천 취소.
  </details>
  <details>
  <summary>뉴스 검색</summary>
   전체목록 view 안에서 조회함. 글제목/글내용/작성자로 검색 가능.
  </details>
  <details>
  <summary>뉴스 번역 (LLM)</summary>
   오픈AI GPT-4o-mini를 이용한 영-한 번역
  </details>
  <details>
  <summary>뉴스 요약 (LLM)</summary>
   오픈AI GPT-4o-mini를 이용한 요약. 텍스트가 입력되지 않으면 에러를 반환함.
  </details>

&nbsp;

## 5. 개발환경
<details>

- aiohappyeyeballs==2.4.0
- aiohttp==3.10.5
- aiosignal==1.3.1
- annotated-types==0.7.0
- anyio==4.4.0
- asgiref==3.8.1
- async-timeout==4.0.3
- attrs==24.2.0
- blinker==1.8.2
- certifi==2024.7.4
- charset-normalizer==3.3.2
- click==8.1.7
- colorama==0.4.6
- distro==1.9.0
- Django==4.2
- django-seed==0.3.1
- djangorestframework==3.15.2
- djangorestframework-simplejwt==5.3.1
- exceptiongroup==1.2.2
- Faker==28.0.0
- Flask==3.0.3
- frozenlist==1.4.1
- greenlet==3.1.0
- h11==0.14.0
- httpcore==1.0.5
- httpx==0.27.2
- idna==3.8
- itsdangerous==2.2.0
- Jinja2==3.1.4
- jiter==0.5.0
- jsonpatch==1.33
- jsonpointer==3.0.0
- langchain==0.3.0
- langchain-core==0.3.0
- langchain-openai==0.2.0
- langchain-text-splitters==0.3.0
- langsmith==0.1.120
- MarkupSafe==2.1.5
- multidict==6.1.0
- numpy==1.26.4
- openai==1.45.0
- orjson==3.10.7
- packaging==24.1
 </details>

## 6. 시작하기

   <details>

#### Installation

```python
git clone https://github.com/KimGyeongMinB/spartanews.git
cd spartanews
```


#### Install Dependencies
```python
pip install -r requirements.txt
```

#### Run Migrations

```python
python manage.py makemigrations
python manage.py migrate
```


#### Start the Servers
```python
python manage.py runserver
```
&nbsp;
&nbsp;
&nbsp;
&nbsp;
</details>


## 7. ERD
![erd 0919](https://github.com/user-attachments/assets/c788555d-1478-4359-bcc4-e4db6fb46c91)

&nbsp;
&nbsp;
&nbsp;
&nbsp;


## 8. API명세
![api명세 0919 2242](https://github.com/user-attachments/assets/d2f0bf36-8465-4507-9e8c-7ccb2dd8fe91)





## 9. 와이어프레임
![wf 0919](https://github.com/user-attachments/assets/4ee545de-88e0-476b-a23c-3acddcefd46f)



## 10. 프로젝트 파일 구조

```
📦 
├─ .gitignore
├─ ERD.png
├─ README.md
├─ accounts
│  ├─ __init__.py
│  ├─ admin.py
│  ├─ apps.py
│  ├─ migrations
│  │  ├─ 0001_initial.py
│  │  └─ __init__.py
│  ├─ models.py
│  ├─ serializers.py
│  ├─ tests.py
│  ├─ urls.py
│  ├─ utils.py
│  └─ views.py
├─ articles
│  ├─ __init__.py
│  ├─ admin.py
│  ├─ apps.py
│  ├─ migrations
│  │  ├─ 0001_initial.py
│  │  ├─ 0002_delete_comment.py
│  │  ├─ 0003_article_author.py
│  │  └─ __init__.py
│  ├─ models.py
│  ├─ serializers.py
│  ├─ tests.py
│  ├─ urls.py
│  └─ views.py
├─ manage.py
├─ requirements.txt
└─ spartanews
   ├─ __init__.py
   ├─ asgi.py
   ├─ settings.py
   ├─ urls.py
   └─ wsgi.py
```


&nbsp;
&nbsp;
&nbsp;

## 11. 역할분담 
* Backend
  - <b>회원가입</b> 강다영
  - <b>이메일인증</b> "
  - <b>로그인</b> "
  - <b>로그아웃</b> "
  - <b>회원탈퇴</b> "
  - <b>기사 검색</b> "
    
  - <b>비밀번호 변경</b> 김경민
  - <b>작성자 구독</b> "
  - <b>마이페이지</b> "
  - <b>전체목록 정렬</b> "
  - <b>뉴스작성시 이미지 추가/수정</b> "
  - <b>뉴스 번역</b> "
  - <b>뉴스 요약</b> "
    
  - <b>뉴스 작성</b> 조민희
  - <b>뉴스 수정</b> "
  - <b>뉴스 삭제</b> "
  - <b>뉴스 목록 보기</b> "
  - <b>뉴스 상세 보기</b> "
    
  - <b>뉴스 좋아요</b> 김나희
  - <b>댓글 작성</b> "
  - <b>댓글 삭제</b> "
  - <b>댓글 추천</b> "

&nbsp;
* etc
  + 전체 개발 일정 및 이슈 관리 - 전 팀원
  + ERD 작성 - 김나희 
  + PPT 제작 - 강다영, 김경민
  + 시연영상 제작 & 발표 - 김경민

&nbsp;

------------------------------------------------------------------------------------
