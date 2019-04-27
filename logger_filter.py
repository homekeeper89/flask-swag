def filter():
    import logging
    import logging.handlers

    huge = logging.getLogger("huge")
    huge_fuga = huge.getChild("fuga")
    huge_fuga_piyo = huge_fuga.getChild("piyo")

    huge.setLevel(logging.CRITICAL)
    huge_fuga.setLevel(logging.DEBUG)

    h = logging.handlers.RotatingFileHandler('./log/huge.log')
    h.setLevel(logging.DEBUG)
    huge.addHandler(h)

    h2 = logging.handlers.RotatingFileHandler('./log/huge_fuga.log')
    h2.setLevel(logging.DEBUG)
    huge_fuga.addHandler(h2)

    h3 = logging.handlers.RotatingFileHandler('./log/huge_fuga_piyo.log')
    h3.setLevel(logging.DEBUG)
    huge_fuga_piyo.addHandler(h3)

    # huge_fuga.debug('I am message from child')
    # huge.critical('I am message from root')
    logging.debug("root mess")

if __name__ == '__main__':
    filter()