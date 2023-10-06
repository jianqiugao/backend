from typing import List
from pydantic import BaseModel


# 用于响应分页数据的数据模型
class PageResponse(BaseModel):
    count: int
    list: List
