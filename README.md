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

