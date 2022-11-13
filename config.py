import os.path


class Config(object):
    '''
    mysql配置类
    '''
    # 数据库连接信息
    HOST = '127.0.0.1'
    PORT = '3306'
    PWD = 'qazplm123456'
    USER = 'root'
    DBNAME = 'hity'

    # 数据库配置
    SQLALCHEMY_DATABASE_URI: str = f"mysql+pymysql://{USER}:{PWD}@{HOST}:{PORT}/{DBNAME}"

    KEY = 'helloalee'  # 盐值
    EXPIRED_HOUR = 6


class Text(object):
    '''
    描述配置
    '''
    TITLE = 'Hity'
    VERSION = 'V1.0'
    DESC = '欢迎'

class  FilePath(object):
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))  #后端服务目录  D:\pythonProject\Hity
    LOG_FILE_PATH = os.path.join(BASE_DIR,'logs')
    if not os.path.isdir(LOG_FILE_PATH) : os.mkdir(LOG_FILE_PATH)
    LOG_NAME = os.path.join(LOG_FILE_PATH,'hu.log')
    APP_PATH = os.path.join(BASE_DIR,'app')
    CURD_PATH = os.path.join(APP_PATH,'curd')

class Permission(object):
    MEMBERS = 0  #成员
    LEADER = 1  #组长
    ADMIN = 2 #超管

HTTP_CODE_MSG  = {
    400:'请求参数有误，请检查',
    401:'token校验失败，请重新登录',
    404:'请求路径找不到',
    405:'请求方法不支持',
    408:"请求超时",
    500:"服务器内部错误",
    302:"请求方法不支持",

}
