from django.core.exceptions import ValidationError


def validate_username(value):
    if not all(ch.isalpha() or ch == "_" for ch in value):
        raise ValidationError("Username must contain only letters, digits, and underscores!")
