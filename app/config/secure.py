
# 安全性配置
from app.config.setting import BaseConfig


class DevelopmentSecure(BaseConfig):
    """
    开发环境安全性配置
    """
    SQLALCHEMY_DATABASE_URI = 'mysql+cymysql://root:ace123@127.0.0.1:3306/lin-cms'

    SQLALCHEMY_ECHO = False

    SECRET_KEY = '\x88W\xf09\x91\x07\x98\x89\x87\x96\xa0A\xc68\xf9\xecJJU\x17\xc5V\xbe\x8b\xef\xd7\xd8\xd3\xe6\x95*4'


class ProductionSecure(BaseConfig):
    """
    生产环境安全性配置
    """
    SQLALCHEMY_DATABASE_URI = 'mysql+cymysql://root:ace123@127.0.0.1:3306/lin-cms'

    SQLALCHEMY_ECHO = False

    SECRET_KEY = '\x88W\xf09\x91\x07\x98\x89\x87\x96\xa0A\xc68\xf9\xecJJU\x17\xc5V\xbe\x8b\xef\xd7\xd8\xd3\xe6\x95*4'
