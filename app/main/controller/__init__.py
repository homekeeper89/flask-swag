#app/main/controlelr/__init__.py
from app import *
from flask import jsonify
from flask.views import MethodView
from flask_restplus import Resource
from ..dto.user_dto import *
from ..service.user_service import *

userApi= UserDto.api
dto_user = UserDto.user

user_reg_api = UserRegisterDto.api
user_dto_register = UserRegisterDto.model


from . import user