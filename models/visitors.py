from datetime import datetime
from core.extensions import db
import uuid

class Visit(db.Model):
    __tablename__ = 'visits'

    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.String(36), nullable=False, default=lambda: str(uuid.uuid4()))

    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    referrer = db.Column(db.String(255), nullable=True)
    utm_source = db.Column(db.String(255), nullable=True)
    utm_medium = db.Column(db.String(255), nullable=True)
    utm_campaign = db.Column(db.String(255), nullable=True)
    path = db.Column(db.String(255), nullable=True)

    visitor_id = db.Column(db.Integer, db.ForeignKey('visitor.id'), nullable=False)

    __table_args__ = (
        db.UniqueConstraint('uuid', name='uq_visits_uuid'),
    )

    def __repr__(self):
        return f"<Visit {self.uuid} at {self.timestamp}>"


class Visitor(db.Model):
    __tablename__ = 'visitor'

    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.String(36), nullable=False, default=lambda: str(uuid.uuid4()))
    visitor_id = db.Column(db.String(36), nullable=False, unique=True)

    ip_address = db.Column(db.String(45), nullable=True)
    user_agent = db.Column(db.String(255), nullable=True)
    first_seen = db.Column(db.DateTime, default=datetime.utcnow)
    last_seen = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    visit_count = db.Column(db.Integer, default=1)
    is_new = db.Column(db.Boolean, default=True)
    visitor_count = db.Column(db.Integer, default=1)


    visits = db.relationship('Visit', backref='visitor', lazy=True)

    __table_args__ = (
        db.UniqueConstraint('uuid', name='uq_visitor_uuid'),
        db.UniqueConstraint('visitor_id', name='uq_visitor_visitor_id'),
    )

    def __repr__(self):
        return f"<Visitor {self.uuid} - Visits: {self.visit_count} - New: {self.is_new}>"