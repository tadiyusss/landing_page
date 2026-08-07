
from re import match
from wtforms import ValidationError

def validate_telegram_username(form, field):
    if field.data:
        pattern = r'^[a-zA-Z0-9_]{5,32}$'
        if not match(pattern, field.data):
            raise ValidationError('Invalid Telegram username. It should be 5-32 characters long and can only contain letters, numbers, and underscores.')
        
def validate_phone_number(form, field):
    if not str(field.data).isdigit():
        raise ValidationError('Invalid phone number. It should only contain digits.')
    if not str(field.data).startswith('09'):
        raise ValidationError('Invalid phone number. It should start with "09".')