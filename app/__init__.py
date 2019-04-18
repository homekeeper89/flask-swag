# app/__init__.py
from flask_restplus import Api
from flask import Blueprint
from flask_restplus import Resource
from .main.controller import user_api_md as user_api_model

user_api = Blueprint('test_blueprint', __name__, url_prefix='/iamblueprint')

user_api_desc = Api(user_api,
                    title = 'FLASK SWAGGER WITH MEDIUM by jkim',
                    version = '0.1',
                    description = 'User API desc for web service'
)

user_api_desc.add_namespace(user_api_model, path='/testuser')
