import sys
sys.path.append('/mnt/c/Users/hyoja/OneDrive/문서/GitHub/fastAPI_for_the_first_time/part3/src')

from fastapi import APIRouter  
from model.explorer import Explorer
import service.explorer as service

router = APIRouter(prefix="/explorer")

@router.get("")
@router.get("/")
def get_all() -> list[Explorer]:
    return service.get_all()

@router.get("/{name}")
def get_one(name) -> Explorer | None:
    return service.get_one(name)

@router.post("/")
def create(explorer: Explorer) -> Explorer:
    return service.create(explorer)

@router.patch("/{name}")
def modify(name, explorer: Explorer) -> Explorer:
    return service.modify(name, explorer)

@router.put("/{name}")
def replace(name, explorer: Explorer) -> Explorer:
    return service.replace(name, explorer) 

@router.delete("/{name}")
def delete(name: str):
    return service.delete(name)  


