import logging

def one():
    logging.debug("debug")
    logging.warning('warning message')
    # WARNING:root:warning message
    # 로그레벨이 기본 워닝이기에 디버그 메세지가 나오지않는다

def two():
    favorite_thing = 'bouldering'
    logging.error('i Love %s!', favorite_thing)
    # ERROR:root:i Love bouldering!

def three():
    logformat = '%(asctime)s %(levelname)s %(message)s'
    logging.basicConfig(filename='/tmp/test.log',
                        level=logging.DEBUG,
                        format=logformat)
    # basicConfig를 통해서 로깅 내용을 수정할 수 있다.
    # 위 내용대로 하면 설정이 바뀌며 디버깅 레벨 이상부터 출력이된다
    # 폴더 위치도 설정되어있음

def four():
    logger = logging.getLogger('hoge.fuga.piyo')
    logger.setLevel(logging.INFO)

    handler = logging.FileHandler('/tmp/test.log')
    handler.setLevel(logging.INFO)

    filter = logging.Filter('hoge.fuga')
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')

    handler.setFormatter(formatter)
    handler.addFilter(filter)
    logger.addHandler(handler)
    logger.addFilter(filter)



if __name__=='__main__':
    one()
    two()