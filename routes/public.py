from .. import bp
from flask import render_template, request, redirect, url_for, flash
from core.extensions import db
from ..forms.contact_us import ContactUsForm
from ..forms.chat import StartChatForm
from ..models.faq import FAQ
from ..models.contact_us import ContactUs
from extensions.landing_page.decorators.visitor_tracker import track_visitor

@bp.route('/', methods=['GET', 'POST'])
@track_visitor
def home():
    contact_us_form = ContactUsForm()
    start_chat_form = StartChatForm()
    faqs = FAQ.query.order_by(FAQ.created_at.desc()).all()

    if request.method == 'POST':

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

    return render_template('index.html', contact_us_form=contact_us_form, faqs=faqs, start_chat_form=start_chat_form)