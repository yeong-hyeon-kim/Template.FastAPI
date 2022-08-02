## 📕 프로젝트 개요(Introduce Project)

### FAST API

* Fast API를 이용하여 RESTful를 확인합니다.

## 🏷️ 기능(Function)

1. [GET](#GET)
2. [POST](#POST)
3. [INSERT](#INSERT)
4. [DELETE](#DELETE)

## 💡 REST(Representational State Transfer)?

* 자원(Resource)을 이름으로 구분하여 해당 자원의 상태(정보)를 주고 받는 모든 것을 의미합니다.
  * 상태(정보) 전달
    * 데이터가 요청되는 시점에서 자원의 상태(정보)를 전달합니다.
    * `JSON`, `XML`를 통해 데이터를 주고 받는 것이 일반적입니다.
  * 자원(Resource)의 표현(Representation)
    * 자원(Resource) : 데이터베이스, 문서, 그림, 데이터 등
    * 자원의 표현 : 사용자 정보가 자원일 때, 그 자원의 별명을 `Users`라고 하는게 자원의 표현 입니다.

### REST(Representational State Transfer)

* 기본적으로 웹의 기존 기술과 HTTP 프로토콜을 그대로 활용하기 때문에 `웹의 장점을 최대한 활용할 수 있는 아키텍처 스타일` 입니다.
* HTTP URL를 통해 자원(Resource)을 명시합니다.
  * `http://localhost:anyPort/Users/1`
  * `http://localhost:anyPort/자원(Resource)/고유값(ID)`
* 모든 자원(Resource)에 고유값(ID)인 HTTP URL를 부여합니다.
  
### CRUD Operation

|CRUD|Operation|
|-|-|
|Create|생성(POST)|
|Read|조회(GET)|
|Update|수정(PUT)|
|Delete|삭제(DELETE)|
|HEAD| header 정보 조회(HEAD)|

## 💡 RESTful?

* REST(Representational State Transfer) API 설계 규칙을 올바르게 지키는 웹 서비스를 `RESTful` 이라고 합니다.
  * ✔ `http://localhost:anyPort/Users/1`
* 모든 CRUD 기능을 POST로 처리하거나, Route에 리소스(Resource), 고유값(ID) 외의 정보가 들어가는 경우 `REST` 이지만 `Full(완벽)` 하지는 못하는 시스템 입니다.
  * ❌ `http://localhost:anyPort/Users/UserName`

## 💻 개발 환경(Develop Environment)

### 세부 환경(Environment Detail)

||운영체제(OS)|언어(Language)|프레임워크(Framework)|종속성(Dependency)|
|-|:-:|:-:|:-:|:-:|
|명칭(Name)|![Windows](https://img.shields.io/badge/Windows-0078D6?style=flat-square&logo=Windows&logoColor=white)|![PYTHON](https://img.shields.io/badge/PYTHON-3776AB?style=flat-square&logo=Python&logoColor=white)|![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=FastAPI&logoColor=white)|![PY-PI](https://img.shields.io/badge/PYPI-3775A9?style=flat-square&logo=PyPI&logoColor=white)|
|버전(Version)|`10, 11`|`3.10`|`0.76`|[requirements](./requirements.txt)|

## 📖 비고(Remark)

### Requried Python Packages

* 'FastAPI'
  * `pip install fastapi`
* 'gunicorn'
  * `pip install gunicorn`

### Run Server

* `uvicorn main:app --reload`
