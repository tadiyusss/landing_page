from extensions.landing_page import bp
from flask import render_template, request, redirect, url_for, flash

@bp.route('/dashboard/landing-page/faqs')
def manage_faqs():
    return render_template('dashboard/faqs.html')