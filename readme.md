main 主文件，用于管理fastapi应用实例
app database负责数据库连接，setting负责全局配置项
auth 登录认证模块
checkin 登记模块
person 预约模块
utlis 公用的函数或者类
这里的加密通过python-jose进行，把字典编码成字符串进行传输
from jose import JOSEError, jwt

encode_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])  # 采用解密算法把token中的信息解密出来

另外，密码验证通过passlib.context中的CryptContext进行实现

db.query(UserInDB).all() 
返回的就是这个UserInDB的类的实例列表
