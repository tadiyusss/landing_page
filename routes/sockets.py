from core.extensions import socketio
from flask import request

connected_users = {}

@socketio.on('connect')
def handle_connect():
    connected_users[request.sid] = True
    print("Client Connected: " + request.sid)


@socketio.on('disconnect')
def handle_disconnect():
    if request.sid in connected_users:
        del connected_users[request.sid]
    print("Client Disconnected: " + request.sid)