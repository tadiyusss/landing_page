from datetime import datetime
from core.extensions import db
import uuid
from .chat_support_clients import ChatSupportClient
from core.models.users import User

SENDER_CHOICES = ['client', 'moderator']
MESSAGE_TYPE = [
    'text',
    'image',
    'video',
    'file'
]


class LiveChatMessage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.String(36), unique=True, nullable=False, default=lambda: str(uuid.uuid4()))

    client_id = db.Column(db.Integer, db.ForeignKey('chat_support_client.id'), nullable=False)
    moderator_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)

    client = db.relationship(ChatSupportClient, backref='messages', lazy=True)
    moderator = db.relationship(User, backref='messages', lazy=True)
    
    sender = db.Column(db.Enum(*SENDER_CHOICES, name='sender_choices'), nullable=False)

    message_type = db.Column(db.Enum(*MESSAGE_TYPE, name='message_type'), nullable=False)
    content = db.Column(db.Text, nullable=False)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)