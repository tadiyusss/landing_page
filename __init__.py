from flask import Blueprint
from .metadata import TEMPLATE_FOLDER, STATIC_FOLDER
from .initialization.settings import register_settings

bp = Blueprint('landing_page', __name__, template_folder=TEMPLATE_FOLDER, static_folder=STATIC_FOLDER, static_url_path="/static/landing_page")

from .routes import public

def init_extension(app, db):
    with app.app_context():
        db.create_all()
        register_settings()
    return bp 
