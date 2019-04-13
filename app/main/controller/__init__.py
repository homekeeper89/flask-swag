#app/main/controlelr/__init__.py
from app import *
from flask import Blueprint
from flask_restplus import Resource

user_blue = Blueprint('user', __name__)

from . import user