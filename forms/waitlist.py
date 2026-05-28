from flask_wtf import FlaskForm
from wtforms import StringField, SelectField
from wtforms.validators import DataRequired, Email, Length
from .validators import validate_telegram_username, validate_waitlist_unique_email, validate_waitlist_unique_telegram


ROLES = [
    ("seller", "Seller"),
    ("buyer", "Buyer"),
    ("both", "Both"),
]

PRODUCT_INTERESTS = [
    ("streaming", "Streaming"),
    ("software_licenses", "Software Licenses"),
    ("digital_services", "Digital Services"),
    ("game_accounts", "Game Accounts"),
    ("others", "Others"),
]

MONTHLY_ORDERS_RANGES = [
    ("range_1_10", "1-10 orders"),
    ("range_11_50", "11-50 orders"),
    ("range_51_200", "51-200 orders"),
    ("range_201_above", "201+ orders"),
]

class WaitlistForm(FlaskForm):
    role = SelectField('I am a...', 
        choices=ROLES, 
        validators=[DataRequired()], 
        render_kw={"class": "text-input"}
    )

    telegram_username = StringField('Telegram Username', 
        validators=[validate_telegram_username, validate_waitlist_unique_telegram], 
        render_kw={
            "placeholder": "@usernameeee", 
            "class": "text-input"
        }
    )

    email = StringField('Email', 
        validators=[DataRequired(), Email(), Length(max=120), validate_waitlist_unique_email], 
        render_kw={
            "placeholder": "you@email.com", 
            "class": "text-input"
        }
    )

    product_interest = SelectField('Product Interest', 
        choices=PRODUCT_INTERESTS,
        validators=[DataRequired()], 
        render_kw={"class": "text-input"}
    )

    monthly_orders_range = SelectField('Monthly Orders Range', 
        choices=MONTHLY_ORDERS_RANGES, 
        validators=[DataRequired()], 
        render_kw={"class": "text-input"}
    )

