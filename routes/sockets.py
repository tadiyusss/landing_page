from core.extensions import socketio
from flask import request
from flask_login import current_user
from ..models.chat_support_clients import ChatSupportClient
from ..models.live_chat_messages import LiveChatMessage
from core.extensions import db

CHAT_MODERATOR_ROLES = ["Administrator", "Support Agent"]

connected_users = {
    "users": [],
    "moderators": []
}


@socketio.on('connect')
def handle_connect():
    if current_user.is_authenticated:
        print(current_user.has_role("Administrator"))

@socketio.on('history')
def handle_history(data):
    user_id = data.get('user_id')
    if not user_id:
        socketio.emit('error', {'message': 'User ID is required to fetch chat history.'}, room=request.sid)
        return

    client = ChatSupportClient.query.filter_by(uuid=user_id).first()
    if not client:
        socketio.emit('error', {'message': 'Unknown user please start a chat session first.'}, room=request.sid)
        return

    messages = LiveChatMessage.query.filter_by(client_id=client.id).order_by(LiveChatMessage.created_at.asc()).all()
    message_history = [
        {
            "sender": msg.sender,
            "message_type": msg.message_type,
            "content": msg.content,
            "created_at": msg.created_at.isoformat()
        } for msg in messages
    ]

    socketio.emit('history', {'messages': message_history}, room=request.sid)

@socketio.on('message')
def handle_message(data):
    user_id = data.get('user_id')
    message = data.get('message')
    
    if not user_id or not message:
        socketio.emit('error', {'message': 'Invalid data received.'}, room=request.sid)
        return

    client = ChatSupportClient.query.filter_by(uuid=user_id).first()
    if not client:
        socketio.emit('error', {'message': 'Unknown user please start a chat session first.'}, room=request.sid)
        return
    
    chat_message = LiveChatMessage(
        client_id=client.id,
        sender='client',
        message_type='text',
        content=message
    )
    db.session.add(chat_message)
    db.session.commit()



@socketio.on('disconnect')
def handle_disconnect():
    if request.sid in connected_users:
        del connected_users[request.sid]
    print("Client Disconnected: " + request.sid)