import sys
sys.path.append('/mnt/c/Users/hyoja/OneDrive/문서/GitHub/fastAPI_for_the_first_time/part3/src')

from datetime import timedelta, datetime  
import os 
from jose import jwt 
import bcrypt 
from model.user import PublicUser, PrivateUser, SignInUser 

if os.getenv("CRYPTID_UNIT_TEST"):
    from fake import user as data 
else:
    from data import user as data

SECRET_KEY = "keep-it-secret-keep-it-safe"
ALGORITHM = "HS256"

def verify_password(plain: str, hash: str) -> bool:
    password_bytes = plain.encode('utf-8')
    hash_bytes = hash.encode('utf-8')
    is_valid = bcrypt.checkpw(password_bytes, hash_bytes)
    return is_valid

def get_hash(plain: str) -> str:
    password_bytes = plain.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password_bytes, salt)
    return hashed_password.decode('utf-8')

def get_jwt_username(token: str) -> str | None:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        if not (username := payload.get("sub")):
            return None 
    except jwt.JWTError:
        return None 
    return username 

def get_current_user(token: str) -> PublicUser | None:
    if not (username := get_jwt_username(token)):
        return None 
    if (user := lookup_user(username)):
        return user 
    return None

def lookup_user(username: str, is_public=True) -> PublicUser | PrivateUser | None:
    if (user := data.get_one(username, is_public=is_public)):
        return user 
    return None
