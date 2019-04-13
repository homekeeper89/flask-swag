# app/main/__init__.py
from flask import Flask

def create_app(config_name):
    from . import config
    app = Flask(__name__)
    env = config.config_by_name[config_name]
    app.config.from_object(env())

    from app.main.controller import user_blue
    
    app.register_blueprint(user_blue)
    return app
