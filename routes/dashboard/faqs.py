from extensions.landing_page import bp
from flask import render_template, request, redirect, url_for, flash
from extensions.landing_page.forms.faq import FAQForm
from extensions.landing_page.models.faq import FAQ
from core.extensions import db
from flask_login import current_user

@bp.route('/dashboard/landing-page/faqs')
def manage_faqs():
    faqs = FAQ.query.order_by(FAQ.created_at.desc()).all()
    return render_template('dashboard/faqs.html', faqs=faqs)

@bp.route('/dashboard/landing-page/faqs/<string:faq_uuid>/delete', methods=['GET'])
def delete_faq(faq_uuid):
    faq = FAQ.query.get_or_404(faq_uuid)
    db.session.delete(faq)
    db.session.commit()
    flash('Entry deleted successfully!', 'success')
    return redirect(url_for('landing_page.manage_faqs'))

@bp.route('/dashboard/landing-page/faqs/create', methods=['GET', 'POST'])
def create_faq():
    form = FAQForm()
    
    if form.validate_on_submit():
        faq = FAQ(
            question=form.question.data,
            answer=form.answer.data,
            created_by=current_user
        )
        db.session.add(faq)
        db.session.commit()
        flash('New entry created successfully!', 'success')
        return redirect(url_for('landing_page.manage_faqs'))
    return render_template('dashboard/create_faq.html', form=form)