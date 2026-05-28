
from re import match
from wtforms import ValidationError
from ..models import Waitlist 

def validate_telegram_username(form, field):
    if field.data:
        pattern = r'^[a-zA-Z0-9_]{5,32}$'
        if not match(pattern, field.data):
            raise ValidationError('Invalid Telegram username. It should be 5-32 characters long and can only contain letters, numbers, and underscores.')
        
def validate_waitlist_unique_email(form, field):
    if Waitlist.query.filter_by(email=field.data).first():
        raise ValidationError('This email is already registered in the waitlist.')
    
def validate_waitlist_unique_telegram(form, field):
    if field.data and Waitlist.query.filter_by(telegram_username=field.data).first():
        raise ValidationError('This Telegram username is already registered in the waitlist.')