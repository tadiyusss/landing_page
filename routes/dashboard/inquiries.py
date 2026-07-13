from extensions.landing_page import bp
from flask import render_template, request, url_for, redirect, flash
from extensions.landing_page.models.contact_us import ContactUs
from core.extensions import db

@bp.route('/dashboard/landing-page/inquiries')
def manage_inquiries():
    page = request.args.get('page', 1, type=int)
    per_page = 10

    pagination = ContactUs.query.order_by(ContactUs.created_at.desc()).paginate(page=page, per_page=per_page)
    inquiries = pagination.items

    return render_template('dashboard/inquiries.html', inquiries=inquiries, pagination=pagination, per_page=per_page)

@bp.route('/dashboard/landing-page/inquiries/delete/<string:inquiry_uuid>')
def delete_inquiry(inquiry_uuid):
    inquiry = ContactUs.query.filter_by(uuid=inquiry_uuid).first_or_404()
    db.session.delete(inquiry)
    db.session.commit()
    flash('Inquiry deleted successfully.', 'success')
    return redirect(url_for('landing_page.manage_inquiries'))

@bp.route('/dashboard/landing-page/inquiries/change-status/<string:inquiry_uuid>')
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
def view_inquiry(inquiry_uuid):
    inquiry = ContactUs.query.filter_by(uuid=inquiry_uuid).first_or_404()

    if inquiry.status == 'new':
        inquiry.status = 'pending'
        db.session.commit()

    return render_template('dashboard/view_inquiry.html', inquiry=inquiry)