from extensions.landing_page import bp
from flask import render_template, request, url_for, redirect, flash
from extensions.landing_page.models.contact_us import ContactUs
from extensions.landing_page.forms.filters.contact_us import FilterContactUsForm
from core.extensions import db
from core.utils.decorators import role_required
from flask_login import login_required

@bp.route('/dashboard/landing-page/inquiries')
@login_required
@role_required("Administrator")
def manage_inquiries():
    filter_form = FilterContactUsForm(request.args)
    page = request.args.get('page', 1, type=int)
    per_page = 10

    query = ContactUs.query.order_by(ContactUs.created_at.desc())

    if filter_form.query.data:
        query = query.filter(ContactUs.first_name.contains(filter_form.query.data) | ContactUs.last_name.contains(filter_form.query.data) | ContactUs.email.contains(filter_form.query.data) | ContactUs.message.contains(filter_form.query.data))

    if filter_form.status.data:
        query = query.filter(ContactUs.status == filter_form.status.data)

    if filter_form.date_start.data:
        query = query.filter(ContactUs.created_at >= filter_form.date_start.data)

    if filter_form.date_end.data:
        query = query.filter(ContactUs.created_at <= filter_form.date_end.data)

    filter_form.process()  

    filters_get_values = request.args.to_dict()
    filters_get_values.pop('page', None)

    pagination = query.paginate(page=page, per_page=per_page)
    inquiries = pagination.items

    return render_template('dashboard/inquiries.html', inquiries=inquiries, pagination=pagination, per_page=per_page, filter_form=filter_form, filters_get_values=filters_get_values)

@bp.route('/dashboard/landing-page/inquiries/delete/<string:inquiry_uuid>')
@login_required
@role_required("Administrator")
def delete_inquiry(inquiry_uuid):
    inquiry = ContactUs.query.filter_by(uuid=inquiry_uuid).first_or_404()
    db.session.delete(inquiry)
    db.session.commit()
    flash('Inquiry deleted successfully.', 'success')
    return redirect(url_for('landing_page.manage_inquiries'))

@bp.route('/dashboard/landing-page/inquiries/change-status/<string:inquiry_uuid>')
@login_required
@role_required("Administrator")
def change_inquiry_status(inquiry_uuid):
    inquiry = ContactUs.query.filter_by(uuid=inquiry_uuid).first_or_404()
    if inquiry.status == 'pending':
        inquiry.status = 'replied'
    elif inquiry.status == 'replied':
        inquiry.status = 'pending'
    db.session.commit()
    flash('Inquiry status updated successfully.', 'success')
    return redirect(url_for('landing_page.view_inquiry', inquiry_uuid=inquiry_uuid))

@bp.route('/dashboard/landing-page/inquiries/view/<string:inquiry_uuid>')
@login_required
@role_required("Administrator")
def view_inquiry(inquiry_uuid):
    inquiry = ContactUs.query.filter_by(uuid=inquiry_uuid).first_or_404()

    if inquiry.status == 'new':
        inquiry.status = 'pending'
        db.session.commit()

    return render_template('dashboard/view_inquiry.html', inquiry=inquiry)