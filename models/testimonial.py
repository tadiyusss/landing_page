from datetime import datetime
from core.extensions import db
import uuid
import os

class Testimonial(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.String(36), unique=True, nullable=False, default=lambda: str(uuid.uuid4()))

    image = db.Column(db.String(255), nullable=True)
    name = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def delete(self):
        if self.image:
            image_path = os.path.join(f"/{self.image}")
            if os.path.exists(image_path):
                os.remove(image_path)

        db.session.delete(self)
        db.session.commit()

