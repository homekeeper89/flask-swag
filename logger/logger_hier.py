
def hier():
    import logging
    import logging.handlers
    log_myapp = logging.getLogger("myapp")
    log_myapp_ui = log_myapp.getChild("ui")

    log_myapp.setLevel(logging.CRITICAL)
    log_myapp_ui.setLevel(logging.DEBUG)

    h = logging.handlers.RotatingFileHandler('./log/root.log')
    h.setLevel(logging.DEBUG)
    log_myapp.addHandler(h)
    h2 = logging.handlers.RotatingFileHandler('./log/child.log')
    h2.setLevel(logging.DEBUG)
    log_myapp_ui.addHandler(h2)

    log_myapp_ui.debug('I am message from child')
    log_myapp.critical('I am message from root')

if __name__ == '__main__':
    hier()