from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, EmailField, SelectField
from wtforms.validators import DataRequired, Length

COUNTRY_CODES = [
    ('+63', 'Philippines (+63)'),
    ('+1', 'United States (+1)'),
    ('+44', 'United Kingdom (+44)'),
    ('+61', 'Australia (+61)'),
    ('+33', 'France (+33)'),
    ('+49', 'Germany (+49)'),
    ('+81', 'Japan (+81)'),
    ('+86', 'China (+86)'),
    ('+91', 'India (+91)'),
    ('+55', 'Brazil (+55)'),
    ('+52', 'Mexico (+52)'),
    ('+34', 'Spain (+34)'),
    ('+39', 'Italy (+39)'),
    ('+7', 'Russia (+7)'),
    ('+82', 'South Korea (+82)'),
    ('+31', 'Netherlands (+31)'),
    ('+46', 'Sweden (+46)'),
    ('+41', 'Switzerland (+41)'),
    ('+65', 'Singapore (+65)'),
    ('+971', 'United Arab Emirates (+971)'),
    ('+966', 'Saudi Arabia (+966)'),
    ('+20', 'Egypt (+20)'),
    ('+234', 'Nigeria (+234)'),
    ('+27', 'South Africa (+27)'),
    ('+54', 'Argentina (+54)'),
    ('+57', 'Colombia (+57)'),
    ('+56', 'Chile (+56)'),
    ('+64', 'New Zealand (+64)'),
    ('+60', 'Malaysia (+60)'),
    ('+66', 'Thailand (+66)'),
    ('+62', 'Indonesia (+62)'),
    ('+84', 'Vietnam (+84)'),
    ('+880', 'Bangladesh (+880)'),
    ('+92', 'Pakistan (+92)'),
    ('+98', 'Iran (+98)'),
    ('+90', 'Turkey (+90)'),
    ('+48', 'Poland (+48)'),
    ('+32', 'Belgium (+32)'),
    ('+43', 'Austria (+43)'),
    ('+351', 'Portugal (+351)'),
    ('+30', 'Greece (+30)'),
    ('+47', 'Norway (+47)'),
    ('+45', 'Denmark (+45)'),
    ('+358', 'Finland (+358)'),
    ('+353', 'Ireland (+353)'),
    ('+420', 'Czech Republic (+420)'),
    ('+36', 'Hungary (+36)'),
    ('+40', 'Romania (+40)'),
    ('+380', 'Ukraine (+380)'),
    ('+972', 'Israel (+972)'),
]

class ContactUsForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired(), Length(max=50)], render_kw={"class": "text-input", "placeholder": "John"})
    last_name = StringField('Last Name', validators=[DataRequired(), Length(max=50)], render_kw={"class": "text-input", "placeholder": "Doe"})
    email = EmailField('Email', validators=[DataRequired(), Length(max=100)], render_kw={"class": "text-input", "placeholder": "john.doe@example.com"})
    number_code = SelectField('Number Code', choices=COUNTRY_CODES, validators=[DataRequired()], render_kw={"class": "text-input"})
    phone_number = StringField('Phone Number', validators=[DataRequired(), Length(max=20)], render_kw={"class": "text-input", "placeholder": "9560000000"})
    message = TextAreaField('Message', validators=[DataRequired()], render_kw={"class": "text-input w-full", "rows": 10})