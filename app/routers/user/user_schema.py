from datetime import datetime

from app.models.base import ToolSchema, ResponseDto
from pydantic import BaseModel, Field, validator
import hashlib
from config import Config


class RegisterUserBody(BaseModel):
    username: str = Field(..., title="用户名", description="必传")
    password: str = Field(..., title="密码", description="必传")
    name: str = Field(..., title="姓名", description="必传")
    email: str = Field(..., title="邮箱号", description="必传")

    @validator('username', 'password', 'name', 'email')
    def check_field(cls, v):
        return ToolSchema.not_empty(v)


    # 该方法给password加密
    @validator('password')
    def md5_decor(cls, value):
        m = hashlib.md5()
        content = f"{value}key={Config.KEY}"
        m.update(content.encode('utf-8'))
        return m.hexdigest()


class LoginUserBody(BaseModel):
    username: str = Field(..., title="用户名", description="必传")
    password: str = Field(..., title="密码", description="必传")

    @validator('username', 'password')
    def check_field(cls, v):
        return ToolSchema.not_empty(v)

    # 该方法给password加密
    @validator('password')
    def md5_decor(cls, value):
        m = hashlib.md5()
        content = f"{value}key={Config.KEY}"
        m.update(content.encode('utf-8'))
        return m.hexdigest()


class UserDto(BaseModel):
    username: str
    name: str
    email: str
    role: int
    is_valid: bool
    last_login_time: datetime

    class Config:
        orm_mode = True
        # json_encoders = {
        #     datetime: lambda v: v.strftime("%Y-%m-%d %H:%M:%S")
        # }



class UserTokenDto(UserDto):
    token: str


class LoginResDto(ResponseDto):
    msg: str = '登录成功'
    data: UserTokenDto
