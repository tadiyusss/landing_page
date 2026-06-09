from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired, Length

class FAQForm(FlaskForm):
    question = StringField('Question', validators=[DataRequired(), Length(max=255)], render_kw={"class": "text-input"})
    answer = TextAreaField('Answer', validators=[DataRequired()], render_kw={"class": "text-area", "rows": 5})