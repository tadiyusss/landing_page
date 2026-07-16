from extensions.landing_page import bp
from flask import render_template
from core.extensions import db

@bp.route('/dashboard/messages')
def view_messages():
    return render_template('dashboard/messages.html')