from extensions.landing_page import bp
from flask import render_template, request, redirect, url_for, flash
from extensions.landing_page.forms.faq import FAQForm
from extensions.landing_page.models.faq import FAQ
from core.extensions import db
from flask_login import current_user
from core.utils.decorators import role_required
from flask_login import login_required


@bp.route('/dashboard/landing-page/faqs')
@role_required('Administrator')
@login_required
def manage_faqs():
    faqs = FAQ.query.order_by(FAQ.created_at.desc()).all()
    return render_template('dashboard/faqs.html', faqs=faqs)

@bp.route('/dashboard/landing-page/faqs/<string:faq_uuid>/delete', methods=['GET'])
@role_required('Administrator')
@login_required
def delete_faq(faq_uuid):
    faq = FAQ.query.filter_by(uuid=faq_uuid).first_or_404()
    db.session.delete(faq)
    db.session.commit()
    flash('Entry deleted successfully!', 'success')
    return redirect(url_for('landing_page.manage_faqs'))

@bp.route('/dashboard/landing-page/faqs/<string:faq_uuid>/edit', methods=['GET', 'POST'])
@role_required('Administrator')
@login_required
def edit_faq(faq_uuid):
    faq = FAQ.query.filter_by(uuid=faq_uuid).first_or_404()
    form = FAQForm(obj=faq)
    
    if form.validate_on_submit():
        faq.question = form.question.data
        faq.answer = form.answer.data
        db.session.commit()
        flash('Entry updated successfully!', 'success')
        return redirect(url_for('landing_page.manage_faqs'))
    return render_template('dashboard/create_or_edit_faq.html', form=form, faq=faq, is_edit=True)

@bp.route('/dashboard/landing-page/faqs/create', methods=['GET', 'POST'])
@role_required('Administrator')
@login_required
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
        flash('New entr y created successfully!', 'success')
        return redirect(url_for('landing_page.manage_faqs'))
    return render_template('dashboard/create_or_edit_faq.html', form=form, is_edit=False)