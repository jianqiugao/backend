from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from auth.services import AUTH_SCHEMA
from utils.response import PageResponse
from .schemas import CheckIn
from .services import QueryParams, save_checkin, list_checkin

route = APIRouter(tags=['登记'])


@route.post('/submit', response_model=CheckIn)
async def submit(data: CheckIn, db: Session = Depends(get_db)):
    return save_checkin(db, data)


@route.get('/get', response_model=PageResponse, dependencies=[Depends(AUTH_SCHEMA)])
async def get(params: QueryParams = Depends(), db: Session = Depends(get_db)):
    return list_checkin(db, params)  # 返回查询的预约信息
