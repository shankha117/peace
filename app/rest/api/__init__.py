from flask import Blueprint

peace_bp = Blueprint('routes', __name__, url_prefix='/peace/v1/api')

from .user import *
