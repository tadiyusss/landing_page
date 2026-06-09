from datetime import datetime
from core.extensions import db
import uuid


class FAQ(db.Model):
    __tablename__ = "faq"

    id = db.Column(db.Integer, primary_key=True)

    uuid = db.Column(db.String(36), unique=True, nullable=False, default=lambda: str(uuid.uuid4()))

    question = db.Column(db.String(255), nullable=False)
    answer = db.Column(db.Text, nullable=False)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    created_by_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=True)

    created_by = db.relationship("User", backref="faqs", lazy=True)

    def __repr__(self):
        return f"<FAQ {self.question}>"