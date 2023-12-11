from fastapi import Depends, HTTPException, status
from jose import JWTError
from sqlalchemy.orm import Session
from sqlalchemy import func

from app.database import get_db, SessionLocal
from app.setting import *
from utils.password import get_password_hash, verify_password
from utils.token import extract_token
from models import UserInDB
from .schemas import UserCreate


# 创建初始管理员账号
def init_admin_user():
    db = SessionLocal() # 创建事务
    cnt = db.query(func.count(UserInDB.username)).scalar() # 传递聚合函数
    if cnt == 0:
        user = UserInDB(username=AUTH_INIT_USER, hashed_password=get_password_hash(AUTH_INIT_PASSWORD))
        db.add(user)  # 通过add进行添加
        db.commit()  # 提交事务
    db.close()


# 获取单个用户
def get_user(db: Session, username: str):
    return db.query(UserInDB).filter(UserInDB.username == username).first()


# 创建一个用户
def create_user(db: Session, username: UserCreate):
    hashed_password = get_password_hash(username.password)
    db_user = UserInDB(username=username.username, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


# 验证用户和密码
def authenticate_user(db: Session, username: str, password: str):
    user = get_user(db, username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user


# 获取当前用户信息的依赖函数

async def get_current_user(token: str = Depends(AUTH_SCHEMA),db: Session = Depends(get_db)):

    Invalid_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="无效的用户数据",
                                      headers={"WWW.Authenticate": "Bearer"}, )
    try:
        username: str = extract_token(token)
        if username is None:
            raise Invalid_exception
    except JWTError:
        raise Invalid_exception
    user = get_user(db, username=username)
    if user is None:
        raise Invalid_exception
    return user
