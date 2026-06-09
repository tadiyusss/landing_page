from datetime import datetime
from core.extensions import db
import uuid
from core.models.users import User

class FAQ(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.String(36), unique=True, nullable=False, default=str(uuid.uuid4()))

    question = db.Column(db.String(255), nullable=False)
    answer = db.Column(db.Text, nullable=False)

    created_by = db.Column(db.Integer, db.ForeignKey(User.id), nullable=False)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return f"<FAQ {self.question} | {self.answer}>"