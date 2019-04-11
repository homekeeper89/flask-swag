import os


# uncomment the line below for postgres database url from environment variable
# postgres_local_base = os.environ['DATABASE_URL']
# app/main/config.py

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'my_precious_secret_key')
    DEBUG = False
    DB = {
        'addr': 'localhost',
        'id': 'root',
        'pass': 'root'
    }


class DevelopmentConfig(Config):
    NAME = 'dev'
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    def __init__(self):
        self.DB['addr'] = 'dev_host'

class TestingConfig(Config):
    def __init__(self):
        self.DB['addr'] = 'test_host'
    DEBUG = True
    TESTING = True
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    DEBUG = False
    def __init__(self):
        self.DB['addr'] = 'prod_host'


key = Config.SECRET_KEY

config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)