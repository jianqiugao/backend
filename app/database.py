from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from app.setting import *

engine = create_engine(f"mysql://{DB_USER_NAME}:{DB_PASSWORD}@{DB_HOST}/{DB_DATABASE}")

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def generate_tables():
    Base.metadata.create_all(bind=engine)  # 在数据库中生成表
