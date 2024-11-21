import bcrypt 

pswd = 'pass1234' # 비밀번호 설정
pswd_to_byte_string = bytes(pswd,'utf-8') # byte string으로 변경
b = bcrypt.hashpw( # 암호화
    pswd_to_byte_string,
    bcrypt.gensalt(rounds=12) # salt추가와 key stretshing
    )
print(b) # hashing 결과
print(bcrypt.checkpw('pass1234'.encode('utf-8'),b)) # 체크1
print(bcrypt.checkpw(bytes('pass1233','utf-8'),b)) # 체크2

