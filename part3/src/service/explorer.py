import sys
sys.path.append('/mnt/c/Users/hyoja/OneDrive/문서/GitHub/fastAPI_for_the_first_time/part3/src')

from model.explorer import Explorer  
import data.explorer as data  

def get_all() -> list[Explorer]:
    return data.get_all() 

def get_one(name: str) -> Explorer | None:
    return data.get_one(name)

def create(explorer: Explorer) -> Explorer:
    return data.create(explorer)

def replace(name: str, explorer: Explorer) -> Explorer:
    return data.replace(name, explorer)

def modify(name: str, explorer: Explorer) -> Explorer:
    return data.modify(name, explorer)

def delete(name: str) -> bool:
    return data.delete(name)
