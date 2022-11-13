import jwt
from fastapi import FastAPI
from starlette.requests import Request
from starlette.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from config import Config
from app.utils.token import TokenUtil
from config import HTTP_CODE_MSG
from app.models.base import ResponseDto
from app.utils.logger import Log
from config import Text
from app.routers.user.user import router
from fastapi.responses import PlainTextResponse
from starlette.exceptions import HTTPException as StarletteHTTPException

huhuhu = FastAPI(title=Text.TITLE, description=Text.DESC, version=Text.VERSION)


# 全局校验token
@huhuhu.middleware('http')
async def all_process_handler(request: Request, call_next):
    response = await call_next(request)
    # 不校验，注册和登录，否则陷入死循环
    temp = str(request.url)[22:]
    if temp == 'api/user/login' or temp == 'api/user/register':
        return response
    try:
        token = request.headers['token']
        TokenUtil.parse_user_token(token)
    except:
        return JSONResponse(f"{HTTP_CODE_MSG.get(401)}")
    return response


# 注册user的路由
huhuhu.include_router(router, prefix='/api/user', tags=['用户模块'])


# 全局异常处理器
@huhuhu.exception_handler(StarletteHTTPException)
async def http_exception_handler(request, exc):
    response = ResponseDto(code=201, msg=HTTP_CODE_MSG.get(exc.status_code, exc.detail))
    return JSONResponse(content=response.dict())

    # 全局请求异常处理器


@huhuhu.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    response = ResponseDto(code=400, msg=HTTP_CODE_MSG.get(400), data=str(exc))
    return JSONResponse(response.dict())
