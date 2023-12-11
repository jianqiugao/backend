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
# ---------------------------------加密解密--------------------------
# from passlib.context import CryptContext
#
# _pwd_contex = CryptContext(schemes=['bcrypt'], deprecated="auto")
#
#
# def verify_password(plain_password, hashed_password):
#     return _pwd_contex.verify(plain_password, hashed_password)
#
#
# def get_password_hash(plain_password):
#     return _pwd_contex.hash(plain_password)
#
#
# if __name__ == '__main__':
#     password = 'data2321'  # 密码不明文存储而是通过哈希后进行存储，当再次进来之后继续用这个哈希进行验证
#     hased_password = get_password_hash(password)
#     print(hased_password)
#     res = verify_password(password, hased_password)
#     print(res)

# 数据库的增删改查crud

# from flask import Flask, request, jsonify
# from flask_sqlalchemy import SQLAlchemy
#
# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
# db = SQLAlchemy(app)
#
# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(80), nullable=False)
#     email = db.Column(db.String(120), nullable=False)
#
# # 增、删、改、查
# @app.route('/users', methods=['POST'])
# def create_user():
#     data = request.get_json()
#     new_user = User(name=data['name'], email=data['email'])
#
#     db.session.add(new_user)
#     db.session.commit()
#     return jsonify({'message': 'User created successfully'})
#
# # 添加其他路由来实现查询、更新和删除操作
#
#
#
# if __name__ == '__main__':
#     db.create_all()
#     app.run(debug=True)

from sqlalchemy import create_engine, Column, Integer, String,ForeignKey
import pymysql
from sqlalchemy.orm import sessionmaker, declarative_base, relationship
pymysql.install_as_MySQLdb()
# 创建数据库连接
engine = create_engine('mysql://root:123456@localhost/nucleic')

# 创建数据模型
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    email = Column(String(50))
    course_s = relationship("Course", back_populates="use_r") # 看一下user链接到下一张表

class Course(Base):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    student_id = Column(Integer, ForeignKey('users.id'))
    use_r = relationship("User", back_populates="course_s")


# 创建表
Base.metadata.create_all(engine)

# 插入数据
Session = sessionmaker(bind=engine)
session = Session()

new_user = User(name='John Doe', email='john@example.com')
session.add(new_user)
session.commit()

newcourse = Course(name='jian',student_id=5)
session.add(newcourse)
session.commit()

# 查询数据
user = session.query(User).filter(User.name=='John Doe').first()
print(user.name, user.email)

# 更新数据
user.email = 'new_email@example.com'
session.commit()

# # 删除数据
# session.delete(user)
# session.commit()

# from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
# from sqlalchemy.orm import declarative_base, relationship, sessionmaker
#
# Base = declarative_base()
#
# class User(Base):
#     __tablename__ = 'users'
#     id = Column(Integer, primary_key=True)
#     name = Column(String(50))
#     email = Column(String(50))
#     courses = relationship("Course", back_populates="user")
#
# class Course(Base):
#     __tablename__ = 'courses'
#     id = Column(Integer, primary_key=True)
#     name = Column(String(50))
#     student_id = Column(Integer, ForeignKey('users.id'))
#     user = relationship("User", back_populates="courses")
#
# engine = create_engine('sqlite:///mydatabase.db', echo=True)
# Base.metadata.create_all(engine)
