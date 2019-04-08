# app/main/__init__.py
from flask import Flask
from .config import *
def create_app(config_name):
    app = Flask(__name__)
    import ipdb; ipdb.set_trace()
    app.config.from_object(config.config_by_name[config_name])
    return app
