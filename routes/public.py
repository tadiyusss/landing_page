from .. import bp
from flask import render_template, request, redirect, url_for, flash
from core.extensions import db
from ..forms.waitlist import WaitlistForm
from ..forms.contact_us import ContactUsForm
from ..models.waitlist import Waitlist
from ..models.faq import FAQ
from ..models.contact_us import ContactUs
from extensions.landing_page.decorators.visitor_tracker import track_visitor

@bp.route('/', methods=['GET', 'POST'])
@track_visitor
def home():
    waitlist_form = WaitlistForm()
    contact_us_form = ContactUsForm()
    faqs = FAQ.query.order_by(FAQ.created_at.desc()).all()
    waitlist_count = Waitlist.query.count()

    if request.method == 'POST':

        if 'waitlist_form' in request.form:
            if waitlist_form.validate_on_submit():
                waitlist_entry = Waitlist(
                    email=waitlist_form.email.data,
                    telegram_username=waitlist_form.telegram_username.data,
                    role=waitlist_form.role.data,
                    product_interest=waitlist_form.product_interest.data,
                    monthly_orders_range=waitlist_form.monthly_orders_range.data,
                    ip_address=request.remote_addr
                )
                db.session.add(waitlist_entry)
                db.session.commit()
                flash('You have been added to the waitlist!', 'success')
                return redirect(url_for('landing_page.home') + '#waitlist')
        
        if 'contact_us_form' in request.form:
            if contact_us_form.validate_on_submit():
                contact_us_entry = ContactUs(
                    first_name=contact_us_form.first_name.data,
                    last_name=contact_us_form.last_name.data,
                    email=contact_us_form.email.data,
                    number_code=contact_us_form.number_code.data,
                    phone_number=contact_us_form.phone_number.data,
                    message=contact_us_form.message.data
                )
                db.session.add(contact_us_entry)
                db.session.commit()
                flash('Your message has been sent!', 'success')
                return redirect(url_for('landing_page.home') + '#contact-us')

    return render_template('index.html', waitlist_form=waitlist_form, contact_us_form=contact_us_form, faqs=faqs, waitlist_count=waitlist_count)