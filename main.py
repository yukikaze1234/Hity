from app import huhuhu
from app.utils.logger import Log
from app.models import Base,engine

Base.metadata.create_all(engine)


@huhuhu.get('/')
async def root():
    logger = Log('测试模块')
    logger.info('欢迎来到数据工厂')
    return {"message": "hello world"}
