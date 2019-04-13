# app/main/__init__.py
from flask import Flask
from app import user_blue
from .controller import *

def create_app(config_name):
    from . import config
    server_app = Flask(__name__)
    env = config.config_by_name[config_name]
    server_app.config.from_object(env())
    server_app.register_blueprint(user_blue)
    return server_app
