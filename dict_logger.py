import logging
from logging.config import dictConfig

config = {
    'version':1,
    'disable_existing_loggers':False,
    'formatters':{
        'example':{
            'format':'%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        },
    },
    'filters':{
        'hoge-filter':{
            'name':'hoge.fuga'
        },
    },
    'handlers':{
        'file':{
            'level':'INFO',
            'class':'logging.FileHandler',
            'filename':'./log/test.log',
            'formatter':'example',
            'filters':['hoge-filter'],
        },
    },
    'loggers':{
        'hoge':{
            'handlers':['file'],
            'level':'INFO',
            'propagate':True,
        },
    },
}
def one():
    dictConfig(config)
    logger = logging.getLogger('hoge.fuga.piyo')
    logger.debug('debug')
    logger.info('info')

if __name__=='__main__':
    one()
