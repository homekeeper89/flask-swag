#app/main/controlelr/__init__.py
from app import *
from flask import jsonify
from flask.views import MethodView
from flask_restplus import Resource
from ..dto.user_dto import *

user_api_md = UserDto.api

from . import user