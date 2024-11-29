import sys
sys.path.append('/mnt/c/Users/hyoja/OneDrive/문서/GitHub/fastAPI_for_the_first_time/part3/src')

from model.creature import Creature 
from error import Duplicate, Missing 

_creatures = [
    Creature(name="Yeti",
             aka="Abominable Snowman",
             country="CN",
             area="Himalayas",
             description="Hirsute Himalayan"),

    Creature(name="Bigfoot",
             description="Yeti's Cousin Eddie",
             country="US",
             area="*",
             aka="Sasquatch"),
]

def get_all() -> list[Creature]:
    return _creatures 

def get_one(name: str) -> Creature | None:
    for _creature in _creatures:
        if _creature.name == name:
            return _creature 
    raise Missing(msg=f"Creature {name} not found")

def create(creature: Creature) -> Creature:
    if next((x for x in _creatures if x.name == creature.name), None): # 일치 할 수 있는 결과가 한 개니까 이런식의 코딩이 가능. true가 여러개면 처음에 걸린 원소가 출력된다.
        raise Duplicate(msg=f"Creature {creature.name} already exists")
    _creatures.append(creature)
    return creature 

def modify(name: str, creature: Creature) -> Creature:
    _creature = next((x for x in _creatures if x.name == creature.name), None)
    if _creature is not None:
        _creature = creature
        return _creature  
    else:
        raise Missing(msg=f"Creature {name} not found")
    
def replace(name: str, creature: Creature) -> Creature:
    _creature = next((x for x in _creatures if x.name == creature.name), None)
    if _creature is None:
        raise Missing(msg=f"Creature {name} not found")
    
    _creature = creature
    return _creature

def delete(name: str) -> bool:
    if not name:
        return False

    _creature = next((x for x in _creatures if x.name == name), None)
    if _creature is None:
        raise Missing(msg=f"Explorer {name} not found")
    
    _creatures.remove(_creature)
    return True 
