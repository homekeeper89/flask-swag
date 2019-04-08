import os


# uncomment the line below for postgres database url from environment variable
# postgres_local_base = os.environ['DATABASE_URL']
# app/main/config.py
class Config:
    DB = {
        'addr': 'localhost',
        'id': 'root',
        'pass': 'root'
    }
    SECRET_KEY = os.getenv('SECRET_KEY', 'my_precious_secret_key')
    DEBUG = False


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    def __init__(self):
        self.DB['addr'] = '127.0.0.1'
        self.DB['db'] = 'dev_table'


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    def __init__(self):
        self.DB['addr'] = '255.255.255.255'
        self.DB['db'] = 'test_table'


class ProductionConfig(Config):
    DEBUG = False


key = Config.SECRET_KEY

config_by_name = dict(
    dev=DevelopmentConfig(),
    test=TestingConfig(),
    prod=ProductionConfig()
)