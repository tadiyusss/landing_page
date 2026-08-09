from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length

class OfficeLocationForm(FlaskForm):
    address = StringField('Address', validators=[DataRequired(), Length(max=255)], render_kw={"placeholder": "123 Main St, City, State, ZIP", "class": "fd-input"})
    city = StringField('City', validators=[DataRequired(), Length(max=100)], render_kw={"placeholder": "City", "class": "fd-input"}, description="Ex: Manila City, Quezon City, Makati City, etc.")
    region = StringField('Region or Province', validators=[DataRequired(), Length(max=100)], render_kw={"placeholder": "Region", "class": "fd-input"}, description="Ex: Manila, Laguna, etc.")
    zip_code = StringField('ZIP Code', validators=[DataRequired(), Length(max=20)], render_kw={"placeholder": "ZIP Code", "class": "fd-input"}, description="Ex: 1000, 1100, 1200, etc.")
    country = StringField('Country', validators=[DataRequired(), Length(max=100)], render_kw={"placeholder": "Country", "class": "fd-input"})