from .. import bp
from flask import render_template, request, redirect, url_for, flash
from core.extensions import db
from ..forms.waitlist import WaitlistForm
from ..models.waitlist import Waitlist, WaitlistRole, ProductInterest, MonthlyOrdersRange
from extensions.utils.visitors import tracking_visitor

@bp.route('/', methods=['GET', 'POST'])
def home():
    visitor = tracking_visitor()
    print(visitor)
    form = WaitlistForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            waitlist_entry = Waitlist(
                email=form.email.data,
                telegram_username=form.telegram_username.data,
                role=form.role.data,
                product_interest=form.product_interest.data,
                monthly_orders_range=form.monthly_orders_range.data,
                ip_address=request.remote_addr
            )
            db.session.add(waitlist_entry)
            db.session.commit()
            flash('You have been added to the waitlist!', 'success')
            return redirect(url_for('landing_page.home') + '#waitlist')

    return render_template('index.html', form=form)