import logging

def same():
    import logging
    import logging.handlers

    a = logging.getLogger('myapp')
    a.setLevel(logging.DEBUG)   # set root's level

    h = logging.handlers.RotatingFileHandler('./log/foo.log')
    h.setLevel(logging.DEBUG)
    a.addHandler(h)

    h2 = logging.handlers.RotatingFileHandler('./log/foo2.log')
    h2.setLevel(logging.WARNING)
    a.addHandler(h2)

    a.debug('foo message')
    a.warn('warning message')

if __name__ == '__main__':
    same()
    print(__name__)