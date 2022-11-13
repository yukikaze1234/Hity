from typing import Any
from pydantic import BaseModel
from app.utils.base_exception import BaseException

class ResponseDto(BaseModel):
    code = 200
    msg = '注册成功'
    data: Any = None





class ToolSchema(object):
    @staticmethod
    def not_empty(v):
        if isinstance(v, str) and len(v.strip()) == 0:
            raise BaseException('字段不允许为空')
        if not isinstance(v, int):
            if not v:
                raise BaseException('字段不允许为空')
        return v