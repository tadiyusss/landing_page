from datetime import datetime
from core.extensions import db
import uuid

class TeamMember(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.String(36), unique=True, nullable=False, default=lambda: str(uuid.uuid4()))

    image = db.Column(db.String(255), nullable=False) 
    name = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(255), nullable=False)
    placement_order = db.Column(db.Integer, nullable=False, default=0)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<TeamMember {self.name}>"

    def switch_order(self, replacement_member):
        """
        Switch the placement order of this team member with another team member.
        """
        if not isinstance(replacement_member, TeamMember):
            raise ValueError("replacement_member must be an instance of TeamMember")

        self.placement_order, replacement_member.placement_order = (
            replacement_member.placement_order,
            self.placement_order,
        )
        db.session.commit()