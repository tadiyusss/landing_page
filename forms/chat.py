from flask_wtf import FlaskForm
from wtforms import StringField, EmailField
from wtforms.validators import DataRequired, Length
from .validators import validate_phone_number

class StartChatForm(FlaskForm):
    first_name = StringField('First Name', 
        validators=[DataRequired(), Length(max=50)], 
        render_kw={"class": "text-input", "placeholder": "John", "x-model": "first_name"}
    )

    last_name = StringField('Last Name', 
        validators=[DataRequired(), Length(max=50)], 
        render_kw={"class": "text-input", "placeholder": "Doe", "x-model": "last_name"}
    )

    email = EmailField('Email', 
        validators=[DataRequired(), Length(max=50)], 
        render_kw={"class": "text-input", "placeholder": "john.doe@example.com", "x-model": "email"}
    )
    phone_number = StringField('Phone Number', 
        validators=[DataRequired(), validate_phone_number, Length(min=11, max=11, message="Phone number must be 11 digits")], 
        render_kw={"class": "text-input", "placeholder": "09255555555", "x-model": "phone_number"}
    )