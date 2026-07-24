from .. import bp
from flask import jsonify, request
from core.extensions import db
from ..forms.chat import StartChatForm
from uuid import uuid4
from ..models.chat_support_clients import ChatSupportClient

@bp.route('/api/chat/start', methods=['POST'])
def start_chat():
    form = StartChatForm()

    if form.validate_on_submit():
        client = ChatSupportClient(
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            email=form.email.data,
            phone_number=form.phone_number.data
        )

        db.session.add(client)
        db.session.commit()

        return jsonify({
            "success": True,
            "message": "Chat started successfully.",
            "user_id": str(client.uuid)
        })
    
    return jsonify({
        "success": False,
        "errors": form.errors
    })