from flask import Blueprint

api = Blueprint(__name__, 'api')

from . import views, errors
