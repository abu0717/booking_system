import re
from django.core.exceptions import ValidationError


def validate_password(password):
    if len(password) < 6:
        raise ValidationError('Password must be at least 6')
    elif not re.match('.*[A-Z]', password):
        raise ValidationError('Password must contain at least 1 upper case character')
    elif not re.match('.*[a-z]', password):
        raise ValidationError("Your password must contain at least 1 lower case character.")
