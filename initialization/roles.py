from core.utils.registry.roles import register_role
from core.utils.roles import Role

ROLES = [
    Role(
        name="Seller",
        description="Can manage their own listings and view analytics related to their sales.",
    ),
    Role(
        name="Buyer",
        description="Can browse listings, make purchases, and view their order history.",
    )
]

def initialize_roles():
    for role in ROLES:
        register_role(role)