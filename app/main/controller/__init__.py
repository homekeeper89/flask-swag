#app/main/controlelr/__init__.py
from app import *
from flask import jsonify, request
from flask.views import MethodView
from flask_restplus import Resource
from ..dto.user_dto import *
from ..service.user_service import *

user_reg_api = UserRegisterDto.api
user_dto_register = UserRegisterDto.model

userApi= UserDto.api
dto_user = UserDto.user

from . import user