from extensions.landing_page import bp
from flask import render_template, request, redirect, url_for, flash
from ...models.waitlist import Waitlist 

@bp.route('/dashboard/landing-page/waitlist')
def waitlist():
    page = request.args.get('page', 1, type=int)
    per_page = 10

    pagination = Waitlist.query.order_by(Waitlist.created_at.desc()).paginate(page=page, per_page=per_page)
    waitlist = pagination.items

    return render_template('dashboard/waitlist.html', waitlist=waitlist, pagination=pagination, per_page=per_page)