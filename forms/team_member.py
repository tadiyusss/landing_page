from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FileField
from wtforms.validators import DataRequired, Length
from flask_wtf.file import FileAllowed, FileRequired

ALLOWED_IMAGE_EXTENSIONS = ['jpg', 'jpeg', 'png']

class TeamMemberForm(FlaskForm):
    image = FileField('Image', validators=[FileAllowed(ALLOWED_IMAGE_EXTENSIONS, 'Invalid file type. Only JPG, JPEG, and PNG are allowed.')], description='Upload an image for the team member. Allowed formats: JPG, JPEG, PNG.', render_kw={"class": "fd-file-input"})
    name = StringField('Name', validators=[DataRequired(), Length(max=255)], render_kw={"placeholder": "John Doe", "class": "fd-input"})
    role = StringField('Role', validators=[DataRequired(), Length(max=255)], render_kw={"placeholder": "Property Manager", "class": "fd-input"})
    placement_order = IntegerField('Placement Order', validators=[DataRequired()], render_kw={"placeholder": "1", "class": "fd-input"}, description='The order in which the team member will appear on the About Us page. Existing placement will override the current order.')
