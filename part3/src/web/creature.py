import sys
sys.path.append('/mnt/c/Users/hyoja/OneDrive/문서/GitHub/fastAPI_for_the_first_time/part3/src')

from fastapi import APIRouter  
from model.creature import Creature  
import service.creature as service 

router = APIRouter(prefix = "/creature")

@router.get("/")
def get_all() -> list[Creature]:
    return service.get_all()

@router.get("/{name}")
def get_one(name) -> Creature | None:
    return service.get_one(name)

@router.post("/")
def create(creature: Creature) -> Creature:
    return service.create(creature)

@router.patch("/{name}")
def modify(name, creature: Creature) -> Creature:
    return service.modify(name, creature)

@router.put("/{name}")
def replace(name, creature: Creature) -> Creature:
    return service.replace(name, creature)

@router.delete("/{name}")
def delete(name: str):
    return service.delete(name)
