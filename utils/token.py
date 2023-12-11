import datetime
from jose import JOSEError, jwt  # 主要是把字典编码成字符串然后解码回来方便传输

SECRET_KEY = '$2b$12$qcc5yi1sDylNxAvOOT7ke.3YflUUnCkxJTaf'
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 5


def create_token(data: dict):
    to_encode = data.copy()
    expires_delta = datetime.timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    expire = datetime.datetime.now() + expires_delta
    print(expire)
    to_encode.update({'exp': expire})
    encode_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encode_jwt


def extract_token(token: str):
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])  # 采用解密算法把token中的信息解密出来
    import time
    time_ = float(payload.get('exp'))
    local_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time_))
    print(local_time)
    return payload.get('username')


if __name__ == '__main__':
    data = {'username': '123'}
    res = create_token(data)
    res = extract_token(res)
    print(res)
