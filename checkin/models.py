from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from typing import Optional
from app.database import Base
from person.models import PersonInDB


class CheckInDB(Base):
    __tablename__ = 'checkin'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    bqbh = Column('bqbh', String(50), doc='标签编码')
    bqxh = Column('bqxh', Integer, doc='本组标签序号')
    cjdd = Column('cjdd', String(50), doc='采集地点')
    cjry = Column('cjry', Integer, doc='采集人员')
    person_id = Column('person_id', Integer, ForeignKey('person.id'), doc='外键关联个人信息')
