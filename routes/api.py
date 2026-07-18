from .. import bp
from flask import jsonify, request
from core.extensions import db

@bp.route('/api/chat/start', methods=['POST'])
def start_chat():
    pass