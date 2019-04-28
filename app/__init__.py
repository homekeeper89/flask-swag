# app/__init__.py
from flask_restplus import Api
from flask import Blueprint
from flask_restplus import Resource
from .main.controller import userApi as user_api_model

user_api = Blueprint('EntryPoint-Blueprint', __name__, url_prefix='/api/v1')

user_api_desc = Api(user_api,
                    title = 'Flask-Swagger Application',
                    version = '1.0',
                    description = 'User API desc for web service',
                    doc='/docs/'
)

user_api_desc.add_namespace(user_api_model, path='/user')
