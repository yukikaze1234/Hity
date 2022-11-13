import logbook
from logbook.more import ColorizedStderrHandler
from config import Config,FilePath

class Log(object):
    def __init__(self,name='hity',filename=FilePath.LOG_NAME):
        self.logger = logbook.Logger(name)
        self.logger.handlers = []
        # 日志打印到文件
        log_file = logbook.FileHandler(filename, encoding='utf-8')
        # 日志打印到控制台
        log_std = ColorizedStderrHandler(bubble=True)
        logbook.set_datetime_format("local")
        self.logger.handlers.append(log_std)
        self.logger.handlers.append(log_file)

    def info(self, *args, **kwargs):
        return self.logger.info(*args, **kwargs)

    def error(self, *args, **kwargs):
        return self.logger.error(*args, **kwargs)

    def warning(self, *args, **kwargs):
        return self.logger.warning(*args, **kwargs)

    def debug(self, *args, **kwargs):
        return self.logger.debug(*args, **kwargs)


