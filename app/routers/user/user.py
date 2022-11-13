import json

from fastapi import APIRouter
from app.curd.user.UserDao import UserDao
from app.models.base import ResponseDto
from app.routers.user.user_schema import RegisterUserBody, LoginUserBody, LoginResDto, UserDto
from app.utils.token import TokenUtil
from app.utils.base_exception import BaseException

router = APIRouter()


@router.post('/register', name='用户注册', description='用户注册', response_model=ResponseDto)
def register(data: RegisterUserBody):
    try:
        print('data is ', data)
        # print('**data.dict is', **data.dict())
        UserDao.register_user(**data.dict())
        return ResponseDto(msg='注册成功')
    except Exception as e:
        raise BaseException(str(e))


@router.post('/login', name='用户登录', description='用户登录', response_model=LoginResDto)
def register(data: LoginUserBody):
    try:
        user = UserDao.login_user(data)

        # 将类加载数据到模型中
        # user_model = UserDto.from_orm(user)
        # xx.dict() 返回模型的字段和值的字典

        # 把user模型转换为 对象实例
        user_model = UserDto.from_orm(user)

        # 注意，我们给Pydantic模型添加了一个 Config类。Config用来给Pydantic提供配置信息，这里我们添加了配置信息"orm_mode = True"。
        #
        # 配置项"orm_mode"除了可以让Pydantic读取字典类型的数据，还支持Pydantic读取属性数据，比如SQLAlchemy模型的数据。
        user_data = user_model.json()  # 转换为Json格式
        token = TokenUtil.get_user_token(json.loads(user_data))  # 转化为dict的数据，进行生成token
        setattr(user, 'token', token)
        return LoginResDto(data=user)


    except Exception as e:
        raise BaseException(f"{e}")


@router.get('/token')
def test_token():
    return {"name": "huxiaodong"}
