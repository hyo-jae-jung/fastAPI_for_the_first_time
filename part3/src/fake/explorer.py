import sys

sys.path.append('/mnt/c/Users/hyoja/OneDrive/문서/GitHub/fastAPI_for_the_first_time/part3/src')

from model.explorer import Explorer 

_explorers = [
    Explorer(name="Claude Hande",
             country="FR",
             description="보름달이 뜨면 만나기 힘듦"),
    Explorer(name="Noah Weiser",
             country="DE",
             description="눈이 나쁘고 벌목도를 가지고 다님"),
]

def get_all() -> list[Explorer]:
    return _explorers

def get_one(name: str) -> Explorer:
    for _explorer in _explorers:
        if _explorer.name == name:
            return _explorer 
    return None

def create(explorer: Explorer) -> Explorer:
    return explorer  

def modify(name: str, explorer: Explorer) -> Explorer:
    return explorer 

def replace(name: str, explorer: Explorer) -> Explorer:
    return explorer

def delete(name: str) -> bool:
    for _explorer in _explorers:
        if _explorer.name == name:
            return True  
    return False 

