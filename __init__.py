from flask import Blueprint
from .metadata import TEMPLATE_FOLDER, STATIC_FOLDER
from .initialization.settings import register_settings
from .initialization.analytics import initialize_analytics
from .initialization.sidebar import initialize_sidebar
from .initialization.roles import initialize_roles

bp = Blueprint('landing_page', __name__, template_folder=TEMPLATE_FOLDER, static_folder=STATIC_FOLDER, static_url_path="/static/landing_page")

from .routes import public
from .routes.dashboard import inquiries, faqs, testimonials

def init_extension(app, db):
    with app.app_context():
        db.create_all()
        register_settings()
        initialize_analytics()
        initialize_sidebar()
        initialize_roles()
    return bp 
