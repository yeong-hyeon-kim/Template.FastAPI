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

### REST(Representational State Transfer) 구체적 개념

* 기본적으로 웹의 기존 기술과 HTTP 프로토콜을 그대로 활용하기 때문에 `웹의 장점을 최대한 활용할 수 있는 아키텍처 스타일` 입니다.
* HTTP URL를 통해 자원(Resource)을 명시합니다.
  * `http://localhost:anyPort/Users`
  * `http://localhost:anyPort/자원(Resource)`
* 모든 자원(Resource)에 고유값(ID)인 HTTP URL를 부여합니다.
  * `http://localhost:anyPort/Users/1`
  * `http://localhost:anyPort/자원(Resource)/고유값(ID)`

### REST(Representational State Transfer) 장단점

#### 장점

* HTTP 프로토콜 표준을 최대한 활용하여 여러 장점을 함께 가져갈 수 있게 해줍니다.
* HTTP 표준 프로토콜을 사용하는 모든 플랫폼에서 사용이 가능합니다.
* 서버(Sever)와 클라이언트(Client)의 역할을 명확하게 분리할 수 있습니다.

#### 단점

* REST 자체가 공식적인 표준이 존재하지 않습니다.
* 메소드가 4가지 받에 없습니다.
* 구형 브라우저에서 완벽하게 호환되지 않습니다.

### CRUD Operation

|CRUD|Operation|
|-|-|
|Create|생성(POST)|
|Read|조회(GET)|
|Update|수정(PUT)|
|Delete|삭제(DELETE)|
|HEAD| header 정보 조회(HEAD)|

### REST(Representational State Transfer) 사용 이유

* 다양한 클라이언트[PC(Mac, Windows), SmartPhone(Glalaxy, iPhone), Tablet(Glalaxy Tab, iPad)]들의 등장
  * 기업들은 서비스를 소비자가 다양한 플랫폼에서 이용할 수 있게 만들어야하기 때문에 플랫폼에 종속되지 않는 웹 기술을 집중했습니다.
  * 모든 플랫폼에는 `HTTP 표준 프로토콜을 사용하는` 브라우저가 내장되어 있기 때문에 REST를 이용하여 `모든 플랫폼에서 이용 가능`하게 만들게 되었다고 추측할 수 있습니다.

### REST(Representational State Transfer) 특징

#### 서버-클라이언트 구조(Server-Client)

* 자원을 제공하는 족이 `Sever`, 자원을 요청하는 쪽이 `Client`

#### 무상태(Stateless)

* HTTP 프로토콜은 Stateless Protocol이므로 REST 역시 무상태성을 가집니다.
  * 비연결성(Connectionless)
    * 클라이언트와 서버가 한 번 연결된 후 서버가 클라이언트 응답을 마치면 연결을 끊어 버리는 성질 입니다.
    * 연결을 유지하기 위한 리소스를 줄이면 더 많은 연결을 할 수 있기 때문입니다.
  * 무상태 (Stateless)
    * 비연결성(Connectionless)으로 서버는 클라이언트를 식별할 수가 없어 쿠키, 세션으로 상태를 기억합니다.

#### 캐시 처리 가능(Cacheable)

* 캐싱(Caching)
  * 이미 가져온 데이터나 계산된 결과값의 복사본을 저장하여 애플리케이션 처리 속도를 향상시킵니다.
* 캐시를 사용하며 응답 시간이 빨라지고 트랜잭션이 발생하지 않기 때문에 응답시간, 성능, 서버 자원 이용률 향상시킬 수 있습니다.

#### 계층화(Layered System)

* 클라이언트(Client)는 REST API Server만 호출하므로 API Server는 순수 비즈니스 로직을 수행하고 그 앞단에 보안, 로드밸런싱, 암호화, 사용자 인증 등을 추가하여 구조상의 유연성을 줄 수 있습니다.

#### 인터페이스 일관성(Uniform Interface)

* HTTP 표준 프로토콜에 따르는 모든 플랫폼에서 사용이 가능합니다.
  * 특정 언어나 기술에 종속되지 않습니다.

## 💡 REST API?

* API(Application Programming Interface)
  * ~~데이터와 기능의 집합을 제공하여 컴퓨터 프로그램간 상호작용을 촉진하며, 서로 정보를 교환가능 하도록 하는 것~~
  * 애플리케이션에서 필요한 데이터를 서버(데이터베이스)에게 전달하고 받아주는 것.
* REST(Representational State Transfer) API(Application Programming Interface)
  * REST 기반으로 서비스 API를 구현한 것을 의미 합니다.

### REST API 특징

* REST는 HTTP 표준을 기반응로 구현하므로 HTTP를 지원하는 프로그램 언어(C#, JAVA, JAVASCRIPT)로 클라이언트, 서버를 구현할 수 있다.

### REST API 설계 기본 규칙

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
