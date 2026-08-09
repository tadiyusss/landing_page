from datetime import datetime
from core.extensions import db
import uuid

class PhoneNumber(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.String(36), unique=True, nullable=False, default=lambda: str(uuid.uuid4()))

    name = db.Column(db.String(100), nullable=False)
    number_code = db.Column(db.String(4), nullable=False)
    phone_number = db.Column(db.String(10), nullable=False)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<PhoneNumber {self.number_code} {self.phone_number}>"