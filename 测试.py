from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer
import uvicorn

# app = FastAPI()
#
# oauth_scheme = OAuth2PasswordBearer(tokenUrl='login')
#
#
# @app.get("/items/")
# async def read_item(token: str = Depends(oauth_scheme)):
#     return {'token': token}
#
#
# if __name__ == '__main__':
#     uvicorn.run(app=app)
# def func(data:str='12345'):
#     print(data)
#
# func('2345')
from passlib.context import CryptContext

_pwd_contex = CryptContext(schemes=['bcrypt'], deprecated="auto")


def verify_password(plain_password, hashed_password):
    return _pwd_contex.verify(plain_password, hashed_password)


def get_password_hash(plain_password):
    return _pwd_contex.hash(plain_password)


if __name__ == '__main__':
    password = 'data2321'
    hased_password = get_password_hash(password)
    print(hased_password)
    res = verify_password(password,hased_password)
    print(res)
