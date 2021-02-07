from flask import Blueprint, g
from flaskapp.db import get_db

bp = Blueprint('stat', __name__, url_prefix='/stat')
