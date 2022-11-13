from config import Config
import jwt
from jwt.exceptions import ExpiredSignatureError
from datetime import timedelta, datetime


class TokenUtil(object):

    @staticmethod
    def get_user_token(data: dict) -> str:
        '''
        :param data: 用户数据
        :return:
        '''
        # exp是过期时间，即当前时间加上配置的token过期时间
        token_data = dict({"exp": datetime.utcnow() + timedelta(hours=Config.EXPIRED_HOUR)}, **data)
        return jwt.encode(token_data, key=Config.KEY)

    @staticmethod
    def parse_user_token(token: str) -> dict:
        '''
        :param token: 解析token
        :return:
        '''
        try:
            return jwt.decode(token, key=Config.KEY, algorithms=["HS256"])
            # token 过期
        except ExpiredSignatureError:
            raise Exception("token已过期, 请重新登录")
            # 解析失败
        except Exception:
            raise Exception("token解析失败, 请重新登录")
