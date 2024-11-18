from jose import jwt 
import bcrypt 

pswd = 'pass1234'
b = bcrypt.hashpw(pswd.encode('utf-8'),bcrypt.gensalt())
print(b)
print(bcrypt.checkpw('pass1234'.encode('utf-8'),b))
print(bcrypt.checkpw(bytes('pass1233','utf-8'),b))

