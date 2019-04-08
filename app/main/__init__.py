# app/main/__init__.py
from flask import Flask
from .config import *
def create_app(config_name):
    app = Flask(__name__)
    settings_map = {'dev': config.DevelopmentConfig,
                    'test': config.TestingConfig,
                    'prod': config.ProductionConfig}
    import ipdb; ipdb.set_trace()
    app.config.from_object(settings_map[config_name])
    return app
