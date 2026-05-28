from datetime import datetime
from core.extensions import db
import uuid
from enum import Enum

class WaitlistRole(Enum):
    seller = "Seller"
    buyer = "Buyer"
    both = "Both"

class ProductInterest(Enum):
    streaming = "Streaming"
    software_licenses = "Software Licenses"
    digital_services = "Digital Services"
    game_accounts = "Game Accounts"
    others = "Others"

class MonthlyOrdersRange(Enum):
    range_1_10 = "1-10 orders"
    range_11_50 = "11-50 orders"
    range_51_200 = "51-200 orders"
    range_201_above = "201+ orders"



class Waitlist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.String(36), unique=True, nullable=False, default=lambda: str(uuid.uuid4()))
    
    email = db.Column(db.String(120), unique=True, nullable=False)
    telegram_username = db.Column(db.String(120), unique=True, nullable=True)

    role = db.Column(db.Enum(WaitlistRole), nullable=False)
    product_interest = db.Column(db.Enum(ProductInterest), nullable=False)
    monthly_orders_range = db.Column(db.Enum(MonthlyOrdersRange), nullable=False)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    ip_address = db.Column(db.String(45), nullable=True) 
    
    def __repr__(self):
        return f"<Waitlist {self.email} - {self.role.value} - {self.product_interest.value} - {self.monthly_orders_range.value}>"