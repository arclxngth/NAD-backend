from flask import Blueprint

bp = Blueprint("traffic", __name__)

from app.traffics import routes