import datetime
from jose import JOSEError, jwt

SECRET_KEY = '$2b$12$qcc5yi1sDylNxAvOOT7ke.3YflUUnCkxJTafRoYD0pdy6RxGG3NGK'
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 5


def create_token(data: dict):
    to_encode = data.copy()
    expires_delta = datetime.timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    expire = datetime.datetime.now() + expires_delta
    to_encode.update({'exp': expire})
    encode_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encode_jwt


def extract_token(token: str):
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])  # 采用解密算法把token中的信息解密出来
    return payload.get('username')
