from core.utils.registry.roles import register_role
from core.utils.roles import Role

ROLES = [
    Role(
        name="Support Agent",
        description="Can view and respond to inquiries, manage FAQs, and assist users with support-related tasks.",
    )
]

def initialize_roles():
    for role in ROLES:
        register_role(role)