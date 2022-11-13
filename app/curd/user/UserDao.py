from datetime import datetime

from sqlalchemy import or_, func
from app.utils.base_exception import BaseException
from app import Log
from app.models import Session
from app.models.user import User
from app.routers.user.user_schema import LoginUserBody
from config import Permission


class UserDao(object):
    log = Log('UserDao')

    @classmethod
    def register_user(cls, username: str, name: str, password: str, email: str) -> None:
        '''

        :param username: 用户名
        :param name:  姓名
        :param password:  密码
        :param email: 邮箱
        :return:
        '''
        with Session() as session:
            users = session.query(User).filter(or_(User.username == username, User.email == email)).first()
            if users:
                raise Exception('用户名或者邮箱重复，请更换')

            count = session.query(func.count(User.id)).group_by(User.id).count()

            user = User(username, name, password, email)
            if count == 0:
                user.role = Permission.ADMIN
            session.add(user)
            session.commit()

    @classmethod
    def login_user(cls, data: LoginUserBody) -> User:
        '''

        :param username: 用户名
        :param password:  密码
        :return:
        '''
        with Session() as session:
            user = session.query(User).filter(User.username == data.username, User.password == data.password).first()
            if user is None:
                raise BaseException('用户名或者密码错误')
            if user.is_valid:
                raise BaseException('账号已经被冻结，请联系管理员')
            user.last_login_time = datetime.now()
            session.refresh(user)
            return user