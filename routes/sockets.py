from core.extensions import socketio
from flask import request
from flask_login import current_user

CHAT_MODERATOR_ROLES = ["Administrator", "Support Agent"]

connected_users = {
    "users": [],
    "moderators": []
}


@socketio.on('connect')
def handle_connect():
    if current_user.is_authenticated:
        print(current_user.has_role("Administrator"))



@socketio.on('disconnect')
def handle_disconnect():
    if request.sid in connected_users:
        del connected_users[request.sid]
    print("Client Disconnected: " + request.sid)