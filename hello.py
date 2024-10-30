from fastapi import FastAPI, Response, Header

app = FastAPI()

@app.get("/agent")
def greet1(user_agent: str = Header()):
    return user_agent

@app.get("/header/{name}/{value}")
def greet(name: str, value: str, response: Response):
    response.headers[name] = value
    return "normal body"

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("hello:app",reload=True)
