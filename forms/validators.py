
from re import match
from wtforms import ValidationError

def validate_phone_number(form, field):
    if not str(field.data).isdigit():
        raise ValidationError('Invalid phone number. It should only contain digits.')
    if not str(field.data).startswith('09'):
        raise ValidationError('Invalid phone number. It should start with "09".')