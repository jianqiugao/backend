from fastapi import APIRouter, Depends, HTTPException, status, Request
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.database import get_db
from app.setting import AUTH_SCHEMA
from utils.token import create_token
from .schemas import Token, User, UserCreate
from .services import authenticate_user, get_user, create_user, get_current_user

route = APIRouter(tags=['登录'])  # 在API文档中定义当前应用路由的标签


@route.post("/login", response_model=Token)  # 把这个接口绑定上是为了每访问一下这个就
async def login(form: OAuth2PasswordRequestForm = Depends(),
                db: Session = Depends(get_db)):
    user = authenticate_user(db, form.username, form.password)

    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="用户名或者密码无效",
                            headers={"WWW.Authenticate": "Bearer"})
    access_token = create_token(data={'username': user.username})  # 发放令牌，通过jwt对整个字典加密，包括了释放token的时间，把名字和时间加入token
    return {"access_token": access_token, "token_type": "bearer"}  # 登录的时候验证通过返回令牌，后续用户在访问的时候把这个token加到头文件中，同时会吧bearer也加上去，下次访问的时候就会自动带上这个头


@route.post('/createuser')  # , dependencies=[Depends(AUTH_SCHEMA)] # 验证头里面有没有这个 "Authenticate":"bearer" 而且这个bear后面会加一个
async def createuser(user: UserCreate, db: Session = Depends(get_db)):
    dbuser = get_user(db, user.username)
    if dbuser:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="用户名已存在",
                            )
    return create_user(db, user)


@route.get('/userinfo', response_model=User)
async def userinfo(request: Request,user: User = Depends(get_current_user)):#
    return user
