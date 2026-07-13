from datetime import datetime
from core.extensions import db
import uuid

STATUS_CHOICES = [
    ('new', 'New'),
    ('seen', 'Seen'),
    ('replied', 'Replied'),
]

class ContactUs(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.String(36), unique=True, nullable=False, default=lambda: str(uuid.uuid4()))
    
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    number_code = db.Column(db.String(4), nullable=False)
    phone_number = db.Column(db.String(20), nullable=False)
    message = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(20), nullable=False, default='new')
    
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
