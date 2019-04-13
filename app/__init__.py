# app/__init__.py
from flask_restplus import Api
from flask import Blueprint
from flask_restplus import Resource

user_blue = Blueprint('user', __name__)