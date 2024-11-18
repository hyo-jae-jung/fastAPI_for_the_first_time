처음 시작하는 FastAPI  

지은이 : 빌 루바노빅  
옳긴이 : 한용재, 한바름  


# FastAPI 특징
[주로 사용하는 기능]
파이썬 타입 힌트  
비동기 지원을 포함한 웹 머신용 Starlette  
데이터 정의 및 유효성 검사를 위한 Pydantic  

----------

# 애플리케이션
FastAPI 프레임워크  
Uvicorn 웹 서버  
HTTPie 텍스트 웹 클라이언트  
Requests 동기식 웹 클라이언트 패키지  
HTTPX 동기/비동기 웹 클라이언트 패키지

---------

# HTTP 요청
[URL 경로]  
Path parameter를 URL경로라고 표현하는듯  

/{val}  

[쿼리 매개변수]  
Query parameter  

?A=a&B=b  

[본문 : Body]
embed=True 는 request body에 JSON형식으로 데이터를 받기 위해 query parameter를 key로 사용하기위해 설정  

※ 클라이언트가 어떤 방식으로 서버에 Body를 전달하는지는 좀 더 생각해봐야 함  

[HTTP 헤더]  
Header 클래스를 사용해서 Request Header에 값을 추가 할 수도 있고 원하는 헤더를 출력 할 수도 있다.  

출력을 원하는 헤더의 키를 소문자로 변환하고 하이픈을 밑줄로 변환하면 출력 할 수 있다.  

Response 클래스를 이용해서 Response Header에 값을 추가 할 수 있다.  
아직 출력하는 방법은 모르며, Request Header와 동일하게 만들어봤지만 오류가 난다. Request Header가 나 자신인 서버가 만드는 값이라 출력의 필요성이 없어서 그런가??  


jsonable_encoder로 json으로 변환이 안되는 데이터 구조를 json과 비슷한 파이썬 데이터구조로 변환 후, json.dumps()로 변환 가능하도록 변환  

response_model로 출력하는 정보를 제한 할 수 있다.  

[자동 문서화]
http://localhost:8000/docs  


# Starlette과 비동기, 동시성

[async, await, asyncio]  

# Pydantic과 타입 힌트, 모델

파이썬에서도 타입 힌트를 사용 할 수 있지만 다른 언어처럼 오류로 처리하지 않는다.  
mypy로 타입 불일치 시 경고를 표시 할 수 있다.  

데이터그룹화를 위한 다양한 도구가 있지만 FastAPI에서 Pydantic을 사용하기 좋아서 사용  

# 의존성


# Web


# DB

# ?
DB연결 후 예시와 같이 동작은 잘 하는데 데이터가 쌓이지 않음  

pytest 사용 방법은 알겠는데 기존 DB 파일 손상 없이 메모리에서 작동한다는 걸 눈으로 확인하고 싶다  
-> os.environ["CRYPTID_SQLITE_DB"] = ":memory:" 해당 코드를 추가하면  
생성된 sample 데이터를 기준으로 Missing, Duplicate 테스트를 할 수 있는데, 그 의미가 sample 데이터를 날리지 않고 잡고있다는 것이다. -> 그래도 메모리에서 데이터의 변화를 보고싶기는 하다.  


# 구조 

web  
    서버와 직접적으로 연결하는 부분. 서버, 라우터를 설정하고 restAPI로 클라이언트와 소통하며, 요청결과로 서비스 부분을 불러온다.  
service  
    데이터와 모델 부분을 정리해서 서버로 전달하는 부분. 기능의 input, output 껍데기만 있는 추상화 부분  
data  
    데이터베이스와 직접적으로 연결해 CRUD를 진행하는 부분.  
model  
    데이터베이스의 테이블을 서버와 함께 소통하기 위한 부분.  

※ 책갈피 - 계층에 해당 내용 있음  

# salt
비밀번호를 hash 할 때 salt를 추가하면 hash 알고리즘을 알아도 salt를 모르면 decode 시 비밀번호를 알기 어렵기 때문에 보안에 이즘이 큼. bcrypt.gensalt() 사용으로 hash 생성 시 salt값을 id별 각각 다르도록 랜덤값 부여 "계정별 salt가 다르다!"  
decode 시, bcrypt.checkpw 메소드는 salt값을 추가입력 안해도 알아서 해준다... 어떻게 하는지 궁금하긴 한데.. 일단 패스  



