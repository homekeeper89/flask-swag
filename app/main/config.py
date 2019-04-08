import os
# uncomment the line below for postgres database url from environment variable
# postgres_local_base = os.environ['DATABASE_URL']
# app/main/config.py
class Config:
    DB = {
    'addr'  : 'localhost',
    'id'    : 'root',
    'pass'  : 'root'
    }
    SECRET_KEY = os.getenv('SECRET_KEY', 'my_precious_secret_key')
    DEBUG = False

class DevelopmentConfig(Config):
    print('i am  Dev config')
    DEBUG = True
    Config.DB['addr'] = '127.0.0.1'
    Config.DB['db'] = 'dev_table'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class TestingConfig(Config):
    print('i am  Testing config')
    Config.DB['addr'] = '255.255.255.255'
    Config.DB['db'] = 'test_table'
    DEBUG = True
    TESTING = True
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProductionConfig(Config):
    print('i am  Prod config')
    DEBUG = False

config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)

key = Config.SECRET_KEY