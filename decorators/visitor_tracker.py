from functools import wraps
import uuid
from extensions.landing_page.models.visitors import Visitor, Visit
from flask import request, session
from core.extensions import db
from datetime import datetime

def track_visitor(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        visitor_id = session.get("visitor_id")

        if not visitor_id:
            visitor_id = str(uuid.uuid4())
            session["visitor_id"] = visitor_id
        
        visitor = Visitor.query.filter_by(visitor_id=visitor_id).first()

        if not visitor:
            visitor = Visitor(
                visitor_id=visitor_id,
                ip_address=request.remote_addr,
                user_agent=request.headers.get('User-Agent'),
                first_seen=datetime.utcnow(),
                last_seen=datetime.utcnow(),
                visit_count=1,
                is_new=True
            )
            db.session.add(visitor)
            db.session.commit()
        else:
            visitor.last_seen = datetime.utcnow()
            visitor.visit_count += 1
            visitor.is_new = False
            db.session.commit()
        
        visit = Visit(
            visitor_id=visitor.uuid,
            referrer=request.referrer,
            utm_source=request.args.get('utm_source'),
            utm_medium=request.args.get('utm_medium'),
            utm_campaign=request.args.get('utm_campaign'),
            path=request.path
        )
        db.session.add(visit)
        db.session.commit()

        return func(*args, **kwargs)
    return wrapper