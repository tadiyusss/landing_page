from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, DateField
from wtforms.validators import Length
from extensions.landing_page.models.contact_us import STATUS_CHOICES

class FilterContactUsForm(FlaskForm):
    query = StringField('Search', validators=[Length(max=100)], render_kw={"class": "fd-input", "placeholder": "Search by name, email, or message..."})
    status = SelectField('Status', choices=[('', 'All')] + STATUS_CHOICES, render_kw={"class": "fd-input"})

    date_start = DateField('Start Date', format='%Y-%m-%d', render_kw={"class": "fd-input", "placeholder": "YYYY-MM-DD"})
    date_end = DateField('End Date', format='%Y-%m-%d', render_kw={"class": "fd-input", "placeholder": "YYYY-MM-DD"})
