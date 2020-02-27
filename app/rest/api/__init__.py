from flask import Blueprint

peace_bp = Blueprint('routes', __name__, url_prefix='/cmm/api/v1')

from .user import *
