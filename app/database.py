from sqlalchemy import create_engine  # 创建连接引擎
from sqlalchemy.orm import declarative_base, sessionmaker  # declarative_base()：这个函数创建了一个基类，您可以通过继承它来定义您自己的声明式类
# 这两个都是工厂函数，前者用来定义类后者用来定义，返回的应该都是一个函数指针
from app.setting import *

engine = create_engine(f"mysql://{DB_USER_NAME}:{DB_PASSWORD}@{DB_HOST}/{DB_DATABASE}")

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)  # 创建一个事务

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def generate_tables():
    Base.metadata.create_all(bind=engine)  # 在数据库中生成表


if __name__ == '__main__':
    generate_tables()  # 先在数据库中创建一下表
