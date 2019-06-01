import logging
# https://realpython.com/python-logging/
# https://www.toptal.com/python/in-depth-python-logging
# https://www.electricmonk.nl/log/2017/08/06/understanding-pythons-logging-module/
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
    logformat = '시간: %(asctime)s  파일이름 : %(filename)s \
                함수이름 : %(funcName)s 로깅레벨: %(levelname)s \
                라인넘버: %(lineno)d 로그메세지 : %(message)s \
                로거이름: %(name)s 파일경로: %(pathname)s \
                프로세스ID: %(process)d 스레드ID : %(thread)d'
    logging.basicConfig(filename='./log/test.log',
                        level=logging.ERROR,
                        format=logformat)
    logging.debug('Hello World')
    # basicConfig를 통해서 로깅 내용을 수정할 수 있다.
    # 위 내용대로 하면 설정이 바뀌며 디버깅 레벨 이상부터 출력이된다
    # 폴더 위치도 설정되어있음

def four():
    logger = logging.getLogger('hoge.fuga.piyo')
    logger.setLevel(logging.INFO)

    handler = logging.FileHandler('./log/test.log')
    handler.setLevel(logging.INFO)

    filter = logging.Filter('hoge.fuga')
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')

    handler.setFormatter(formatter)
    handler.addFilter(filter)
    logger.addHandler(handler)
    logger.addFilter(filter)

    logger.debug('deb')
    logger.info('info mess')
    # 로거 작성 순서
    # 1. 로거 작성(로거 계층 생성)
    # 2. 로거 레벨 셋
    # 3. 핸들러 작성(파일로 할지, print할지 등)
    # 4. 필터 작성 -> 이건 뭐하는건지 잘 모르겟음
    # 5. 포맷터 작성 : 로깅 모양 설정
    # 6. 합치기 : 핸들러 + 포매터 -> 핸들러 + 필터 -> 로거 + 핸들러 -> 로거+필터
    # 자식 로거는 메시지를 부모에게 전달,
    # logging.getLogger('hoge.fuga')
    # 필터는 로거 이름에 따라 실행된다. 현재 필터는 hoge.fuga가 설정되어있음.

def five():
    logger = logging.getLogger('hoge.fuga.piyo')
    logger.setLevel(logging.INFO)

    handler = logging.FileHandler('./log/filter.log')
    handler.setLevel(logging.INFO)

    filter = logging.Filter('thanks')
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')

    handler.setFormatter(formatter)
    handler.addFilter(filter)
    logger.addHandler(handler)
    logger.addFilter(filter)

    logger.debug('deb')
    logger.info('info mess')

if __name__ == "__main__":
    #four()
    # five()
    three()