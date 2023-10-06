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
from 测试1 import data

print(data)