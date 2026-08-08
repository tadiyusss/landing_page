from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, FileField
from flask_wtf.file import FileAllowed, FileRequired
from wtforms.validators import DataRequired, Length

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

class TestimonialForm(FlaskForm):
    image = FileField('Client Profile', 
                render_kw={"class": "fd-file-input"}, 
                validators=[FileAllowed(ALLOWED_EXTENSIONS, "Invalid file type.")], 
                description="Upload a profile image for the client. Allowed formats: png, jpg, jpeg, gif.",
            )
    name = StringField('Client Name', validators=[DataRequired(), Length(max=255)], render_kw={"class": "fd-input", "placeholder": "John Doe"})
    content = TextAreaField('Testimonial', validators=[DataRequired()], render_kw={"class": "fd-input", "rows": 5, "placeholder": "I had a great experience with this company..."})