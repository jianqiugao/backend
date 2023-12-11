from fastapi.security import OAuth2PasswordBearer
from urllib import parse
JWT_SECRET_KEY = '2a3dsek5b6f3sdf5'
JWT_ALGORITHM ='HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 1440
AUTH_SCHEMA = OAuth2PasswordBearer(tokenUrl='auth/login')
AUTH_INIT_USER = 'admin'
AUTH_INIT_PASSWORD = 'admin'
DB_HOST = 'localhost'
DB_USER_NAME = 'root'
DB_PASSWORD = parse.quote('123456') # 把字符串编码
DB_DATABASE = 'nucleic'