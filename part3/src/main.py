from fastapi import FastAPI  
from web import creature, explorer, user

app = FastAPI()

@app.get("/")
def top():
    return "top here"

app.include_router(explorer.router)
app.include_router(creature.router)
app.include_router(user.router)

if __name__ == "__main__":
    import uvicorn  
    uvicorn.run("main:app",reload=True)
