from flask import Blueprint
routes = Blueprint('routes', __name__)

from .home import *
from .user import *
from .organization import *
from .task import *