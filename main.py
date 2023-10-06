import uvicorn
from fastapi import FastAPI, Depends,Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse

from app.database import generate_tables
from app.setting import AUTH_SCHEMA
from auth.router import route as auth_router
from auth.services import init_admin_user
from checkin.router import route as checkin_router
from person.router import route as person_router

app = FastAPI()

oringins = ["http://localhost:8000",
            "http://localhost:8000"]

app.add_middleware(CORSMiddleware,
                   allow_origins=oringins,
                   allow_credentials=True,
                   allow_methods=['*'],
                   allow_headers=['*']
                   )

app.include_router(checkin_router, prefix='/checkin')
dependeces = Depends((AUTH_SCHEMA))
app.include_router(person_router, prefix='/person')

app.include_router(auth_router, prefix='/auth')



# 注册静态资源文件，将前端和后端项目整合运行
app.mount('/web', StaticFiles(directory='web/dist'), 'web')
# app.mount('/h5', StaticFiles(directory='h5/dist'), 'h5')

app.get('/')


def toweb():
    return RedirectResponse('/web1/index.html')


generate_tables()
init_admin_user()
if __name__ == '__main__':
    uvicorn.run(app=app)
