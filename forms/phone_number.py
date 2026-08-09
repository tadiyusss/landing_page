from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, Length, NumberRange

class PhoneNumberForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(max=100)], render_kw={"placeholder": "John Doe", "class": "fd-input"})
    number_code = StringField('Country Code', validators=[DataRequired(), Length(max=5)], render_kw={"placeholder": "+63", "class": "fd-input"})
    phone_number = IntegerField('Phone Number', validators=[DataRequired(), NumberRange(min=9000000000, max=9999999999, message="Please enter a valid phone number (Ex: 09555555555)")], render_kw={"placeholder": "9123456789", "class": "fd-input"})
