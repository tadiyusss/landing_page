from extensions.landing_page import bp
from flask import render_template, request, url_for, redirect, flash
from core.extensions import db
from core.utils.decorators import role_required, roles_required
from flask_login import login_required
from extensions.landing_page.models.testimonial import Testimonial
from extensions.landing_page.forms.testimonial import TestimonialForm
import os
from flask_wtf.file import FileRequired
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'media'

@bp.route('/dashboard/landing-page/testimonials')
@login_required
@roles_required(['Administrator', 'Editor'])
def manage_testimonials():
    testimonials = Testimonial.query.all()
    return render_template('dashboard/testimonials.html', testimonials=testimonials)

@bp.route('/dashboard/landing-page/testimonials/create', methods=['GET', 'POST'])
@login_required
@roles_required(['Administrator', 'Editor'])
def add_testimonial():
    form = TestimonialForm()
    form.image.validators.append(FileRequired(message="Please upload an image for the testimonial."))

    if request.method == "POST":
        if form.validate_on_submit():
            os.makedirs(UPLOAD_FOLDER, exist_ok=True)   
            image_file = form.image.data
            if image_file:
                filename = image_file.filename
                filename = secure_filename(filename)
                image_path = f"{UPLOAD_FOLDER}/{filename}"
                image_file.save(filename)
            else:
                flash('No image uploaded.', 'danger')
                return render_template('dashboard/create_or_edit_testimonial.html', form=form)

            new_testimonial = Testimonial(
                name=form.name.data,
                content=form.content.data,
                image=filename
            )

            db.session.add(new_testimonial)
            db.session.commit()

            flash('Testimonial created successfully!', 'success')
            return redirect(url_for('landing_page.manage_testimonials'))
        else:
            flash('Error creating testimonial. Please check the form for errors.', 'danger')

    return render_template('dashboard/create_or_edit_testimonial.html', form=form)

@bp.route('/dashboard/landing-page/testimonials/edit/<string:testimonial_uuid>', methods=['GET', 'POST'])
@login_required
@roles_required(['Administrator', 'Editor'])
def edit_testimonial(testimonial_uuid):
    testimonial = Testimonial.query.filter_by(uuid=testimonial_uuid).first_or_404()
    form = TestimonialForm(obj=testimonial)
    
    if request.method == "POST":
        if form.validate_on_submit():
            testimonial.name = form.name.data
            testimonial.content = form.content.data

            image_file = form.image.data
            if image_file:
                os.makedirs(UPLOAD_FOLDER, exist_ok=True)
                filename = image_file.filename
                filename = secure_filename(filename)
                image_path = f"{UPLOAD_FOLDER}/{filename}"
                image_file.save(image_path)
                testimonial.image = filename

            db.session.commit()

            flash('Testimonial updated successfully!', 'success')
            return redirect(url_for('landing_page.manage_testimonials'))
        else:
            flash('Error updating testimonial. Please check the form for errors.', 'danger')

    return render_template('dashboard/create_or_edit_testimonial.html', form=form, testimonial=testimonial)

@bp.route('/dashboard/landing-page/testimonials/delete/<string:testimonial_uuid>', methods=['GET', 'POST'])
@login_required
@roles_required(['Administrator', 'Editor'])
def delete_testimonial(testimonial_uuid):
    testimonial = Testimonial.query.filter_by(uuid=testimonial_uuid).first_or_404()

    testimonial.delete()
    flash('Testimonial deleted successfully!', 'success')
    return redirect(url_for('landing_page.manage_testimonials'))   
    