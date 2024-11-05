import sys

sys.path.append('/mnt/c/Users/hyoja/OneDrive/문서/GitHub/fastAPI_for_the_first_time/part3/src')

from model.creature import Creature 

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
    return None 

def create(creature: Creature) -> Creature:
    return creature 

def modify(name: str, creature: Creature) -> Creature:
    return creature  

def replace(name: str, creature: Creature) -> Creature:
    return creature

def delete(name: str) -> bool:
    for _creature in _creatures:
        if _creature.name == name: 
            return True 
    return False

