from extensions.landing_page import bp
from flask import render_template, request, redirect, url_for, flash
from core.extensions import db
from flask_login import current_user
from core.utils.decorators import roles_required
from flask_login import login_required
from extensions.landing_page.models.team_member import TeamMember
from extensions.landing_page.forms.team_member import TeamMemberForm
from flask_wtf.file import FileRequired
from extensions.landing_page.forms.office_location import OfficeLocationForm
from extensions.landing_page.models.office_location import OfficeLocation
from extensions.landing_page.models.phone_number import PhoneNumber
from extensions.landing_page.forms.phone_number import PhoneNumberForm


@bp.route('/dashboard/landing-page/about-us', methods=['GET', 'POST'])
@login_required
@roles_required(['Administrator', 'Editor'])
def manage_about_us():
    team_members = TeamMember.query.order_by(TeamMember.placement_order).all()
    office_locations = OfficeLocation.query.order_by(OfficeLocation.created_at.desc()).all()
    phone_numbers = PhoneNumber.query.order_by(PhoneNumber.created_at.desc()).all()

    return render_template('dashboard/about_us.html', team_members=team_members, office_locations=office_locations, phone_numbers=phone_numbers)

@bp.route('/dashboard/landing-page/about-us/team-member/create', methods=['GET', 'POST'])
@login_required
@roles_required(['Administrator', 'Editor'])
def create_team_member():
    form = TeamMemberForm()
    form.image.validators.append(FileRequired())
    
    if request.method == "POST":
        if form.validate_on_submit():

            existing_member = TeamMember.query.filter_by(placement_order=form.placement_order.data).first()
            if existing_member:
                existing_member.placement_order = TeamMember.query.count() + 1
                db.session.commit()

            new_member = TeamMember(
                name=form.name.data,
                role=form.role.data,
                placement_order=form.placement_order.data
            )

            if form.image.data:
                image_file = form.image.data
                image_path = f'media/{image_file.filename}'
                image_file.save(image_path)
                new_member.image = image_file.filename  

            db.session.add(new_member)
            db.session.commit()
            flash('Team member created successfully!', 'success')
            return redirect(url_for('landing_page.manage_about_us'))
        else:
            flash('Error creating team member. Please check the form for errors.', 'danger')

    return render_template('dashboard/create_or_edit_team_member.html', action='create', form=form)

@bp.route('/dashboard/landing-page/about-us/team-member/delete/<string:member_uuid>')
@login_required
@roles_required(['Administrator', 'Editor'])
def delete_team_member(member_uuid):
    member = TeamMember.query.filter_by(uuid=member_uuid).first_or_404()
    db.session.delete(member)
    db.session.commit()
    flash('Team member deleted successfully!', 'success')
    return redirect(url_for('landing_page.manage_about_us'))

@bp.route('/dashboard/landing-page/about-us/team-member/edit/<string:member_uuid>', methods=['GET', 'POST'])
@login_required
@roles_required(['Administrator', 'Editor'])
def edit_team_member(member_uuid):
    member = TeamMember.query.filter_by(uuid=member_uuid).first_or_404()
    form = TeamMemberForm(obj=member)

    if request.method == "POST":
        if form.validate_on_submit():
            member.name = form.name.data
            member.role = form.role.data

            if form.placement_order.data != member.placement_order:
                existing_member = TeamMember.query.filter_by(placement_order=form.placement_order.data).first()
                if existing_member:
                    existing_member.placement_order = member.placement_order
                    db.session.commit()

                member.placement_order = form.placement_order.data

            if form.image.data:
                image_file = form.image.data
                image_path = f'media/{image_file.filename}'
                image_file.save(image_path)
                member.image = image_file.filename  

            db.session.commit()
            flash('Team member updated successfully!', 'success')
            return redirect(url_for('landing_page.manage_about_us'))
        else:
            flash('Error updating team member. Please check the form for errors.', 'danger')

    return render_template('dashboard/create_or_edit_team_member.html', is_edit=True, form=form, member=member)

@bp.route('/dashboard/landing-page/about-us/office-location/create', methods=['GET', 'POST'])
@login_required
@roles_required(['Administrator', 'Editor'])
def create_office_location():
    form = OfficeLocationForm()

    if request.method == "POST":
        if form.validate_on_submit():
            new_location = OfficeLocation(
                address=form.address.data,
                city=form.city.data,
                region=form.region.data,
                zip_code=form.zip_code.data,
                country=form.country.data
            )
            db.session.add(new_location)
            db.session.commit()
            flash('Office location created successfully!', 'success')
            return redirect(url_for('landing_page.manage_about_us'))
        else:
            flash('Error creating office location. Please check the form for errors.', 'danger')

    return render_template('dashboard/create_or_edit_office_location.html', action='create', form=form)

@bp.route('/dashboard/landing-page/about-us/office-location/delete/<string:location_uuid>')
@login_required
@roles_required(['Administrator', 'Editor'])
def delete_office_location(location_uuid):
    location = OfficeLocation.query.filter_by(uuid=location_uuid).first_or_404()
    db.session.delete(location)
    db.session.commit()
    flash('Office location deleted successfully!', 'success')
    return redirect(url_for('landing_page.manage_about_us'))

@bp.route('/dashboard/landing-page/about-us/office-location/edit/<string:location_uuid>', methods=['GET', 'POST'])
@login_required
@roles_required(['Administrator', 'Editor'])
def edit_office_location(location_uuid):
    location = OfficeLocation.query.filter_by(uuid=location_uuid).first_or_404()
    form = OfficeLocationForm(obj=location)

    if request.method == "POST":
        if form.validate_on_submit():
            location.address = form.address.data
            location.city = form.city.data
            location.region = form.region.data
            location.zip_code = form.zip_code.data
            location.country = form.country.data

            db.session.commit()
            flash('Office location updated successfully!', 'success')
            return redirect(url_for('landing_page.manage_about_us'))
        else:
            flash('Error updating office location. Please check the form for errors.', 'danger')

    return render_template('dashboard/create_or_edit_office_location.html', is_edit=True, form=form, location=location)

@bp.route('/dashboard/landing-page/about-us/phone-number/create', methods=['GET', 'POST'])
@login_required
@roles_required(['Administrator', 'Editor'])
def create_phone_number():
    form = PhoneNumberForm()

    if request.method == "POST":
        if form.validate_on_submit():
            new_number = PhoneNumber(
                name=form.name.data,
                number_code=form.number_code.data,
                phone_number=form.phone_number.data
            )
            db.session.add(new_number)
            db.session.commit()
            flash('Phone number created successfully!', 'success')
            return redirect(url_for('landing_page.manage_about_us'))
        else:
            flash('Error creating phone number. Please check the form for errors.', 'danger')

    return render_template('dashboard/create_or_edit_phone_number.html', action='create', form=form)

@bp.route('/dashboard/landing-page/about-us/phone-number/delete/<string:number_uuid>')
@login_required
@roles_required(['Administrator', 'Editor'])
def delete_phone_number(number_uuid):
    number = PhoneNumber.query.filter_by(uuid=number_uuid).first_or_404()
    db.session.delete(number)
    db.session.commit()
    flash('Phone number deleted successfully!', 'success')
    return redirect(url_for('landing_page.manage_about_us'))

@bp.route('/dashboard/landing-page/about-us/phone-number/edit/<string:number_uuid>', methods=['GET', 'POST'])
@login_required
@roles_required(['Administrator', 'Editor'])
def edit_phone_number(number_uuid):
    number = PhoneNumber.query.filter_by(uuid=number_uuid).first_or_404()
    form = PhoneNumberForm(obj=number)

    if request.method == "POST":
        if form.validate_on_submit():
            number.name = form.name.data
            number.number_code = form.number_code.data
            number.phone_number = form.phone_number.data

            db.session.commit()
            flash('Phone number updated successfully!', 'success')
            return redirect(url_for('landing_page.manage_about_us'))
        else:
            flash('Error updating phone number. Please check the form for errors.', 'danger')

    return render_template('dashboard/create_or_edit_phone_number.html', is_edit=True, form=form, number=number)