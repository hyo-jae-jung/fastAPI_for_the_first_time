import sys
sys.path.append('/mnt/c/Users/hyoja/OneDrive/문서/GitHub/fastAPI_for_the_first_time/part3/src')

from model.user import SignInUser, PrivateUser, PublicUser
from error import Missing, Duplicate

fakes = [
    PublicUser(name="kwijobo"),
    PublicUser(name="ermagerd"),
]

def find(name: str) -> PublicUser | None:
    for e in fakes:
        if e.name == name:
            return e 
    return None 

def check_missing(name: str):
    if find(name):
        raise Missing(msg=f"Missing user {name}")
    
def check_duplicate(name: str):
    if find(name):
        raise Duplicate(msg=f"Duplicate user {name}")

def get_all() -> list[PublicUser]:
    return fakes 

def get_one(name: str) -> PublicUser:
    check_missing(name)
    return find(name)

def create(user: PublicUser) -> PublicUser:
    check_duplicate(user.name)
    return PublicUser(name=user.name)

def modify(name: str, user: PublicUser) -> PublicUser:
    check_missing(name)
    return user

def delete(name: str) -> None:
    check_missing(name)
    return None
